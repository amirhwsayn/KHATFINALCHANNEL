from django.urls import path
from rest_framework import exceptions as exaa
from rest_framework import generics
from rest_framework.views import APIView

from .Permssion import *
from .serializers import *


# Create your views here.

class CreateRegisterToken(APIView):
    def get(self, request):
        if 'email' in request.headers and 'id' in request.headers:
            if not Teacher.objects.filter(Teacher_Id=request.headers['id']).exists():
                if not Teacher.objects.filter(Teacher_Email=request.headers['email']).exists():
                    mRegisterToken_Token = get_random_string(50)
                    mcode = get_random_string(6, '123456789')
                    mEmail = request.headers['email']
                    token = RegisterToken.objects.create(
                        RegisterToken_Token=mRegisterToken_Token,
                        RegisterToken_Code=mcode
                    )
                    sendcode(mEmail, mcode)
                    return Response({"token": token.RegisterToken_Token, "data": token.RegisterToken_CreateDate},
                                    status=status.HTTP_200_OK)
                else:
                    return errore_Build('کاربر دیگری قبلا با این پست الکترونیکی وارد شده')
            else:
                return errore_Build('این نام کاربری قبلا انتخاب شده')
        else:
            return errore_Build('درخواست نا معتبر')


class Register_Teacher(APIView):
    permission_classes = [Perm_Register]

    def post(self, request):
        Teacher_obj = Serializer_Teacher(data=request.data)
        if Teacher_obj.is_valid():
            if Teacher_id_uinq(Teacher_obj['Teacher_Id']):
                if not Teacher.objects.filter(Teacher_Email=Teacher_obj['Teacher_Email']).exists():
                    Teacher_obj.save()
                    data = Teacher.objects.filter(Teacher_Id=Teacher_obj['Teacher_Id'])
                    Teacherobj = Serializer_Teacher(data=data, many=True)
                    return Response(data=Teacherobj.data, status=status.HTTP_200_OK)
                else:
                    return errore_Build('کاربر دیگری قبلا با این پست الکترونیکی وارد شده')
            else:
                return errore_Build('این نام کاربری قبلا انتخاب شده')
        else:
            return errore_Build('درخواست نا معتبر')


urls = [
    # Create Register Token -> Header = email
    path('cret', CreateRegisterToken.as_view()),

    # Register Admin Via Token -> Header = Token , Code
    path('rigt', Register_Teacher.as_view()),

]
