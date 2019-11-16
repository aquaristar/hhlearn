# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UtilAnonymousIps'
        db.create_table('util_anonymous_ips', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilAnonymousIps'])

        # Adding model 'UtilZipCodes'
        db.create_table('util_zip_codes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('zip_type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city_type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('county_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('county_fips', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state_abbr', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state_fips', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('msa_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('area_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('time_zone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('utc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1)),
            ('dst', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6)),
        ))
        db.send_create_signal(u'utility', ['UtilZipCodes'])

        # Adding model 'UtilUSAStates'
        db.create_table('util_usa_states', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('occupied', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('fips_state', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('assoc_press', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('standard_federal_region', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('census_region', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('census_region_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('census_division', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('census_division_name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('circuit_court', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name_possessive', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('dme_macs', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_dme_macs', to=orm['utility.UtilDMEMACS'])),
        ))
        db.send_create_signal(u'utility', ['UtilUSAStates'])

        # Adding model 'UtilPaymentMethods'
        db.create_table('util_payment_methods', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilPaymentMethods'])

        # Adding model 'UtilMonths'
        db.create_table('util_months', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilMonths'])

        # Adding model 'UtilYesorNo'
        db.create_table('util_yes_or_no', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilYesorNo'])

        # Adding model 'UtilYears'
        db.create_table('util_years', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilYears'])

        # Adding model 'UtilOrganizationType'
        db.create_table('util_organization_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilOrganizationType'])

        # Adding model 'UtilRenewalTerms'
        db.create_table('util_renewal_terms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilRenewalTerms'])

        # Adding model 'UtilPassingScores'
        db.create_table('util_passing_scores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilPassingScores'])

        # Adding model 'UtilOfficialTypes'
        db.create_table('util_official_types', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('default_job_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilOfficialTypes'])

        # Adding model 'UtilDMEMACS'
        db.create_table('util_dme_macs', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=1, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('street_address_1', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('street_address_2', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilDMEMACS'])

        # Adding model 'UtilJobCategories'
        db.create_table('util_job_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilJobCategories'])

        # Adding model 'UtilFlsaStatus'
        db.create_table('util_flsa_status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilFlsaStatus'])

        # Adding model 'UtilRegAgencies'
        db.create_table('util_reg_agencies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=256, null=True)),
            ('classification', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_reg_agencies_classification', null=True, to=orm['utility.UtilRegAgencyClassification'])),
            ('subclassification', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_reg_agencies_subclassification', null=True, to=orm['utility.UtilRegAgencySubClassification'])),
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
            ('membership_agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_reg_agencies_membership_agency', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('dot_intrastste_age', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('fema_region', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('osha_state_plan', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('hhs_region', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('approved_ce_provider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_reg_agencies_approved_ce_provider', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilRegAgencies'])

        # Adding M2M table for field regulations on 'UtilRegAgencies'
        m2m_table_name = db.shorten_name('util_reg_agencies_regulations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('utilregagencies', models.ForeignKey(orm[u'utility.utilregagencies'], null=False)),
            ('utilregagencyregulations', models.ForeignKey(orm[u'utility.utilregagencyregulations'], null=False))
        ))
        db.create_unique(m2m_table_name, ['utilregagencies_id', 'utilregagencyregulations_id'])

        # Adding M2M table for field states on 'UtilRegAgencies'
        m2m_table_name = db.shorten_name('util_reg_agencies_states')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('utilregagencies', models.ForeignKey(orm[u'utility.utilregagencies'], null=False)),
            ('utilusastates', models.ForeignKey(orm[u'utility.utilusastates'], null=False))
        ))
        db.create_unique(m2m_table_name, ['utilregagencies_id', 'utilusastates_id'])

        # Adding M2M table for field cities on 'UtilRegAgencies'
        m2m_table_name = db.shorten_name('util_reg_agencies_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('utilregagencies', models.ForeignKey(orm[u'utility.utilregagencies'], null=False)),
            ('utilzipcodes', models.ForeignKey(orm[u'utility.utilzipcodes'], null=False))
        ))
        db.create_unique(m2m_table_name, ['utilregagencies_id', 'utilzipcodes_id'])

        # Adding M2M table for field counties on 'UtilRegAgencies'
        m2m_table_name = db.shorten_name('util_reg_agencies_counties')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('utilregagencies', models.ForeignKey(orm[u'utility.utilregagencies'], null=False)),
            ('utilzipcodes', models.ForeignKey(orm[u'utility.utilzipcodes'], null=False))
        ))
        db.create_unique(m2m_table_name, ['utilregagencies_id', 'utilzipcodes_id'])

        # Adding model 'UtilRegAgencyClassification'
        db.create_table('util_reg_agency_classification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilRegAgencyClassification'])

        # Adding model 'UtilRegAgencySubClassification'
        db.create_table('util_reg_agency_sub_classification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['utility.UtilRegAgencySubClassification'], null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilRegAgencySubClassification'])

        # Adding model 'UtilRegAgencyRegulations'
        db.create_table('util_reg_agency_regulations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('reg_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('reg_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilRegAgencyRegulations'])

        # Adding model 'UtilObjectives'
        db.create_table('util_objectives', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilObjectives'])

        # Adding model 'UtilReplacementTags'
        db.create_table('util_replacement_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('default', self.gf('django.db.models.fields.TextField')(null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilReplacementTags'])

        # Adding model 'UtilStateCellPhoneLaws'
        db.create_table('util_state_cell_phone_laws', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('cell_handheld_ban', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('cell_bus_drivers', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('cell_novice_drivers', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('text_all_drivers', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('text_bus_drivers', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('text_novice_drivers', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('enforcement', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('footnote', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'utility', ['UtilStateCellPhoneLaws'])


    def backwards(self, orm):
        # Deleting model 'UtilAnonymousIps'
        db.delete_table('util_anonymous_ips')

        # Deleting model 'UtilZipCodes'
        db.delete_table('util_zip_codes')

        # Deleting model 'UtilUSAStates'
        db.delete_table('util_usa_states')

        # Deleting model 'UtilPaymentMethods'
        db.delete_table('util_payment_methods')

        # Deleting model 'UtilMonths'
        db.delete_table('util_months')

        # Deleting model 'UtilYesorNo'
        db.delete_table('util_yes_or_no')

        # Deleting model 'UtilYears'
        db.delete_table('util_years')

        # Deleting model 'UtilOrganizationType'
        db.delete_table('util_organization_type')

        # Deleting model 'UtilRenewalTerms'
        db.delete_table('util_renewal_terms')

        # Deleting model 'UtilPassingScores'
        db.delete_table('util_passing_scores')

        # Deleting model 'UtilOfficialTypes'
        db.delete_table('util_official_types')

        # Deleting model 'UtilDMEMACS'
        db.delete_table('util_dme_macs')

        # Deleting model 'UtilJobCategories'
        db.delete_table('util_job_categories')

        # Deleting model 'UtilFlsaStatus'
        db.delete_table('util_flsa_status')

        # Deleting model 'UtilRegAgencies'
        db.delete_table('util_reg_agencies')

        # Removing M2M table for field regulations on 'UtilRegAgencies'
        db.delete_table(db.shorten_name('util_reg_agencies_regulations'))

        # Removing M2M table for field states on 'UtilRegAgencies'
        db.delete_table(db.shorten_name('util_reg_agencies_states'))

        # Removing M2M table for field cities on 'UtilRegAgencies'
        db.delete_table(db.shorten_name('util_reg_agencies_cities'))

        # Removing M2M table for field counties on 'UtilRegAgencies'
        db.delete_table(db.shorten_name('util_reg_agencies_counties'))

        # Deleting model 'UtilRegAgencyClassification'
        db.delete_table('util_reg_agency_classification')

        # Deleting model 'UtilRegAgencySubClassification'
        db.delete_table('util_reg_agency_sub_classification')

        # Deleting model 'UtilRegAgencyRegulations'
        db.delete_table('util_reg_agency_regulations')

        # Deleting model 'UtilObjectives'
        db.delete_table('util_objectives')

        # Deleting model 'UtilReplacementTags'
        db.delete_table('util_replacement_tags')

        # Deleting model 'UtilStateCellPhoneLaws'
        db.delete_table('util_state_cell_phone_laws')


    models = {
        u'utility.utilanonymousips': {
            'Meta': {'object_name': 'UtilAnonymousIps', 'db_table': "'util_anonymous_ips'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
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
        u'utility.utilmonths': {
            'Meta': {'object_name': 'UtilMonths', 'db_table': "'util_months'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilobjectives': {
            'Meta': {'object_name': 'UtilObjectives', 'db_table': "'util_objectives'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
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
        u'utility.utilreplacementtags': {
            'Meta': {'object_name': 'UtilReplacementTags', 'db_table': "'util_replacement_tags'"},
            'default': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'utility.utilstatecellphonelaws': {
            'Meta': {'object_name': 'UtilStateCellPhoneLaws', 'db_table': "'util_state_cell_phone_laws'"},
            'cell_bus_drivers': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'cell_handheld_ban': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'cell_novice_drivers': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'enforcement': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'footnote': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'text_all_drivers': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'text_bus_drivers': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'text_novice_drivers': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
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
        u'utility.utilyears': {
            'Meta': {'object_name': 'UtilYears', 'db_table': "'util_years'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True'})
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

    complete_apps = ['utility']