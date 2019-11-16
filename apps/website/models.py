from django.db import models

from django.contrib.auth.models import User

from apps.utility.models import *


"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')

    organization = models.ForeignKey(CoreOrganizations, related_name='user_profile')

    activation_token = models.CharField(max_length=256, null=True)

    signup_stage_code = models.CharField(max_length=256, null=True)

    class Meta():
        db_table = 'user_profile'


class UserBilling(models.Model):

    user_profile = models.OneToOneField(UserProfile, related_name='user_billing')

    membership_plan = models.ForeignKey(UtilMembershipPlans, null=True)

    user_pack = models.ForeignKey(UtilUserPack, null=True)

    payment_method = models.ForeignKey(UtilPaymentMethods, null=True)

    credit_card_person_name = models.CharField(max_length=256, null=True)

    credit_card_number = models.CharField(max_length=256, null=True)

    card_expiry_month = models.CharField(max_length=256, null=True)

    card_expiry_year = models.CharField(max_length=256, null=True)

    billing_address_1 = models.CharField(max_length=256, null=True)

    billing_address_1 = models.CharField(max_length=256, null=True)

    city = models.CharField(max_length=256, null=True)

    state = models.CharField(max_length=256, null=True)

    zip_code = models.CharField(max_length=256, null=True)

    class Meta():
        db_table = 'user_billing'


class UserTransactions(models.Model):

    user_billing = models.ForeignKey(UserBilling, null=True)

    membership_plan = models.ForeignKey(UtilMembershipPlans, null=True)

    user_pack = models.ForeignKey(UtilUserPack, null=True)

    create_time = models.DateField(auto_now_add=True)

    transaction_code = models.CharField(max_length=256, null=True)

    transaction_state = models.CharField(max_length=256, null=True)

    payment_method = models.ForeignKey(UtilPaymentMethods, null=True)

    description = models.CharField(max_length=256, null=True)

    total = models.CharField(max_length=256, null=True)

    currency = models.CharField(max_length=256, null=True)

    tax = models.CharField(max_length=256, null=True)

    class Meta():
        db_table = 'user_transactions'
"""