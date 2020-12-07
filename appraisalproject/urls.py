"""appraisalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include
from django.contrib.auth import views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('appraisalapp.urls')),
    url('^accounts/register/',
        RegistrationView.as_view(success_url='/accounts/login'),
        name='django_registration_register'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^logout/$',views.LogoutView.as_view(), {'next_page': 'settings.LOGOUT_REDIRECT_URL'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
