from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method=="POST":
        # print("email",request.POST['email'])
        # print("pas",request.POST['password'])
        # print("cpas",request.POST['cpas'])
        name = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['cpas']

        user = User.objects.create_user(username=name,password=password)
        user.save()
        user_login = authenticate(request, username=name, password=password)
        if user_login:
            return redirect('exp')
    return render(request,'signin.html')

def exp(request):
    print(request.user)
    name = "abc"
    return render(request,'working.html',{'name':name})

def login_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user:
            login(request, user)    
            return redirect('exp')
    return render(request, 'login.html')