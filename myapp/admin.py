from django.contrib import admin
from .models import DailyBudget,Expense
# Register your models here.
admin.site.register(DailyBudget)
admin.site.register(Expense)