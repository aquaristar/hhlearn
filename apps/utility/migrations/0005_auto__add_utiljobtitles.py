# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UtilJobTitles'
        db.create_table('util_job_titles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('short_code', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('name_possessive', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_category', null=True, to=orm['utility.UtilJobCategories'])),
            ('patient_file_access', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_patient_file_access', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('exposure_to_chemicals', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_exposure_to_chemicals', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('exposure_to_BBP', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_exposure_to_BBP', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('exposure_to_TB', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_exposure_to_TB', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('requires_license', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_requires_license', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('cpr', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_cpr', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('on_call', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_on_call', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('all_occupational_exposure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_all_occupational_exposure', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('some_occupational_exposure', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_some_occupational_exposure', to_field='value', null=True, to=orm['utility.UtilYesorNo'])),
            ('flsa_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='util_job_title_flsa_status', null=True, to=orm['utility.UtilFlsaStatus'])),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'utility', ['UtilJobTitles'])


    def backwards(self, orm):
        # Deleting model 'UtilJobTitles'
        db.delete_table('util_job_titles')


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
        u'utility.utiljobtitles': {
            'Meta': {'object_name': 'UtilJobTitles', 'db_table': "'util_job_titles'"},
            'all_occupational_exposure': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_all_occupational_exposure'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_category'", 'null': 'True', 'to': u"orm['utility.UtilJobCategories']"}),
            'cpr': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_cpr'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'exposure_to_BBP': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_exposure_to_BBP'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'exposure_to_TB': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_exposure_to_TB'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'exposure_to_chemicals': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_exposure_to_chemicals'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'flsa_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_flsa_status'", 'null': 'True', 'to': u"orm['utility.UtilFlsaStatus']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'name_possessive': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'on_call': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_on_call'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'patient_file_access': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_patient_file_access'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'requires_license': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_requires_license'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"}),
            'short_code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'some_occupational_exposure': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'util_job_title_some_occupational_exposure'", 'to_field': "'value'", 'null': 'True', 'to': u"orm['utility.UtilYesorNo']"})
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