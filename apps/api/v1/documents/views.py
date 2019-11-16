from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.dashboard.models import *

from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg

from apps.api.v1.documents.serializers import *


# Class based view for profile page.
class APIDocuments(APIView):
    # this will be executed ONLY on GET request.
    def get(self, request, format=None):
        try:
            # need to get logged in user.
            user_profile = request.user.core_user_profile
            
            #get location and organization
            location = user_profile.location.id
            if user_profile.department is not None:
                department = user_profile.department.id
            else:
                department = None
            organization_ids = CoreOrganizationsLocations.objects.filter(corelocations_id = location).values_list('coreorganizations_id', flat=True)
            
            #step1  get electronic postings
            
            # get state mandatory resource
            state = user_profile.location.state            
            resources_ids = CoreResourcesForSpecificStates.objects.filter(state_id = state).values_list('resources_id', flat=True)
            
            state_resources = CoreResources.objects.filter(can_be_electronically_posted=1, id__in=resources_ids)            
            federal_resources = CoreResources.objects.filter(can_be_electronically_posted=1, is_federal_mandatory_posting=1, is_active=1)            
            
            resources = state_resources | federal_resources            
            resources_serializer = ResourcesSerializer(resources)
            
            #step2 get frequents            
            
            location_ids = CoreResourcesForLocations.objects.filter(locations_id = location).values_list('resources_id', flat=True)
            location_frequent_ids = CoreResourcesVisited.objects.values('coreresources_id').annotate(rcount=Count('coreresources')).filter(coreresources_id__in=location_ids, user_id=request.user.id).order_by('-rcount')[:10]
            if len(location_frequent_ids) == 0:
                location_frequents = CoreResources.objects.filter(id=-1)
            else:                                
                location_frequents = CoreResources.objects.filter(id__in=location_frequent_ids)
            frequents = location_frequents
            frequent_ids = frequents.values_list('id', flat=True)
            remain_count = 10 - len(frequents)
                        
            if len(frequents) < 10:                
                organization_resource_ids = CoreResources.objects.filter(coreorganizations_id__in=organization_ids).values_list('id', flat=True)
                if len(organization_resource_ids) > 0: 
                    organization_frequent_ids = CoreResourcesVisited.objects.values('coreresources_id').annotate(rcount=Count('coreresources')).filter(coreresources_id__in=organization_resource_ids, user_id=request.user.id).order_by('-rcount')
                    organization_frequent_ids = [x.get('coreresources_id') for x in organization_frequent_ids]
                    if len(organization_frequent_ids) > 0: 
                        organization_frequents = CoreResources.objects.filter(id__in=organization_frequent_ids)
                        frequents = (frequents | organization_frequents)[:10]
                        frequent_ids = frequents.values_list('id', flat=True)
                remain_count = 10 - len(frequents)                       
            
            if department and len(frequents) < 10:
                department_ids = CoreResourcesForDepartments.objects.filter(departments_id = department).values_list('resources_id', flat=True)
                if len(department_ids) > 0:
                    department_frequent_ids = CoreResourcesVisited.objects.values('coreresources_id').annotate(rcount=Count('coreresources')).filter(coreresources_id__in=department_ids, user_id=request.user.id).order_by('-rcount')
                    department_frequent_ids = [x.get('coreresources_id') for x in department_frequent_ids]
                    if len(department_frequent_ids) > 0:
                        department_frequents = CoreResources.objects.filter(id__in=department_frequent_ids)
                        frequents = (frequents | department_frequents)[:10]
                        frequent_ids = frequents.values_list('id', flat=True)
                remain_count = 10 - len(frequents)
            
            if len(frequents) < 10:
                t_frequent_ids = CoreResourcesVisited.objects.values('coreresources_id').annotate(rcount=Count('coreresources')).filter(user_id=request.user.id).order_by('-rcount')
                t_frequent_ids = [x.get('coreresources_id') for x in t_frequent_ids]
                if len(t_frequent_ids) > 0:
                    t_frequents = CoreResources.objects.filter(id__in=t_frequent_ids)
                    frequents = (frequents | t_frequents)[:10]
            
            frequents_serializer = ResourcesSerializer(frequents)
            frequents_data = frequents_serializer.data
                        
            
            #step3 get custom forms
            
            modules = CoreUserProfilesModules.objects.filter(coremodules_id=5, coreuserprofiles=user_profile.id)            
            if len(modules) > 0:
                forms = CoreResources.objects.filter(is_form=1, coreorganizations_id__in=organization_ids)
                forms_serializer = ResourcesSerializer(forms)
                forms_data = forms_serializer.data
            else:
                forms_data = 0
            
                
            #step4 get videos
            
            modules = CoreUserProfilesModules.objects.filter(coremodules_id=9, coreuserprofiles=user_profile.id)
            if len(modules) > 0:
                videos = CoreResources.objects.filter(is_video=1, coreorganizations_id__in=organization_ids)
                videos_serializer = ResourcesSerializer(videos)
                videos_data = videos_serializer.data
            else:
                videos_data = 0
            
            #step5 get publications
            
            modules = CoreUserProfilesModules.objects.filter(coremodules_id=7, coreuserprofiles=user_profile.id)
            
            if len(modules) > 0:
                publications = CoreResources.objects.filter(is_publication=1, coreorganizations_id__in=organization_ids)
                publications_serializer = ResourcesSerializer(publications)
                publications_data = publications_serializer.data
            else:
                publications_data = 0;
                        
            
            # finalizing our output content.
            content = {
                'status': 'success',
                'data': {
                    'e_postings': resources_serializer.data,
                    'frequents': frequents_data,
                    'videos': videos_data,
                    'forms': forms_data,
                    'publications': publications_data
                }
            }

        except Exception as e:
           
            # finalizing our output content.
            content = {
                'status': 'fail',
                'data': e                    
            }

        # sending final response.
        return Response(content)
