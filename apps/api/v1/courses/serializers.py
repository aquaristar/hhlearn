from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import serializers

from apps.dashboard.models import *

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *
from apps.api.v1.documents.views import *

from datetime import datetime, timedelta

# This serializer class will use objectives model and will map the objects.
class ObjectivesSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField('get_description')
    
    class Meta:
        model = CoreObjectives
    
    def get_description(self, obj):
        description = replace_tags(self.context['request'], obj.description)
        return description
        # fields = ('id', 'description')


# This serializer class will use objectives model and will map the objects.
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreImages
        # fields = ('id', 'description')


# This serializer class will use objectives model and will map the objects.
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreVideos
        # fields = ('id', 'description')


# This serializer class will use objectives model and will map the objects.
class GlossaryWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreGlossaryWords
        # fields = ('id', 'description')


# This serializer class will use objectives model and will map the objects.
class ReferralAgenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreReferralAgencies
        # fields = ('id', 'description')


# This serializer class will use objectives model and will map the objects.
class CorePagesSerializer(serializers.ModelSerializer):
    raw_html = serializers.SerializerMethodField('get_raw_html')
    resources = serializers.SerializerMethodField('get_resources')
    
    class Meta:
        model = CorePages
        # fields = ('id', 'description')
    
    def get_raw_html(self, obj):
        return replace_tags(self.context['request'], obj.raw_html)
    
    def get_resources(self, obj):
        resources = get_replace_resources(obj.raw_html)
        if resources is not 0:
            resources = ResourcesSerializer(resources)
            resources = resources.data
        return resources        


