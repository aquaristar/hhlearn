from django.db import models
from django.contrib.auth.models import User
from apps.utility.models import *
from apps.utility.helpers import *
from datetime import datetime



class CoreSettings(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    value = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    is_active = models.NullBooleanField(null=True)

    class Meta():
        db_table = 'core_settings'


class CorePlans(models.Model):
    """
        CorePlans
        """
    description = models.TextField(null=True)
    name = models.CharField(max_length=256, null=True)
    short_code = models.CharField(max_length=256, null=True)
    is_active = models.NullBooleanField(null=True)
    #monthly_price = models.IntegerField(max_length=1, null=True)
    modules = models.ManyToManyField('CoreModules', related_name='core_plans')
    user_packs = models.ManyToManyField('CoreUserPacks', related_name='core_plans')

    class Meta():
        db_table = 'core_plans'


class CoreModules(models.Model):
    name = models.CharField(max_length=255, null=True)
    short_code = models.CharField(max_length=255, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    is_addon = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)

    class Meta():
        db_table = 'core_modules'


class CoreUserPacks(models.Model):
    """
        CoreUserPacks
        """
    description = models.TextField(null=True)
    name = models.CharField(max_length=256, null=True)
    short_code = models.CharField(max_length=256, null=True)
    is_active = models.IntegerField(max_length=1, null=True)
    monthly_price = models.IntegerField(max_length=1, null=True)
    allowed_users = models.IntegerField()

    class Meta():
        db_table = 'core_user_packs'


class CoreBilling(models.Model):
    plan = models.ForeignKey(CorePlans, null=True, related_name='plan')
    user_pack = models.ForeignKey(CoreUserPacks, null=True, related_name='user_pack')
    renewal_term = models.ForeignKey(UtilRenewalTerms, null=True)
    payment_method = models.ForeignKey(UtilPaymentMethods, null=True, related_name='payment_method')
    credit_card_person_name = models.CharField(max_length=256, null=True)
    credit_card_number = models.CharField(max_length=256, null=True)
    card_expiry_month = models.CharField(max_length=256, null=True)
    card_expiry_year = models.CharField(max_length=256, null=True)
    billing_address_1 = models.CharField(max_length=256, null=True)
    billing_address_1 = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=256, null=True)
    zip_code = models.CharField(max_length=256, null=True)
    is_active = models.NullBooleanField(null=True)
    
    class Meta():
        db_table = 'core_billing'


class CoreOfficials(models.Model):
    organization_job_title = models.CharField(max_length=256, null=True)
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    actual_job_title = models.CharField(max_length=256, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=256, null=True)
    official_type = models.ForeignKey(UtilOfficialTypes, null=True, related_name='official_type')
    is_organization_wide = models.IntegerField(null=True)
    is_location_wide = models.IntegerField(null=True)
    is_active = models.NullBooleanField(null=True)
    
    class Meta():
        db_table = 'core_officials'


class CoreDepartments(models.Model):
    short_name = models.CharField(max_length=256, null=True)
    no_of_fire_exists = models.IntegerField(null=True)
    where_written_hazard_located = models.CharField(max_length=256, null=True)
    when_hazard_prog_available = models.CharField(max_length=256, null=True)
    where_safety_data_located = models.CharField(max_length=256, null=True)
    emergency_location = models.CharField(max_length=256, null=True)
    use_electronic_posting = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                               related_name='department_use_electronic_posting')
    is_accredited = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='department_is_accredited')
    hippa_notice_location = models.CharField(max_length=256, null=True)
    accreditation_agency = models.ForeignKey(UtilRegAgencies, null=True, related_name='department_accreditation_agency')
    use_electronic_posting = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                               related_name='department_use_electronic_posting')
    # What is your minimum percent passing score for General Knowledge exams? (These are a majority of all courses on HHLEARN)*
    min_score_general_knowledge = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                    related_name='department_min_score_general_knowledge')
    # What is your minimum percent passing score for courses that have Continuing Education credits?*
    min_score_continuing_education = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                       related_name='department_min_score_continuing_education')
    #What is your minimum percent passing score for Employee Competency exams?*
    min_score_employee_competency = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                      related_name='department_min_score_employee_competency')
    #What is your minimum percent passing score for Custom Courses that only belong to your organization?
    min_score_custom_courses = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                 related_name='department_min_score_custom_courses')
    officials = models.ManyToManyField(CoreOfficials, related_name='core_departments')
    modules = models.ManyToManyField(CoreModules, related_name='core_departments')
    services_offered = models.ManyToManyField('CoreServicesOffered', related_name='core_departments')
    job_titles = models.ManyToManyField('CoreJobTitles', related_name='core_departments')
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_departments'


class CoreLocations(models.Model):
    short_name = models.CharField(max_length=256, null=True)
    street_address_1 = models.CharField(max_length=256, null=True)
    street_address_2 = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)
    state = models.ForeignKey(UtilUSAStates, related_name='state')
    zip_code = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    fax = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=256, null=True)
    modules = models.ManyToManyField(CoreModules, related_name='core_location')
    is_primary = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='is_primary')
    is_command_location = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                            related_name='is_command_location')
    officials = models.ManyToManyField(CoreOfficials, related_name='core_location')
    no_of_fire_exists = models.IntegerField(null=True)
    where_written_hazard_located = models.CharField(max_length=256, null=True)
    when_hazard_prog_available = models.CharField(max_length=256, null=True)
    where_safety_data_located = models.CharField(max_length=256, null=True)
    eer_location = models.CharField(max_length=256, null=True)
    when_eer_available = models.CharField(max_length=256, null=True)
    emr_location = models.CharField(max_length=256, null=True)
    when_emr_available = models.CharField(max_length=256, null=True)
    hippa_notice_location = models.CharField(max_length=256, null=True)
    emergency_location = models.CharField(max_length=256, null=True)
    use_electronic_posting = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                               related_name='use_electronic_posting')
    is_accredited = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='is_accredited')
    accreditation_agency = models.ForeignKey(UtilRegAgencies, null=True, related_name='accreditation_agency')
    # What is your minimum percent passing score for General Knowledge exams? (These are a majority of all courses on HHLEARN)*
    min_score_general_knowledge = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                    related_name='location_min_score_general_knowledge')
    # What is your minimum percent passing score for courses that have Continuing Education credits?*
    min_score_continuing_education = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                       related_name='location_min_score_continuing_education')
    #What is your minimum percent passing score for Employee Competency exams?*
    min_score_employee_competency = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                      related_name='location_min_score_employee_competency')
    #What is your minimum percent passing score for Custom Courses that only belong to your organization?
    min_score_custom_courses = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                 related_name='location_min_score_custom_courses')
    services_offered = models.ManyToManyField('CoreServicesOffered', related_name='core_locations')
    departments = models.ManyToManyField('CoreDepartments', related_name='core_departments')
    departments_enabled = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                            related_name='departments_enabled')
    total_departments = models.IntegerField(null=True)
    job_titles = models.ManyToManyField('CoreJobTitles', related_name='core_locations')
    is_active = models.IntegerField(null=True)
    class Meta():
        db_table = 'core_locations'

class CoreDepartmentsCustomPolicies(models.Model):
    departments = models.ForeignKey(CoreDepartments, related_name='custom_policies')
    custom_policy_title = models.CharField(max_length=255, null=False)
    policies_titles = models.ForeignKey(UtilCustomPoliciesTitles, null=False)
    policy_raw_html	= models.TextField(null=False)
    activation_date = models.DateField(null=False)
    activated_by_user = models.ForeignKey(User, related_name='department_custom_policies_activated_user')
    deactivation_date = models.DateField(null=True)
    deactivated_by_user = models.ForeignKey(User, related_name='department_custom_policies_deactivated_user')
    is_active = models.BooleanField(default=True, null=False)
    class Meta():
        db_table = 'core_departments_custom_policies'

class CoreLocationsCustomPolicies(models.Model):
    locations = models.ForeignKey(CoreLocations, related_name='custom_policies')
    custom_policy_title = models.CharField(max_length=255, null=False)
    policies_titles = models.ForeignKey(UtilCustomPoliciesTitles, null=False)
    policy_raw_html	= models.TextField(null=False)
    activation_date = models.DateField(null=False)
    activated_by_user = models.ForeignKey(User, related_name='location_custom_policies_activated_user')
    deactivation_date = models.DateField(null=True)
    deactivated_by_user = models.ForeignKey(User, related_name='location_custom_policies_deactivated_user')
    is_active = models.BooleanField(default=True, null=False)
    class Meta():
        db_table = 'core_locations_custom_policies'

