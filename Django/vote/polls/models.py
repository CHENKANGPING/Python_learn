# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone


class Subject(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='名称', 
                          validators=[MinLengthValidator(2, '名称至少需要2个字符')])
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_subject'
        verbose_name = '学科'
        verbose_name_plural = '学科'
        ordering = ['no']


class Teacher(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名',
                          validators=[MinLengthValidator(2, '姓名至少需要2个字符')])
    sex = models.BooleanField(default=True, verbose_name='性别')
    birth = models.DateField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='个人介绍')
    photo = models.ImageField(upload_to='teachers/', verbose_name='照片')
    good_count = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='sno', verbose_name='所属学科')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = '教师'
        verbose_name_plural = '教师'
        ordering = ['no']

    def __str__(self):
        return self.name


class User(models.Model):
    """用户"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名',
                              validators=[MinLengthValidator(3, '用户名至少需要3个字符')])
    password = models.CharField(max_length=128, verbose_name='密码')  # 增加长度以支持哈希密码
    tel = models.CharField(max_length=20, verbose_name='手机号',
                         validators=[RegexValidator(r'^1[3-9]\d{9}$', '请输入正确的手机号')])
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    last_visit = models.DateTimeField(null=True, verbose_name='最后登录时间')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['-reg_date']

    def __str__(self):
        return self.username













