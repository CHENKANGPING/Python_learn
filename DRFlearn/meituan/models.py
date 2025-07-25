from django.db import models
from django.contrib.auth.models import User

class Merchant(models.Model):
    """
    商家
    """
    name = models.CharField(max_length=200,verbose_name='商家名称',null=False)
    address = models.CharField(max_length=200,verbose_name='商家',null=False)
    logo = models.CharField(max_length=200,verbose_name='商家logo',null=False)
    notice = models.CharField(max_length=200, verbose_name='商家的公告',null=True,blank=True)
    up_send = models.DecimalField(verbose_name='起送价',default=0,max_digits=6,decimal_places=2)
    lon = models.FloatField(verbose_name='经度')
    lat = models.FloatField(verbose_name='纬度')

    created = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

class GoodsCategory(models.Model):
    """
    商家商品分类
    """
    name = models.CharField(max_length=20,verbose_name='分类名称')
    merchant = models.ForeignKey(Merchant,on_delete=models.CASCADE,verbose_name='所属商家',related_name='categories')

class Goods(models.Model):
    """
    商品
    """
    name = models.CharField(max_length=200,verbose_name='商品名称')
    picture = models.CharField(max_length=200,verbose_name='商品图片')
    intro = models.CharField(max_length=200)
    price = models.DecimalField(verbose_name='商品价格',max_digits=6,decimal_places=2) # 最多6位数，2位小数。9999.99
    category = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE,related_name='goods_list')