class CorePointOfContacts(models.Model):
    name = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    type = models.CharField(max_length=256, null=True)
    is_primary = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_point_of_contacts'
        
class CoreUserProfiles(models.Model):
    user = models.OneToOneField(User, related_name='core_user_profile')
    activation_token = models.CharField(max_length=256, null=True)
    requested_welcome_email = models.IntegerField(null=True)
    requested_tos_email = models.IntegerField(null=True)
    modules = models.ManyToManyField(CoreModules, related_name='core_user_profile')
    location = models.ForeignKey('CoreLocations', null=True, related_name='core_user_profile_location')
    department = models.ForeignKey('CoreDepartments', null=True, related_name='core_user_profile_department')
    job_title = models.ForeignKey('CoreJobTitles', null=True, related_name='core_user_profile_job_title')
    region = models.ForeignKey('CoreRegions', null=True, related_name='core_user_profile_region')    
    util_timezones = models.ForeignKey(UtilTimezones, null=True, related_name='core_user_profile_timezone')    
    util_language_iso_codes = models.ForeignKey(UtilLanguageIsoCodes, null=True, related_name='core_user_profile_language')
    _home_address = models.CharField(max_length=256, null=True)
    _home_city = models.CharField(max_length=256, null=True)
    _home_zipcode = models.CharField(max_length=256, null=True)
    home_state = models.ForeignKey(UtilUSAStates, null=True)    
    # curriculums = models.ManyToManyField('CoreCurriculums', related_name='core_user_profile_curriculums')
    subscribe_to_newsletter = models.BooleanField(default=0)    
    _organization_id_number = models.CharField(max_length=256, null=True)    
    _user_social_security_number = models.CharField(max_length=256, null=True)
    _phone_work = models.CharField(max_length=256, null=True)
    _phone_oncall = models.CharField(max_length=256, null=True)
    _phone_alternate = models.CharField(max_length=256, null=True)    
    photo_file = models.CharField(max_length=256, null=True)    
    fontsize = models.ForeignKey(UtilFontSizes, null=True)
    gender = models.ForeignKey(UtilGenders, default=lambda: UtilGenders.objects.get(id=1))
    
    class Meta():
        db_table = 'core_user_profiles'

        permissions = (
            ("is_admin", "Access level set to admin."),
            ("is_moderator", "Access level set to moderator."),
            ("is_member", "Access level set to member."),
            ("is_developer", "Access level set to developer."),
        )
    @property
    def organization_id_number(self):
        return decrypt_str(self._organization_id_number)
    
    @organization_id_number.setter
    def organization_id_number(self, value):        
        self._organization_id_number = encrypt_str(value)
        
    @property
    def phone_work(self):
        return decrypt_str(self._phone_work)

    @phone_work.setter
    def phone_work(self, value):        
        self._phone_work = encrypt_str(value)
        
    @property
    def home_address(self):
        return decrypt_str(self._home_address)

    @home_address.setter
    def home_address(self, value):        
        self._home_address = encrypt_str(value)
        
    @property
    def home_city(self):
        return decrypt_str(self._home_city)

    @home_city.setter
    def home_city(self, value):        
        self._home_city = encrypt_str(value)
    
    @property
    def home_zipcode(self):
        return decrypt_str(self._home_zipcode)

    @home_zipcode.setter
    def home_zipcode(self, value):        
        self._home_zipcode = encrypt_str(value)    
        
    @property
    def user_social_security_number(self):
        return decrypt_str(self._user_social_security_number)

    @user_social_security_number.setter
    def user_social_security_number(self, value):        
        self._user_social_security_number = encrypt_str(value)
    
    @property
    def phone_oncall(self):
        return decrypt_str(self._phone_oncall)

    @phone_oncall.setter
    def phone_oncall(self, value):        
        self._phone_oncall = encrypt_str(value)
        
    @property
    def phone_alternate(self):
        return decrypt_str(self._phone_alternate)

    @phone_alternate.setter
    def phone_alternate(self, value):        
        self._phone_alternate = encrypt_str(value)

class CoreUserProfilesModules(models.Model):    
    coreuserprofiles = models.ForeignKey(CoreUserProfiles, null=True)
    coremodules = models.ForeignKey(CoreModules, null=True, related_name='core_user_profile_module')
    active_inactive = models.BooleanField(default=False)
    date = models.DateField(null=True)        
    class Meta():
        db_table = 'core_user_profiles_modules'

class CoreServicesOffered(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    job_titles = models.ManyToManyField(UtilJobTitles, related_name='core_services_offered')
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_services_offered'


class CoreRegions(models.Model):
    short_name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    locations = models.ManyToManyField(CoreLocations, related_name='region_core_locations')
    departments = models.ManyToManyField(CoreDepartments, related_name='region_core_departments')
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_regions'


class CoreObjectives(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_objectives'
        # def __unicode__(self):
        # return '%d: %s' % (self.id, self.description)


class CoreImages(models.Model):
    file_name = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    short_code = models.CharField(max_length=256, null=True)
    alt = models.TextField(null=True)
    title = models.TextField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    hspace = models.IntegerField(null=True)
    vspace = models.IntegerField(null=True)
    align = models.CharField(max_length=256, null=True)
    source = models.TextField(null=True)
    border = models.IntegerField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_images'


class CoreVideos(models.Model):
    name = models.CharField(max_length=256, null=True)
    short_code = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    duration = models.CharField(max_length=256, null=True)
    cover = models.CharField(max_length=256, null=True)
    title = models.TextField(null=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_videos'


class CoreGlossarySources(models.Model):
    name = models.CharField(max_length=256, null=True)

    class Meta():
        db_table = 'core_glossary_sources'


class CoreGlossaryWords(models.Model):
    word = models.CharField(max_length=256, null=True)
    pronounce = models.CharField(max_length=256, null=True)
    syllable = models.CharField(max_length=256, null=True)
    definition = models.TextField(null=True)
    glossary_source = models.ForeignKey(CoreGlossarySources, null=True, related_name='core_glossary_word_course')
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_glossary_words'
        ordering = ('word',)


class CorePages(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    raw_html = models.TextField(null=True)
    page_number = models.IntegerField(max_length=256, null=True)
    required_time = models.IntegerField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_pages'

class CoreCourseTypes(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_course_types'

class CoreCourseCategories(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    abbreviation = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_course_categories'


class CoreReferralAgencies(models.Model):
    name = models.CharField(max_length=256, null=True)
    acronym = models.CharField(max_length=256, null=True)
    referral_agency_description = models.TextField(null=True)
    address1 = models.CharField(max_length=256, null=True)
    address2 = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=256, null=True)
    zip = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=256, null=True)
    tty_phone = models.CharField(max_length=256, null=True)
    fax = models.CharField(max_length=256, null=True)
    website = models.CharField(max_length=256, null=True)
    email = models.CharField(max_length=256, null=True)
    point_of_contact = models.CharField(max_length=256, null=True)
    point_of_contact_title = models.CharField(max_length=256, null=True)
    point_of_contact_email = models.CharField(max_length=256, null=True)
    point_of_contact_phone = models.CharField(max_length=256, null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_referral_agencies'
        ordering = ('name',)


class CoreCourses(models.Model):
    short_name = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    number = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    long_description = models.TextField(null=True)
    type = models.ForeignKey(CoreCourseTypes, null=True, related_name='core_course_type')
    category = models.ForeignKey(CoreCourseCategories, null=True, related_name='core_course_category')
    referral_agencies = models.ManyToManyField(CoreReferralAgencies, null=True,
                                               related_name='core_course_referral_agencies')
    prerequisite = models.ManyToManyField("self",through='CoreCoursesPrerequisite', symmetrical=False, null=True)
    regulatory_comments = models.CharField(max_length=256, null=True)
    hours = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    continuing_education = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                             related_name='core_course_continuing_education')
    date_loaded = models.DateTimeField(null=True)
    date_last_updated = models.DateTimeField(null=True)
    #number_of_pages = models.IntegerField(null=True)
    number_test_questions = models.IntegerField(null=True)
    has_referral_agencies = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                              related_name='core_course_has_referral_agencies')
    has_appendices = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                       related_name='core_course_has_appendices')
    has_glossary = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='core_course_has_glossary')
    is_annual_course = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                         related_name='core_course_is_annual_course')
    monthly_safety_course = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                              related_name='core_course_monthly_safety_course')
    date_deactivated = models.DateTimeField(null=True)
    annual_start_date = models.DateTimeField(null=True)
    annual_end_date = models.DateTimeField(null=True)
    appendix = models.TextField(null=True)
    objectives = models.ManyToManyField(CoreObjectives, related_name='core_course_objectives')
    regulations = models.ManyToManyField(UtilRegAgencyRegulations, related_name='util_course_regulations')
    pages = models.ManyToManyField(CorePages, related_name='core_course_pages')
    is_custom = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='core_course_is_custom')
    images = models.ManyToManyField(CoreImages, related_name='core_course_images')
    #videos = models.ManyToManyField(CoreVideos, related_name='core_course_images')
    resources = models.ManyToManyField('CoreResources', related_name='core_course_resources')
    glossary_words = models.ManyToManyField(CoreGlossaryWords, related_name='core_courses_glossary_words')
    is_active = models.NullBooleanField(null=True)
    requires_additional_documentation = models.BooleanField(default=False)
    class Meta():
        db_table = 'core_courses'