# This class will map all the objects we pass
class CourseSerializer(serializers.ModelSerializer):
    # courses have many to many relation to objectives so we will make another serializer for objectives and pass objectives into it.
    # many=true defines manay to many relation.
    appendix = serializers.SerializerMethodField('get_appendix')
    objectives = serializers.SerializerMethodField('get_objectives')
    images = ImagesSerializer(many=True)
    #videos = serializers.SerializerMethodField('get_videos')
    glossary_words = GlossaryWordsSerializer(many=True)
    referral_agencies = ReferralAgenciesSerializer(many=True)
    # regulations are stored in util tables so we need to get regulation using short_code and add it to courses object.
    # this method will execute and return regulations.
    regulations = serializers.SerializerMethodField('get_regulations')
    # we will get the page content using  "get_pages" method.
    page = serializers.SerializerMethodField('get_page')
    #pages = CorePagesSerializer(many=False)
    # we have access to self.context in methods so this method will only return the current page which we passed  in class APICourses get method
    currentPage = serializers.SerializerMethodField('get_current_page')
    # we have access to self.context in methods so this method will only return the current page which we passed  in class APICourses get method
    totalPages = serializers.SerializerMethodField('get_total_pages')    
    user_notes = serializers.SerializerMethodField('get_user_notes')    
    long_description = serializers.SerializerMethodField('get_long_description')    
    description = serializers.SerializerMethodField('get_description')    
    accreditation = serializers.SerializerMethodField('get_accreditation')
    
    # just setting the modal for this serializer.
    class Meta:
        model = CoreCourses
    # fields = ('id', 'name', 'number', 'description')
    
    # regulations are stored in util table. So we need to get those using short_code.
    #@staticmethod    
    def get_regulations(self, obj):
        # first we are getting course from  "UtilCourses" using short_code and the it's regulations.
        # Regulations are not modified by users to we are using util table.

        user = self.context['request'].user
        location = user.core_user_profile.location
        state = location.state
        state_reg_ids = UtilRegAgencyRegulationsByState.objects.filter(states=state).values_list('util_reg_agency_regulations_id', flat=True)

        current_page = self.get_current_page(obj)
        if current_page is 0:
            regulations = CoreCourses.objects.get(short_name=obj.short_name).regulations.filter(is_active=1, is_federal=1).order_by('reg_code')
            state_regulations = CoreCourses.objects.get(short_name=obj.short_name).regulations.filter(is_active=1, id__in=state_reg_ids).order_by('reg_code')
            regulations = regulations | state_regulations
            #regulations = state_regulations
        else:
            regulations = []
        if regulations:
            return regulations.values()
        return []
    
    def get_appendix(self, obj):        
        appendix = replace_tags(self.context['request'], obj.appendix)
        return appendix
    
    def get_videos(self, obj):
        videos = obj.resources.filter(is_video=1)
        if len(videos) is not 0:
            videos = ResourcesSerializer(videos)
            videos = videos.data
        return videos 
    
    def get_accreditation(self, obj):        
        current_page = self.get_current_page(obj)
        data = dict()        
        if current_page is 0:             
            request = self.context['request']
            profile = request.user.core_user_profile
            if profile.department_id is not None:                
                container = profile.department               
            else:                
                container = profile.location            
            if container.is_accredited_id == 1:
                data['enabled'] = 1
                accreditation_agency = container.accreditation_agency
                st_data = []                
                
                if accreditation_agency is not None:
                    data['agency_name'] = accreditation_agency.name
                    #case agency id is 11
                    if accreditation_agency.id == 11:
                        standards = CoreCoursesAccreditationStandardsAchc11.objects.filter(courses__id=obj.id)
                        for standard in standards:
                            st_data.append(standard.achc.standard_number)                    
                    
                    elif accreditation_agency.id == 9:
                        element_ids = CoreCoursesAccreditationStandardsTjc9.objects.filter(courses__id=obj.id).values_list('tjc_elements_id', flat=True)
                        elements = AccreditingAgencyTjcElements.objects.filter(id__in=element_ids)
                        standards = elements.values('util_accrediting_agency_tjc_standards')\
                                    .annotate(dcount=Count('util_accrediting_agency_tjc_standards'))
                        for standard_ids in standards:
                            standard = AccreditingAgencyTjcStandards.objects.get(id=standard_ids['util_accrediting_agency_tjc_standards'])
                            str_standard = standard.standard_number
                            elements = AccreditingAgencyTjcElements.objects.filter(id__in=element_ids, util_accrediting_agency_tjc_standards__id=standard.id)
                            
                            for element in elements:
                                str_standard = str_standard + ', ' + element.element_of_performance_number
                            
                            st_data.append(str_standard)
                            
                    elif accreditation_agency.id == 586:
                        standards = CoreCoursesAccreditationStandardsHqaa586.objects.filter(courses__id=obj.id)
                        for standard in standards:
                            st_data.append(standard.hqaa.standard_number)
                    
                    elif accreditation_agency.id == 587:
                        element_ids = CoreCoursesAccreditationStandardsCteam587.objects.filter(courses__id=obj.id).values_list('cteam_evidence_of_compliance_id', flat=True)
                        elements = AccreditingAgencyCteamEvidenceOfCompliance.objects.filter(id__in=element_ids)
                        standards = elements.values('accrediting_agency_cteam_standards')\
                                    .annotate(dcount=Count('accrediting_agency_cteam_standards'))
                        for standard_ids in standards:
                            standard = AccreditingAgencyCteamStandards.objects.get(id=standard_ids['accrediting_agency_cteam_standards'])
                            str_standard = standard.standard_number
                            elements = AccreditingAgencyCteamEvidenceOfCompliance.objects.filter(id__in=element_ids, accrediting_agency_cteam_standards__id=standard.id)
                            
                            for element in elements:
                                str_standard = str_standard + ', ' + element.evidence_of_compliance_number
                            
                            st_data.append(str_standard)
                    
                    elif accreditation_agency.id == 588:
                        element_ids = CoreCoursesAccreditationStandardsBoc588.objects.filter(courses__id=obj.id).values_list('boc_standards_id', flat=True)
                        elements = AccreditingAgencyBocStandards.objects.filter(id__in=element_ids)
                        standards = elements.values('accrediting_agency_boc')\
                                    .annotate(dcount=Count('accrediting_agency_boc'))
                        for standard_ids in standards:
                            standard = AccreditingAgencyBoc.objects.get(id=standard_ids['accrediting_agency_boc'])
                            str_standard = standard.standard_number
                            elements = AccreditingAgencyBocStandards.objects.filter(id__in=element_ids, accrediting_agency_boc__id=standard.id)
                            
                            for element in elements:
                                str_standard = str_standard + ', ' + element.sub_standard_number
                            
                            st_data.append(str_standard)                    
                
                    data['standards'] = sorted(st_data)
                    
                else:
                    data['enabled'] = 0                                            
            else:
                data['enabled'] = 0
        else:
            data['enabled'] = 0                    
                
        return data
    
    def get_objectives(self, obj):
        current_page = self.get_current_page(obj)
        if current_page is 0:
            return ObjectivesSerializer(obj.objectives.all(), context={'request': self.context['request']}).data
        else:
            return None
        
    def get_page(self, obj):
        # first we getting course from  "UtilCourses" using short_code and the it's pages.
        # pages are NOT modified by user so we just use util table.
        page = CoreCourses.objects.get(short_name=obj.short_name).pages.filter(is_active=1, page_number=self.context[
            'page_number'])

        page_serializer = CorePagesSerializer(page, context={'request': self.context['request'], 'course': obj})

        #glossary_words = CoreCourses.objects.get(short_name=obj.short_name).glossary_words.all().values()
        #for page in pages:
            #page['raw_html'] = highlight_glossary_words(glossary_words, page['raw_html'])
            #page['raw_html'] = replace_tags(self.context['request'], page['raw_html'])
        # raw_html = list(page)[0]['raw_html']
        # list(page)[0]['raw_html'] = highlight_glossary_words(raw_html)
        return page_serializer.data    

    def get_current_page(self, obj):
        # just return the current page.
        current_page = int(self.context['page_number'])
        return current_page
    
    def get_user_notes(self, obj):
        user_note = CoreCoursesNote.objects.filter(user=self.context['request'].user, courses_id=obj.id)
        if len(user_note) is 0:
            return None
        else:
            notes = user_note[0].notes
        return notes
    
    def get_long_description(self, obj):
        description = replace_tags(self.context['request'], obj.long_description)
        return description

    def get_description(self, obj):
        description = replace_tags(self.context['request'], obj.description)
        return description

    @staticmethod
    def get_total_pages(obj):
        # just return the total number of pages.
        total_pages = CoreCourses.objects.get(short_name=obj.short_name).pages.filter(is_active=1).count()
        return total_pages

