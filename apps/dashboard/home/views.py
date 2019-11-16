from django.shortcuts import render
from apps.dashboard.models import *

import math

from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg

def index(request):
    
    #get assignment url and count
    
    user_profile = request.user.core_user_profile
    assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True, course__is_active=True).exclude(is_completed=True)        
    safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True).exclude(is_completed=True)
    
    assignment_count = len(assignments) + len(safety_assignments)
    
    #get history count
    test_attempts = CoreTestAttempts.objects.filter(user=request.user).values('test').annotate(dcount=Count('test'))    
    inservices = CoreInservicesCompleted.objects.all()
    external_courses = CoreExternalCoursesCompleted.objects.all()
    
    history_count = len(test_attempts) + len(inservices) + len(external_courses);
    
    #get Metrics count
    
    assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True)        
    safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True)
    
    completed_assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True, is_completed=True)            
    completed_safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True, is_completed=True)
               
    t1 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=0, assignment_id__in=assignments.values_list('id', flat=True), passed=True).exclude(test__type__id=3)
    t2 = CoreTestAttempts.objects.filter(test__course__monthly_safety_course_id=1, assignment_id__in=safety_assignments.values_list('id', flat=True), passed=True).exclude(test__type__id=3)
    
    my_gpa = 0
    cch = 0
    
    if len(t1) is not 0:
        my_gpa = t1.aggregate(sum_grade=Sum('grade_points'))['sum_grade']
        cch = t1.aggregate(all_hours=Sum('test__course__hours'))['all_hours']
    if len(t2) is not 0:
        my_gpa += t2.aggregate(sum_grade=Sum('grade_points'))['sum_grade']
        cch += t2.aggregate(all_hours=Sum('test__course__hours'))['all_hours']
                    
    if cch is not 0:
        my_gpa = my_gpa / cch
    my_gpa = math.floor(float(my_gpa)*100+0.5)/float(100)
    
    grade_value = math.floor(float(my_gpa)*10+0.5)/float(10)
    
    if int(my_gpa) is not 0:
        obj = UtilGradingScales.objects.filter(gpa = grade_value)
        if len(obj) > 0:
            my_avg_test_grade = obj[0].letter_grade
        else:
            my_avg_test_grade = 'A'
        metrics_count = my_avg_test_grade
    else:
        metrics_count = 'A'
    
    #get messages count
    messages = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_message=1, message_alert_cleared_id=0,
                                                            date_acknowledged_UTC=None, deactivated_date=None)
    message_count = len(messages)
    
    #get alert count
    alerts = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_alert=1, message_alert_cleared_id=0,
                                                            date_acknowledged_UTC=None, deactivated_date=None)
    alert_count = len(alerts)
    
    #get mail count 
    mail_count = 44
    
    #get document count
    try:
        organization = request.user.core_user_profile.core_organization.get(
                user_profiles__id=request.user.core_user_profile.id)    
        documents = CoreResources.objects.filter(coreorganizations_id=organization.id)
        document_count = len(documents)
    except Exception as e:
        document_count = 0
    
    #get accreditation count
    profile = request.user.core_user_profile        
    
    if profile.department_id is not None:                
        container = profile.department               
    else:                
        container = profile.location
    
    if container.is_accredited_id == 1:
        accreditation_agency = container.accreditation_agency
        if accreditation_agency is not None:
            accreditation = accreditation_agency.acronym
        else:
            accreditation = 'TBD'
    else:
        accreditation = 'TBD'
    
    #get task count
    tasks = CoreTasks.objects.filter(user=request.user, date_deativated=None, task_cleared_id=0, date_completed = None)
    task_count = len(tasks)
    
    #get group count
    group_count = 25
    
    count_data = {'assignment': assignment_count,
                  'history': history_count,
                  'metrics': metrics_count,
                  'message': message_count,
                  'alert': alert_count,
                  'mail': mail_count,
                  'document': document_count,
                  'accreditation': accreditation,
                  'task': task_count,
                  'group': group_count
                 }
    
    return render(request, 'dashboard/home/index.html', {'request': request, 'countData': count_data, })

