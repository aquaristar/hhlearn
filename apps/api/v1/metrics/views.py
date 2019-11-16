from django.views.generic import View
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.dashboard.models import *
from apps.api.v1.metrics.serializers import *

from datetime import *
from datetime import datetime
from datetime import timedelta
from datetime import date
import math

# Class based view for profile page.
class APIMetrics(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):
        try:
            # need to get logged in user.
            user_profile = request.user.core_user_profile
            
            #get assigned Courses count
            assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True, course__is_active=True)            
            safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True, course__is_active=True)
            
            all_course_count = len(assignments) + len(safety_assignments)
            
            #get all assigned hours
            assigned_course_hours = 0
            if len(assignments) is not 0:                
                assigned_course_hours = assignments.aggregate(all_hours=Sum('course__hours'))['all_hours']
            
            if len(safety_assignments) is not 0:
                assigned_course_hours += safety_assignments.aggregate(all_hours=Sum('course__hours'))['all_hours']
            
            #get completed courses count
            completed_assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True, is_completed=True)            
            completed_safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True, is_completed=True)
            
            completed_course_count = len(completed_assignments) + len(completed_safety_assignments)
            
            #get completed course hours
            completed_course_hours = 0
            if len(completed_assignments) is not 0:
                completed_course_hours = completed_assignments.aggregate(all_hours=Sum('course__hours'))['all_hours']
            if len(completed_safety_assignments) is not 0:                        
                completed_course_hours += completed_safety_assignments.aggregate(all_hours=Sum('course__hours'))['all_hours']
            
            assigned_course_hours -= completed_course_hours
            
            #get location user profiles
            location = user_profile.location
            location_user_profiles = CoreUserProfiles.objects.filter(location=location).values_list('id', flat=True)
            
            #get location assignment count
            location_assignments = CoreUserAssignments.objects.filter(user_profile__in=location_user_profiles, is_active=True, course__is_active=True)            
            location_safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile__in=location_user_profiles, is_active=True, course__is_active=True)
            location_assigned_course_count = len(location_assignments) + len(location_safety_assignments)
            
            completed_location_assignments = CoreUserAssignments.objects.filter(user_profile__in=location_user_profiles, is_active=True, is_completed=True)            
            completed_location_safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile__in=location_user_profiles, is_active=True, is_completed=True)
            completed_location_assigned_course_count = len(completed_location_assignments) + len(completed_location_safety_assignments)
            
            #get location completed course hours
            location_completed_course_hours = 0
            if len(completed_location_assignments) is not 0:
                location_completed_course_hours = completed_location_assignments.aggregate(all_hours=Sum('course__hours'))['all_hours']
            if len(completed_location_safety_assignments) is not 0:                        
                location_completed_course_hours += completed_location_safety_assignments.aggregate(all_hours=Sum('course__hours'))['all_hours']
            
            #get completed percentage and location completed percentage
            if all_course_count is not 0:
                my_percent = int(completed_course_count / float(all_course_count) * 100)
            else:
                my_percent = 0
            if location_assigned_course_count is not 0:
                location_percent = int(completed_location_assigned_course_count / float(location_assigned_course_count) * 100)
            else:
                location_percent = 0
            
            #get my test attempts and location test attempts            
            t1 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=0, assignment_id__in=assignments.values_list('id', flat=True), passed=True).exclude(test__type__id=3)
            t2 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=1, assignment_id__in=safety_assignments.values_list('id', flat=True), passed=True).exclude(test__type__id=3)
            
            #get my gpa(average of grade point)
            my_gpa = 0
            cch = 0
            if len(t1) is not 0:
                my_gpa = t1.aggregate(sum_grade=Sum('grade_points'))['sum_grade']
                # we need to calculate completed course hours again(except test type ==3)
                cch = t1.aggregate(all_hours=Sum('test__course__hours'))['all_hours']
            if len(t2) is not 0:
                my_gpa += t2.aggregate(sum_grade=Sum('grade_points'))['sum_grade']
                cch += t2.aggregate(all_hours=Sum('test__course__hours'))['all_hours']
                            
            if cch is not 0:
                my_gpa = my_gpa / cch
            my_gpa = math.floor(float(my_gpa)*100+0.5)/float(100)           
            
            l_t1 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=0, assignment_id__in=location_assignments.values_list('id', flat=True), passed=True).exclude(test__type__id=3)
            l_t2 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=1, assignment_id__in=location_safety_assignments.values_list('id', flat=True), passed=True).exclude(test__type__id=3)
            
            #get location gpa(average of grade point)
            location_gpa = 0
            location_cch = 0
            if len(l_t1) is not 0:                
                location_gpa = l_t1.aggregate(sum_grade=Sum('grade_points'))['sum_grade']
                location_cch = l_t1.aggregate(all_hours=Sum('test__course__hours'))['all_hours']
            if len(l_t2) is not 0:
                location_gpa += l_t2.aggregate(sum_grade=Sum('grade_points'))['sum_grade']
                location_cch += l_t2.aggregate(all_hours=Sum('test__course__hours'))['all_hours']
                
            if location_cch is not 0:
                location_gpa = location_gpa / location_cch
            #math.floor(float(location_gpa)*100+0.5)/float(100)           
            
            #get my test average grade location Test Averaage Grade
            grade_value = math.floor(float(my_gpa)*10+0.5)/float(10)
            if int(grade_value) is not 0:
                obj = UtilGradingScales.objects.filter(gpa = grade_value)
                if len(obj) > 0:
                    my_avg_test_grade = UtilGradingScales.objects.filter(gpa = grade_value)[0].letter_grade
                else:
                    my_avg_test_grade = 'A'
            else:
                my_avg_test_grade = 'A'
            
            grade_value = math.floor(float(location_gpa)*10+0.5)/float(10)
            if int(grade_value) is not 0:
                obj = UtilGradingScales.objects.filter(gpa = grade_value)
                if len(obj) > 0:
                    location_avg_test_grade = obj[0].letter_grade
                else:
                    location_avg_test_grade = 'A'
            else:
                location_avg_test_grade = 'A'
            
            #get average test attempts and location average test attempts
            avg_test_attempts = len(t1) + len(t2)
            if avg_test_attempts != 0: 
                ta1 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=0, assignment_id__in=assignments.values_list('id', flat=True))
                ta2 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=1, assignment_id__in=safety_assignments.values_list('id', flat=True))            
                avg_test_attempts = math.floor(float( (len(ta1)+len(ta2)) / float(avg_test_attempts)) * 10 + 0.5) / 10
            
            location_avg_test_attempts = len(l_t1) + len(l_t2)
            if location_avg_test_attempts != 0:
                l_ta1 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=0, assignment_id__in=location_assignments.values_list('id', flat=True))
                l_ta2 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=1, assignment_id__in=location_safety_assignments.values_list('id', flat=True))
                
                location_avg_test_attempts = math.floor((len(l_ta1)+len(l_ta2)) / float(location_avg_test_attempts) * 10 + 0.5) / 10
            
            
            #calculating montly safety course history data
            
            cur_datetime = convert_timezone(datetime.now(), request.user)            
            
            '''
            module_ids = [1,2]
            modules = CoreUserProfilesModules.objects.filter(coremodules_id__in=module_ids, coreuserprofiles=user_profile.id)
            
            active_months = []
            
            for module in modules:
                if module.active_inactive == 1:
                    active_months.append(module.date.month)
                        
            if len(modules) is not 0:
            '''
            user_assignments = []
            if cur_datetime.month == 12:
                end_date = date(cur_datetime.year+1, 1, 1) - timedelta(days=1)
            else:                
                end_date = date(cur_datetime.year, cur_datetime.month+1, 1) - timedelta(days=1)
            
            if end_date.month == 12:
                start_date = date(end_date.year, 1, 1)
            else:
                start_date = date(end_date.year-1, end_date.month+1, 1)
            
            #get user safety assignment
            user_safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile_id=user_profile.id, date_assigned__lte=end_date, date_assigned__gte=start_date)            
            
            tmpdate = start_date            
            for i in xrange(1, 13):
                obj = {'year': tmpdate.year, 'month':tmpdate.strftime('%b'), 'course_id': '', 'value': -1}                                
                user_assignments.append(obj)
                tmpdate = tmpdate + timedelta(31)
                
            
            cur_index = 11-cur_datetime.month
            
            
            for assignment in user_safety_assignments:                
                # except for aknowledge test
                #if test_attempt.test.type.id != 3:             
                if assignment.is_completed == True and assignment.date_completed is not None:
                    test_attempt = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=1, assignment_id = assignment.id, passed=True, user_id=request.user.id)[0]                    
                    if test_attempt.completed_by_due_date == True: #or assignment.date_completed <= assignment.due_date:
                        user_assignments[(assignment.date_assigned.month + cur_index)%12]['value'] = 1                        
                    else:
                        user_assignments[(assignment.date_assigned.month + cur_index)%12]['value'] = 2                    
                else:
                    user_assignments[(assignment.date_assigned.month + cur_index)%12]['value'] = 0
                user_assignments[(assignment.date_assigned.month + cur_index)%12]['course_id'] = assignment.course.number
                    
            
            #get trending grade point average
            
            #get monthly my gpas
            my_gpa_hours = []
            my_gpas = []
            
            tmpdate = start_date            
            for i in xrange(1, 13):                
                obj = {'year': tmpdate.year, 'month':tmpdate.strftime('%b'), 'value': 0}                 
                my_gpas.append(obj)
                my_gpa_hours.append(0)
                tmpdate = tmpdate + timedelta(31)
            
            cur_index = 11-cur_datetime.month
            for test_attempt in t1:
                assignment = CoreUserAssignments.objects.get(id=test_attempt.assignment_id)
                my_gpa_hours[(assignment.date_completed.month + cur_index)%12] += test_attempt.test.course.hours
                if assignment.date_completed is not None and assignment.date_completed > assignment.date_assigned:
                    my_gpas[(assignment.date_completed.month + cur_index)%12]['value'] += test_attempt.grade_points
            
            for test_attempt in t2:
                assignment = CoreUserSafetyAssignments.objects.get(id=test_attempt.assignment_id)
                my_gpa_hours[(assignment.date_completed.month + cur_index)%12] += test_attempt.test.course.hours
                if assignment.date_completed is not None and assignment.date_completed > assignment.date_assigned:
                    my_gpas[(assignment.date_completed.month + cur_index)%12]['value'] += test_attempt.grade_points
            
            for i in xrange(0, 12):
                if my_gpa_hours[i] is not 0:
                    my_gpas[i]['value'] = my_gpas[i]['value'] / my_gpa_hours[i]
            
            #get location gpas
            location_gpa_hours =[]
            location_gpas = []
            
            tmpdate = start_date            
            for i in xrange(1, 13):                
                obj = {'year': tmpdate.year, 'month':tmpdate.strftime('%b'), 'value': 0}                 
                location_gpas.append(obj)
                location_gpa_hours.append(0)
                tmpdate = tmpdate + timedelta(31)
            
            cur_index = 11-cur_datetime.month
            for test_attempt in l_t1:
                assignment = CoreUserAssignments.objects.get(id=test_attempt.assignment_id)
                location_gpa_hours[(assignment.date_completed.month + cur_index)%12] += test_attempt.test.course.hours
                if assignment.date_completed is not None and assignment.date_completed > assignment.date_assigned:
                    location_gpas[(assignment.date_completed.month + cur_index)%12]['value'] += test_attempt.grade_points
            
            for test_attempt in l_t2:
                assignment = CoreUserSafetyAssignments.objects.get(id=test_attempt.assignment_id)
                location_gpa_hours[(assignment.date_completed.month + cur_index)%12] += test_attempt.test.course.hours
                if assignment.date_completed is not None and assignment.date_completed > assignment.date_assigned:
                    location_gpas[(assignment.date_completed.month + cur_index)%12]['value'] += test_attempt.grade_points
            
            for i in xrange(0, 12):
                if location_gpa_hours[i] is not 0:
                    location_gpas[i]['value'] = location_gpas[i]['value'] / location_gpa_hours[i]
            
            
            # finalizing our output content.
            content = {
                # this node will have all organization related data
                'metrics': {'assigned_course_count': all_course_count,
                            'completed_course_count': completed_course_count,
                            'assigned_course_hours': assigned_course_hours,
                            'completed_course_hours': completed_course_hours,
                            'my_percent': my_percent,
                            'location_percent': location_percent,
                            'my_gpa': my_gpa,
                            'location_gpa': location_gpa,
                            'my_avg_test_grade': my_avg_test_grade,
                            'location_avg_test_grade': location_avg_test_grade,
                            'my_avg_test_attempts': avg_test_attempts,
                            'location_avg_test_attempts': location_avg_test_attempts,                            
                            },
                'safety_course_history': user_assignments,
                'gpa_charts_data': {'my_gpas': my_gpas,
                                    'location_gpas': location_gpas,
                                    }
            }

        except Exception as e:

            # set data to None
            assignments = None

            # sending blank data to serializer.
            assignments_serializer = CoreUserAssignmentsSerializer(assignments)

            # set data to None
            safety_assignments = None

            # sending blank data to serializer.
            safety_assignments_serializer = CoreUserAssignmentsSerializer(safety_assignments)

            # finalizing our output content.
            content = {
                # this node will have all organization related data
                'data': {'assignments': assignments_serializer.data, 'safety_assignments': safety_assignments_serializer.data},
    
            }

        # sending final response.
        return Response(content)
