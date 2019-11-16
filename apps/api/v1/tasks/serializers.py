from rest_framework import serializers

from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.views import *
from apps.api.v1.utils.helpers import *

from apps.dashboard.models import *

class TaskSerializer(serializers.ModelSerializer):
    
    date_added = serializers.SerializerMethodField('get_added_date')
    date_due = serializers.SerializerMethodField('get_due_date')
    date_completed = serializers.SerializerMethodField('get_completed_date') 
    date_deativated = serializers.SerializerMethodField('get_deactivated_date')
    assigned_user_name = serializers.SerializerMethodField('get_assigned_by_user_name')    
    completed = serializers.SerializerMethodField('is_completed')
    overdue = serializers.SerializerMethodField('is_overdue')
    
    class Meta:        
        model = CoreTasks
    
    def get_added_date(self, obj):
        return convert_timezone(obj.date_added, self.context['request'].user)
    
    def get_due_date(self, obj):
        if obj.date_due is not None and obj.date_due is not '':
            return convert_timezone(obj.date_due, self.context['request'].user)
        else:
            return None
    
    def get_completed_date(self, obj):
        if obj.date_completed is not None and obj.date_completed is not '':
            return convert_timezone(obj.date_completed, self.context['request'].user)
        else:
            return None
    
    def get_deactivated_date(self, obj):
        if obj.date_deativated is not None and obj.date_deativated is not '':
            return convert_timezone(obj.date_deativated, self.context['request'].user)
        else:
            return None
    
    def get_assigned_by_user_name(self, obj):
        user = obj.assigned_by_user
        if user is not None:
            username = user.first_name + ' ' + user.last_name
        else:
            username = ''
        return username
    
    def is_completed(self, obj):
        if obj.date_completed is not None and obj.date_completed is not '':
            return True
        else:
            return False
    
    def is_overdue(self, obj):
        cur_date = datetime.now()
        if obj.date_due is not None and cur_date > obj.date_due.replace(tzinfo=None):
            return True
        else:
            return False