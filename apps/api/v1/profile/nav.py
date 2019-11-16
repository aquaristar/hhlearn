from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import serializers
from apps.api.v1.utils.exceptions import *

from apps.api.v1.utils.responses import *
from apps.dashboard.models import *


# Class based view for profile page.
class APIToggelMenu(APIView):
    # this will be executed ONLY on POST request.
    def get(self, request, format=None):

        if 'menu_type' not in request.session:

            request.session['menu_type'] = 'nav-min'

        else:

            if not request.session['menu_type']:
                request.session['menu_type'] = 'nav-min'
            else:
                request.session['menu_type'] = ''

        # finalizing our output content.
        content = {  # sending success response
                     'response': request.session['menu_type']

        }

        # sending final response.
        return Response(content)
