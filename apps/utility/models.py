from django.db import modelsclass UtilAnonymousIps(models.Model):    """        this model stores  IPS.        """    ip_address = models.IPAddressField()    description = models.TextField(null=True)    class Meta():        db_table = 'util_anonymous_ips'class UtilZipCodes(models.Model):    """        ZIP codes database        """    zip_code = models.CharField(max_length=256, null=True)    zip_type = models.CharField(max_length=256, null=True)    city_name = models.CharField(max_length=256, null=True)    city_type = models.CharField(max_length=256, null=True)    county_name = models.CharField(max_length=256, null=True)    county_fips = models.CharField(max_length=256, null=True)    state_name = models.CharField(max_length=256, null=True)    state_abbr = models.CharField(max_length=256, null=True)    state_fips = models.CharField(max_length=256, null=True)    msa_code = models.CharField(max_length=256, null=True)    area_code = models.CharField(max_length=256, null=True)    time_zone = models.CharField(max_length=256, null=True)    utc = models.DecimalField(max_digits=3, decimal_places=1, null=True)    dst = models.CharField(max_length=256, null=True)    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)    class Meta():        db_table = 'util_zip_codes'class UtilUSAStates(models.Model):    """        list of USA states        """    name = models.CharField(max_length=256, null=True)    abbreviation = models.CharField(max_length=256, null=True)    name_possessive = models.CharField(max_length=256, null=True)    country = models.CharField(max_length=256, null=True)    type = models.CharField(max_length=256, null=True)    sort = models.IntegerField(null=True)    status = models.CharField(max_length=256, null=True)    occupied = models.CharField(max_length=256, null=True)    notes = models.CharField(max_length=256, null=True)    fips_state = models.CharField(max_length=256, null=True)    assoc_press = models.CharField(max_length=256, null=True)    standard_federal_region = models.CharField(max_length=256, null=True)    census_region = models.CharField(max_length=256, null=True)    census_region_name = models.CharField(max_length=256, null=True)    census_division = models.CharField(max_length=256, null=True)    census_division_name = models.CharField(max_length=256, null=True)    circuit_court = models.CharField(max_length=256, null=True)    name_possessive = models.CharField(max_length=256, null=True)    dme_macs = models.ForeignKey('UtilDMEMACS', related_name='util_dme_macs')    class Meta():        db_table = 'util_usa_states'class UtilPaymentMethods(models.Model):    """        payment methods        """    description = models.TextField(null=True)    name = models.CharField(max_length=256, null=True)    short_code = models.CharField(max_length=256, null=True)    is_active = models.IntegerField(max_length=1, null=True)    class Meta():        db_table = 'util_payment_methods'"""class UtilMembershipPlans(models.Model):    description = models.TextField(null=True)    name = models.CharField(max_length=256, null=True)    short_code = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    monthly_price = models.IntegerField(max_length=1, null=True)    class Meta():        db_table = 'util_membership_plans'""""""class UtilUserPack(models.Model):    description = models.TextField(null=True)    name = models.CharField(max_length=256, null=True)    short_code = models.CharField(max_length=256, null=True)    is_active = models.IntegerField(max_length=1, null=True)    monthly_price = models.IntegerField(max_length=1, null=True)    allowed_users = models.IntegerField()    membership_plan = models.ForeignKey(UtilMembershipPlans, related_name='util_user_pack')    class Meta():        db_table = 'util_user_pack'"""class UtilMonths(models.Model):    """        number of users pack        """    name = models.CharField(max_length=256, null=True)    short_code = models.CharField(max_length=256, null=True)    number = models.IntegerField(max_length=2, null=True)    class Meta():        db_table = 'util_months'class UtilYesorNo(models.Model):    """       UtilYesorNo        """    value = models.IntegerField(null=True, unique=True)    name = models.CharField(max_length=256, null=True)    class Meta():        db_table = 'util_yes_or_no'class UtilYears(models.Model):    """        number of users pack        """    year = models.IntegerField(max_length=4, null=True)    class Meta():        db_table = 'util_years'class UtilOrganizationType(models.Model):    """        number of users pack        """    name = models.CharField(max_length=256, null=True)    description = models.CharField(max_length=256, null=True)    class Meta():        db_table = 'util_organization_type'class UtilRenewalTerms(models.Model):    """        UtilRenewalTerms        """    name = models.CharField(max_length=256, null=True)    description = models.CharField(max_length=256, null=True)    class Meta():        db_table = 'util_renewal_terms'class UtilPassingScores(models.Model):    """       UtilPssingScores        """    score = models.IntegerField(null=True, unique=True)    class Meta():        db_table = 'util_passing_scores'class UtilOfficialTypes(models.Model):    """       UtilOfficialTypes        """    short_code = models.CharField(max_length=256, null=True)    default_job_title = models.CharField(max_length=256, null=True)    question = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_official_types'class UtilDMEMACS(models.Model):    """        UtilDMEMACS        """    id = models.CharField(max_length=1, primary_key=True)    name = models.CharField(max_length=256, null=True)    street_address_1 = models.CharField(max_length=256, null=True)    street_address_2 = models.CharField(max_length=256, null=True)    city = models.CharField(max_length=256, null=True)    state = models.CharField(max_length=256, null=True)    zip = models.CharField(max_length=256, null=True)    phone = models.CharField(max_length=256, null=True)    fax = models.CharField(max_length=256, null=True)    website = models.CharField(max_length=256, null=True)    email = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_dme_macs'class UtilJobCategories(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    description = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_job_categories'class UtilFlsaStatus(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    description = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_flsa_status'class UtilJobTitles(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    name_possessive = models.CharField(max_length=256, null=True)    description = models.CharField(max_length=256, null=True)    category = models.ForeignKey(UtilJobCategories, null=True, related_name='util_job_title_category')    patient_file_access = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                            related_name='util_job_title_patient_file_access')    exposure_to_chemicals = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                              related_name='util_job_title_exposure_to_chemicals')    exposure_to_BBP = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                        related_name='util_job_title_exposure_to_BBP')    exposure_to_TB = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                       related_name='util_job_title_exposure_to_TB')    requires_license = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                         related_name='util_job_title_requires_license')    cpr = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_job_title_cpr')    on_call = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_job_title_on_call')    all_occupational_exposure = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                                  related_name='util_job_title_all_occupational_exposure')    some_occupational_exposure = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                                   related_name='util_job_title_some_occupational_exposure')    flsa_status = models.ForeignKey(UtilFlsaStatus, null=True, related_name='util_job_title_flsa_status')    curriculums = models.ManyToManyField('UtilCurriculums', related_name='util_job_title_curriculums')    safety_curriculums = models.ManyToManyField('UtilSafetyCurriculums', related_name='util_job_title_safety_curriculums')    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_job_titles'class UtilCurriculums(models.Model):    course = models.ForeignKey('dashboard.CoreCourses')    number_of_days = models.IntegerField(null=True)    date_assigned = models.DateField(auto_now_add=True)    date_completed = models.DateField(null=True)    last_started = models.DateField(null=True)    resume_from_page = models.IntegerField(null=True, default=0)    user_notes = models.TextField(null=True)    is_completed = models.NullBooleanField(null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_curriculums'class UtilCustomPoliciesTitles(models.Model):    policy_title = models.CharField(max_length=255, null=False)    is_active = models.BooleanField(null=False)    class Meta():        db_table = 'util_custom_policies_titles'class UtilSafetyCurriculums(models.Model):    course = models.ForeignKey('dashboard.CoreCourses')    month_assigned = models.IntegerField(null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_safety_curriculums'class UtilRegAgencies(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    acronym = models.CharField(max_length=256, null=True)    description = models.TextField(max_length=256, null=True)    classification = models.ForeignKey('UtilRegAgencyClassification', null=True,                                       related_name='util_reg_agencies_classification')    subclassification = models.ForeignKey('UtilRegAgencySubClassification', null=True,                                          related_name='util_reg_agencies_subclassification')    address1 = models.CharField(max_length=256, null=True)    address2 = models.CharField(max_length=256, null=True)    city = models.CharField(max_length=256, null=True)    state = models.CharField(max_length=256, null=True)    zip = models.CharField(max_length=256, null=True)    phone = models.CharField(max_length=256, null=True)    tty_phone = models.CharField(max_length=256, null=True)    fax = models.CharField(max_length=256, null=True)    website = models.CharField(max_length=256, null=True)    email = models.CharField(max_length=256, null=True)    point_of_contact = models.CharField(max_length=256, null=True)    point_of_contact_title = models.CharField(max_length=256, null=True)    point_of_contact_email = models.CharField(max_length=256, null=True)    point_of_contact_phone = models.CharField(max_length=256, null=True)    membership_agency = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                          related_name='util_reg_agencies_membership_agency')    dot_intrastste_age = models.CharField(max_length=256, null=True)    fema_region = models.CharField(max_length=256, null=True)    osha_state_plan = models.CharField(max_length=256, null=True)    hhs_region = models.CharField(max_length=256, null=True)    approved_ce_provider = models.ForeignKey(UtilYesorNo, to_field='value', null=True,                                             related_name='util_reg_agencies_approved_ce_provider')    regulations = models.ManyToManyField('UtilRegAgencyRegulations', related_name='util_reg_agencies_regulations')    states = models.ManyToManyField(UtilUSAStates, related_name='util_reg_agencies_states')    cities = models.ManyToManyField(UtilZipCodes, related_name='util_reg_agencies_cities')    counties = models.ManyToManyField(UtilZipCodes, related_name='util_reg_agencies_counties')    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_reg_agencies'    @property    def sorted_regulations(self):        return self.regulations.all().order_by('reg_code')class UtilRegAgenciesRegulations(models.Model):    utilregagencies = models.ForeignKey(UtilRegAgencies, related_name='agencies_regulations')    utilregagencyregulations = models.ForeignKey('UtilRegAgencyRegulations')    class Meta():        db_table = 'util_reg_agencies_regulations'class UtilRegAgencyRegulationsByCity(models.Model):    util_reg_agency_regulations = models.ForeignKey('UtilRegAgencyRegulations')    state_abbr = models.CharField(max_length=2)    city_name = models.CharField(max_length=64)    class Meta():        db_table = 'util_reg_agency_regulations_by_city'class UtilRegAgencyRegulationsByCounty(models.Model):    util_reg_agency_regulations = models.ForeignKey('UtilRegAgencyRegulations')    county_fips = models.CharField(max_length=11)    class Meta():        db_table = 'util_reg_agency_regulations_by_county'class UtilRegAgencyRegulationsByState(models.Model):    util_reg_agency_regulations = models.ForeignKey('UtilRegAgencyRegulations')    states = models.ForeignKey('UtilUSAStates')    class Meta():        db_table = 'util_reg_agency_regulations_by_state'class UtilRegAgencyClassification(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_reg_agency_classification'class UtilRegAgencySubClassification(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    parent = models.ForeignKey("self", null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_reg_agency_sub_classification'class UtilRegAgencyRegulations(models.Model):    short_code = models.CharField(max_length=256, null=True)    reg_code = models.CharField(max_length=256, null=True)    reg_title = models.CharField(max_length=256, null=True)    description = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    is_federal = models.NullBooleanField(null=True)    is_state = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_reg_agency_regulations'        ordering = ['reg_code']class UtilObjectives(models.Model):    short_code = models.CharField(max_length=256, null=True)    name = models.CharField(max_length=256, null=True)    description = models.TextField(null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_objectives'"""class UtilPages(models.Model):	short_code = models.CharField(max_length=256, null=True)	raw_html = models.TextField(null=True)	page_number = models.IntegerField(max_length=256, null=True)	required_time = models.IntegerField(null=True)	is_active = models.NullBooleanField(null=True)	class Meta():		db_table = 'util_pages'class UtilCourses(models.Model):	short_name = models.CharField(max_length=256, null=True)	name = models.CharField(max_length=256, null=True)	number = models.CharField(max_length=256, null=True)	description = models.CharField(max_length=256, null=True)	long_description = models.TextField(null=True)	type = models.ForeignKey(UtilCourseTypes, null=True, related_name='util_course_type')	category = models.ForeignKey(UtilCourseCategories, null=True, related_name='util_course_category')	prerequisite = models.ManyToManyField("self", symmetrical=False, null=True, related_name='util_course_prerequisite')	regulatory_comments = models.CharField(max_length=256, null=True)	hours = models.DecimalField(null=True, max_digits=5, decimal_places=2)	continuing_education = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_continuing_education')	date_loaded = models.DateTimeField(null=True)	date_last_updated = models.DateTimeField(null=True)	number_of_pages = models.IntegerField(null=True)	number_test_questions = models.IntegerField(null=True)	has_referral_agencies = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_has_referral_agencies')	has_appendices = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_has_appendices')	has_glossary = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_has_glossary')	is_annual_course = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_is_annual_course')	monthly_safety_course = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_monthly_safety_course')	date_deactivated = models.DateTimeField(null=True)	date_deactivated = models.DateTimeField(null=True)	annual_start_date = models.DateTimeField(null=True)	annual_end_date = models.DateTimeField(null=True)	appendix = models.TextField(null=True)	objectives = models.ManyToManyField(UtilObjectives, related_name='util_course_objectives')	regulations = models.ManyToManyField('UtilRegAgencyRegulations', related_name='util_course_regulations')	pages = models.ManyToManyField(UtilPages, related_name='util_course_UtilPages')	is_custom = models.ForeignKey(UtilYesorNo, to_field='value', null=True, related_name='util_course_is_custom')	is_active = models.NullBooleanField(null=True)	class Meta():		db_table = 'util_courses' """class UtilReplacementTags(models.Model):    name = models.CharField(max_length=256, null=True)    short_code = models.CharField(max_length=256, null=True)    description = models.TextField(null=True)    default = models.TextField(null=True)    type = models.CharField(max_length=256, null=True)    is_active = models.NullBooleanField(null=True)    class Meta():        db_table = 'util_replacement_tags'class UtilStateCellPhoneLaws(models.Model):    state = models.CharField(max_length=2, null=True)    cell_handheld_ban = models.CharField(max_length=256, null=True)    cell_bus_drivers = models.CharField(max_length=256, null=True)    cell_novice_drivers = models.CharField(max_length=256, null=True)    text_all_drivers = models.CharField(max_length=256, null=True)    text_bus_drivers = models.CharField(max_length=256, null=True)    text_novice_drivers = models.CharField(max_length=256, null=True)    enforcement = models.CharField(max_length=256, null=True)    footnote = models.TextField(null=True)    class Meta():        db_table = 'util_state_cell_phone_laws'"""class UtilMediaType(models.Model):	name = models.CharField(max_length=256, null=True)	short_code = models.CharField(max_length=256, null=True)	description = models.TextField(null=True)	class Meta():		db_table = 'util_media_type'"""class UtilGradingScales(models.Model):    percent = models.IntegerField(primary_key=True)        gpa = models.DecimalField(max_digits=2, decimal_places=1, null=True)        letter_grade = models.CharField(max_length=256, null=True)        class Meta():        db_table = 'util_grading_scales'class UtilTimezones(models.Model):        TimeZones = models.CharField(max_length=45, null=True)    DST = models.CharField(max_length=1, null=True)    UTC_DT = models.DecimalField(max_digits=3, decimal_places=1, null=True)    DT_Abbreviation = models.CharField(max_length=4, null=True)    UTC_ST = models.DecimalField(max_digits=3, decimal_places=1, null=True)    ST_Abbreviation = models.CharField(max_length=4, null=True)    is_active = models.BooleanField(default=1)        class Meta():        db_table = 'util_timezones'class UtilResourceCategories(models.Model):        parent_id = models.IntegerField(null=True)    name = models.CharField(max_length=150, null=True)    icon = models.CharField(max_length=50, null=True)     is_noncustom = models.BooleanField(default=0)         is_custom = models.BooleanField(default=0)     display_in_video_library = models.BooleanField(default=0)    display_in_forms_library = models.BooleanField(default=0)     display_in_pubs_library = models.BooleanField(default=0)     is_active = models.BooleanField(default=0)        class Meta():        db_table = 'util_resource_categories'class UtilLanguageIsoCodes(models.Model):        language = models.CharField(max_length=45, null=True)     short_code = models.CharField(max_length=3, null=True)     flag = models.CharField(max_length=255, null=True)     is_active = models.BooleanField(default=0)         class Meta():        db_table = 'util_language_iso_codes'class UtilResourceSizes(models.Model):        size = models.CharField(max_length=255)     type = models.CharField(max_length=255, null=True)         class Meta():        db_table = 'util_resource_sizes'class UtilResourceFormats(models.Model):        format_name = models.CharField(max_length=255)     file_extension = models.CharField(max_length=10)     icon = models.CharField(max_length=50, null=True)     icon_load_color = models.CharField(max_length=10, null=True)     icon_hover_color = models.CharField(max_length=10, null=True)     description = models.TextField(null=True)     display_in_forms_library = models.BooleanField(default=0)     display_in_custom_forms = models.BooleanField(default=0)    display_in_pubs_library = models.BooleanField(default=0)     display_in_custom_pubs = models.BooleanField(default=0)     display_in_images_library = models.BooleanField(default=0)     display_in_custom_images = models.BooleanField(default=0)     display_in_video_library = models.BooleanField(default=0)     display_in_custom_videos = models.BooleanField(default=0)     display_in_audio_library = models.BooleanField(default=0)     display_in_custom_audio = models.BooleanField(default=0)     display_in_inservice_tracker = models.BooleanField(default=0)     is_active = models.BooleanField(default=0)         class Meta():        db_table = 'util_resource_formats'class UtilFontSizes(models.Model):        font_size = models.CharField(max_length=256)    short_code = models.CharField(max_length=256)    is_active = models.BooleanField(default=1)        class Meta():        db_table = 'util_font_sizes'        class UtilCeUnitsOfMeasure(models.Model):            ce_units_description = models.CharField(max_length=45, null=True)     ce_units_description_plural = models.CharField(max_length=45, null=True)     ce_hours_desc = models.CharField(max_length=45, null=True)     ce_conversion_factor = models.DecimalField(null=True, max_digits=4, decimal_places=2)     ce_units_explanation = models.CharField(max_length=256, null=True)     is_active = models.BooleanField(default=0)        class Meta():        db_table = 'util_ce_units_of_measure'class UtilPriorities(models.Model):        priority_desc = models.CharField(max_length=45)     is_active = models.BooleanField(default=1)    class Meta():        db_table = 'util_priorities'class UtilGenders(models.Model):        gender_abbreviation = models.CharField(max_length=1)    gender = models.CharField(max_length=20)    is_active = models.BooleanField(default=True)    class Meta():        db_table = 'util_genders'class UtilReportCategories(models.Model):    report_category = models.CharField(max_length=45, null=True)    report_desc = models.CharField(max_length=360, null=True)    hexcolor = models.CharField(max_length=7, null=True)    icon = models.CharField(max_length=75, null=True)    is_active = models.BooleanField(default=True)    report_url = models.CharField(max_length=255, null=False)    display_priority = models.IntegerField(null=True)    class Meta():        db_table = 'util_report_categories'    @property    def reports_count(self):        return len(self.reports.filter(is_active=True))#faq tablesclass UtilFaqCategories(models.Model):    show_outside = models.BooleanField(default=False)    show_inside = models.BooleanField(default=False)    title = models.CharField(max_length=250, null=False)    description = models.TextField(null=False)    is_active = models.BooleanField(default=False)    class Meta():        db_table = 'util_faq_categories'class UtilFaqs(models.Model):    faq_category = models.ForeignKey(UtilFaqCategories)    show_outside = models.BooleanField(default=False)    show_inside = models.BooleanField(default=False)    question = models.CharField(max_length=255, default='')    answer = models.TextField(null=False)    is_active = models.BooleanField(default=False)    class Meta():        db_table = 'util_faqs'class UtilLeadSources(models.Model):    lead_source_name = models.CharField(max_length=256, null=False)    is_active = models.BooleanField(default=True)    class Meta():        db_table = 'util_lead_sources'class UtilLMSSystems(models.Model):    LMS_name = models.CharField(max_length=255, null=False)    is_active = models.BooleanField(default=True)    class Meta():        db_table = 'util_LMS_systems'class UtilIndustryEvents(models.Model):    industry_event_name = models.CharField(max_length=26, null=False)    event_description = models.CharField(max_length=150, null=False)    event_image_370x322 = models.CharField(max_length=255, null=False)    event_start_date = models.DateField(null=False)    remove_date_plus_one_day = models.DateField(null=False)    event_dates = models.CharField(max_length=40, null=False)    event_website_url = models.CharField(max_length=255, null=True)    will_hhlearn_be_there = models.BooleanField(default=True)    is_active = models.BooleanField(default=True)    class Meta():        db_table = 'util_industry_events'class UtilChangeOrDeactivate(models.Model):    status = models.CharField(max_length=255, null=False)    is_active = models.BooleanField(default=True)    class Meta():        db_table = 'util_change_or_deactivate'class UtilEmailTemplates(models.Model):    template_name = models.CharField(max_length=255, null=False)    template_description = models.CharField(max_length=255, null=True)    email_template_code	= models.TextField(null=False)    is_active = models.BooleanField(default=True)    class Meta():        db_table = 'util_email_templates'