from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.app, name="app"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('mainpg/', views.mainpg, name="mainpg"),
    path('forgotp', views.forgotp, name="forgotp"),
]

#If in DEBUG mode, server static files using Django during development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()