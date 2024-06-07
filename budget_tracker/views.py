from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login

def homePage(request):
    return render(request, "index.html")

def loginPage(request):
    return render(request, "login.html")

def signinPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signin.html', {'form': form})

def workingPage(request):
    return render(request, "working.html")


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# import json

# def homePage(request):
#     return render(request, "index.html")

# def login_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         username = data.get('username')
#         password = data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'message': 'Login successful'})
#         else:
#             return JsonResponse({'message': 'Invalid credentials'}, status=400)
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('home')

# def signup_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         username = data.get('username')
#         password = data.get('password')
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({'message': 'Username already taken'}, status=400)
#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#         login(request, user)
#         return JsonResponse({'message': 'Signup successful'})
#     return render(request, 'signin.html')

# def workingPage(request):
#     return render(request, "working.html")
