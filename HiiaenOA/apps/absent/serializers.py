from rest_framework import exceptions
from rest_framework import serializers

from apps.oaauth.serializers import UserSerializer
from .models import Absent, AbsentType, AbsentStatusChoices
from .utlis import get_responder


class AbsentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsentType
        fields = '__all__'


class AbsentSerializer(serializers.ModelSerializer):
    absent_type = AbsentTypeSerializer(read_only=True)
    absent_type_id = serializers.IntegerField(write_only=True)
    requester = UserSerializer(read_only=True)
    responder = UserSerializer(read_only=True)

    class Meta:
        model = Absent
        fields = '__all__'

    # 验证absent_type_id是否在数据库中
    def validate_absent_type_id(self, value):
        if not AbsentType.objects.filter(pk=value).exists():
            raise exceptions.ValidationError(detail='请假类型不存在！')
        return value

    # create
    def create(self, validated_data):
        request = self.context['request']
        user = request.user

        responder = get_responder(request)

        if responder is None:
            validated_data['status'] = AbsentStatusChoices.PASS
        else:
            validated_data['status'] = AbsentStatusChoices.AUDITING
        return Absent.objects.create(**validated_data, requester=user, responder=responder)

    # update
    # update
    def update(self, instance, validated_data):
        if instance.status != AbsentStatusChoices.AUDITING:
            raise exceptions.ValidationError(detail='不能修改已经确定的请假数据！')
        request = self.context['request']
        user = request.user
        if instance.responder.uid != user.uid:
            raise exceptions.ValidationError(detail='您无权处理该考勤！')

        # 使用 get() 方法安全地获取字段值
        instance.status = validated_data.get('status', instance.status)
        instance.responder_content = validated_data.get('responder_content', instance.responder_content)
        instance.save()
        return instance
