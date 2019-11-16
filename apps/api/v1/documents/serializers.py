from rest_framework import serializers

from apps.api.v1.utils.views import *
from apps.api.v1.utils.exceptions import *
from apps.api.v1.utils.responses import *
from apps.api.v1.utils.helpers import *

from apps.dashboard.models import *


# languages Serializer
class UtilLanguagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UtilLanguageIsoCodes
        fields = ('language', 'flag')

# resource sizes Serializer
class UtilResourceSizesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UtilResourceSizes
        fields = ('id', 'size')    

# util resource formats serializer
class UtilResourceFormatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilResourceFormats
        fields = ('file_extension', 'icon')

# core resources formats serializer
class CoreResourcesFormatsSerializer(serializers.ModelSerializer):
    
    utilresourceformats = UtilResourceFormatsSerializer(many=False) 
    
    class Meta:
        model = CoreResourcesFormats
        fields = ('utilresourcesformats')


# Resoures serializer.
class ResourcesSerializer(serializers.ModelSerializer):
    
    resourcesizes = UtilResourceSizesSerializer(many=False)
    language = UtilLanguagesSerializer(many=False)
    formats = serializers.SerializerMethodField('get_resource_formats')

    class Meta:        
        model = CoreResources
        fields = ('id', 'language', 'resourcesizes', 'resource_name', 'resource_name_language', 
                  'electronically_posted_url', 'electronically_posted_official_description', 'formats',
                  'number_of_pages', 'video_duration', 'resource_color', 'resource_last_update_date',
                  'resource_revision_date_or_version', 'resource_identifier', 'resource_short_description', 'where_was_resource_obtained')

    # get resources formats
    def get_resource_formats(self, obj):
        #formats = CoreResourcesFormats.objects.filter(coreresources_id = obj.id)
        formats = obj.formats.all()
        formats_serializer = UtilResourceFormatsSerializer(formats)                
        return formats_serializer.data