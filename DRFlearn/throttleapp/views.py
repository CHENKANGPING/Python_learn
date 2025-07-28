from rest_framework import viewsets
from meituan.models import  Merchant
from .serializers import MerchantSerializer

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    throttle_scope = 'merchant'