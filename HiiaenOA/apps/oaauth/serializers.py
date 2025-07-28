from rest_framework import serializers

from .models import OAUser, UserStatusChoices


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
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
