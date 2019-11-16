from rest_framework import serializers

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *

from apps.dashboard.models import *

# course serializer.
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        # model we want to use with serializer.
        model = CoreCourses


# course assignment serializer.
class CoreUserAssignmentsSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    # flag to check overdue assignment.
    is_overdue = serializers.SerializerMethodField('check_if_overdue')

    class Meta:
        # model we want to use with serializer.
        model = CoreUserAssignments

    # need to check if assignment is overdue or not?
    def check_if_overdue(self, obj):
        if obj.due_date < datetime.today().date():
            return True
        else:
            return False


# user profile serializer.
class CoreUserSafetyAssignmentsSerializer(serializers.ModelSerializer):

    course = CourseSerializer()
    # flag to check overdue assignment.
    is_overdue = serializers.SerializerMethodField('check_if_overdue')

    class Meta:
        # model we want to use with serializer.
        model = CoreUserSafetyAssignments

    # need to check if assignment is overdue or not?
    def check_if_overdue(self, obj):
        if obj.due_date < datetime.today().date():
            return True
        else:
            return False