from django.contrib import messages
from django.http import request, response
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.template import context


def Home(request):
      if request.user.is_authenticated:
            return redirect('assets:home')
      else:
            return redirect('appcore:login')


def Login(request):
      if not request.user.is_authenticated:

            if request.method == "GET":
                  return render(request, "login.html")

            elif request.method =="POST":
                  username = request.POST.get("username")
                  password = request.POST.get("password")

                  if username and password:
                        try:
                              user = authenticate(request, username=username, password=password)
                              login(request,user)
                        except:
                              return render(request, "error.html")
                        return redirect('assets:home')
                  else:
                        return render(request, 'error.html')
      else:
            return redirect('assets:home')


def Logout(request):
      logout(request)
      return redirect('appcore:home')


def Register(request):
      
      if request.method == "POST":

            form = UserRegistrationForm(request.POST)
            print("sdadas")
            if form.is_valid():

                  form.save()
                  messages.success(request,'You created your account succesfully! You can login now and enjoy!')

                  return redirect("appcore:login")
      else:
            form = UserRegistrationForm()

      context = {'form' : form}

      return render(request, 'register.html', context)
