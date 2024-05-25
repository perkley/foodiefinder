"""
URL configuration for foodiefinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from home.views import home
from login.views import log_in_user, log_out_user, sign_up

urlpatterns = [
    path('', home, name='home'),
    path('login/', log_in_user, name='log_in_user'),
    path('logout/', log_out_user, name='log_out_user'),
    path('signup/', sign_up, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),

    path('admin/', admin.site.urls),
]
