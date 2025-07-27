from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from .authentications import generate_jwt,JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from .permissions import MyPermission

from meituan.models import Merchant
from .serializers import MerchantSerializer

User = get_user_model()

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    # authentication_classes:用来验证用户是否已经成功登录
    authentication_classes = [JWTAuthentication]
    # permission_classes：用来根据用户的权限来限制访问
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    permission_classes = [MyPermission]


    # AUTHORIZATION
    # basic username:password
    # createsuperuser 创建超级用户

@api_view(['GET'])
def token_view(request):
    user = User.objects.first()
    if not user:
        return Response({'error': '没有用户，请先创建超级用户'}, status=400)
    token = generate_jwt(user)
    return Response({'token':token})
