from django.conf import settings
from apps.dashboard.models import *


def cdn_url(request):
	return { 'CDN_URL': settings.CDN_URL }

def dashboard(request):
    if request.user.is_authenticated():
        #get messages count
        messages = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_message=1, message_alert_cleared_id=0,
                                                                date_acknowledged_UTC=None, deactivated_date=None)
        message_count = len(messages)
        
        #get alert count
        alerts = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_alert=1, message_alert_cleared_id=0,
                                                                date_acknowledged_UTC=None, deactivated_date=None)
        alert_count = len(alerts)
        
        #get tasks count
        task_count = 2
        
        return {'message_count': message_count,
                'alert_count': alert_count,
                'task_count': task_count }
    else:
        return {}