class CoreAuthors(models.Model):
    author_fullname_or_business = models.CharField(max_length=256, null=True)
    is_active = models.BooleanField(default=True)
    class Meta():
        db_table = 'core_authors'

class CoreCoursesAuthors(models.Model):    
    authors = models.ForeignKey(CoreAuthors, null=False)
    courses = models.ForeignKey(CoreCourses, null=False)
    class Meta():
        db_table = 'core_courses_authors'

class CoreCourseAuthorQualifications(models.Model):
    courses = models.ForeignKey(CoreCourses, null=False)
    authors = models.ForeignKey(CoreAuthors, null=False)
    author_course_qualifications = models.TextField(null=False)
    official_types = models.ForeignKey(UtilOfficialTypes, null=False)
    class Meta():
        db_table = 'core_course_author_qualifications'

class CoreCoursesRegulations(models.Model):
    corecourses = models.ForeignKey(CoreCourses, null=False)
    utilregagencyregulations = models.ForeignKey(UtilRegAgencyRegulations, null=False)
    class Meta():
        db_table = 'core_courses_regulations'

class CoreCoursesResources(models.Model):
    corecourses = models.ForeignKey(CoreCourses)
    coreresources = models.ForeignKey('CoreResources')
    is_active = models.BooleanField(default=True)
    class Meta():
        db_table = 'core_courses_resources'

class CoreJobTitles(models.Model):
    short_code = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    name_possessive = models.CharField(max_length=256, null=True)
    name_custom = models.CharField(max_length=256, null=True)
    name_custom_possessive = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True)
    category = models.ForeignKey(UtilJobCategories, null=True, related_name='job_title_category')
    patient_file_access = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                            related_name='job_title_patient_file_access')
    exposure_to_chemicals = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                              related_name='job_title_exposure_to_chemicals')
    exposure_to_BBP = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                        related_name='job_title_exposure_to_BBP')
    exposure_to_TB = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                       related_name='job_title_exposure_to_TB')
    requires_license = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                         related_name='job_title_requires_license')
    cpr = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='job_title_cpr')
    on_call = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='job_title_on_call')
    flsa_status = models.ForeignKey(UtilFlsaStatus, null=True, related_name='job_title_flsa_status')
    is_custom = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='job_title_is_custom')
    all_occupational_exposure = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                  related_name='job_title_all_occupational_exposure')
    some_occupational_exposure = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                   related_name='job_title_some_occupational_exposure')
    curriculums = models.ManyToManyField('CoreCurriculums', related_name='core_job_title_curriculums')
    safety_curriculums = models.ManyToManyField('CoreSafetyCurriculums',
                                                related_name='core_job_title_safety_curriculums')
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_job_titles'


class CoreCurriculums(models.Model):
    # job_title = models.ForeignKey(CoreJobTitles)
    course = models.ForeignKey(CoreCourses)
    number_of_days = models.IntegerField(null=True)
    date_assigned = models.DateField(auto_now_add=True)
    date_completed = models.DateField(null=True)
    last_started = models.DateField(null=True)
    resume_from_page = models.IntegerField(null=True, default=0)
    user_notes = models.TextField(null=True)
    is_completed = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_curriculums'


class CoreUserAssignments(models.Model):
    user_profile = models.ForeignKey(CoreUserProfiles)
    course = models.ForeignKey(CoreCourses)
    requires_additional_documentation = models.BooleanField(default=False)
    date_assigned = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    date_completed = models.DateField(null=True)
    last_started = models.DateField(null=True)
    resume_from_page = models.IntegerField(null=True, default=0)
    #user_notes = models.TextField(null=True)
    is_completed = models.NullBooleanField(null=True)
    is_started = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_user_assignments'


class CoreUserSafetyAssignments(models.Model):
    user_profile = models.ForeignKey(CoreUserProfiles)
    course = models.ForeignKey(CoreCourses)
    requires_additional_documentation = models.BooleanField(default=False)
    date_assigned = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    date_completed = models.DateField(null=True)
    last_started = models.DateField(null=True)
    resume_from_page = models.IntegerField(null=True, default=0)
    #user_notes = models.TextField(null=True)
    is_completed = models.NullBooleanField(null=True)
    is_started = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_user_safety_assignments'

class CoreUserAssignmentsModifications(models.Model):

    assignments = models.ForeignKey(CoreUserAssignments)
    performed_by_user = models.ForeignKey(User)
    change_or_deactivte = models.ForeignKey(UtilChangeOrDeactivate, null=False)
    date = models.DateTimeField(default=datetime.now)
    class Meta():
        db_table = 'core_user_assignments_modifications'



class CoreSafetyCurriculums(models.Model):
    # job_title = models.ForeignKey(CoreJobTitles)
    course = models.ForeignKey(CoreCourses)
    month_assigned = models.IntegerField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_safety_curriculums'


class CoreAnswers(models.Model):
    text = models.TextField(null=True)
    why_this_choice = models.TextField(null=True)
    is_correct = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_answers'


class CoreTestTypes(models.Model):
    name = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_test_types'


class CoreTests(models.Model):
    course = models.ForeignKey(CoreCourses)
    type = models.ForeignKey(CoreTestTypes)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_tests'

class CoreTestAttempts(models.Model):    
    user = models.ForeignKey(User)    
    test = models.ForeignKey(CoreTests)    
    assignment_id = models.IntegerField(default=0)    
    test_grade = models.DecimalField(default=None, max_digits=4, decimal_places=1)    
    start_time = models.DateTimeField(default=datetime.now, blank=True)    
    grade_date_time = models.DateTimeField(default=None)    
    seconds_taken = models.IntegerField(default=0)     
    taking_for_ce_credit = models.BooleanField(default=0)    
    ip_address = models.TextField()    
    grade_points = models.DecimalField(null=True, max_digits=4, decimal_places=2)    
    passing_percentage = models.IntegerField(null=True, default=None)     
    passed = models.BooleanField(default=False)    
    cert_id = models.CharField(max_length=255, null=True)    
    cert_encrypted_id = models.CharField(max_length=255, null=True)
    completed_by_due_date = models.BooleanField(default=False)
    #questions = models.TextField()     
    #current_question_number = models.IntegerField(default=0)    
    class Meta():
        db_table = 'core_test_attempts'

class CoreTempTestAttempts(models.Model):    
    user = models.ForeignKey(User)    
    test = models.ForeignKey(CoreTests)    
    assignment_id = models.IntegerField(default=0)    
    test_grade = models.DecimalField(default=None, max_digits=4, decimal_places=1)    
    start_time = models.DateTimeField(auto_now_add=True, blank=True)    
    seconds_taken = models.IntegerField(default=0)    
    grade_date_time = models.DateTimeField(default=None)    
    ip_address = models.TextField()    
    grade_points = models.DecimalField(null=True, max_digits=4, decimal_places=2)    
    current_question_number = models.IntegerField(default=0)    
    current_test_attempt_number = models.IntegerField(default=1)    
    total_questions_count = models.IntegerField(default=0)    
    class Meta():
        db_table = 'core_temp_test_attempts'


class CoreQuestionTypes(models.Model):
    name = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)
    is_active = models.NullBooleanField(null=True)
    class Meta():
        db_table = 'core_question_types'

class CoreQuestionAnswers(models.Model):    
    corequestions = models.ForeignKey('CoreQuestions', related_name='question_answers')    
    coreanswers = models.ForeignKey(CoreAnswers)    
    class Meta():
        db_table = 'core_questions_answers'


