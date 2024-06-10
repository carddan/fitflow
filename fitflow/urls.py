from django.contrib import admin
from django.urls import path, include
from . import views
from .views import activate_account
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from allauth.account.views import SignupView, LoginView, LogoutView


urlpatterns = [
    path('', views.app, name="app"),
    path('signup/', views.signup, name="signup"),
    path('confirmation/', views.confirmation_page, name="confirmation_page"),
    path('login/', views.login_view, name="login"),
    path('forgotp/', views.forgotp, name="forgotp"),
    path('mainpg/', views.mainpg, name="mainpg"),
    path('activate/<uidb64>/<token>/', activate_account, name="activate"),
    
]


#If in DEBUG mode, server static files using Django during development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()