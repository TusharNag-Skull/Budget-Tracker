from django.urls import path

from .views import signup,login_user,home,budget_list,daily_budget_entry,delete_expense

urlpatterns = [
  
    path('', home, name="home"),
    # path('login/', views.loginPage, name="login"),
    path('signup/', signup, name="signup"),
    path('login_user/', login_user, name="login_user"),
    path('landing-entry/', budget_list, name='budget_list'),
    path('daily_budget_entry/', daily_budget_entry, name='daily_budget_entry'),                                                                     
    path('delete/<id>',delete_expense,name="delete_expense")
    
]