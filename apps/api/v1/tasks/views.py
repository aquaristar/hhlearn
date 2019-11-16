from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.dashboard.models import *
from apps.api.v1.tasks.serializers import *
 
from datetime import datetime, timedelta
from django.db.models import Q

# Class based view for alerts
class APITasks(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):

        try:

            # need to get logged in user.
            user_profile = request.user.core_user_profile
            tasks = CoreTasks.objects.filter(user=request.user, date_deativated=None, task_cleared_id=0).order_by('-date_due')
            tasks_data = TaskSerializer(tasks, context={'request': request})
            
        except:
            
            tasks = None            
            tasks_data = TaskSerializer(tasks)

        tzCode = get_user_timezone_code(request.user)
        
        # finalizing our output content.
        content = {
            # this node will have all organization related data
            'tasks': tasks_data.data,            
            'tzCode': tzCode,
            'user': request.user.id
        }

        # sending final response.
        return Response(content)
    
    def post(self, request, format=None):
        
        method = self.request.DATA.get('method', None)
        task_id = self.request.DATA.get('task_id', None)
        completed = self.request.DATA.get('completed', None)        
        description = self.request.DATA.get('description', None)
        due_date = self.request.DATA.get('due_date', None)
        
        if method == 'add':
            if due_date is not None and due_date != '':
                due_datetime = datetime.strptime(due_date, '%m/%d/%Y')
                task = CoreTasks.objects.create(user=request.user,
                                            tasks_description=description,
                                            date_added=datetime.now(),
                                            date_due=due_datetime,
                                            assigned_by_user=request.user,
                                            user_ip_address=get_client_ip(request),                                            
                                            )
            else:
                due_datetime = None
                task = CoreTasks.objects.create(user=request.user,
                                            tasks_description=description,
                                            date_added=datetime.now(),
                                            user_ip_address=get_client_ip(request),                                            
                                            )  
            
            task.save()
            task_data = TaskSerializer(task, context={'request': request})
            content = {  # sending success response
                        'status': 'success',                         
                        'task': task_data.data,
            }
            
        elif method == 'change':
            if task_id is not None:
                try:
                    task = CoreTasks.objects.get(id=int(task_id))
                    if description is not None:
                        task.tasks_description = description
                    if completed is not None:
                        if completed is True:
                            task.date_completed = datetime.now()
                        elif completed is False:
                            task.date_completed = None
                    if due_date is not None:
                        task.date_due = convert_timezone_reverse(datetime.strptime(due_date, '%m/%d/%Y'), request.user)                         
                    
                    task.save()
                    task_data = TaskSerializer(task, context={'request': request})
                    response = response_profile_save_successful()
                    # if there's any exception then just send None data.
                except:
        
                    response = response_profile_save_successful()
        
                    raise ExceptionUnknownError(detail=response)
            
            # finalizing our output content.
            content = {  # sending success response
                        'status': 'success',
                         'response': response,
                         'task': task_data.data,
            }
        elif method == 'delete':
            if task_id is not None:
                try:
                    task = CoreTasks.objects.get(id=int(task_id))
                    task.date_deativated = datetime.now()
                    task.deactivateduser = request.user
                    task.save()
                except:
                    raise ExceptionUnknownError(detail=response)
                
                content = {'status': 'success',
                       'response': 'Tasks is deactivated'
                       }
                
        elif method == 'clear_all_completed':
            tasks = CoreTasks.objects.filter(user=request.user, date_deativated=None, task_cleared_id=0).exclude(date_completed=None)
            for task in tasks:
                task.task_cleared_id = 1
                task.save()
                
            content = {'status': 'success',
                       'response': 'All completed tasks is cleared'
                       }
        
            
        elif method == 'mark_all_as_done':            
            if completed is not None:                
                if completed is True:                        
                    tasks = CoreTasks.objects.filter(user=request.user, date_deativated=None, task_cleared_id=0, date_completed=None)
                    for task in tasks:
                        task.date_completed = datetime.now()
                        task.save()
                else:
                    tasks = CoreTasks.objects.filter(user=request.user, date_deativated=None, task_cleared_id=0)
                    for task in tasks:
                        task.date_completed = None
                        task.save()
                
            content = {'status': 'success',
                       'response': 'All completed marked as done!'
                       }            
        else:
            content = {'status': 'fail',
                       'response': 'Alert ID should be defined!'
                       }
        
        # sending final response.
        return Response(content)