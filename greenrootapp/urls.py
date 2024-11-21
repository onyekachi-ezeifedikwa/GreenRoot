from django.urls import path
from greenrootapp import views



urlpatterns=[
    path("home",views.home,name="home"),
    path("signup",views.register,name="register"),
    path("login",views.Login,name="Login"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("post",views.posts,name="posts"),
    path("<int:pk>",views.problem,name="problem"),
     path("logout",views.Logout,name="Logout"),
    
    ]