class CoreQuestions(models.Model):
    test = models.ForeignKey(CoreTests)
    type = models.ForeignKey(CoreQuestionTypes)
    text = models.CharField(max_length=500, null=True)
    topic = models.CharField(max_length=500, null=True)
    is_regular = models.NullBooleanField(null=True)
    is_mandatory = models.NullBooleanField(null=True)
    is_competency = models.NullBooleanField(null=True)
    is_active = models.NullBooleanField(null=True)
    accredited_agency = models.ForeignKey(UtilRegAgencies, null=True)    
    accredited_is_mandatory = models.BooleanField(default=False)    
    state = models.ForeignKey(UtilUSAStates, null=True)    
    state_is_mandatory = models.BooleanField(default=False)    
    county_fips = models.CharField(max_length=256, null=True)
    county_fips_mandatory = models.BooleanField(default=False)  
    class Meta():
        db_table = 'core_questions'            
    @property
    def answers(self):
        return CoreQuestionAnswers.objects.filter(corequestions_id=self.id)
    
class CoreQuestionAnswersAttempts(models.Model):
    
    test_attempt = models.ForeignKey(CoreTestAttempts)    
    question = models.ForeignKey(CoreQuestions)    
    question_answer = models.ForeignKey(CoreQuestionAnswers, related_name='question_answers_attempt')    
    attempt_time = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta():
        db_table = 'core_question_answers_attempts'

class CoreTempQuestionAnswersAttempts(models.Model):
    
    temp_test_attempt = models.ForeignKey(CoreTempTestAttempts)    
    question = models.ForeignKey(CoreQuestions)    
    question_answer = models.ForeignKey(CoreQuestionAnswers, null=True, default=None)    
    attempt_time = models.DateTimeField(default=datetime.now, blank=True)    
    passed = models.BooleanField(default=False)
    
    class Meta():
        db_table = 'core_temp_question_answers_attempts'


class CoreOrganizations(models.Model):
    name = models.CharField(max_length=256, null=True)
    add_date = models.DateField(auto_now=True, auto_now_add=True)
    activation_date = models.DateField(auto_now=True, auto_now_add=False)    
    #deactivation_date = models.DateField(null=True)
    number_of_licenses = models.IntegerField(null=True)
    modules_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='modules_consistent')
    modules = models.ManyToManyField(CoreModules, related_name='core_organization')
    services_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                            related_name='services_consistent')
    # grades_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='grades_consistent')
    jobs_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='jobs_consistent')
    is_organization_accredited = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                   related_name='is_organization_accredited')
    locations = models.ManyToManyField(CoreLocations, related_name='core_organization')
    user_profiles = models.ManyToManyField(CoreUserProfiles, related_name='core_organization')
    billing = models.ForeignKey(CoreBilling, null=True, related_name='core_organization')
    point_of_contacts = models.ManyToManyField(CorePointOfContacts, related_name='core_organization')
    accreditation_agency = models.ForeignKey(UtilRegAgencies, null=True, related_name='core_organization')
    is_entire_organization_accredited = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                          related_name='is_entire_organization_accredited')
    is_accredited_by_same_agency = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                     related_name='is_accredited_by_same_agency')
    use_monthly_safety_courses = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                   related_name='use_monthly_safety_courses')
    entity_type = models.ForeignKey(UtilOrganizationType, null=True, related_name='core_organization')
    """
        START dashboard_admin_setup_organization_1_2
    """
    # Do you want your minimum passing scores to be consistent across your entire organization?*
    is_score_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='score_consistent')
    #What is your minimum percent passing score for General Knowledge exams? (These are a majority of all courses on HHLEARN)*
    min_score_general_knowledge = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                    related_name='min_score_general_knowledge')
    #What is your minimum percent passing score for courses that have Continuing Education credits?*
    min_score_continuing_education = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                       related_name='min_score_continuing_education')
    #What is your minimum percent passing score for Employee Competency exams?*
    min_score_employee_competency = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                      related_name='min_score_employee_competency')
    #What is your minimum percent passing score for Custom Courses that only belong to your organization?
    min_score_custom_courses = models.ForeignKey(UtilPassingScores, to_field='score', null=True,
                                                 related_name='min_score_custom_courses')
    #Would your organization like to utilize this monthly safety program?
    is_signup_monthly_safety_program = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                         related_name='signup_monthly_safety_program')
    #Do you want the course selections, either using the pre-selections we provide or the ones you select, to be consistent across your entire
    # organization?
    is_course_selections_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                        related_name='course_selections_consistent')
    """
        END dashboard_admin_setup_organization_1_2
        """
    """
        START dashboard_admin_setup_organization_1_3
        """
    is_electronic_postings_enabled = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                       related_name='is_electronic_postings_enabled')
    is_electronic_postings_consistent = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                          related_name='is_electronic_postings_consistent')
    is_use_ssn_for_user = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                            related_name='is_use_ssn_for_user')
    total_number_of_employees = models.IntegerField(null=True)
    is_employee_specific_id = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                related_name='is_employee_specific_id')
    total_number_of_locations = models.IntegerField(null=True)
    """
        END dashboard_admin_setup_organization_1_3
        """
    """
        START dashboard_admin_setup_organization_1_4
        """
    services_offered = models.ManyToManyField(CoreServicesOffered, related_name='core_organization')
    """
        END dashboard_admin_setup_organization_1_4
        """
    """
          START dashboard_admin_setup_organization_1_6
        """
    officials = models.ManyToManyField(CoreOfficials, related_name='core_organization')
    """
        END dashboard_admin_setup_organization_1_6
        """
    current_setup_section = models.CharField(max_length=256, null=True)
    is_initial_setup_complete = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                  related_name='is_initial_setup_complete')
    departments_enabled = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                            related_name='org_departments_enabled')
    regions = models.ManyToManyField(CoreRegions, related_name='core_regions')
    regions_enabled = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='org_regions_enabled')
    total_regions = models.IntegerField(null=True)
    job_titles = models.ManyToManyField(CoreJobTitles, related_name='org_job_titles')
    is_active = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='is_active')
    custom_job_titles_enabled = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                  related_name='org_custom_job_titles_enabled')
    location_specific_job_titles = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                     related_name='org_location_specific_job_titles')
    department_specific_job_titles = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                       related_name='org_department_specific_job_titles')
    total_custom_job_titles = models.IntegerField(null=True)
    courses = models.ManyToManyField(CoreCourses, related_name='org_courses')
    custom_job_courses_enabled = models.ForeignKey(UtilYesorNo, to_field='value', null=True,
                                                   related_name='org_custom_job_courses_enabled')
    #curriculums = models.ManyToManyField(CoreCurriculums, related_name='core_organization_curriculums')
    class Meta():
        db_table = 'core_organizations'

class CoreOrganizationsCustomCourses(models.Model):    
    organizations = models.ForeignKey(CoreOrganizations)
    courses = models.ForeignKey(CoreCourses)
    class Meta():
        db_table = 'core_organizations_custom_courses'


class CoreOrganizationsLocations(models.Model):
    coreorganizations = models.ForeignKey(CoreOrganizations) 
    corelocations = models.ForeignKey(CoreLocations) 
    
    class Meta():
        db_table = 'core_organizations_locations'

class CoreResources(models.Model):
    
    resource_name_language = models.CharField(max_length=255, null=True)
    coreorganizations = models.ForeignKey(CoreOrganizations)
    resource_name = models.CharField(max_length=255, null=True)
    resourcecategories = models.ForeignKey(UtilResourceCategories)
    resource_short_description = models.CharField(max_length=255, null=True) 
    resource_long_description = models.TextField(null=True) 
    is_form = models.BooleanField(default=0) 
    is_publication = models.BooleanField(default=0) 
    is_video = models.BooleanField(default=0) 
    video_duration = models.DateTimeField(null=True) 
    video_cover_image = models.CharField(max_length=255, null=True) 
    resource_keywords = models.CharField(max_length=250, null=True) 
    resource_identifier = models.CharField(max_length=250, null=True) 
    resource_revision_date_or_version = models.CharField(max_length=150, null=True) 
    resource_last_update_date = models.DateField(null=True) 
    days_between_updates = models.IntegerField(default=0) 
    language = models.ForeignKey(UtilLanguageIsoCodes, default=1, null=False)    
    resourcesizes = models.ForeignKey(UtilResourceSizes, null=False)
    number_of_pages = models.IntegerField(default=0)
    resource_color = models.CharField(max_length=55, null=True) 
    can_be_electronically_posted = models.BooleanField(default=0) 
    electronically_posted_official_description = models.CharField(max_length=150, null=True) 
    electronically_posted_url = models.CharField(max_length=250, null=True) 
    is_federal_or_nationwide = models.BooleanField(default=0) 
    is_federal_mandatory_posting = models.BooleanField(default=0) 
    is_state_mandatory_posting = models.BooleanField(default=0) 
    does_resource_replace_hhlearn_resource = models.BooleanField(default=0) 
    replaced_hhlearn_resources_id = models.IntegerField(default=0) 
    where_was_resource_obtained = models.CharField(max_length=500, null=True) 
    is_active = models.BooleanField(default=0)
    formats = models.ManyToManyField(UtilResourceFormats, related_name='core_resources_formats')
    
    class Meta():
        db_table = 'core_resources'

