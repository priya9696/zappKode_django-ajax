from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from zappApp.form import UserRegistrationForm, UserLoginForm
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,template_name='zappApp/login.html')

def signup(request):
    form = UserRegistrationForm()  #object of Urf
    data = {
        'form':form, 
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if(password != confirm_password):
            messages.add_message(request, Message.info , 'Invalid Password')
        else:
            user = User.objects.create_user(username= username, password= password, email= email,first_name = name)
            if(user.is_active):
                print('Register')
            else:
                print("error")
    return render(request,template_name='zappApp/signup.html', context = data)

def Userlogin(request):
    form = UserLoginForm()
    data = {
        'form': form, 
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            print(user)
            return redirect('Home')
        else:
            return redirect('Login')
        
        print(username, password)
    return render(request, template_name='zappApp/login.html', context = data)
  

