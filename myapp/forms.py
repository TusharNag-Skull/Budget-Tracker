# forms.py
from django import forms
from .models import DailyBudget

class DailyBudgetForm(forms.ModelForm):
    class Meta:
        model = DailyBudget
        fields = ['date', 'budget_amount']
