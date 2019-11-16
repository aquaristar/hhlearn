from tastypie.resources import ModelResource

from apps.utility.models import UtilUSAStates

from tastypie.authentication import SessionAuthentication


class MyModelResource(ModelResource):

	def determine_format(self, request):
		return 'application/json'

	class Meta:
		queryset = UtilUSAStates.objects.all()
		allowed_methods = ['get']
		authentication = SessionAuthentication()