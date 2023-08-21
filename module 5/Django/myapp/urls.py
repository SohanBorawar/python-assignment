from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('otp-verification/',views.otp_verification,name='otp_verification'),
    path('new-password/',views.new_password,name='new-password'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('editprofile/',views.editprofile,name='editprofile'),
]