from rest_framework import serializers

from apps.dashboard.models import *

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *

from apps.api.v1.courses.serializers import *

#serializers

class AgenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilRegAgencies
        fields = ('id', 'name')

class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilUSAStates
        fields = ('id', 'name', 'abbreviation')

class CountyFipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilZipCodes
        fields = ('county_name', 'state_abbr', 'county_fips')

'''
class AgenciesSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    name = serializers.Field()

class StatesSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    name = serializers.Field()
    abbreviation = serializers.Field()

class CountyFipsSerializer(serializers.ModelSerializer):    
    id = serializers.Field()
    city_name = serializers.Field()
    state_abbr = serializers.Field()
    county_fips = serializers.Field()
'''        

class TestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreTestTypes

class AnswersSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField('get_text')
    why_this_choice = serializers.SerializerMethodField('get_explaination')
    class Meta:        
        model = CoreAnswers
    def get_text(self, obj):
        if 'request' in self.context:
            return replace_tags(self.context['request'], obj.text, True)
        else:
            return obj.text
    def get_explaination(self, obj):
        if 'request' in self.context:
            return replace_tags(self.context['request'], obj.why_this_choice, True)
        else:
            return obj.text
        
# This class will map all the objects we pass
class QuestionAnswersSerializer(serializers.ModelSerializer):    
    # just setting the modal for this serializer.
    coreanswers = serializers.SerializerMethodField('get_answer')    
    class Meta:
        model = CoreQuestionAnswers
    def get_answer(self, obj):
        if 'request' in self.context:
            answer = AnswersSerializer(obj.coreanswers, context={'request':self.context['request']}).data
        else:
            answer = AnswersSerializer(obj.coreanswers).data
        return answer

class QuestionTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreQuestionTypes      

class QuestionsSerializer(serializers.ModelSerializer):    
    # just setting the modal for this serializer.
    type = QuestionTypesSerializer(many=False)
    answers = serializers.SerializerMethodField('get_question_answers')
    text = serializers.SerializerMethodField('get_question_text')
    
    class Meta:
        model = CoreQuestions
    
    def get_question_answers(self, obj):        
        answers = obj.answers
        answers_list = []
        for answer in answers:
            if 'request' in self.context:
                answers_list.append(QuestionAnswersSerializer(answer, context={'request':self.context['request']}).data)
            else:
                answers_list.append(QuestionAnswersSerializer(answer).data)
        return answers_list
    
    def get_question_text(self, obj):
        if 'request' in self.context:
            return replace_tags(self.context['request'], obj.text, True)
        else:
            return obj.text
'''
class QuestionsMiniSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_question_type')       
    class Meta:        
        model = CoreQuestions
        fields = ('id', 'type', 'text', 'is_active')
    
    def get_question_type(self, obj):        
        return obj['type']
'''
            
class QuestionsMiniSerializer(serializers.ModelSerializer):           
    class Meta:        
        model = CoreQuestions
        
class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreCourses
        fields = ('id', 'number', 'name', 'number_test_questions', 'requires_additional_documentation')

class TestSerializer(serializers.ModelSerializer):
    course = CourseMiniSerializer(many=False)
    #course_id = serializers.SerializerMethodField('get_course_id')
    #course_questions = serializers.SerializerMethodField('get_course_questions')
    type = TestTypeSerializer(many=False)
    pool = serializers.SerializerMethodField('get_pool_questions_count')
            
    class Meta:
        model = CoreTests
        
    def get_pool_questions_count(self, obj):
        questions = CoreQuestions.objects.filter(test_id=obj.id, is_active=1)
        return len(questions)
    
class TempTestAttemptSerializer(serializers.ModelSerializer):
    test = TestSerializer(many=False)    
    current_question = serializers.SerializerMethodField('get_current_question')    
    cur_total_questions_count = serializers.SerializerMethodField('get_total_questions_count')    
    min_score = serializers.SerializerMethodField('get_min_score')    
    location_name = serializers.SerializerMethodField('get_location')
    
    class Meta:
        model = CoreTempTestAttempts
    
    def get_current_question(self, obj): 
        if obj.test.type.id == 3:
            return None       
        cur_question_id = int(self.context['cur_question_id'])        
        cur_question = CoreQuestions.objects.get(id=cur_question_id)        
        question_serializer = QuestionsSerializer(cur_question, context={'request':self.context['request']})
        return question_serializer.data
    
    def get_total_questions_count(self, obj):        
        if obj.current_test_attempt_number == 1:
            count = obj.total_questions_count
        else:
            questions = CoreTempQuestionAnswersAttempts.objects.filter(temp_test_attempt_id=obj.id, passed=False)
            count = len(questions)        
        return count

    def get_min_score(self, obj):        
        user = self.context['request'].user        
        #get user profile
        profile = user.core_user_profile
        if profile.department_id is not None:                
            min_passing_score = profile.department.min_score_general_knowledge                
        else:                
            min_passing_score = profile.location.min_score_general_knowledge            
        return min_passing_score.score
    
    def get_location(self, obj):
        location_name = '{{LOCATION:NAME}}'        
        location_name =  replace_tags(self.context['request'], location_name)        
        return location_name