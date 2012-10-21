from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rock.views.index_view', name='index'),
    url(r'^login$', 'rock.views.login_view', name='login'),
    url(r'^logout$', 'rock.views.logout_view', name='logout'),
    url(r'^signup$', 'rock.views.signup_view', name='signup'),
    url(r'^contact$', 'rock.views.contact_view', name='contact'),
    url(r'^search$', 'rock.views.search_view', name='search'),
    url(r'^activities$', 'rock.views.activities_view', name='activities'),
    url(r'^activity/(\w+)$', 'rock.views.activity_view', name='activity'),
    url(r'^join/(\w+)$', 'rock.views.join_view', name='join'),
    url(r'^leave/(\w+)$', 'rock.views.leave_view', name='leave'),
    url(r'^calendar$', 'rock.views.calendar_view', name='calendar'),
    # url(r'^rock/', include('rock.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