class CoreResourcesForSpecificStates(models.Model):
    
    resources = models.ForeignKey(CoreResources) 
    state = models.ForeignKey(UtilUSAStates) 
    is_active = models.BooleanField(default=0)
    
    class Meta():
        db_table = 'core_resources_for_specific_states'

class CoreResourcesForLocations(models.Model):
    
    resources = models.ForeignKey(CoreResources) 
    locations = models.ForeignKey(CoreLocations) 
    is_active = models.BooleanField(default=0)
    
    class Meta():
        db_table = 'core_resources_for_locations'

class CoreResourcesForDepartments(models.Model):
    
    resources = models.ForeignKey(CoreResources) 
    departments = models.ForeignKey(CoreDepartments) 
    is_active = models.BooleanField(default=0)
    
    class Meta():
        db_table = 'core_resources_for_departments'

class CoreResourcesFormats(models.Model):

    coreresources = models.ForeignKey(CoreResources, related_name="resource_format") 
    utilresourceformats = models.ForeignKey(UtilResourceFormats)
    
    class Meta():
        db_table = 'core_resources_formats'


class CoreResourcesVisited(models.Model):
    
    coreresources = models.ForeignKey(CoreResources) 
    user = models.ForeignKey(User) 
    access_date_time_UTC = models.DateTimeField(null=True) 
    browser_used = models.CharField(max_length=250, null=True) 
    ip_address_of_user = models.CharField(max_length=100, null=True) 
    
    class Meta():
        db_table = 'core_resources_visited'
        
class CoreCoursesNote(models.Model):
    
    user = models.ForeignKey(User)
    courses = models.ForeignKey(CoreCourses, related_name="course_note") 
    notes = models.TextField(null=True) 
    date_added = models.DateTimeField(default=datetime.now, blank=True) 
    date_last_saved = models.DateTimeField(default=datetime.now, blank=True) 
    date_passed_test = models.DateTimeField(null=True)     
    date_to_purge = models.DateTimeField(null=True)
    
    class Meta():
        db_table = 'core_courses_notes_temp'

#inservices model

class CoreInservices(models.Model):    
    
    inservice_title = models.CharField(max_length=256, null=True)
    inservice_summary = models.TextField(null=True)    
    organizations = models.ForeignKey(CoreOrganizations, null=True) 
    continuing_education_provided = models.BooleanField(default=0) 
    continuing_education_sponsor_id = models.CharField(max_length=256, null=True) 
    ce_sponsoring_organization_name = models.CharField(max_length=256, null=True) 
    ce_sponsoring_org_address1 = models.CharField(max_length=256, null=True) 
    ce_sponsoring_org_address2 = models.CharField(max_length=45, null=True) 
    ce_sponsoring_org_city = models.CharField(max_length=256, null=True) 
    ce_sponsoring_org_states = models.ForeignKey(UtilUSAStates, null=True) 
    zip_code = models.CharField(max_length=45) 
    ce_units_of_measure = models.ForeignKey(UtilCeUnitsOfMeasure, null=True) 
    ce_approved_units = models.DecimalField(null=True, max_digits=4, decimal_places=2) 
    ce_converted_units_to_hours = models.DecimalField(null=True, max_digits=4, decimal_places=2) 
    added_by_user_profiles = models.ForeignKey(User, related_name='inservices_added') 
    add_date = models.DateTimeField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True)
    deactivated_user_profiles = models.ForeignKey(User, null=True, related_name='inservices_deactivated')
    
    class Meta():
        db_table = 'core_inservices' 

class CoreInserviceTrainingSites(models.Model):
    
    inservice_training_site_name = models.CharField(max_length=256, null=True) 
    inservice_site_address1 = models.CharField(max_length=256, null=True) 
    inservice_site_address2 = models.CharField(max_length=256, null=True) 
    inservice_site_city = models.CharField(max_length=256, null=True) 
    states = models.ForeignKey(UtilUSAStates, null=True) 
    zip_code = models.CharField(max_length=45, null=True) 
    #county = models.ForeignKey(UtilZipCodes, db_column='county_fips', null=True) 
    organizations = models.ForeignKey(CoreOrganizations, null=True) 
    add_date_time = models.DateTimeField(null=True) 
    added_by_user_profiles = models.ForeignKey(User, related_name='inservice_training_sites') 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True) 
    
    class Meta():
        db_table = 'core_inservice_training_sites'
        
class CoreInservicesCompleted(models.Model):
    
    inservices = models.ForeignKey(CoreInservices, null=True)
    start_date_time = models.DateTimeField(null=True)
    stop_date_time = models.DateTimeField(null=True)
    inservice_duration = models.DateTimeField(null=True) 
    inservice_training_sites = models.ForeignKey(CoreInserviceTrainingSites, null=True) 
    added_by_user_profiles = models.ForeignKey(User, related_name='inservices_completed')
    add_date = models.DateTimeField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True)

    class Meta():
        db_table = 'core_inservices_completed'

class CoreInserviceFileUploadTypes(models.Model):
    
    inservice_file_title = models.CharField(max_length=256, null=True) 
    is_active = models.BooleanField(default=1)
    
    class Meta():  
        db_table = 'core_inservice_file_upload_types'

class CoreOrganizationsInserviceFileUploads(models.Model):
    
    inservice_file_upload_types = models.ForeignKey(CoreInserviceFileUploadTypes, null=True) 
    inservice_file_title = models.CharField(max_length=256, null=True) 
    inservice_filename = models.CharField(max_length=256, null=True) 
    inservice_filename_formats = models.ForeignKey(UtilResourceFormats, null=True) 
    uploaded_date = models.DateTimeField(null=True) 
    uploaded_by_user_id = models.ForeignKey(User, related_name = 'organizations_inservice_file_uploads') 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True)

    class Meta():
        db_table = 'core_organizations_inservice_file_uploads'

class CoreInserviceTrainers(models.Model):
    
    first_name = models.CharField(max_length=22, null=True) 
    last_name = models.CharField(max_length=22, null=True) 
    trainer_professional_credentials = models.CharField(max_length=256, null=True) 
    address1 = models.CharField(max_length=256, null=True) 
    address2 = models.CharField(max_length=256, null=True) 
    city = models.CharField(max_length=256, null=True) 
    states = models.ForeignKey(UtilUSAStates, null=True) 
    zip_code = models.CharField(max_length=45, null=True) 
    #county = models.ForeignKey(UtilZipCodes, db_column='county_fips', null=True) 
    trainers_day_phone = models.CharField(max_length=45, null=True) 
    trainers_email = models.CharField(max_length=256, null=True) 
    trainer_qualifications_form_uploaded = models.BooleanField(default=0)
    trainer_qualifications_form_file_uploads = models.ForeignKey(CoreOrganizationsInserviceFileUploads, null=True)  
    trainer_qualifications_form_filename = models.CharField(max_length=256, null=True) 
    add_date = models.DateTimeField(null=True) 
    added_by_user_profiles = models.ForeignKey(User, related_name='inservice_trainers') 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True)
    
    class Meta():
        db_table = 'core_inservice_trainers'

class CoreInservicesCompletedTrainers(models.Model):

    inservice_trainers = models.ForeignKey(CoreInserviceTrainers, null=True) 
    inservices_completed = models.ForeignKey(CoreInservicesCompleted, null=True) 
    add_date = models.DateTimeField(null=True) 
    added_by_user_profiles = models.ForeignKey(User, related_name='inservices_completed_trainers') 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True) 
    
    class Meta():
        db_table = 'core_inservices_completed_trainers'

#core external course models

class CoreExternalCoursesSources(models.Model):    

    external_source_name = models.CharField(max_length=256, null=True) 
    is_active = models.BooleanField(default=1)
    
    class Meta():
        db_table = 'core_external_courses_sources'
        
