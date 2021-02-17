from rest_framework import serializers
from .models import *


class Serializer_Teacher(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'Teacher_Token',
            'Teacher_Id',
            'Teacher_Password',
            'Teacher_Email',
            'Teacher_Name',
            'Teacher_Description',
            'Teacher_ProfileImage',
            'Teacher_CreatDate',
        )
        read_only_fields = ('Teacher_Token', 'Teacher_CreatDate')
