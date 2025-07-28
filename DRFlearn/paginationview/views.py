from .serializers import MerchantSerializer

from rest_framework.decorators import action
from meituan.models import Merchant
from rest_framework import status, viewsets
from rest_framework.response import Response
from .paginations import MerchantPageNumberPagination



class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    pagination_class = MerchantPageNumberPagination

    @action(['GET'], detail=False,url_path='cs')
    def changsha(self,request):
        queryset = self.get_queryset()
        result = queryset.filter(name__contains='长沙')
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(result, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)