from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User

from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company
 

# Create your views here.
def registre_applicant(request):
    if request.method =='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request,'Your account has been created.')
            return redirect('login')
        else:
            messages.info(request,'Something went wrong.')
            return redirect('register-applicant')
    else:
        form=RegisterUserForm()
        context={'form':form}
        return redirect(request,'user/register-applicant.html',context)
    
#register  recruter only

def register_recruiter(request):
    if request.method =='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request,'Your account has been created.')
            return redirect('login')
        else:
            messages.info(request,'Something went wrong.')
            return redirect('register-recruiter')
    else:
        form=RegisterUserForm()
        context={'form':form}
        return redirect(request,'user/register-recruiter.html',context)
    
#login user

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        
        user=authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,'something went wrong')
            return redirect('login')
    else:
        return render(request,'users/login.html')
    
#logout user
def logout_user(request):
    logout(request)
    messages.info(request,"your session has ended")
    return redirect("login")

    



        


        