class CoreExternalCourses(models.Model):
    
    external_courses_id = models.CharField(max_length=25, null=True) 
    external_courses_sources = models.ForeignKey(CoreExternalCoursesSources, null=True) 
    external_courses_title = models.CharField(max_length=256, null=True) 
    course_hours = models.DecimalField(max_digits=3, decimal_places=1, null=True) 
    organizations = models.ForeignKey(CoreOrganizations, null=True) 
    continuing_education_provided = models.BooleanField(default=0) 
    ce_education_sponsor_id = models.CharField(max_length=256, null=True) 
    ce_sponsoring_organization_name = models.CharField(max_length=256, null=True)
    ce_sponsoring_org_address1 = models.CharField(max_length=256, null=True) 
    ce_sponsoring_org_address2 = models.CharField(max_length=256, null=True) 
    ce_sponsoring_org_city = models.CharField(max_length=256, null=True) 
    ce_sponsoring_states = models.ForeignKey(UtilUSAStates, null=True) 
    zip_code = models.CharField(max_length=45, null=True) 
    ce_units_of_measure = models.ForeignKey(UtilCeUnitsOfMeasure, null=True) 
    ce_approved_units = models.DecimalField(null=True, max_digits=4, decimal_places=2) 
    ce_converted_units_to_hours = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    added_by_user_profiles = models.ForeignKey(User, related_name='added_external_courses') 
    add_date = models.DateTimeField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True) 
    deactivated_by_user_profiles = models.ForeignKey(User, related_name='deactivated_external_courses')
    
    class Meta():
        db_table = 'core_external_courses'

class CoreExternalCoursesCompleted(models.Model): 

    external_courses = models.ForeignKey(CoreExternalCourses, null=True) 
    completion_date = models.DateField(null=True) 
    hours = models.DecimalField(null=True, max_digits=3, decimal_places=1) 
    added_by_user_profiles = models.ForeignKey(User, related_name='added_external_courses_completed') 
    add_date = models.DateTimeField(null=True)     
    is_active = models.BooleanField(default=1) 
    deactivated_date = models.DateTimeField(null=True) 
    deactivated_by_user_profiles = models.ForeignKey(User, related_name='deactivated_external_courses_completed')
    
    class Meta():
        db_table = 'core_external_courses_completed'

class AccreditingAgencyAchcCategories(models.Model):
    category_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=255)
    category_description = models.TextField(null=True)
    efffective_date	= models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    deactivation_date = models.DateField(null=True)

    class Meta():
        db_table = 'accrediting_agency_achc_categories'

class AccreditingAgencyAchcSubCategories(models.Model):
    achc_categories = models.ForeignKey(AccreditingAgencyAchcCategories)
    subcategory_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=255)
    category_description = models.TextField(null=True)
    efffective_date	= models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    deactivation_date = models.DateField(null=True)

    class Meta():
        db_table = 'accrediting_agency_achc_subcategories'

#accreditation models
class AccreditingAgencyAchc(models.Model): 
    
    util_reg_agencies = models.ForeignKey(UtilRegAgencies, null=True)
    achc_categories = models.ForeignKey(AccreditingAgencyAchcCategories, null=True)
    standard_number = models.CharField(max_length=256, null=True) 
    short_code = models.CharField(max_length=256, null=True) 
    standrard_description = models.TextField(null=True)
    effective_date = models.DateField(null=True) 
    applies_CMGT = models.BooleanField(default=0) 
    applies_CS = models.BooleanField(default=0) 
    applies_DTX = models.BooleanField(default=0) 
    applies_OTX = models.BooleanField(default=0) 
    applies_PSR = models.BooleanField(default=0) 
    applies_PDA = models.BooleanField(default=0) 
    applies_PDC = models.BooleanField(default=0) 
    applies_PDN = models.BooleanField(default=0) 
    applies_PDOT = models.BooleanField(default=0) 
    applies_PDPT = models.BooleanField(default=0) 
    applies_PDST = models.BooleanField(default=0) 
    applies_PDSW = models.BooleanField(default=0) 
    applies_HRC = models.BooleanField(default=0) 
    applies_HIC = models.BooleanField(default=0) 
    applies_BHHC = models.BooleanField(default=0) 
    applies_HHA = models.BooleanField(default=0) 
    applies_MSS = models.BooleanField(default=0) 
    applies_OT = models.BooleanField(default=0) 
    applies_PD = models.BooleanField(default=0) 
    applies_PT = models.BooleanField(default=0) 
    applies_SN = models.BooleanField(default=0) 
    applies_ST = models.BooleanField(default=0) 
    applies_CRTL = models.BooleanField(default=0) 
    applies_CRDS = models.BooleanField(default=0) 
    applies_AIC = models.BooleanField(default=0) 
    applies_CRCS = models.BooleanField(default=0) 
    applies_Fitter = models.BooleanField(default=0) 
    applies_HME = models.BooleanField(default=0) 
    applies_IRN = models.BooleanField(default=0) 
    applies_IRX = models.BooleanField(default=0) 
    applies_LTC = models.BooleanField(default=0) 
    applies_MSP = models.BooleanField(default=0) 
    applies_RTS = models.BooleanField(default=0) 
    applies_SRX = models.BooleanField(default=0) 
    applies_SLC = models.BooleanField(default=0) 
    applies_HST = models.BooleanField(default=0) 
    is_active = models.BooleanField(default=0) 
    deactiviation_date = models.DateField(null=True)
    
    class Meta():
        db_table = 'accrediting_agency_achc'


class CoreCoursesAccreditationStandardsAchc11(models.Model):

    courses = models.ForeignKey(CoreCourses, null=True) 
    achc = models.ForeignKey(AccreditingAgencyAchc, null=True) 
    is_active = models.BooleanField(default=1)
    
    class Meta():
        db_table = 'core_courses_accreditation_standards_achc_11'

#Agency id is 9
class AccreditingAgencyTjcCategories(models.Model):
    category_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=255)
    category_description = models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=0)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_tjc_categories'

class AccreditingAgencyTjcStandards(models.Model):

    util_reg_agencies = models.ForeignKey(UtilRegAgencies, null=True)
    tjc_categories = models.ForeignKey(AccreditingAgencyTjcCategories, null=True)
    short_code = models.CharField(max_length=256, null=True) 
    standard_number = models.CharField(max_length=256, null=True)
    standard_description = models.CharField(max_length=256, null=True) 
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    deactivation_date = models.DateField(null=True)

    class Meta():
        db_table = 'accrediting_agency_tjc_standards'
        
class AccreditingAgencyTjcElements(models.Model):
    
    util_accrediting_agency_tjc_standards = models.ForeignKey(AccreditingAgencyTjcStandards, null=True)
    short_code = models.CharField(max_length=256, null=True) 
    element_of_performance_number = models.CharField(max_length=256, null=True) 
    element_description = models.CharField(max_length=512, null=True) 
    element_scoring = models.CharField(max_length=1, null=True) 
    documentation_required = models.BooleanField(default=0)
    measure_of_success_needed = models.BooleanField(default=0)
    immediate_threat_to_health_or_safety_1 = models.BooleanField(default=0)
    situational_decision_rules_apply_2 = models.BooleanField(default=0)
    direct_requirements_apply_3 = models.BooleanField(default=0)
    identified_risk = models.BooleanField(default=0)
    applies_homehealth_hh = models.BooleanField(default=0)
    applies_homehealth_pcs = models.BooleanField(default=0)
    applies_hospice_inp = models.BooleanField(default=0)
    applies_hospice_ptre = models.BooleanField(default=0)
    applies_dme_h = models.BooleanField(default=0)
    applies_dme_f = models.BooleanField(default=0)
    applies_dme_m = models.BooleanField(default=0)
    applies_respiratory = models.BooleanField(default=0)
    applies_sup_h = models.BooleanField(default=0)
    applies_sup_m = models.BooleanField(default=0)
    applies_op_h = models.BooleanField(default=0)
    applies_op_f = models.BooleanField(default=0)
    applies_crs = models.BooleanField(default=0)
    applies_rt_h = models.BooleanField(default=0)
    applies_rt_f = models.BooleanField(default=0)
    applies_pharmacy_disp = models.BooleanField(default=0)
    applies_pharmacy_ccp = models.BooleanField(default=0)
    applies_pharmacy_fsai = models.BooleanField(default=0)
    applies_pharmacy_ltp = models.BooleanField(default=0)
    effective_date = models.DateField(null=True) 
    is_active = models.BooleanField(default=1)
    deactivation_date = models.DateField(null=True) 
    
    class Meta():
        db_table='accrediting_agency_tjc_elements'
      
