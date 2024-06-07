# budget_tracker/urls.py

from django.contrib import admin
from django.urls import path,include
from budget_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homePage, name="home"),
    # path('login/', views.loginPage, name="login"),
    # path('signup/', views.signinPage, name="signup"),
    path('working/', views.workingPage, name="working"),
    path('', include('myapp.urls'))
]
# from django.urls import path
# from .views import login_view, logout_view, signup_view, homePage, workingPage

# urlpatterns = [
#     path('', homePage, name="home"),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('signup/', signup_view, name='signup'),
#     path('working/', workingPage, name="working"),
# ]
# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', include('myapp.urls')),  # Include the app's URLs
# # ]
