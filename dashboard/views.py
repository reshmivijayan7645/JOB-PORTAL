from django.shortcuts import render,redirect

# Create your views here.
def dashboard(request):
    if request.user.is_applicant:
        return redirect('dashboard/dashboard.html')
    

     




