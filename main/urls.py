from django.urls import path
from . import views


urlpatterns = [
path("",views.dashboard,name = 'dashboard'),
path("home/",views.dashboard,name = 'home'),
path("video/",views.video,name='video'),
path("login/",views.user_login,name='login'),
path("singup/",views.singup,name='singup'),
path("contactus/",views.contact,name='contact'),
path("logout/",views.user_logout,name = 'logout'),
path('pwd_change/',views.pwd_change,name='pwdchange')
]

