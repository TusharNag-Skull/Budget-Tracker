from django.urls import path

from .views import signup,exp,login_user

urlpatterns = [
  
    # path('', views.homePage, name="home"),
    # path('login/', views.loginPage, name="login"),
    path('signup/', signup, name="signup"),
    path('login_user/', login_user, name="login_user"),
    path('exp/', exp, name="exp"),
    
]