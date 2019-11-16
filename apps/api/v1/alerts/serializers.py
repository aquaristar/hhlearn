from rest_framework import serializers

from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.views import *
from apps.api.v1.utils.helpers import *

from apps.dashboard.models import *

class PrioritiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilPriorities

class MessagesAlertsSerializer(serializers.ModelSerializer):
    util_priorities = PrioritiesSerializer(many=False)
    date_created_UTC = serializers.SerializerMethodField('get_created_date')  
    date_auto_start_UTC = serializers.SerializerMethodField('get_auto_start_date') 
    date_auto_stop_UTC  = serializers.SerializerMethodField('get_auto_stop_date') 
    date_deactivated_UTC = serializers.SerializerMethodField('get_deactivated_date')
    message_alert_content =  serializers.SerializerMethodField('get_alert_content')
    
    class Meta:        
        model = CoreMessagesAlerts
    
    def get_alert_content(self, obj):
        return replace_tags(self.context['request'], obj.message_alert_content)
    
    def get_created_date(self, obj):
        return convert_timezone(obj.date_created_UTC, self.context['request'].user)
    
    def get_auto_start_date(self, obj):
        return convert_timezone(obj.date_auto_start_UTC, self.context['request'].user)
    
    def get_auto_stop_date(self, obj):
        return convert_timezone(obj.date_auto_stop_UTC, self.context['request'].user)
    
    def get_deactivated_date(self, obj):
        return convert_timezone(obj.date_deactivated_UTC, self.context['request'].user)

class UserMessagesAlertsSerializer(serializers.ModelSerializer):
    core_messages_alerts = MessagesAlertsSerializer(many=False)
    date_assigned_UTC = serializers.SerializerMethodField('get_assigned_date') 
    date_acknowledged_UTC = serializers.SerializerMethodField('get_acknowledged_date')
    
    class Meta:
        model = CoreUserMessagesAlerts
    
    def get_assigned_date(self, obj):
        return convert_timezone(obj.date_assigned_UTC, self.context['request'].user)
    
    def get_acknowledged_date(self, obj):
        return convert_timezone(obj.date_acknowledged_UTC, self.context['request'].user)
