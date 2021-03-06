"""planventure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings

import hello.views
import accounts.views
import Calculator.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', hello.views.about, name='about'),
    path('detail/', hello.views.detail, name='detail'),
    path('funding/', hello.views.funding, name='funding'),
    path('history/', hello.views.history, name='history'),
    path('success/', hello.views.success, name='success'),
    path('', hello.views.index, name='index'),
    path('management/', Calculator.views.management, name='management'),
    path('management_send/',Calculator.views.management_send,name="management_send"),
    path('management2/', Calculator.views.management2, name='management2'),
    path('management3/', Calculator.views.management3, name='management3'),
    path('management3_send/',Calculator.views.management3_send, name = 'management3_send'),
    #userAccounts
    path('information1/',Calculator.views.information1,name= 'information1'),

    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
]