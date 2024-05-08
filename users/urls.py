from django.urls import path
from.import views

urlpatten = [
    path('register-applicant/',views.registre_applicant,name='register-applicant'),
    path('register-recruiter/',views.register_recruiter,name='register-recruiter'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),


]
