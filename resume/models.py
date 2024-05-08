from django.db import models
from users.models import User


# Create your models here.
class Resume(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)

    #inser cv
def __str__(self):
    return f'{self.firstname}{self.surname}'


    