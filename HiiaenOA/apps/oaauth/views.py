from datetime import datetime

from django.core.serializers import serialize
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentications import generate_jwt
from .serializers import LoginSerializer,UserSerializer,ResetPasswordSerializer
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        # 1.验证数据是否可用
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = datetime.now()
            user.save()
            token = generate_jwt(user)
            return Response({'token': token,'user': UserSerializer(user).data})
        else:
            detail = list(serializer.errors.values())[0][0]  
            return Response({"detail": detail}, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):  
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data,context={'request':request})
        if serializer.is_valid(): 
            newpwd = serializer.validated_data.get('newpwd')
            request.user.set_password(newpwd)
            request.user.save()
            return Response()
        else:
            print(serializer.errors)
            detail = list(serializer.errors.values())[0][0]  
            return Response({'detail': detail}, status=status.HTTP_400_BAD_REQUEST)

    