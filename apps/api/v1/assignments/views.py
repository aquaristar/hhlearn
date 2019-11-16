from django.views.generic import View
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.api.v1.assignments.serializers import *
from django.http import Http404
from rest_framework import status

from apps.dashboard.models import *

from datetime import *


# Class based view for profile page.
class Assignments(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):
        user_id = self.request.QUERY_PARAMS.get('user_id', None)
        try:
            # need to get logged in user.
            if user_id is not None and user_id != "":
                user_profile = CoreUserProfiles.objects.get(id=user_id)
            else:
                user_profile = request.user.core_user_profile

            assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True, course__is_active=True).exclude(is_completed=True)
            # sending logged in user data to serializer.
            assignments_serializer = CoreUserAssignmentsSerializer(assignments, context={'request': request})
            safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True, course__is_active=True).exclude(is_completed=True)
            # sending logged in user data to serializer.
            safety_assignments_serializer = CoreUserSafetyAssignmentsSerializer(safety_assignments, context={'request': request})
        except:
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

    def post(self, request, format=None):

        course_id = self.request.DATA.get('course_id', None)
        user_profile_id = self.request.DATA.get('user_id', None)
        over_due = self.request.DATA.get('over_due', None)


        if course_id is not None and user_profile_id is not None and over_due is not None:
            try:
                # need to get logged in user.
                user_profile = CoreUserProfiles.objects.get(id=user_profile_id)
#                cur_date = datetime.now()
                over_due = datetime.strptime(over_due, '%Y/%m/%d')
                assignment = CoreUserAssignments.objects.create(user_profile=user_profile,
                                                                course_id=course_id,
                                                                due_date=over_due.date(),
                                                                is_active=True)
                assignment.save()
                CoreUserAssignmentsModifications.objects.create(assignments=assignment,
                                                                performed_by_user=request.user,
                                                                change_or_deactivte_id=1)
                assignment_data = CoreUserAssignmentsSerializer(assignment, context={'request': request}).data
            except:
                response = response_profile_save_successful()
                raise ExceptionUnknownError(detail=response)
            # finalizing our output content.
            content = {  # sending success response
                        'status': 'success',
                         'response': assignment_data,
            }
        else:
            content = {'status': 'fail',
                       'response': 'CourseId should be defined!'
                       }

        # sending final response.
        return Response(content)

# Class based view for profile page.
class AssignmentDetail(APIView):
    def get_object(self, pk):
        try:
            return CoreUserAssignments.objects.get(pk=pk)
        except CoreUserAssignments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        assignment = self.get_object(pk)
        serializer = CoreUserAssignmentsSerializer(assignment, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        assignment = self.get_object(pk)
        over_due = self.request.DATA.get('over_due', None)
        over_due = datetime.strptime(over_due, '%Y/%m/%d')
        assignment.due_date = over_due.date()
        #serializer = CoreUserAssignmentsSerializer(assignment, data=request.DATA)
        try:
            assignment.save()
            CoreUserAssignmentsModifications.objects.create(assignments=assignment,
                                                                performed_by_user=request.user,
                                                                change_or_deactivte_id=2)

            #serializer.save()
            serializer = CoreUserAssignmentsSerializer(assignment, context={'request': request})
            return Response({'assignment':serializer.data})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assignment = self.get_object(pk)
        assignment.is_active = False
        assignment.save()
        CoreUserAssignmentsModifications.objects.create(assignments=assignment,
                                                                performed_by_user=request.user,
                                                                change_or_deactivte_id=3)

        return Response(status=status.HTTP_204_NO_CONTENT)
