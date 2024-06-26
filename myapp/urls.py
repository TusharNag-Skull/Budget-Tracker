from django.urls import path

from .views import signup,login_user,home,budget_list,daily_budget_entry,delete_expense,edit_budget, edit_expense,add_expense,export_budget_to_excel

urlpatterns = [
  
    path('', home, name="home"),
    # path('login/', views.loginPage, name="login"),
    path('signup/', signup, name="signup"),
    path('login_user/', login_user, name="login_user"),
    path('landing-entry/', budget_list, name='budget_list'),
    path('daily_budget_entry/', daily_budget_entry, name='daily_budget_entry'),                                                                     
    path('delete/<id>',delete_expense,name="delete_expense"),
    path('edit_budget/<int:budget_id>/', edit_budget, name='edit_budget'),
    path('add_expense/<int:budget_id>/', add_expense, name='add_expense'),
    path('edit_expense/<int:expense_id>/', edit_expense, name='edit_expense'),
    path('export/', export_budget_to_excel, name='export_budget_to_excel'),
]


