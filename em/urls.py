from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.EmployeeListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.SubTree, name='subtree'),
    url(r'^employee/create/$', views.EmployeeCreate.as_view(), name='emp_create'),
]
