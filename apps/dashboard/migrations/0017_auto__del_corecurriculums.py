# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CoreCurriculums'
        db.delete_table('core_curriculums')

        # Removing M2M table for field curriculums on 'CoreUserProfiles'
        db.delete_table(db.shorten_name('core_user_profiles_curriculums'))

        # Removing M2M table for field curriculums on 'CoreJobTitles'
        db.delete_table(db.shorten_name('core_job_titles_curriculums'))

        # Removing M2M table for field curriculums on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_curriculums'))


    def backwards(self, orm):
        # Adding model 'CoreCurriculums'
        db.create_table('core_curriculums', (
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.CoreCourses'])),
            ('number_of_days', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreCurriculums'])

        # Adding M2M table for field curriculums on 'CoreUserProfiles'
        m2m_table_name = db.shorten_name('core_user_profiles_curriculums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreuserprofiles', models.ForeignKey(orm[u'dashboard.coreuserprofiles'], null=False)),
            ('corecurriculums', models.ForeignKey(orm[u'dashboard.corecurriculums'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreuserprofiles_id', 'corecurriculums_id'])

        # Adding M2M table for field curriculums on 'CoreJobTitles'
        m2m_table_name = db.shorten_name('core_job_titles_curriculums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corejobtitles', models.ForeignKey(orm[u'dashboard.corejobtitles'], null=False)),
            ('corecurriculums', models.ForeignKey(orm[u'dashboard.corecurriculums'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corejobtitles_id', 'corecurriculums_id'])

        # Adding M2M table for field curriculums on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_curriculums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('corecurriculums', models.ForeignKey(orm[u'dashboard.corecurriculums'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'corecurriculums_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dashboard.corebilling': {
            'Meta': {'object_name': 'CoreBilling', 'db_table': "'core_billing'"},
            'billing_address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'card_expiry_month': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'card_expiry_year': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'credit_card_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'credit_card_person_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payment_method'", 'null': 'True', 'to': u"orm['utility.UtilPaymentMethods']"}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plan'", 'null': 'True', 'to': u"orm['dashboard.CorePlans']"}),
            'renewal_term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['utility.UtilRenewalTerms']", 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'user_pack': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_pack'", 'null': 'True', 'to': u"orm['dashboard.CoreUserPacks']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.corecoursecategories': {
            'Meta': {'object_name': 'CoreCourseCategories', 'db_table': "'core_course_categories'"},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.corecourses': {
            'Meta': {'object_name': 'CoreCourses', 'db_table': "'core_courses'"},
            'annual_end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'annual_start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appendix': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_category'", 'null': 'True', 'to': u"orm['dashboard.CoreCourseCategories']"}),
            'continuing_education': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_continuing_education'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'date_deactivated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_loaded': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'glossary_words': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_courses_glossary_words'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreGlossaryWords']"}),
            'has_appendices': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_has_appendices'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'has_glossary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_has_glossary'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'has_referral_agencies': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_has_referral_agencies'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_course_images'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreImages']"}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_annual_course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_is_annual_course'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_custom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_is_custom'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'long_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'monthly_safety_course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_monthly_safety_course'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'number_of_pages': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'number_test_questions': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'objectives': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_course_objectives'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreObjectives']"}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_course_pages'", 'symmetrical': 'False', 'to': u"orm['dashboard.CorePages']"}),
            'prerequisite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'core_course_prerequisite'", 'null': 'True', 'to': u"orm['dashboard.CoreCourses']"}),
            'referral_agencies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'core_course_referral_agencies'", 'null': 'True', 'to': u"orm['dashboard.CoreReferralAgencies']"}),
            'regulations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'util_course_regulations'", 'symmetrical': 'False', 'to': u"orm['utility.UtilRegAgencyRegulations']"}),
            'regulatory_comments': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_course_type'", 'null': 'True', 'to': u"orm['dashboard.CoreCourseTypes']"}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_course_images'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreVideos']"})
        },
        u'dashboard.corecoursetypes': {
            'Meta': {'object_name': 'CoreCourseTypes', 'db_table': "'core_course_types'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coredepartments': {
            'Meta': {'object_name': 'CoreDepartments', 'db_table': "'core_departments'"},
            'accreditation_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_accreditation_agency'", 'null': 'True', 'to': u"orm['utility.UtilRegAgencies']"}),
            'emergency_location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'hippa_notice_location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accredited': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_is_accredited'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'job_titles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_departments'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreJobTitles']"}),
            'min_score_continuing_education': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_min_score_continuing_education'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_custom_courses': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_min_score_custom_courses'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_employee_competency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_min_score_employee_competency'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_general_knowledge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_min_score_general_knowledge'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_departments'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreModules']"}),
            'no_of_fire_exists': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'officials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_departments'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreOfficials']"}),
            'services_offered': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_departments'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreServicesOffered']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'use_electronic_posting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'department_use_electronic_posting'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'when_hazard_prog_available': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'where_safety_data_located': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'where_written_hazard_located': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreglossarysources': {
            'Meta': {'object_name': 'CoreGlossarySources', 'db_table': "'core_glossary_sources'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreglossarywords': {
            'Meta': {'ordering': "('word',)", 'object_name': 'CoreGlossaryWords', 'db_table': "'core_glossary_words'"},
            'definition': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'glossary_source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_glossary_word_course'", 'null': 'True', 'to': u"orm['dashboard.CoreGlossarySources']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pronounce': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'syllable': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreimages': {
            'Meta': {'object_name': 'CoreImages', 'db_table': "'core_images'"},
            'align': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'alt': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'border': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hspace': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'source': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'vspace': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'dashboard.corejobtitles': {
            'Meta': {'object_name': 'CoreJobTitles', 'db_table': "'core_job_titles'"},
            'all_occupational_exposure': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_all_occupational_exposure'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_category'", 'null': 'True', 'to': u"orm['utility.UtilJobCategories']"}),
            'cpr': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_cpr'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'exposure_to_BBP': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_exposure_to_BBP'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'exposure_to_TB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_exposure_to_TB'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'exposure_to_chemicals': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_exposure_to_chemicals'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'flsa_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_flsa_status'", 'null': 'True', 'to': u"orm['utility.UtilFlsaStatus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_custom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_is_custom'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'name_custom': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'name_custom_possessive': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'name_possessive': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'on_call': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_on_call'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'patient_file_access': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_patient_file_access'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'requires_license': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_requires_license'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'some_occupational_exposure': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_title_some_occupational_exposure'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"})
        },
        u'dashboard.corelocations': {
            'Meta': {'object_name': 'CoreLocations', 'db_table': "'core_locations'"},
            'accreditation_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accreditation_agency'", 'null': 'True', 'to': u"orm['utility.UtilRegAgencies']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'departments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_departments'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreDepartments']"}),
            'departments_enabled': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'departments_enabled'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'eer_location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'emergency_location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'emr_location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'hippa_notice_location': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accredited': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_accredited'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'is_command_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_command_location'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_primary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_primary'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'job_titles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_locations'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreJobTitles']"}),
            'min_score_continuing_education': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_min_score_continuing_education'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_custom_courses': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_min_score_custom_courses'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_employee_competency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_min_score_employee_competency'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_general_knowledge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_min_score_general_knowledge'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_location'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreModules']"}),
            'no_of_fire_exists': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'officials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_location'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreOfficials']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'services_offered': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_locations'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreServicesOffered']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'state'", 'to': u"orm['utility.UtilUSAStates']"}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'total_departments': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'use_electronic_posting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'use_electronic_posting'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'when_eer_available': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'when_emr_available': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'when_hazard_prog_available': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'where_safety_data_located': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'where_written_hazard_located': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coremodules': {
            'Meta': {'object_name': 'CoreModules', 'db_table': "'core_modules'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_addon': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'})
        },
        u'dashboard.coreobjectives': {
            'Meta': {'object_name': 'CoreObjectives', 'db_table': "'core_objectives'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreofficials': {
            'Meta': {'object_name': 'CoreOfficials', 'db_table': "'core_officials'"},
            'actual_job_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_location_wide': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'is_organization_wide': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'official_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'official_type'", 'null': 'True', 'to': u"orm['utility.UtilOfficialTypes']"}),
            'organization_job_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreorganizations': {
            'Meta': {'object_name': 'CoreOrganizations', 'db_table': "'core_organizations'"},
            'accreditation_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_organization'", 'null': 'True', 'to': u"orm['utility.UtilRegAgencies']"}),
            'activation_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'add_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'billing': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_organization'", 'null': 'True', 'to': u"orm['dashboard.CoreBilling']"}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'org_courses'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreCourses']"}),
            'current_setup_section': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'custom_job_courses_enabled': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'org_custom_job_courses_enabled'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'custom_job_titles_enabled': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'org_custom_job_titles_enabled'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'department_specific_job_titles': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'org_department_specific_job_titles'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'departments_enabled': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'org_departments_enabled'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accredited_by_same_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_accredited_by_same_agency'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_active': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_active'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_course_selections_consistent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'course_selections_consistent'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_electronic_postings_consistent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_electronic_postings_consistent'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_electronic_postings_enabled': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_electronic_postings_enabled'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_employee_specific_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_employee_specific_id'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_entire_organization_accredited': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_entire_organization_accredited'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_initial_setup_complete': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_initial_setup_complete'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_organization_accredited': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_organization_accredited'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_score_consistent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'score_consistent'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_signup_monthly_safety_program': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signup_monthly_safety_program'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'is_use_ssn_for_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'is_use_ssn_for_user'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'job_titles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'org_job_titles'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreJobTitles']"}),
            'jobs_consistent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobs_consistent'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'location_specific_job_titles': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'org_location_specific_job_titles'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_organization'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreLocations']"}),
            'min_score_continuing_education': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'min_score_continuing_education'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_custom_courses': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'min_score_custom_courses'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_employee_competency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'min_score_employee_competency'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'min_score_general_knowledge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'min_score_general_knowledge'", 'to_field': "'score'", 'null': 'True', 'to': u"orm['utility.UtilPassingScores']"}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_organization'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreModules']"}),
            'modules_consistent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'modules_consistent'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'number_of_licenses': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'officials': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_organization'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreOfficials']"}),
            'point_of_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_organization'", 'symmetrical': 'False', 'to': u"orm['dashboard.CorePointOfContacts']"}),
            'regions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_regions'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreRegions']"}),
            'regions_enabled': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'org_regions_enabled'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'services_consistent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services_consistent'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'services_offered': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_organization'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreServicesOffered']"}),
            'total_custom_job_titles': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total_number_of_employees': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total_number_of_locations': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'total_regions': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_organization'", 'null': 'True', 'to': u"orm['utility.UtilOrganizationType']"}),
            'use_monthly_safety_courses': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'use_monthly_safety_courses'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'user_profiles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_organization'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreUserProfiles']"})
        },
        u'dashboard.corepages': {
            'Meta': {'object_name': 'CorePages', 'db_table': "'core_pages'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'page_number': ('django.db.models.fields.IntegerField', [], {'max_length': '256', 'null': 'True'}),
            'raw_html': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'required_time': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreplans': {
            'Meta': {'object_name': 'CorePlans', 'db_table': "'core_plans'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_plans'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreModules']"}),
            'monthly_price': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'user_packs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_plans'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreUserPacks']"})
        },
        u'dashboard.corepointofcontacts': {
            'Meta': {'object_name': 'CorePointOfContacts', 'db_table': "'core_point_of_contacts'"},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_primary': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.corereferralagencies': {
            'Meta': {'object_name': 'CoreReferralAgencies', 'db_table': "'core_referral_agencies'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact_email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'referral_agency_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'tty_phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreregions': {
            'Meta': {'object_name': 'CoreRegions', 'db_table': "'core_regions'"},
            'departments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'region_core_departments'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreDepartments']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'region_core_locations'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreLocations']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreservicesoffered': {
            'Meta': {'object_name': 'CoreServicesOffered', 'db_table': "'core_services_offered'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'job_titles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_services_offered'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreJobTitles']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coresettings': {
            'Meta': {'object_name': 'CoreSettings', 'db_table': "'core_settings'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreuserpacks': {
            'Meta': {'object_name': 'CoreUserPacks', 'db_table': "'core_user_packs'"},
            'allowed_users': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True'}),
            'monthly_price': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'dashboard.coreuserprofiles': {
            'Meta': {'object_name': 'CoreUserProfiles', 'db_table': "'core_user_profiles'"},
            'activation_token': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_user_profile_department'", 'null': 'True', 'to': u"orm['dashboard.CoreDepartments']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_user_profile_job_title'", 'null': 'True', 'to': u"orm['dashboard.CoreJobTitles']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_user_profile_location'", 'null': 'True', 'to': u"orm['dashboard.CoreLocations']"}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'core_user_profile'", 'symmetrical': 'False', 'to': u"orm['dashboard.CoreModules']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_user_profile_region'", 'null': 'True', 'to': u"orm['dashboard.CoreRegions']"}),
            'requested_tos_email': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'requested_welcome_email': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'core_user_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.corevideos': {
            'Meta': {'object_name': 'CoreVideos', 'db_table': "'core_videos'"},
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'utility.utildmemacs': {
            'Meta': {'object_name': 'UtilDMEMACS', 'db_table': "'util_dme_macs'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '1', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilflsastatus': {
            'Meta': {'object_name': 'UtilFlsaStatus', 'db_table': "'util_flsa_status'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utiljobcategories': {
            'Meta': {'object_name': 'UtilJobCategories', 'db_table': "'util_job_categories'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilofficialtypes': {
            'Meta': {'object_name': 'UtilOfficialTypes', 'db_table': "'util_official_types'"},
            'default_job_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilorganizationtype': {
            'Meta': {'object_name': 'UtilOrganizationType', 'db_table': "'util_organization_type'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilpassingscores': {
            'Meta': {'object_name': 'UtilPassingScores', 'db_table': "'util_passing_scores'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'})
        },
        u'utility.utilpaymentmethods': {
            'Meta': {'object_name': 'UtilPaymentMethods', 'db_table': "'util_payment_methods'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilregagencies': {
            'Meta': {'object_name': 'UtilRegAgencies', 'db_table': "'util_reg_agencies'"},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'approved_ce_provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_reg_agencies_approved_ce_provider'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'util_reg_agencies_cities'", 'symmetrical': 'False', 'to': u"orm['utility.UtilZipCodes']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'classification': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_reg_agencies_classification'", 'null': 'True', 'to': u"orm['utility.UtilRegAgencyClassification']"}),
            'counties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'util_reg_agencies_counties'", 'symmetrical': 'False', 'to': u"orm['utility.UtilZipCodes']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True'}),
            'dot_intrastste_age': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'fema_region': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'hhs_region': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'membership_agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_reg_agencies_membership_agency'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'osha_state_plan': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact_email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'point_of_contact_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'regulations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'util_reg_agencies_regulations'", 'symmetrical': 'False', 'to': u"orm['utility.UtilRegAgencyRegulations']"}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'states': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'util_reg_agencies_states'", 'symmetrical': 'False', 'to': u"orm['utility.UtilUSAStates']"}),
            'subclassification': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_reg_agencies_subclassification'", 'null': 'True', 'to': u"orm['utility.UtilRegAgencySubClassification']"}),
            'tty_phone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilregagencyclassification': {
            'Meta': {'object_name': 'UtilRegAgencyClassification', 'db_table': "'util_reg_agency_classification'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilregagencyregulations': {
            'Meta': {'object_name': 'UtilRegAgencyRegulations', 'db_table': "'util_reg_agency_regulations'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'reg_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'reg_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilregagencysubclassification': {
            'Meta': {'object_name': 'UtilRegAgencySubClassification', 'db_table': "'util_reg_agency_sub_classification'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['utility.UtilRegAgencySubClassification']", 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilrenewalterms': {
            'Meta': {'object_name': 'UtilRenewalTerms', 'db_table': "'util_renewal_terms'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilusastates': {
            'Meta': {'object_name': 'UtilUSAStates', 'db_table': "'util_usa_states'"},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'assoc_press': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'census_division': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'census_division_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'census_region': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'census_region_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'circuit_court': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'dme_macs': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_dme_macs'", 'to': u"orm['utility.UtilDMEMACS']"}),
            'fips_state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'name_possessive': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'occupied': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'standard_federal_region': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilyesorno': {
            'Meta': {'object_name': 'UtilYesorNo', 'db_table': "'util_yes_or_no'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'})
        },
        u'utility.utilzipcodes': {
            'Meta': {'object_name': 'UtilZipCodes', 'db_table': "'util_zip_codes'"},
            'area_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'city_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'county_fips': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'county_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'dst': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6'}),
            'msa_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state_abbr': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state_fips': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'utc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'zip_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        }
    }

    complete_apps = ['dashboard']