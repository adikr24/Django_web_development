"""webdev URL Configuration

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
from django.urls import path
from django.conf.urls import url 
from audio.views import *
from audio import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.homepage),
    url(r'^intro/', views.temp_l),
    url(r'^search/$', views.disp_results),
    url(r'^store/$', views.store_results),
   
   # url(r'^disp_speech/$', views.sample_voice),
   ## to get a syndrome from a user and put it in the database
   url(r'^form/$', views.form_res),
   url(r'^show_more/$',views.get_form_res),
   url(r'^store_syndrome/$',views.store_data),
### rec speech urls
   url(r'^speak/$', views.sample_voice),
   url(r'^show_speech/$', views.display_speech),
   url(r'^speech_save/$', views.save_speech),
   url(r'^doctor_dash/$', views.doctors_view),
   url(r'^show_pat_data/$',views.pat_data),


]
