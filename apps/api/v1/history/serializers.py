from rest_framework import serializers

from apps.dashboard.models import *

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *

from apps.api.v1.courses.serializers import *
from apps.api.v1.tests.serializers import *

class AnswerAttemptSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField('get_question')
    question_answer = QuestionAnswersSerializer(many=False)
    attempt_time = serializers.DateTimeField(source='attempt_time')
    
    class Meta:
        model = CoreQuestionAnswersAttempts
    
    def get_question(self, obj):
        question = QuestionsSerializer(obj.question, context={'request':self.context['request']})
        return question.data
            

# This class will map all the objects we pass
class TestAttemptsSerializer(serializers.ModelSerializer):    
    # just setting the modal for this serializer.
    
    #questions = serializers.SerializerMethodField('get_questions')
    start_time = serializers.SerializerMethodField('get_start_time')
    grade_date_time = serializers.SerializerMethodField('get_grade_date_time') 
    test_type = serializers.SerializerMethodField('get_test_type')          
    
    class Meta:
        model = CoreTestAttempts
    
    def get_start_time(self, obj):        
        return convert_timezone(obj.start_time, self.context['request'].user)
    
    def get_grade_date_time(self, obj):
        return convert_timezone(obj.grade_date_time, self.context['request'].user)
    
    def get_test_type(self, obj):
        return obj.test.type.id
    '''
    def get_questions(self, obj):
        # get questions for this test attempt.
        questions = CoreQuestionAnswersAttempts.objects.filter(test_attempt_id=obj.id)
        questions_list = []
        for question in questions:
            questions_list.append(AnswerAttemptSerializer(question).data)
        
        return questions_list
    '''

# This class will map all the objects we pass
class TestAttemptSerializer(serializers.ModelSerializer):    
    
    course_name = serializers.SerializerMethodField('get_course_name')
    questions = serializers.SerializerMethodField('get_questions')
    total_questions_count = serializers.SerializerMethodField('get_total_questions_count')
    correct_questions_count = serializers.SerializerMethodField('get_correct_questions_count')
    start_time = serializers.SerializerMethodField('get_start_time')
    grade_date_time = serializers.SerializerMethodField('get_grade_date_time') 
    due_date = serializers.SerializerMethodField('get_due_date')   
    
    class Meta:
        model = CoreTestAttempts
    
    def get_course_name(self, obj):        
        return obj.test.course.name

    def get_questions(self, obj):
        # get questions for this test attempt.
        questions = CoreQuestionAnswersAttempts.objects.filter(test_attempt_id=obj.id)
        questions_list = AnswerAttemptSerializer(questions, context={'request':self.context['request']})
        return questions_list.data
    
    def get_total_questions_count(self, object):
        return len(self.fields['questions']._value)
    
    def get_correct_questions_count(self, obj):
        questions = CoreQuestionAnswersAttempts.objects.filter(test_attempt_id=obj.id, question_answer__coreanswers__is_correct=1)
        return len(questions)
    
    def get_start_time(self, obj):        
        return convert_timezone(obj.start_time, self.context['request'].user)
    
    def get_grade_date_time(self, obj):
        return convert_timezone(obj.grade_date_time, self.context['request'].user)
    
    def get_due_date(self, obj):
        if obj.test.course.monthly_safety_course_id == 1:
            assignment = CoreUserSafetyAssignments.objects.get(id=obj.assignment_id)
        else:
            assignment = CoreUserAssignments.objects.get(id=obj.assignment_id)
        return assignment.due_date.strftime("%m/%d/%Y")

class InserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreInservices

class InserviceTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreInserviceTrainers
            
class InserviceCompletedTrainerSerializer(serializers.ModelSerializer):
    inservice_trainers = InserviceTrainerSerializer(many=False)
    class Meta:
        model = CoreInservicesCompletedTrainers
    
                
class CompletedInserviceSerializer(serializers.ModelSerializer):
    inservices = InserviceSerializer(many=False)
    completed_trainer = serializers.SerializerMethodField('get_completed_trainer')
    
    class Meta:
        model = CoreInservicesCompleted
    
    def get_completed_trainer(self, obj):
        completed_trainer = CoreInservicesCompletedTrainers.objects.filter(inservices_completed__id=obj.id)
        trainer = InserviceCompletedTrainerSerializer(completed_trainer)
        return trainer.data

class ExternalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreExternalCourses

class CompletedExternalCourseSerializer(serializers.ModelSerializer):
    external_courses = ExternalCourseSerializer(many=False)
    
    class Meta:
        model = CoreExternalCoursesCompleted