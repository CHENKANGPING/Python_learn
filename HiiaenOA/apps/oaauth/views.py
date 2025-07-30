from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .authentications import generate_jwt
from .serializers import LoginSerializer,UserSerializer


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
            detial = list(serializer.errors.values())[0][0]
            return Response({"detail": detial}, status=status.HTTP_400_BAD_REQUEST)
