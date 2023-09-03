from django.urls import path
from main.views import signup,login,profile,logout,pass_change,pass_change2,cookie_demo,get_cookie,set_session,get_session

urlpatterns=[
    path('',signup,name='signup'),
    path('login/',login,name='login'),
    path('profile/',profile,name='profile'),
    path('logout/',logout,name='logout'),
    path('passchange/',pass_change,name='passchange'),
    path('passchange2/',pass_change2,name='passchange2'),
    # path('cookiew/',cookie_demo,name='cookiew'),
    # path('cookiew/',get_cookie,name='cookiew'),
    # path('cookiew/',set_session,name='cookiew'),
    path('cookiew/',get_session,name='cookiew'),
]