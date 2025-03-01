from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    # Check tp see if logging in
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate
        user = authenticate(request,username= username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In")
            return redirect('home')
        else:
            messages.success(request, "There was an error Logging In,Please try again..")
            return redirect('home')
    else:
        return render(request,'home.html' ,{})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully Registered")
            return redirect('home')
    else:    
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})