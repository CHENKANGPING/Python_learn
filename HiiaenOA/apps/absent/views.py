from django.shortcuts import render
from rest_framework import viewsets
from .models import Absent, AbsentType, AbsentStatusChoices
from rest_framework import mixins,generics
from .serializers import AbsentSerializer
# Create your views here.
"""
    1. 发起考勤(create)
    2. 处理考勤(update)
    3. 查看自己的考勤列表(list?who=my)
    4. 查看下属的考勤列表(list?who=sub
    
"""

class AbsentViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Absent.objects.all()
    serializer_class = AbsentSerializer
    
    def update(self, request, *args, **kwargs):
        # 默认情况下，如果要修改某一条数据，那么要把这个数据的序列化中制定的字段都上传
        # 如果只想修改一部分数据，可以在kwargs中设置partial为True
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
