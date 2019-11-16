from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.website.home.views',
                       #url(r'^dashboard/$', 'home', name='home'),
                       url(r'^$', 'home', name='home'),
                       url(r'^home/$', 'old_home', name='old_home'),
                       url(r'^contacts/$', 'contacts', name='contacts'),
                       url(r'^contact_us/$', 'contact_us', name='contact_us'),
                       url(r'^contact_newsletter/$', 'contact_newsletter', name='contact_newsletter'),
                       )