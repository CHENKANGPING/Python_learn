from rest_framework import serializers
from rest_framework import exceptions

from .models import OAUser, UserStatusChoices, OADepartment


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={'required': '请输入邮箱！'})
    password = serializers.CharField(max_length=20, min_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = OAUser.objects.filter(email=email).first()
            if not user:
                raise serializers.ValidationError("请输入正确的邮箱！")
            if not user.check_password(password):
                raise serializers.ValidationError("请输入正确的密码！")
            # 判读状态
            if user.status == UserStatusChoices.UNACTIVE:
                raise serializers.ValidationError("该用户尚未激活！")
            elif user.status == UserStatusChoices.LOCKED:
                raise serializers.ValidationError("该用户已被锁定，请联系管理员!")
            # 为了节省查找执行sql语句的次数，这里我们把user放在attrs中，方便在视同中使用
            attrs['user'] = user
        else:
            raise serializers.ValidationError('请传入邮箱和密码！')
        return attrs

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OADepartment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = OAUser
        # fields = "__all__"
        exclude = ('password','groups','user_permissions')
        
        
class ResetPasswordSerializer(serializers.Serializer):
    oldpwd = serializers.CharField(max_length=20, min_length=6)
    newpwd = serializers.CharField(max_length=20, min_length=6)
    newpwd2 = serializers.CharField(max_length=20, min_length=6)
    
    def validate(self, attrs):
        oldpwd = attrs['oldpwd']
        newpwd = attrs['newpwd']
        newpwd2 = attrs['newpwd2']
        
        user = self.context['request'].user
        if not user.check_password(oldpwd):
            raise exceptions.ValidationError('旧密码错误！')
        
        if newpwd != newpwd2:
            raise exceptions.ValidationError('两次密码不一致！')
        return attrs