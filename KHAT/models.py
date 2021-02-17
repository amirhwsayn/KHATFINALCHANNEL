from django.db.models import *
from django.utils import timezone
from django.utils.crypto import get_random_string
from django_jalali.db import models as jmodels


# Create your models here.


class ClassRoom(Model):
    ClassRoom_Token = CharField(max_length=100, default=get_random_string(length=50), unique=True, primary_key=True)
    ClassRoom_Name = CharField(max_length=200)
    ClassRoom_Description = TextField(max_length=300)
    ClassRoom_ProfileImage = ImageField(upload_to='Images')


class Teacher(Model):
    Teacher_Token = CharField(max_length=100, default=get_random_string(length=50))
    Teacher_Id = CharField(max_length=50, unique=True, primary_key=True)
    Teacher_Password = CharField(max_length=100)
    Teacher_Email = EmailField()
    Teacher_Name = CharField(max_length=100, default=f'user{get_random_string(10)}')
    Teacher_Description = TextField(max_length=300, blank=True)
    Teacher_ProfileImage = ImageField(upload_to='Images', blank=True)
    Teacher_CreatDate = jmodels.jDateField(auto_now=True)


class RegisterToken(Model):
    RegisterToken_Token = CharField(max_length=50, default=get_random_string(50))
    RegisterToken_Code = CharField(max_length=50, default=get_random_string(6))
    RegisterToken_CreateDate = DateTimeField(auto_now=True)
