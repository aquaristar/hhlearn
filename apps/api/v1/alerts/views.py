from django.views.generic import View
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.dashboard.models import *
from serializers import *

from datetime import datetime, timedelta


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

# Class based view for alerts
class APIAlerts(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):

        try:

            # need to get logged in user.
            user_profile = request.user.core_user_profile
            alerts = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_alert=1, message_alert_cleared_id=0,
                                                            date_acknowledged_UTC=None, deactivated_date=None)            
            alerts_data = UserMessagesAlertsSerializer(alerts, context={'request':request})
            alerts = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_alert=1)\
                                            .exclude(message_alert_cleared_id=0, date_acknowledged_UTC=None, deactivated_date=None)
            readed_alerts_data = UserMessagesAlertsSerializer(alerts, context={'request':request})            

        except:
            
            alerts = None            
            alerts_data = UserMessagesAlertsSerializer(alerts)
            readed_alerts_data = UserMessagesAlertsSerializer(alerts)
            

        tzCode = get_user_timezone_code(request.user)
        
        # finalizing our output content.
        content = {
            # this node will have all organization related data
            'alerts': alerts_data.data,
            'readed_alerts': readed_alerts_data.data,
            'tzCode': tzCode
        }

        # sending final response.
        return Response(content)
    
    def post(self, request, format=None):

        alert_id = self.request.DATA.get('alert_id', None)
        acknowledged = self.request.DATA.get('acknowledged', None)        
        
        if alert_id is not None:
            try:
                alert = CoreUserMessagesAlerts.objects.get(id=int(alert_id))
                if acknowledged == 1:
                    alert.date_acknowledged_UTC = datetime.now()
                elif acknowledged == 0:
                    alert.date_acknowledged_UTC = None
                
                alert.save()
                alert_data = UserMessagesAlertsSerializer(alert, context={'request':request})
                
                response = response_profile_save_successful()
    
                # if there's any exception then just send None data.
            except:
    
                response = response_profile_save_successful()
    
                raise ExceptionUnknownError(detail=response)
            
            # finalizing our output content.
            content = {  # sending success response
                        'status': 'success',
                         'response': response,
                         'alert': alert_data.data,
            }

        else:
            content = {'status': 'fail',
                       'response': 'Alert ID should be defined!'
                       }
        
        # sending final response.
        return Response(content)
