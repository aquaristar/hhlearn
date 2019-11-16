from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.admin.users.views',
                       
                       url(r'^admin/users/$', 'home', name='admin_users'),
                       url(r'^admin/users/add/$', 'add', name='admin_users_add'),                       
                       url(r'^admin/users/add_initial/$', 'add_initial', name='admin_users_add_initial'),
                       url(r'^admin/users/edit/(?P<user_id>.+)?$', 'edit', name='admin_users_edit'),                       
                       )
