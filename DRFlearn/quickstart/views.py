from rest_framework import viewsets
from meituan.models import Merchant
from .serializers import MerchantSerializer

# 这个试图函数已经包含了增删改检索
class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
