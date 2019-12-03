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
    url(r'^new/team/(\d+)', views.create_team, name='create_team'),
    url(r'^chat/(\d+)', views.chat, name='chat'),
    #  url(r'^all/$', views.all_events, name='allevents'),
    # url(r'^comment/(\d+)', views.comment, name='comment'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/blog/(\d+)', views.new_blog, name='new_blog'),
    url(r'^ajax/message/$', views.message, name='message'),
    url(r'^location/(\w+)', views.page_location,name='page_location'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)