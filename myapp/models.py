from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DailyBudget(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f"{self.date}: {self.budget_amount}"

class Expense(models.Model):
    daily_budget = models.ForeignKey(DailyBudget, on_delete=models.CASCADE, related_name='expenses')
    detail = models.CharField(max_length=255,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True)

    def __str__(self):
        return f"{self.detail}: {self.amount}"
