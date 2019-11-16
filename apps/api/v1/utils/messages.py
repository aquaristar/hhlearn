from apps.dashboard.models import *
from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *
from datetime import datetime



def add_user_signup_message(request, user):
	'''
	1. All users when added get core_messages_alerts= 1
	2. If the user is added as an Administrator, they also get core_messages_alerts= 2
	3. If the user is added as a Manager, they also get core_messages_alerts=3
	4. If they are a Location Manager, core_messages_alerts= 4
	5. If they are a Department Manager, core_messages_alerts= 5
	6. If they are a Regional Manager, core_messages_alerts= 6
	7. All users on initial load get core_messages_alerts= 11 & 12
	'''    
		
	message = CoreUserMessagesAlerts.objects.create(core_messages_alerts_id=1,
													 auth_user=user,
													 date_assigned_UTC=datetime.now(),
													 user_ip_address=get_client_ip(request))
	message.save()
	user_group = User.groups.through.objects.get(user=user)	
	if user_group.id == 2:
		message = CoreUserMessagesAlerts.objects.create(core_messages_alerts_id=2,
													 auth_user=user,
													 date_assigned_UTC=datetime.now(),
													 user_ip_address=get_client_ip(request))
		message.save()
	if user_group.id == 3:
		message = CoreUserMessagesAlerts.objects.create(core_messages_alerts_id=3,
													 auth_user=user,
													 date_assigned_UTC=datetime.now(),
													 user_ip_address=get_client_ip(request))
		message.save()
	
	return True

def add_user_initial_message(request, user):	
	message = CoreUserMessagesAlerts.objects.create(core_messages_alerts_id=11,
													 auth_user=user,
													 date_assigned_UTC=datetime.now(),
													 user_ip_address=get_client_ip(request))
	message.save()
	message = CoreUserMessagesAlerts.objects.create(core_messages_alerts_id=12,
													 auth_user=user,
													 date_assigned_UTC=datetime.now(),
													 user_ip_address=get_client_ip(request))
	message.save()
	return True

def add_user_signup_milestones(request, user):
	
	#1. All users when added get core_milestones= 2
	milestone = CoreUsersMilestonesEarned.objects.create(user=user,
														milestones_id=2,
														date_earned=datetime.now(),
														awarded_by_user=request.user)
	milestone.save()
	
	#2. All users when login for the first time get core_milestones=3
	milestone = CoreUsersMilestonesEarned.objects.create(user=user,
														milestones_id=3,
														date_earned=datetime.now(),
														awarded_by_user=request.user)
	milestone.save()	
	return True

def add_user_course_completion_milestones(request, user):

	#get completed courses count
    completed_assignments = CoreUserAssignments.objects.filter(user_profile=user_profile, is_active=True, is_completed=True)            
    completed_safety_assignments = CoreUserSafetyAssignments.objects.filter(user_profile=user_profile, is_active=True, is_completed=True)    
    completed_course_count = len(completed_assignments) + len(completed_safety_assignments)
    
    '''
	3. All users when they complete their first course get core_milestones= 1
	4. All users when they complete their 10th course get core_milestones= 10
	5. All users when they complete their 20th course get core_milestones= 20
	6. All users when they complete their 30th course get core_milestones= 30
	7. All users when they complete their 40th course get core_milestones= 40
	8. All users when they complete their 50th course get core_milestones= 50
	9. All users when they complete their 60th course get core_milestones= 60
	10. All users when they complete their 70th course get core_milestones= 70
	11. All users when they complete their 80th course get core_milestones= 80
	12. All users when they complete their 90th course get core_milestones= 90
	13. All users when they complete their 100th course get core_milestones= 100
	'''    
    if ( completed_course_count == 1 or completed_course_count % 10 == 0 ) and completed_course_count <= 100:    	
		milestone = CoreUsersMilestonesEarned.objects.create(user=user,
														milestones_id=3,
														date_earned=datetime.now(),
														awarded_by_user=request.user)
		milestone.save()    
    return True
	
	
	