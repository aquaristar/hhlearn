from rest_framework import serializers

from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.views import *
from apps.api.v1.utils.helpers import *

from apps.dashboard.models import *
from datetime import *

# Course serializer.
class CourseSerializer(serializers.ModelSerializer):    
    description = serializers.SerializerMethodField('get_description')    
    class Meta:
        # model we want to use with serializer.
        model = CoreCourses
        fields = ('id', 'number', 'name', 'hours', 'continuing_education', 'description', 'monthly_safety_course')
    
    def get_description(self, obj):
        description = replace_tags(self.context['request'], obj.description)
        return description


# user assignment serializer.
class CoreUserAssignmentsSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField('get_course')
    # flag to check overdue assignment.
    is_overdue = serializers.SerializerMethodField('check_if_overdue')
    prerequisite = serializers.SerializerMethodField('check_can_resume')
    class Meta:
        # model we want to use with serializer.
        model = CoreUserAssignments
    # need to check if assignment is overdue or not?
    def check_if_overdue(self, obj):
        if obj.due_date < datetime.today().date():
            return True
        else:
            return False
    def check_can_resume(self, obj):
        parent_courses = CoreCoursesPrerequisite.objects.filter(child_courses=obj.course)
        if len(parent_courses) > 0:
            return {'name': parent_courses[0].parent_courses.name, 'number':parent_courses[0].parent_courses.number}  
        return None
    def get_course(self, obj):
        return CourseSerializer(obj.course, context=self.context).data

# user safety assignment serializer.
class CoreUserSafetyAssignmentsSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField('get_course')
    # flag to check overdue assignment.
    is_overdue = serializers.SerializerMethodField('check_if_overdue')
    prerequisite = serializers.SerializerMethodField('check_can_resume')
    class Meta:
        # model we want to use with serializer.
        model = CoreUserSafetyAssignments
    # need to check if assignment is overdue or not?
    def check_if_overdue(self, obj):
        if obj.due_date < datetime.today().date():
            return True
        else:
            return False
    def check_can_resume(self, obj):
        parent_courses = CoreCoursesPrerequisite.objects.filter(child_courses=obj.course)
        if len(parent_courses) > 0:
            return {'name': parent_courses[0].parent_courses.name, 'number':parent_courses[0].parent_courses.number}  
        return None
    def get_course(self, obj):
        return CourseSerializer(obj.course, context=self.context).data