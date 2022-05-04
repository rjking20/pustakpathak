from django.urls import path
from . import views

urlpatterns = [
    path('hi',views.hindhome,name='Home'),
    path('en',views.enghome,name='Home'),
    path('signin',views.signin,name='Signin'),
    path('signup',views.signup,name='Signup'),
    path('register',views.register,name='Register'),
    path('login',views.login,name='Login'),
    path('logout',views.logout,name='Logout'),
    path('error',views.error,name='Error')
]