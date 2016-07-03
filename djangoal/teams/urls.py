from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.team_list, name='list'),
    url(r'^(?P<pk>\d+)/$', views.team_detail, name='detail'),
]
