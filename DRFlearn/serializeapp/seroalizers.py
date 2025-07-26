from rest_framework import serializers

from meituan.models import Merchant, Goods,GoodsCategory


"""
1.用来序列化 ORM->JSON
2.用来验证表单数据 Form
3.可以创建数据 修改数据等

serializer的构造函数的参数
1. instance: 需要传递一个orm对象，或者一个queryset对象，用来将orm模型序列化为json的
2. data: 把需要验证的数据传给data 用来验证这些数据是不是符合要求
3. many: 如果instance是一个queryset对象， 那么就需要设置为true

"""


# class MerchantSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200, required=True, error_messages={"required": "name必须要传！"})
#     logo = serializers.CharField(max_length=200, required=True)
#     address = serializers.CharField(max_length=200, required=True)
#     notice = serializers.CharField(max_length=200, required=False)
#     up_send = serializers.DecimalField(required=False, max_digits=4, decimal_places=2)
#     lon = serializers.FloatField(required=True)
#     lat = serializers.FloatField(required=True)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.logo = validated_data.get('logo', instance.logo)
#         instance.address = validated_data.get('address', instance.address)
#         instance.notice = validated_data.get('notice', instance.notice)
#         instance.up_send = validated_data.get('up_send', instance.up_send)
#         instance.lon = validated_data.get('lon', instance.lon)
#         instance.lat = validated_data.get('lat', instance.lat)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return Merchant.objects.create(**validated_data)


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = "__all__"
        # exclude = ['name']

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"

class GoodsCategorySerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer(read_only=True)
    merchant_id = serializers.IntegerField(write_only=True)
    goods_list = GoodsSerializer(many=True,read_only=True)
    class Meta:
        model = GoodsCategory
    class Meta:
        model = GoodsCategory
        fields = "__all__"

    def validate_merchant_id(self, value):
        if not Merchant.objects.filter(pk=value).exists():
            raise serializers.ValidationError("商家不存在")
        return value

    def create(self, validated_data):
        merchant_id = validated_data.get('merchant_id')
        merchant = Merchant.objects.get(pk=merchant_id)
        category = GoodsCategory.objects.create(**validated_data,merchant=merchant)
        return category
