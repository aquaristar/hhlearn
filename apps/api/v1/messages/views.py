from django.views.generic import View
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.dashboard.models import *
from apps.api.v1.messages.serializers import *

from datetime import datetime, timedelta

# Class based view for messages
class APIMessages(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):
        try:
            # need to get logged in user.
            user_profile = request.user.core_user_profile
            messages = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_message=1, message_alert_cleared_id=0,
                                                            date_acknowledged_UTC=None, deactivated_date=None)            
            messages_data = UserMessagesAlertsSerializer(messages, context={'request':request})
            
            messages = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_message=1)\
                                            .exclude(message_alert_cleared_id=0, date_acknowledged_UTC=None, deactivated_date=None)
            readed_messages_data = UserMessagesAlertsSerializer(messages, context={'request':request})
        except:
            messages = None            
            messages_data = UserMessagesAlertsSerializer(messages)
            readed_messages_data = UserMessagesAlertsSerializer(messages)

        tzCode = get_user_timezone_code(request.user)
        # finalizing our output content.
        content = {
            # this node will have all organization related data
            'messages': messages_data.data,
            'readed_messages': readed_messages_data.data,
            'tzCode': tzCode
        }

        # sending final response.
        return Response(content)
    
    def post(self, request, format=None):

        message_id = self.request.DATA.get('message_id', None)
        acknowledged = self.request.DATA.get('acknowledged', None)        
        
        if message_id is not None:
            try:
                message = CoreUserMessagesAlerts.objects.get(id=int(message_id))
                if acknowledged == 1:
                    message.date_acknowledged_UTC = datetime.now()
                elif acknowledged == 0:
                    message.date_acknowledged_UTC = None
                
                message.save()
                message_data = UserMessagesAlertsSerializer(message, context={'request':request})
                
                response = response_profile_save_successful()
    
                # if there's any exception then just send None data.
            except:
    
                response = response_profile_save_successful()
    
                raise ExceptionUnknownError(detail=response)
            
            # finalizing our output content.
            content = {  # sending success response
                        'status': 'success',
                         'response': response,
                         'message': message_data.data,
            }

        else:
            content = {'status': 'fail',
                       'response': 'Message ID should be defined!'
                       }
        
        # sending final response.
        return Response(content)
