import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication,get_authorization_header
from rest_framework import exceptions
from django.contrib.auth import get_user_model
from jwt.exceptions import ExpiredSignatureError
MTUser = get_user_model()
import time
from .models import OAUser

def generate_jwt(user):
    expire_time = int(time.time() + 60*60*24*7)
    return jwt.encode({"userid":user.pk,"exp":expire_time},key=settings.SECRET_KEY)

class UserTokenAuthmentication(BaseAuthentication):
    def authenticate(self, request):
        return request._request.user,request._request.auth

class JWTAuthentication(BaseAuthentication):
    """
    Authorization: JWT 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Authorization不可用！'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Authorization不可用！应该提供一个空格！'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms="HS256")
            userid = jwt_info.get('userid')
            try:
                user = OAUser.objects.get(pk=userid)
                return (user, jwt_token)
            except Exception:
                msg = '用户不存在！'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'token格式错误！'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = 'token已过期！'
            raise exceptions.AuthenticationFailed(msg)