from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'auth' 

urlpatterns = [
    path('', views.login_view, name = 'login'),
    path('logout/',views.logout_view,name = 'logout' ),
    path('signup/',views.user_signup,name = 'signup'),
    path('register/',views.user_register,name = 'register'),
    path('approval/',views.user_approval,name = 'approval'),
    path('approvalupdate/',views.user_approval_update,name = 'approvalupdate'),
]