class CoreCoursesAccreditationStandardsTjc9(models.Model):
    courses = models.ForeignKey(CoreCourses, null=True) 
    tjc_elements = models.ForeignKey(AccreditingAgencyTjcElements, null=True) 
    is_active = models.BooleanField(default=1)
    
    class Meta():
        db_table = 'core_courses_accreditation_standards_tjc_9'

# agency id is 586

class AccreditingAgencyHqaaCategories(models.Model):
    category_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=256, null=True)
    category_description	= models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=1)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_hqaa_categories'

class AccreditingAgencyHqaaSubcategories(models.Model):
    hqaa_categories = models.ForeignKey(AccreditingAgencyHqaaCategories)
    subcategory_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=256, null=True)
    subcategory_description	= models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=1)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_hqaa_subcategories'

class AccreditingAgencyHqaa(models.Model):
    
    util_reg_agencies = models.ForeignKey(UtilRegAgencies, null=True)
    hqaa_subcategories = models.ForeignKey(AccreditingAgencyHqaaSubcategories, null=True)
    short_code = models.CharField(max_length=256, null=True) 
    standard_number = models.CharField(max_length=256, null=True)
    standard_description = models.CharField(max_length=256, null=True) 
    description = models.TextField(null=True) 
    effective_date = models.DateField(null=True) 
    is_active  = models.BooleanField(default=1) 
    deactivation_date = models.DateField(null=True)

    class Meta():
        db_table = 'accrediting_agency_hqaa'

class CoreCoursesAccreditationStandardsHqaa586(models.Model):    
    
    courses = models.ForeignKey(CoreCourses, null=True) 
    hqaa = models.ForeignKey(AccreditingAgencyHqaa, null=True) 
    is_active = models.BooleanField(default=1)

    class Meta():
        db_table = 'core_courses_accreditation_standards_hqaa_586'

#agency id is 587

class AccreditingAgencyCteamCategories(models.Model):
    category_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=256, null=True)
    category_description	= models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=1)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_cteam_categories'

class AccreditingAgencyCteamSubcategories(models.Model):
    cteam_categories = models.ForeignKey(AccreditingAgencyCteamCategories)
    subcategory_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=256, null=True)
    subcategory_description	= models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=1)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_cteam_subcategories'

class AccreditingAgencyCteamStandards(models.Model):
        
    util_reg_agencies = models.ForeignKey(UtilRegAgencies, null=True)
    cteam_subcategories = models.ForeignKey(AccreditingAgencyCteamSubcategories)
    short_code = models.CharField(max_length=256, null=True)
    standard_number = models.CharField(max_length=256, null=True) 
    standard_description = models.CharField(max_length=500, null=True) 
    effective_date = models.DateField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivation_date = models.DateField(null=True)
    
    class Meta():
        db_table = 'accrediting_agency_cteam_standards'

class AccreditingAgencyCteamEvidenceOfCompliance(models.Model):

    accrediting_agency_cteam_standards = models.ForeignKey(AccreditingAgencyCteamStandards, null=True)
    short_code = models.CharField(max_length=256, null=True) 
    evidence_of_compliance_number = models.CharField(max_length=256, null=True) 
    evidence_of_compliane_description = models.TextField(null=True) 
    effective_date = models.DateField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivation_date = models.DateField(null=True) 

    class Meta():
        db_table = 'accrediting_agency_cteam_evidence_of_compliance'

class CoreCoursesAccreditationStandardsCteam587(models.Model):
    
    courses = models.ForeignKey(CoreCourses, null=True) 
    cteam_evidence_of_compliance = models.ForeignKey(AccreditingAgencyCteamEvidenceOfCompliance, null=True) 
    is_active = models.BooleanField(default=1)

    class Meta():
        db_table = 'core_courses_accreditation_standards_cteam_587'

#agency id is 588

class AccreditingAgencyBocCategories(models.Model):
    category_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=255)
    category_description = models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_boc_categories'

class AccreditingAgencyBocSubcategories(models.Model):
    boc_categories = models.ForeignKey(AccreditingAgencyBocCategories)
    subcategory_name = models.CharField(max_length=255)
    short_code = models.CharField(max_length=255)
    subcategory_description = models.TextField(null=True)
    effective_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    deactivation_date = models.DateField(null=True)
    class Meta():
        db_table = 'accrediting_agency_boc_subcategories'

class AccreditingAgencyBoc(models.Model):

    util_reg_agencies = models.ForeignKey(UtilRegAgencies, null=True)
    accrediting_agency_boc_subcategories = models.ForeignKey(AccreditingAgencyBocSubcategories, null=True)
    short_code = models.CharField(max_length=256, null=True) 
    standard_number = models.CharField(max_length=256, null=True) 
    standard_description = models.CharField(max_length=256, null=True) 
    effective_date = models.DateField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivation_date = models.DateField(null=True)
    
    class Meta():
        db_table = 'accrediting_agency_boc' 

class AccreditingAgencyBocStandards(models.Model):

    accrediting_agency_boc = models.ForeignKey(AccreditingAgencyBoc, null=True) 
    short_code = models.CharField(max_length=256, null=True) 
    sub_standard_number = models.CharField(max_length=256, null=True) 
    standard_description = models.TextField(null=True) 
    effective_date = models.DateField(null=True) 
    is_active = models.BooleanField(default=1) 
    deactivation_date = models.DateField(null=True)
    
    class Meta():
        db_table = 'accrediting_agency_boc_standards'

class CoreCoursesAccreditationStandardsBoc588(models.Model):    

    courses = models.ForeignKey(CoreCourses, null=True) 
    boc_standards = models.ForeignKey(AccreditingAgencyBocStandards, null=True) 
    is_active = models.BooleanField(default=1)
    
    class Meta():
        db_table = 'core_courses_accreditation_standards_boc_588'

#Social Media
class CoreSocialMedia(models.Model):
    social_media_name = models.CharField(max_length=250, null=True)
    short_code = models.CharField(max_length=50, null=True)
    website_address = models.CharField(max_length=250, null=True)
    fa_icon = models.CharField(max_length=45, null=True)
    load_color = models.CharField(max_length=10, null=True)
    hover_color = models.CharField(max_length=10, null=True)
    is_active = models.BooleanField(default=1)
    
    class Meta():
        db_table = 'core_social_media'

class AccreditingAgencySocialMedia(models.Model):
    
    accreditingagency = models.ForeignKey(UtilRegAgencies, null=True)
    socialmedia = models.ForeignKey(CoreSocialMedia, null=True)
    social_media_url = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=1)
    
    class Meta(): 
        db_table = 'accrediting_agency_social_media'

#messages and alert models
class CoreMessagesAlerts(models.Model):

    core_organizations = models.ForeignKey(CoreOrganizations, null=True) 
    creating_user = models.ForeignKey(User, related_name='messages_alerts_created_user') 
    util_priorities = models.ForeignKey(UtilPriorities, null=True) 
    is_alert = models.BooleanField(default=0) 
    is_message = models.BooleanField(default=0)
    is_automatic_message_alert = models.BooleanField(default=0)
    is_hhlearn_system_message_alert = models.BooleanField(default=0)
    is_hhlearn_administrators_message_alert = models.BooleanField(default=0)
    is_hhlearn_all_managers_message_alert = models.BooleanField(default=0)
    is_hhlearn_location_managers_message_alerts = models.BooleanField(default=0)
    is_hhlearn_department_managers_message_alerts = models.BooleanField(default=0)
    is_hhlearn_region_managers_message_alerts = models.BooleanField(default=0)
    is_hhlearn_specific_users_message_alerts = models.BooleanField(default=0)
    is_hhlearn_specific_job_titles_message_alerts = models.BooleanField(default=0)
    is_hhlearn_specific_course_id_message_alerts = models.BooleanField(default=0)
    is_organizationwide_message_alert = models.BooleanField(default=0)
    is_locationwide_message_alert = models.BooleanField(default=0)
    is_departmentwide_message_alert = models.BooleanField(default=0)
    is_regionwide_message_alert = models.BooleanField(default=0)
    is_organizationwide_message_alert = models.BooleanField(default=0)
    is_locationwide_message_alert = models.BooleanField(default=0)
    is_departmentwide_message_alert = models.BooleanField(default=0)
    is_regionwide_message_alert = models.BooleanField(default=0)
    is_organization_administrators_message_alert = models.BooleanField(default=0)
    is_all_managers_message_alert = models.BooleanField(default=0)
    is_location_managers_message_alerts = models.BooleanField(default=0)
    is_department_managers_message_alerts = models.BooleanField(default=0)
    is_region_managers_message_alerts = models.BooleanField(default=0)
    is_specific_users_message_alert = models.BooleanField(default=0)
    is_specific_job_titles_message_alerts = models.BooleanField(default=0)
    is_specific_course_id_message_alerts = models.BooleanField(default=0)
    message_alert_subject = models.CharField(max_length=100, null=True) 
    message_alert_content = models.TextField(null=True) 
    date_created_UTC = models.DateTimeField(null=True) 
    date_auto_start_UTC = models.DateTimeField(null=True) 
    date_auto_stop_UTC = models.DateTimeField(null=True) 
    date_deactivated_UTC = models.DateTimeField(null=True) 
    deactivation_user = models.ForeignKey(User, related_name='messages_alerts_deactivated_user')
    date_deleted = models.DateTimeField(null=True)
    deleted_by_user = models.ForeignKey(User, related_name='messages_alerts_deleted_user') 
    is_active = models.BooleanField(default=0)
        
    class Meta():
        db_table = 'core_messages_alerts'
        