# This class will map all the objects we pass
class OrganizationSerializer(serializers.ModelSerializer):
    # just setting the modal for this serializer.
    class Meta:
        model = CoreOrganizations

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilUSAStates

# This class will map all the objects we pass
class LocationSerializer(serializers.ModelSerializer):
    # just setting the modal for this serializer.
    state = StateSerializer(many=False)
    class Meta:
        model = CoreLocations


# This class will map all the objects we pass
class JobTitleSerializer(serializers.ModelSerializer):
    # just setting the modal for this serializer.
    class Meta:
        model = CoreJobTitles


# This class will map all the objects we pass
class DepartmentSerializer(serializers.ModelSerializer):
    # just setting the modal for this serializer.
    class Meta:
        model = CoreDepartments

class FontSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilFontSizes

# This class will map all the objects we pass
class UserProfileSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False)
    job_title = JobTitleSerializer(many=False)
    department = DepartmentSerializer(many=False)    
    fontsize = FontSizeSerializer(many=False)    
    all_fontsizes = serializers.SerializerMethodField('get_font_sizes_list')
    # just setting the modal for this serializer.
    class Meta:
        model = CoreUserProfiles
    
    def get_font_sizes_list(self, obj):
        sizes = UtilFontSizes.objects.all()
        sizes_data = FontSizeSerializer(sizes)        
        return sizes_data.data
        

# This class will map all the objects we pass
class UtilStateCellPhoneLawsSerializer(serializers.ModelSerializer):
    # just setting the modal for this serializer.
    class Meta:
        model = UtilStateCellPhoneLaws()

class CoursesListSerializer(serializers.ModelSerializer):
    has_assignment = serializers.SerializerMethodField('check_has_assignment')
    class Meta:
        model = CoreCourses
        fields = ('id', 'number', 'name', 'has_assignment')

    def check_has_assignment(self, obj):
        assignments = CoreUserAssignments.objects.filter(user_profile=self.context['user_profile'], course_id=obj.id).exclude(is_completed=True)
        if len(assignments) > 0:
            return "&#8226;"
        assignments = CoreUserAssignments.objects.filter(user_profile=self.context['user_profile'], course_id=obj.id, is_completed=True)
        if len(assignments) > 0:
            return "&diams;"

        return ""
