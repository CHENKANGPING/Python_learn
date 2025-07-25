from rest_framework import serializers

from meituan.models import Merchant


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
        # exclude = ['name']
