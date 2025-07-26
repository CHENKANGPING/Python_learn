from .seroalizers import MerchantSerializer, GoodsCategorySerializer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from meituan.models import Merchant, GoodsCategory,Goods
from rest_framework.response import Response
from rest_framework.decorators import api_view

# @require_http_methods(["GET", "POST"])
@api_view(['GET','POST'])
def merchant(request):
    # get:返回所有商家
    # post：创建新的商家
    if request.method == 'GET':
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)

    else:
        serializer = MerchantSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)


def category(request):
    if request.method == 'GET':
        queryset = GoodsCategory.objects.all()
        serializer = GoodsCategorySerializer(instance=queryset, many=True)
        return JsonResponse(serializer.data, status=200,safe=False)
    else:
        serializer = GoodsCategorySerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)