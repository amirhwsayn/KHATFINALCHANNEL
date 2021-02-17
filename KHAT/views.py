from django.urls import path
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions as exaa
from .Permssion import *
from .serializers import *
from django.utils.crypto import get_random_string


# Create your views here.

class CreateRegisterToken(APIView):
    def get(self, request):
        if 'email' in request.headers:
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
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Register_Teacher(generics.CreateAPIView):
    permission_classes = (Perm_Register,)
    serializer_class = Serializer_Teacher

    def handle_exception(self, exc):
        if isinstance(exc, exaa.NotAuthenticated):
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        if isinstance(exc, exaa.ValidationError):
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TEST(generics.ListAPIView):
    queryset = Teacher.objects.filter(Teacher_Id='amir')
    serializer_class = Serializer_Teacher


urls = [
    # Create Register Token -> Header = email
    path('cret', CreateRegisterToken.as_view()),

    # Register Admin Via Token -> Header = Token , Code
    path('rigt', Register_Teacher.as_view()),

    path('a', TEST.as_view())
]
