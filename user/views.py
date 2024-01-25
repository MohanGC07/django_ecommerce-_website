



from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return redirect('login')
            login_url = reverse('login')  # Use the correct URL pattern name for the login view
            return redirect(login_url)  



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password1')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            # return redirect('home')
            home_url = reverse('index')  # Use the correct URL pattern name for the login view
            return redirect(home_url)  
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    # return redirect('login')
    login_url = reverse('login')  # Use the correct URL pattern name for the login view
    return redirect(login_url) 

def index(request):
    return render (request,'index.html')
