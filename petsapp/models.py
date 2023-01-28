from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    name = models.CharField(max_length=20,null=True)
    age=models.IntegerField(null=True)
    contact_no=models.CharField(max_length=13,null=True)
    address=models.TextField(null=True)
    qualification=models.CharField(max_length=100,null=True)
