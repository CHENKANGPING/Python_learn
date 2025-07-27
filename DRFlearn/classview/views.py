from rest_framework import status, viewsets
from rest_framework.views import APIView
from meituan.models import Merchant
from django.http import Http404
from .serializers import MerchantSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action

############################APIView的代码############################
# class MerchantView(APIView):
#     """
#     检索, 更新和删除一个merchant实例对象.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Merchant.objects.get(pk=pk)
#         except Merchant.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk=None):
#         if pk:
#             merchant = self.get_object(pk)
#             serializer = MerchantSerializer(merchant)
#             return Response(serializer.data)
#         else:
#             queryset = Merchant.objects.all()
#             serializer = MerchantSerializer(instance=queryset, many=True)
#             return Response(serializer.data)
#
#     def put(self, request, pk):
#         merchant = self.get_object(pk)
#         serializer = MerchantSerializer(merchant, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         merchant = self.get_object(pk)
#         merchant.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
############################APIView的代码############################


############################Mixn的代码###############################
# class MerchantView(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins. CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):
#     queryset = Merchant.objects.all()
#     serializer_class = MerchantSerializer
#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     # def perform_create(self, serializer):
#     #     serializer.save(created=self.request.user)
#
#     def post(self, request):
#         # 如果想要更改添加的逻辑，那么应该重写perform_create方法
#         return self.create(request)
#
#     def put(self, request,pk):
#         return self.update(request,pk)
#
#     def delete(self, request,pk):
#         return self.destroy(request,pk)
############################Mixn的代码##################################

############################generic的代码###############################

class MerchantView(
    # generics.ListAPIView,
    generics.CreateAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.RetrieveAPIView,
):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    lookup_field = 'name'

class MerchantListView(generics.ListAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

############################generic的代码###############################

############################视图集的代码#################################
class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    @action(['GET'], detail=False,url_path='cs')
    def changsha(self,request):
        queryset = self.get_queryset()
        result = queryset.filter(name__contains='长沙')
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(result, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


############################视图集的代码#################################






















