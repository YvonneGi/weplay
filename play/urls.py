from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
    url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
    url(r'^all/$', views.all_playgrounds, name='allplaygrounds'),
    url(r'^detail/(\d+)', views.detail, name='detail'),
    url(r'^new/team$', views.create_team, name='create_team'),
]
## this references the location to the uploaded files.
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)