from apps.dashboard.models import *

def dashboard(request):
    if request.user.is_authenticated():
        #get current url
        path = request.path.split('/')[1]
        
        #get messages count
        messages = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_message=1, message_alert_cleared_id=0,
                                                                date_acknowledged_UTC=None, deactivated_date=None)
        message_count = len(messages)
        
        #get alert count
        alerts = CoreUserMessagesAlerts.objects.filter(auth_user=request.user, core_messages_alerts__is_alert=1, message_alert_cleared_id=0,
                                                                date_acknowledged_UTC=None, deactivated_date=None)
        alert_count = len(alerts)
        
        #get tasks count
        tasks = CoreTasks.objects.filter(user=request.user, date_deativated=None, task_cleared_id=0, date_completed = None)
        task_count = len(tasks)
        
        return {'path': path,
                'message_count': message_count,
                'alert_count': alert_count,
                'task_count': task_count }
    else:
        return {}
