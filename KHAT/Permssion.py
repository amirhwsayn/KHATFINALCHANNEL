from django.core.mail import send_mail
from django.template import loader
from jdatetime import timedelta
from rest_framework import permissions

from KHATFINAL import settings
from .models import *


class Perm_Register(permissions.BasePermission):
    def has_permission(self, request, view):
        if 'token' in request.headers and 'code' in request.headers:
            token = request.headers['token']
            code = request.headers['code']
            try:
                RegisterToken.objects.get(RegisterToken_Token=token)
            except ObjectDoesNotExist:
                return False
            else:
                if code == RegisterToken.objects.get(RegisterToken_Token=token).RegisterToken_Code:
                    if RegisterToken.objects.get(RegisterToken_Token=token).RegisterToken_CreateDate + timedelta(
                            minutes=5) > timezone.now():
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


def sendcode(email, code):
    subject = 'تایید حساب کاربری'
    message = ''
    email_from = settings.EMAIL_HOST_USER
    html_message = loader.render_to_string(
        'EmailCodeSend/SendCode.html',
        {
            'code': code,
        }
    )
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, fail_silently=True, html_message=html_message)


def TeacherToken_Uniq():
    while True:
        Token = get_random_string(50)
        if not Teacher.objects.filter(Teacher_Token=Token).exists() or not ClassRoom.objects.filter(ClassRoom_Token = Token):
            return Token


def Teacher_id_uinq(Token):
    if Teacher.objects.filter(Teacher_Token=Token).exists():
        return False
    else:
        return True


def errore_Build(message):
    return {"detail": f"{message}"}
