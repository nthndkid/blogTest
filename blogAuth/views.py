from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from .forms import RegisterUser

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Inavlid Username or Password!")
            return redirect('login_user')
    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    messages.warning(request, "Successfully Logout!")
    return redirect('login_user')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Been Registered!")
            return redirect('login_user')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'auth/register.html', context)

# def register_user(request):
#     if request.method == "POST":
#         form = RegisterUser(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.password = make_password(form.cleaned_data['password1'])  # Hash the password
#             user.save()
#             messages.success(request, "You Have Been Registered!")
#             return redirect('login_user')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = RegisterUser()
#     return render(request, 'auth/register.html', {'form': form})

# def register_user(request):
#     if request.method == "POST":
#         form = RegisterUser(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Don't save yet
#             user.set_password(form.cleaned_data['password1'])  # Hash the password
#             user.save()  # Now save the user
#             messages.success(request, "You Have Been Registered!")
#             return redirect('login_user')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = RegisterUser()
#     return render(request, 'auth/register.html', {'form': form})
