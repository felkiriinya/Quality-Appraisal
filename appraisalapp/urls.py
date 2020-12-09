from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.landing, name='landing'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^companylist/$', views.companylist, name='companylist'),
    url(r'^createcompany/$', views.createcompany, name='createcompany'),
    url(r'^companydetails/(\d+)$', views.companydetails, name='companydetails'),
    url(r'^reviewhome/$', views.reviewhome, name='reviewhome'),
    url(r'^addreview/(\d+)$', views.addreview, name='addreview'),
    url(r'^reviewdetails/(\d+)$', views.reviewdetails, name='reviewdetails'),

]   