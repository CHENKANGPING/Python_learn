from rest_framework import serializers

from meituan.models import Merchant, Goods,GoodsCategory


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