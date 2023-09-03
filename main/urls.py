from django.urls import path
from main.views import signup,login,profile,logout,pass_change,pass_change2

urlpatterns=[
    path('',signup,name='signup'),
    path('login/',login,name='login'),
    path('profile/',profile,name='profile'),
    path('logout/',logout,name='logout'),
    path('passchange/',pass_change,name='passchange'),
    path('passchange2/',pass_change2,name='passchange2'),
]