class CoreUserMessagesAlerts(models.Model):
    
    core_messages_alerts = models.ForeignKey(CoreMessagesAlerts, null=True) 
    auth_user = models.ForeignKey(User, related_name='user_messages_alerts') 
    date_assigned_UTC = models.DateTimeField(null=True) 
    date_acknowledged_UTC = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=255, null=True)
    message_alert_cleared_id = models.BooleanField(default=0)
    deactivated_date = models.DateTimeField(null=True)
    deactivated_by_user = models.ForeignKey(User, related_name='user_messages_alerts_deactivated_user')
    
    class Meta():
        db_table = 'core_user_messages_alerts'


#task modules
class CoreTasks(models.Model):
 
    user = models.ForeignKey(User, related_name='task_user') 
    tasks_description = models.CharField(max_length=256, null=True) 
    recurring_task = models.BooleanField(default=0) 
    assigned_by_user = models.ForeignKey(User, related_name='task_assigned_user', null=True) 
    date_added = models.DateTimeField(null=True)
    date_due = models.DateTimeField(null=True)
    date_completed = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=45, null=True)
    task_cleared_id = models.BooleanField(default=0) 
    date_deativated = models.DateTimeField(null=True) 
    deactivateduser = models.ForeignKey(User, related_name='task_deactivated_user', null=True)
     

    class Meta():
        db_table = 'core_tasks'

class CoreCoursesPrerequisite(models.Model):
    
    parent_courses = models.ForeignKey(CoreCourses, related_name='source')
    child_courses = models.ForeignKey(CoreCourses, related_name='target')
    is_active = models.BooleanField(default=1)
    
    class Meta():
        db_table = 'core_courses_prerequisite' 

class UserStatus(models.Model):    
    user = models.ForeignKey(User, related_name='status_user')
    status_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=True)
    making_change_user = models.ForeignKey(User, related_name='status_change_user')
    
    class Meta():
        db_table = 'auth_user_status'

class CoreMilestones(models.Model):
    organizations = models.ForeignKey(CoreOrganizations)
    added_by_user = models.ForeignKey(User, related_name='milestone_added_user')
    milestone_description = models.CharField(max_length=256, null=False)
    timeline_message = models.CharField(max_length=256, default='')
    completion_message = models.CharField(max_length=256, null=False)
    hex_stroke_color = models.CharField(max_length=10, null=True)
    hex_box_color = models.CharField(max_length=10, null=True)
    milestone_image = models.CharField(max_length=256, null=True)
    milestone_icon = models.CharField(max_length=45, null=True)
    hex_icon_color = models.CharField(max_length=10, null=True)
    milestone_heading = models.CharField(max_length=256, null=True)
    hex_heading_color = models.CharField(max_length=10, null=True)
    milestone_subheading = models.CharField(max_length=256, null=True)
    hex_subheading_color = models.CharField(max_length=10, null=True)
    show_on_timeline = models.BooleanField(default=True)
    show_on_myprofile = models.BooleanField(default=True)
    can_award_milestone = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta():
        db_table = 'core_milestones'
        
class CoreUsersMilestonesEarned(models.Model):
    user = models.ForeignKey(User, related_name='user_milestones')
    milestones = models.ForeignKey(CoreMilestones, null=False)
    date_earned = models.DateTimeField(default=datetime.now(), null=False)    
    awarded_by_user = models.ForeignKey(User, related_name='user_milestones_awarded', null=True)
    deactivated_date = models.DateTimeField(null=True)
    deactivated_by_user = models.ForeignKey(User, related_name='user_milestones_deactivated', null=True)
    show_on_timeline = models.BooleanField(default=True)
    show_on_myprofile = models.BooleanField(default=True)
    
    class Meta():
        db_table = 'core_users_milestones_earned'
        
class CorePromoCodes(models.Model):
    promo_code = models.CharField(max_length=45, null=False)
    core_promo_description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_months_free = models.BooleanField(default=False)
    number_of_months = models.IntegerField(null=True)
    is_percent_off = models.BooleanField(default=False)
    percent_off = models.IntegerField(null=True)
    is_fixed_price = models.BooleanField(default=False)
    fixed_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    is_system_code = models.BooleanField(default=False)
    is_core_plan_1_pro = models.BooleanField(default=False)
    is_core_plan_2_sbe = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta():
        db_table = 'core_promo_codes'

class CoreLeads(models.Model):
    lead_organization_name = models.CharField(max_length=256, null=False)
    lead_address1 = models.CharField(max_length=256, null=False)
    lead_address2 = models.CharField(max_length=256, null=True)
    lead_org_city = models.CharField(max_length=45, null=False)
    states = models.ForeignKey(UtilUSAStates, null=False)
    #county = models.ForeignKey(UtilZipCodes, db_column='county_fips', null=True)
    county_id = models.IntegerField(null=True)
    zip_codes = models.ForeignKey(UtilZipCodes, null=False)
    lead_first_name = models.CharField(max_length=22, null=False)
    lead_last_name = models.CharField(max_length=22, null=False)
    lead_email_address = models.CharField(max_length=75, null=False)
    lead_work_phone = models.CharField(max_length=45, null=False)
    lead_add_date = models.DateTimeField(null=True)
    lead_ip_address = models.CharField(max_length=256, null=True)
    lead_sources = models.ForeignKey(UtilLeadSources, null=False)
    promo_codes = models.ForeignKey(CorePromoCodes, null=True)
    converted_to_subscriber = models.BooleanField(default=False)
        
    class Meta():
        db_table = 'core_leads'

#contact us table
class CoreContactUs(models.Model):
    contact_full_name = models.CharField(max_length=150)
    contact_email = models.CharField(max_length=75)
    contact_company = models.CharField(max_length=255)
    contact_company_website = models.CharField(max_length=255)
    contact_ip_address = models.CharField(max_length=255)
    contact_add_date = models.DateTimeField(null=False)
    contact_message = models.CharField(max_length=500)
    
    class Meta():
        db_table = 'core_contact_us'

class CoreReportsCopyrightStatements(models.Model):
    copyright_statement = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)

    class Meta():
        db_table = 'core_reports_copyright_statements'

class CoreReportsDisclaimerStatements(models.Model):
    reg_agencies = models.ForeignKey(UtilRegAgencies)
    disclaimer_statement = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    class Meta():
        db_table = 'core_reports_disclaimer_statements'

class CoreReports(models.Model):
    report_categories = models.ForeignKey(UtilReportCategories, null=False, related_name='reports')
    report_title = models.CharField(max_length=255)
    report_description = models.TextField(null=True)
    display_order = models.IntegerField(max_length=11, null=True)
    tile_hex_color = models.CharField(max_length=7)
    tile_hex_color_hover = models.CharField(max_length=7)
    icon = models.CharField(max_length=75)
    report_url = models.CharField(max_length=255)
    reports_copyright_statements = models.ForeignKey(CoreReportsCopyrightStatements)
    can_email = models.BooleanField(default=False)
    email_templates = models.ForeignKey(UtilEmailTemplates, null=True)
    email_subject = models.CharField(max_length=255, null=True)
    email_message = models.TextField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta():
        db_table = 'core_reports'

"""
changed by louis
"""