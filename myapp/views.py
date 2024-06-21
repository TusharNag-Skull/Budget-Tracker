from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import DailyBudget, Expense
from django.shortcuts import render, redirect
from .models import DailyBudget, Expense
from django.utils import timezone
from django.db.models import Sum




# Create your views here.
def signup(request):
    if request.method=="POST":
        print(request.POST)
        # print("email",request.POST['email'])
        # print("pas",request.POST['password'])
        # print("cpas",request.POST['cpas'])
        name = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['cpas']

        user = User.objects.create_user(username=name,password=password)
        user.save()

        user_login = authenticate(request, username=name, password=password)
        print("ckecijg",user_login)
        if user_login:
            login(request, user_login)
            return redirect('daily_budget_entry')
    return render(request,'signin.html')



def login_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user:
            login(request, user)    
            return redirect('daily_budget_entry')
        else:
            print("wrong mess")
    return render(request, 'login.html')

def home(request):
    # print(request.user)
    name = "abc"
    return render(request,'index.html',{'name':name})

def budget_list(request):
    print("login",request.user)
    budgets = DailyBudget.objects.filter(user=request.user).prefetch_related('expenses')

    # Calculate total expenses for each budget
    for budget in budgets:
        total_expenses = budget.expenses.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        budget.total_expenses = total_expenses  # Add total_expenses attribute to each budget object

    return render(request, 'landing.html', {'budgets': budgets})

def daily_budget_entry(request):
    print(request.user)
    try:
        today = timezone.now().date()
        daily_budget = DailyBudget.objects.get(user=request.user, date=today)
        print(daily_budget)
        initial_data = {'date': daily_budget.date, 'budget_amount': daily_budget.budget_amount}
    except DailyBudget.DoesNotExist:
        initial_data = {}


    if request.method == 'POST':
        date = request.POST['date']
        budget_amount = request.POST['budget_amount']
        try:
            daily_budget = DailyBudget.objects.get(user=request.user, date=date)
            daily_budget.budget_amount = budget_amount
            daily_budget.save()
        except DailyBudget.DoesNotExist:
            daily_budget = DailyBudget.objects.create(user=request.user, date=date, budget_amount=budget_amount)
     
        detail = request.POST.getlist('expense_detail')
        amount = request.POST.getlist('expense_amount')
        if detail and amount:
            for i in range(len(detail)):
                expense = Expense(daily_budget=daily_budget, detail=detail[i], amount=amount[i])
                expense.save()

        return redirect('budget_list')  # Redirect to budget list after submission
    else:
        return render(request, 'working.html', {'budget': initial_data})

def delete_expense(request,id):
    print(id)
    expense=Expense.objects.get(id=id)
    expense.delete()
    return redirect('budget_list')
