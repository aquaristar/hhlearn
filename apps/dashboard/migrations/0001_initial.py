# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CoreSettings'
        db.create_table('core_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreSettings'])

        # Adding model 'CorePlans'
        db.create_table('core_plans', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('monthly_price', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True)),
        ))
        db.send_create_signal(u'dashboard', ['CorePlans'])

        # Adding M2M table for field modules on 'CorePlans'
        m2m_table_name = db.shorten_name('core_plans_modules')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreplans', models.ForeignKey(orm[u'dashboard.coreplans'], null=False)),
            ('coremodules', models.ForeignKey(orm[u'dashboard.coremodules'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreplans_id', 'coremodules_id'])

        # Adding M2M table for field user_packs on 'CorePlans'
        m2m_table_name = db.shorten_name('core_plans_user_packs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreplans', models.ForeignKey(orm[u'dashboard.coreplans'], null=False)),
            ('coreuserpacks', models.ForeignKey(orm[u'dashboard.coreuserpacks'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreplans_id', 'coreuserpacks_id'])

        # Adding model 'CoreModules'
        db.create_table('core_modules', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('is_addon', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreModules'])

        # Adding model 'CoreUserPacks'
        db.create_table('core_user_packs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True)),
            ('monthly_price', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True)),
            ('allowed_users', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'dashboard', ['CoreUserPacks'])

        # Adding model 'CoreBilling'
        db.create_table('core_billing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plan', null=True, to=orm['dashboard.CorePlans'])),
            ('user_pack', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_pack', null=True, to=orm['dashboard.CoreUserPacks'])),
            ('renewal_term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['utility.UtilRenewalTerms'], null=True)),
            ('payment_method', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payment_method', null=True, to=orm['utility.UtilPaymentMethods'])),
            ('credit_card_person_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('credit_card_number', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('card_expiry_month', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('card_expiry_year', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('billing_address_1', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreBilling'])

        # Adding model 'CoreOfficials'
        db.create_table('core_officials', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organization_job_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('actual_job_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('official_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='official_type', null=True, to=orm['utility.UtilOfficialTypes'])),
            ('is_organization_wide', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_location_wide', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreOfficials'])

        # Adding model 'CoreDepartments'
        db.create_table('core_departments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('no_of_fire_exists', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('where_written_hazard_located', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('when_hazard_prog_available', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('where_safety_data_located', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('emergency_location', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_accredited', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_is_accredited', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('hippa_notice_location', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('accreditation_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_accreditation_agency', null=True, to=orm['utility.UtilRegAgencies'])),
            ('use_electronic_posting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_use_electronic_posting', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('min_score_general_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_min_score_general_knowledge', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_continuing_education', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_min_score_continuing_education', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_employee_competency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_min_score_employee_competency', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_custom_courses', self.gf('django.db.models.fields.related.ForeignKey')(related_name='department_min_score_custom_courses', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreDepartments'])

        # Adding M2M table for field officials on 'CoreDepartments'
        m2m_table_name = db.shorten_name('core_departments_officials')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coredepartments', models.ForeignKey(orm[u'dashboard.coredepartments'], null=False)),
            ('coreofficials', models.ForeignKey(orm[u'dashboard.coreofficials'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coredepartments_id', 'coreofficials_id'])

        # Adding M2M table for field modules on 'CoreDepartments'
        m2m_table_name = db.shorten_name('core_departments_modules')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coredepartments', models.ForeignKey(orm[u'dashboard.coredepartments'], null=False)),
            ('coremodules', models.ForeignKey(orm[u'dashboard.coremodules'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coredepartments_id', 'coremodules_id'])

        # Adding M2M table for field services_offered on 'CoreDepartments'
        m2m_table_name = db.shorten_name('core_departments_services_offered')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coredepartments', models.ForeignKey(orm[u'dashboard.coredepartments'], null=False)),
            ('coreservicesoffered', models.ForeignKey(orm[u'dashboard.coreservicesoffered'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coredepartments_id', 'coreservicesoffered_id'])

        # Adding M2M table for field job_titles on 'CoreDepartments'
        m2m_table_name = db.shorten_name('core_departments_job_titles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coredepartments', models.ForeignKey(orm[u'dashboard.coredepartments'], null=False)),
            ('corejobtitles', models.ForeignKey(orm[u'dashboard.corejobtitles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coredepartments_id', 'corejobtitles_id'])

        # Adding model 'CoreLocations'
        db.create_table('core_locations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('street_address_1', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('street_address_2', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='state', to=orm['utility.UtilUSAStates'])),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_primary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_primary', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_command_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_command_location', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('no_of_fire_exists', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('where_written_hazard_located', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('when_hazard_prog_available', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('where_safety_data_located', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('eer_location', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('when_eer_available', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('emr_location', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('when_emr_available', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('hippa_notice_location', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('emergency_location', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('use_electronic_posting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='use_electronic_posting', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_accredited', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_accredited', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('accreditation_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accreditation_agency', null=True, to=orm['utility.UtilRegAgencies'])),
            ('min_score_general_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_min_score_general_knowledge', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_continuing_education', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_min_score_continuing_education', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_employee_competency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_min_score_employee_competency', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_custom_courses', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_min_score_custom_courses', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('departments_enabled', self.gf('django.db.models.fields.related.ForeignKey')(related_name='departments_enabled', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('total_departments', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreLocations'])

        # Adding M2M table for field modules on 'CoreLocations'
        m2m_table_name = db.shorten_name('core_locations_modules')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False)),
            ('coremodules', models.ForeignKey(orm[u'dashboard.coremodules'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corelocations_id', 'coremodules_id'])

        # Adding M2M table for field officials on 'CoreLocations'
        m2m_table_name = db.shorten_name('core_locations_officials')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False)),
            ('coreofficials', models.ForeignKey(orm[u'dashboard.coreofficials'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corelocations_id', 'coreofficials_id'])

        # Adding M2M table for field services_offered on 'CoreLocations'
        m2m_table_name = db.shorten_name('core_locations_services_offered')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False)),
            ('coreservicesoffered', models.ForeignKey(orm[u'dashboard.coreservicesoffered'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corelocations_id', 'coreservicesoffered_id'])

        # Adding M2M table for field departments on 'CoreLocations'
        m2m_table_name = db.shorten_name('core_locations_departments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False)),
            ('coredepartments', models.ForeignKey(orm[u'dashboard.coredepartments'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corelocations_id', 'coredepartments_id'])

        # Adding M2M table for field job_titles on 'CoreLocations'
        m2m_table_name = db.shorten_name('core_locations_job_titles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False)),
            ('corejobtitles', models.ForeignKey(orm[u'dashboard.corejobtitles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corelocations_id', 'corejobtitles_id'])

        # Adding model 'CorePointOfContacts'
        db.create_table('core_point_of_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_primary', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CorePointOfContacts'])

        # Adding model 'CoreUserProfiles'
        db.create_table('core_user_profiles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='core_user_profile', unique=True, to=orm['auth.User'])),
            ('activation_token', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('requested_welcome_email', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('requested_tos_email', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_user_profile_location', null=True, to=orm['dashboard.CoreLocations'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_user_profile_department', null=True, to=orm['dashboard.CoreDepartments'])),
            ('job_title', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_user_profile_job_title', null=True, to=orm['dashboard.CoreJobTitles'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_user_profile_region', null=True, to=orm['dashboard.CoreRegions'])),
        ))
        db.send_create_signal(u'dashboard', ['CoreUserProfiles'])

        # Adding M2M table for field modules on 'CoreUserProfiles'
        m2m_table_name = db.shorten_name('core_user_profiles_modules')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreuserprofiles', models.ForeignKey(orm[u'dashboard.coreuserprofiles'], null=False)),
            ('coremodules', models.ForeignKey(orm[u'dashboard.coremodules'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreuserprofiles_id', 'coremodules_id'])

        # Adding model 'CoreServicesOffered'
        db.create_table('core_services_offered', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreServicesOffered'])

        # Adding M2M table for field job_titles on 'CoreServicesOffered'
        m2m_table_name = db.shorten_name('core_services_offered_job_titles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreservicesoffered', models.ForeignKey(orm[u'dashboard.coreservicesoffered'], null=False)),
            ('corejobtitles', models.ForeignKey(orm[u'dashboard.corejobtitles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreservicesoffered_id', 'corejobtitles_id'])

        # Adding model 'CoreRegions'
        db.create_table('core_regions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreRegions'])

        # Adding M2M table for field locations on 'CoreRegions'
        m2m_table_name = db.shorten_name('core_regions_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreregions', models.ForeignKey(orm[u'dashboard.coreregions'], null=False)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreregions_id', 'corelocations_id'])

        # Adding M2M table for field departments on 'CoreRegions'
        m2m_table_name = db.shorten_name('core_regions_departments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreregions', models.ForeignKey(orm[u'dashboard.coreregions'], null=False)),
            ('coredepartments', models.ForeignKey(orm[u'dashboard.coredepartments'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreregions_id', 'coredepartments_id'])

        # Adding model 'CoreObjectives'
        db.create_table('core_objectives', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreObjectives'])

        # Adding model 'CoreImages'
        db.create_table('core_images', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('alt', self.gf('django.db.models.fields.TextField')(null=True)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('hspace', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('vspace', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('align', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('source', self.gf('django.db.models.fields.TextField')(null=True)),
            ('border', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreImages'])

        # Adding model 'CoreVideos'
        db.create_table('core_videos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('cover', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreVideos'])

        # Adding model 'CoreGlossarySources'
        db.create_table('core_glossary_sources', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreGlossarySources'])

        # Adding model 'CoreGlossaryWords'
        db.create_table('core_glossary_words', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('pronounce', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('syllable', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('definition', self.gf('django.db.models.fields.TextField')(null=True)),
            ('glossary_source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_glossary_word_course', null=True, to=orm['dashboard.CoreGlossarySources'])),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreGlossaryWords'])

        # Adding model 'CorePages'
        db.create_table('core_pages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('raw_html', self.gf('django.db.models.fields.TextField')(null=True)),
            ('page_number', self.gf('django.db.models.fields.IntegerField')(max_length=256, null=True)),
            ('required_time', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CorePages'])

        # Adding model 'CoreCourseTypes'
        db.create_table('core_course_types', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreCourseTypes'])

        # Adding model 'CoreCourseCategories'
        db.create_table('core_course_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreCourseCategories'])

        # Adding model 'CoreReferralAgencies'
        db.create_table('core_referral_agencies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('referral_agency_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('tty_phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('point_of_contact', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('point_of_contact_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('point_of_contact_email', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('point_of_contact_phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreReferralAgencies'])

        # Adding model 'CoreCourses'
        db.create_table('core_courses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('long_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_type', null=True, to=orm['dashboard.CoreCourseTypes'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_category', null=True, to=orm['dashboard.CoreCourseCategories'])),
            ('regulatory_comments', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
            ('continuing_education', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_continuing_education', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('date_loaded', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('date_last_updated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('number_of_pages', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('number_test_questions', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('has_referral_agencies', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_has_referral_agencies', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('has_appendices', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_has_appendices', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('has_glossary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_has_glossary', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_annual_course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_is_annual_course', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('monthly_safety_course', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_monthly_safety_course', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('date_deactivated', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('annual_start_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('annual_end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('appendix', self.gf('django.db.models.fields.TextField')(null=True)),
            ('is_custom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_course_is_custom', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreCourses'])

        # Adding M2M table for field referral_agencies on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_referral_agencies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('corereferralagencies', models.ForeignKey(orm[u'dashboard.corereferralagencies'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'corereferralagencies_id'])

        # Adding M2M table for field prerequisite on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_prerequisite')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('to_corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_corecourses_id', 'to_corecourses_id'])

        # Adding M2M table for field objectives on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_objectives')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('coreobjectives', models.ForeignKey(orm[u'dashboard.coreobjectives'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'coreobjectives_id'])

        # Adding M2M table for field regulations on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_regulations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('utilregagencyregulations', models.ForeignKey(orm[u'utility.utilregagencyregulations'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'utilregagencyregulations_id'])

        # Adding M2M table for field pages on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_pages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('corepages', models.ForeignKey(orm[u'dashboard.corepages'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'corepages_id'])

        # Adding M2M table for field images on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('coreimages', models.ForeignKey(orm[u'dashboard.coreimages'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'coreimages_id'])

        # Adding M2M table for field videos on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_videos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('corevideos', models.ForeignKey(orm[u'dashboard.corevideos'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'corevideos_id'])

        # Adding M2M table for field glossary_words on 'CoreCourses'
        m2m_table_name = db.shorten_name('core_courses_glossary_words')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False)),
            ('coreglossarywords', models.ForeignKey(orm[u'dashboard.coreglossarywords'], null=False))
        ))
        db.create_unique(m2m_table_name, ['corecourses_id', 'coreglossarywords_id'])

        # Adding model 'CoreJobTitles'
        db.create_table('core_job_titles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name_possessive', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name_custom', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name_custom_possessive', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_category', null=True, to=orm['utility.UtilJobCategories'])),
            ('patient_file_access', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_patient_file_access', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('exposure_to_chemicals', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_exposure_to_chemicals', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('exposure_to_BBP', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_exposure_to_BBP', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('exposure_to_TB', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_exposure_to_TB', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('requires_license', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_requires_license', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('cpr', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_cpr', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('on_call', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_on_call', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('flsa_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_flsa_status', null=True, to=orm['utility.UtilFlsaStatus'])),
            ('is_custom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_is_custom', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('all_occupational_exposure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_all_occupational_exposure', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('some_occupational_exposure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_title_some_occupational_exposure', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreJobTitles'])

        # Adding model 'CoreCurriculums'
        db.create_table('core_curriculums', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.CoreJobTitles'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.CoreCourses'])),
            ('number_of_days', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'dashboard', ['CoreCurriculums'])

        # Adding model 'CoreOrganizations'
        db.create_table('core_organizations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('add_date', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('activation_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('number_of_licenses', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('modules_consistent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='modules_consistent', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('services_consistent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services_consistent', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('jobs_consistent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='jobs_consistent', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_organization_accredited', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_organization_accredited', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('billing', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_organization', null=True, to=orm['dashboard.CoreBilling'])),
            ('accreditation_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_organization', null=True, to=orm['utility.UtilRegAgencies'])),
            ('is_entire_organization_accredited', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_entire_organization_accredited', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_accredited_by_same_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_accredited_by_same_agency', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('use_monthly_safety_courses', self.gf('django.db.models.fields.related.ForeignKey')(related_name='use_monthly_safety_courses', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_organization', null=True, to=orm['utility.UtilOrganizationType'])),
            ('is_score_consistent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='score_consistent', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('min_score_general_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='min_score_general_knowledge', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_continuing_education', self.gf('django.db.models.fields.related.ForeignKey')(related_name='min_score_continuing_education', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_employee_competency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='min_score_employee_competency', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('min_score_custom_courses', self.gf('django.db.models.fields.related.ForeignKey')(related_name='min_score_custom_courses', to_field='score', null=True, to=orm['utility.UtilPassingScores'])),
            ('is_signup_monthly_safety_program', self.gf('django.db.models.fields.related.ForeignKey')(related_name='signup_monthly_safety_program', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_course_selections_consistent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='course_selections_consistent', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_electronic_postings_enabled', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_electronic_postings_enabled', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_electronic_postings_consistent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_electronic_postings_consistent', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_use_ssn_for_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_use_ssn_for_user', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('total_number_of_employees', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_employee_specific_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_employee_specific_id', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('total_number_of_locations', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('current_setup_section', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_initial_setup_complete', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_initial_setup_complete', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('departments_enabled', self.gf('django.db.models.fields.related.ForeignKey')(related_name='org_departments_enabled', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('regions_enabled', self.gf('django.db.models.fields.related.ForeignKey')(related_name='org_regions_enabled', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('total_regions', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.related.ForeignKey')(related_name='is_active', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('custom_job_titles_enabled', self.gf('django.db.models.fields.related.ForeignKey')(related_name='org_custom_job_titles_enabled', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('location_specific_job_titles', self.gf('django.db.models.fields.related.ForeignKey')(related_name='org_location_specific_job_titles', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('department_specific_job_titles', self.gf('django.db.models.fields.related.ForeignKey')(related_name='org_department_specific_job_titles', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('total_custom_job_titles', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('custom_job_courses_enabled', self.gf('django.db.models.fields.related.ForeignKey')(related_name='org_custom_job_courses_enabled', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
        ))
        db.send_create_signal(u'dashboard', ['CoreOrganizations'])

        # Adding M2M table for field modules on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_modules')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('coremodules', models.ForeignKey(orm[u'dashboard.coremodules'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'coremodules_id'])

        # Adding M2M table for field locations on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('corelocations', models.ForeignKey(orm[u'dashboard.corelocations'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'corelocations_id'])

        # Adding M2M table for field user_profiles on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_user_profiles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('coreuserprofiles', models.ForeignKey(orm[u'dashboard.coreuserprofiles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'coreuserprofiles_id'])

        # Adding M2M table for field point_of_contacts on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_point_of_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('corepointofcontacts', models.ForeignKey(orm[u'dashboard.corepointofcontacts'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'corepointofcontacts_id'])

        # Adding M2M table for field services_offered on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_services_offered')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('coreservicesoffered', models.ForeignKey(orm[u'dashboard.coreservicesoffered'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'coreservicesoffered_id'])

        # Adding M2M table for field officials on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_officials')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('coreofficials', models.ForeignKey(orm[u'dashboard.coreofficials'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'coreofficials_id'])

        # Adding M2M table for field regions on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_regions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('coreregions', models.ForeignKey(orm[u'dashboard.coreregions'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'coreregions_id'])

        # Adding M2M table for field job_titles on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_job_titles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('corejobtitles', models.ForeignKey(orm[u'dashboard.corejobtitles'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'corejobtitles_id'])

        # Adding M2M table for field courses on 'CoreOrganizations'
        m2m_table_name = db.shorten_name('core_organizations_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coreorganizations', models.ForeignKey(orm[u'dashboard.coreorganizations'], null=False)),
            ('corecourses', models.ForeignKey(orm[u'dashboard.corecourses'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coreorganizations_id', 'corecourses_id'])


    def backwards(self, orm):
        # Deleting model 'CoreSettings'
        db.delete_table('core_settings')

        # Deleting model 'CorePlans'
        db.delete_table('core_plans')

        # Removing M2M table for field modules on 'CorePlans'
        db.delete_table(db.shorten_name('core_plans_modules'))

        # Removing M2M table for field user_packs on 'CorePlans'
        db.delete_table(db.shorten_name('core_plans_user_packs'))

        # Deleting model 'CoreModules'
        db.delete_table('core_modules')

        # Deleting model 'CoreUserPacks'
        db.delete_table('core_user_packs')

        # Deleting model 'CoreBilling'
        db.delete_table('core_billing')

        # Deleting model 'CoreOfficials'
        db.delete_table('core_officials')

        # Deleting model 'CoreDepartments'
        db.delete_table('core_departments')

        # Removing M2M table for field officials on 'CoreDepartments'
        db.delete_table(db.shorten_name('core_departments_officials'))

        # Removing M2M table for field modules on 'CoreDepartments'
        db.delete_table(db.shorten_name('core_departments_modules'))

        # Removing M2M table for field services_offered on 'CoreDepartments'
        db.delete_table(db.shorten_name('core_departments_services_offered'))

        # Removing M2M table for field job_titles on 'CoreDepartments'
        db.delete_table(db.shorten_name('core_departments_job_titles'))

        # Deleting model 'CoreLocations'
        db.delete_table('core_locations')

        # Removing M2M table for field modules on 'CoreLocations'
        db.delete_table(db.shorten_name('core_locations_modules'))

        # Removing M2M table for field officials on 'CoreLocations'
        db.delete_table(db.shorten_name('core_locations_officials'))

        # Removing M2M table for field services_offered on 'CoreLocations'
        db.delete_table(db.shorten_name('core_locations_services_offered'))

        # Removing M2M table for field departments on 'CoreLocations'
        db.delete_table(db.shorten_name('core_locations_departments'))

        # Removing M2M table for field job_titles on 'CoreLocations'
        db.delete_table(db.shorten_name('core_locations_job_titles'))

        # Deleting model 'CorePointOfContacts'
        db.delete_table('core_point_of_contacts')

        # Deleting model 'CoreUserProfiles'
        db.delete_table('core_user_profiles')

        # Removing M2M table for field modules on 'CoreUserProfiles'
        db.delete_table(db.shorten_name('core_user_profiles_modules'))

        # Deleting model 'CoreServicesOffered'
        db.delete_table('core_services_offered')

        # Removing M2M table for field job_titles on 'CoreServicesOffered'
        db.delete_table(db.shorten_name('core_services_offered_job_titles'))

        # Deleting model 'CoreRegions'
        db.delete_table('core_regions')

        # Removing M2M table for field locations on 'CoreRegions'
        db.delete_table(db.shorten_name('core_regions_locations'))

        # Removing M2M table for field departments on 'CoreRegions'
        db.delete_table(db.shorten_name('core_regions_departments'))

        # Deleting model 'CoreObjectives'
        db.delete_table('core_objectives')

        # Deleting model 'CoreImages'
        db.delete_table('core_images')

        # Deleting model 'CoreVideos'
        db.delete_table('core_videos')

        # Deleting model 'CoreGlossarySources'
        db.delete_table('core_glossary_sources')

        # Deleting model 'CoreGlossaryWords'
        db.delete_table('core_glossary_words')

        # Deleting model 'CorePages'
        db.delete_table('core_pages')

        # Deleting model 'CoreCourseTypes'
        db.delete_table('core_course_types')

        # Deleting model 'CoreCourseCategories'
        db.delete_table('core_course_categories')

        # Deleting model 'CoreReferralAgencies'
        db.delete_table('core_referral_agencies')

        # Deleting model 'CoreCourses'
        db.delete_table('core_courses')

        # Removing M2M table for field referral_agencies on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_referral_agencies'))

        # Removing M2M table for field prerequisite on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_prerequisite'))

        # Removing M2M table for field objectives on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_objectives'))

        # Removing M2M table for field regulations on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_regulations'))

        # Removing M2M table for field pages on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_pages'))

        # Removing M2M table for field images on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_images'))

        # Removing M2M table for field videos on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_videos'))

        # Removing M2M table for field glossary_words on 'CoreCourses'
        db.delete_table(db.shorten_name('core_courses_glossary_words'))

        # Deleting model 'CoreJobTitles'
        db.delete_table('core_job_titles')

        # Deleting model 'CoreCurriculums'
        db.delete_table('core_curriculums')

        # Deleting model 'CoreOrganizations'
        db.delete_table('core_organizations')

        # Removing M2M table for field modules on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_modules'))

        # Removing M2M table for field locations on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_locations'))

        # Removing M2M table for field user_profiles on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_user_profiles'))

        # Removing M2M table for field point_of_contacts on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_point_of_contacts'))

        # Removing M2M table for field services_offered on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_services_offered'))

        # Removing M2M table for field officials on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_officials'))

        # Removing M2M table for field regions on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_regions'))

        # Removing M2M table for field job_titles on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_job_titles'))

        # Removing M2M table for field courses on 'CoreOrganizations'
        db.delete_table(db.shorten_name('core_organizations_courses'))


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
        u'dashboard.corecurriculums': {
            'Meta': {'object_name': 'CoreCurriculums', 'db_table': "'core_curriculums'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.CoreCourses']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.CoreJobTitles']"}),
            'number_of_days': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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