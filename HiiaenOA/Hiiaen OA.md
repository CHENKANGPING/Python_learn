# Hiiaen OA

## 1.Django配置

### 1.1语言时区配置

```python
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False
```

### 1.2数据库配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hiiaenoa',
        'USER': 'root',
        'PASSWORD': '8737',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 1.3安装rest_framework

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 安装rest_framework
    'rest_framework',
]
```

### 1.4关闭CSRF保护

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #关闭CSRF保护
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## 2.跨域访问配置

https://pypi.org/project/django-cors-headers/

### 2.1安装django-cors-headers

```bash
pip install django-cors-headers
```

### 2.2配置django-cors-headers

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 安装rest_framework
    'rest_framework',
    # 安装django-cors-headers
    'corsheaders',
]
```

### 2.3中间件配置

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 跨域中间件配置，一定要在CommonMiddleware前
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    # 关闭CSRF保护
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### 2.4 允许所有域名跨域访问

```python
# 允许所有域名跨域访问
CORS_ALLOW_ALL_ORIGINS = True
```

## 3.重写User模型

Django自带的User模型无法满足业务的需求，需要重写User模型。

### 3.1创建oaauthapp

```bash
python manage.py startapp oaauth
```

### 3.2创建apps

将oaauth拖入apps中

### 3.3重写User模型

1.查看原来的User模型

```py
from django.contrib.auth.models import User
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

```

2.重写User模型

```python
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password

class UserStatusChoices(models.IntegerChoices):
    # 已经激活的
    ACTIVED = 1
    # 未激活的
    UNACTIVE = 2
    # 被锁定
    LOCKED = 3


class OAUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, realname, email, password, **extra_fields):
        """
        创建用户
        """
        if not realname:
            raise ValueError("必须设置真实姓名！")
        email = self.normalize_email(email)
        user = self.model(realname=realname, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, realname, email=None, password=None, **extra_fields):
        """
        创建普通用户
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(realname, email, password, **extra_fields)

    def create_superuser(self, realname, email=None, password=None, **extra_fields):
        """
        创建超级用户
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("status",UserStatusChoices.ACTIVED)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("超级用户必须设置is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("超级用户必须设置is_superuser=True.")

        return self._create_user(realname, email, password, **extra_fields)





# 重写User模型
class OAUser(AbstractBaseUser, PermissionsMixin):
    """
    自定义的User模型
    """
    realname = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True, blank=False, )
    telephone = models.CharField(max_length=11, blank=True)
    is_staff = models.BooleanField(default=True)
    # 只要关注status即可，无需关注is_active
    status = models.IntegerField(choices=UserStatusChoices.choices,default=UserStatusChoices.UNACTIVE)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = OAUserManager()

    EMAIL_FIELD = "email"
    # USERNAME_FIELD:是用来鉴权的，会把authenticate的username的参数，传给USERNAME_FIELD制定的字段
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS：指定哪些字段是必须要传的，但是不能重复包含USERNAME_FIELD和EMAIL_FIELD已经设置过的值
    REQUIRED_FIELDS = ["realname", "password"]


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.realname

    def get_short_name(self):
        return self.realname
```

3.覆盖Django自带的User模型

```python
# 覆盖Django自带的User模型
# 'app.User模型名'
# 下面写法是不对的
# AUTH_USER_MODEL = 'apps.oaauth.models.OAUser'
AUTH_USER_MODEL = 'oaauth.OAUser'
```

4.将User模型翻译成数据库脚本

```bash
python manage.py makemigrations
```

5.将数据库脚本执行到数据库中

```bash
python manage.py migrate
```

6.创建超级用户

```bash
python manage.py createsuperuser
```

7.使用Navicat查看是否成功

![image-20250728140333081](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250728140333081.png)

## 4.修改OAUser主键

### 4.1删除数据库，删除migrations文件中的文件，只保留`__init__.py`

### 4.2安装  django-shortuuidfield

```bash
 pip install django-shortuuidfield
```

### 4.3使用  django-shortuuidfield

```python
from shortuuidfield import ShortUUIDField
uid = ShortUUIDField(primary_key=True)
```

### 4.5重新将User模型翻译成数据库脚本

```bash
python manage.py makemigrations
```

### 4.6将数据库脚本执行到数据库中

```bash
python manage.py migrate
```

## 5.添加部门表

### 5.1部门组织架构图

![image-20250728152045903](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250728152045903.png)

### 5.2添加部门模型

```python
class OADepartment(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)
    # leader
    leader = models.OneToOneField(OAUser,null=True,on_delete=models.SET_NULL,related_name="leader_department",related_query_name="leader_department")
    #manager
    manager = models.ForeignKey(OAUser,null=True,on_delete=models.SET_NULL,related_name="manager_department",related_query_name="manager_department")

# 在User模型中添加
deparment = models.ForeignKey("OADepartment", null=True, on_delete=models.SET_NULL,related_name="staffs",related_query_name="staff")

```

### 5.3翻译模型成数据库脚本，并执行到数据库

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5.4使用Navicat查看

![image-20250728154346784](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250728154346784.png)

## 6.自定义命令初始化部门表

### 6.1创建名为`management`的python包，在`management`下创建名为`commands`的python包，创建`initdeparments.py`文件。

### 6.2在`initdeparments.py`内写入

```python
from django.core.management.base import BaseCommand
from apps.oaauth.models import OADepartment

class Command(BaseCommand):
    def handle(self, *args, **options):
        # 初始化部门数据
        boarder = OADepartment.objects.create(name="董事会", introduction = "董事会")
        developer = OADepartment.objects.create(name="产品开发部", introduction = "产品设计,技术开发")
        operator = OADepartment.objects.create(name="运营部", introduction = "客户运营,产品运营")
        saler = OADepartment.objects.create(name="销售部", introduction = "销售产品")
        hr = OADepartment.objects.create(name="人事部", introduction = "员工招聘,员工培训,员工考核")
        finance = OADepartment.objects.create(name="财务部", introduction = "财务报表,财务审核")
        self.stdout.write("部门数据初始化成功！")
```

### 6.3运行自定义指令

```python
python manage.py initdeparments.py
```

### 6.4使用Naivcat查看

![image-20250728160645588](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250728160645588.png)

## 7.自定义命令初始化领导数据

### 7.1在`commands`下创建`inituser.py`文件

### 7.2编写`inituser.py`

```python
from django.core.management.base import BaseCommand

from apps.oaauth.models import OAUser, OADepartment


class Command(BaseCommand):
    def handle(self, *args, **options):
        boarder = OADepartment.objects.get(name="董事会")
        developer = OADepartment.objects.get(name="产品开发部")
        operator = OADepartment.objects.get(name="运营部")
        saler = OADepartment.objects.get(name="销售部")
        hr = OADepartment.objects.get(name="人事部")
        finance = OADepartment.objects.get(name="财务部")
        # 董事会的员工都是superuser用户
        # 1.东东：属于董事会的leader
        dongdong = OAUser.objects.create_superuser(email='dongdong@qq.com', realname='东东', password='111111',department=boarder)
        # 2.多多：属于董事会
        duoduo = OAUser.objects.create_superuser(email='duoduo@qq.com', realname='多多', password='111111',department=boarder)
        # 3.张三：产品开发部leader
        zhangsan = OAUser.objects.create_user(email='zhangsan@qq.com', realname='张三', password='111111',department=developer)
        # 4.李四：运营部的leader
        lisi = OAUser.objects.create_user(email='lisi@qq.com', realname='李四', password='111111',department=operator)
        # 5.王五：人事部的leader
        wangwu = OAUser.objects.create_user(email='wangwu@qq.com', realname='王五', password='111111',department=hr)
        # 6.赵六：财务部的leader
        zhaoliu = OAUser.objects.create_user(email='zhaoliu@qq.com', realname='赵六', password='111111',department=finance)
        # 7.孙七：销售部的leader
        sunqi = OAUser.objects.create_user(email='sunqi@qq.com', realname='孙七', password='111111',department=saler)

        # 给部门制定leader和manager
        # 1.董事会
        boarder.leader = dongdong
        boarder.manager = None

        # 2.产品开发部
        developer.leader = zhangsan
        developer.manager = dongdong

        # 3.运营部
        operator.leader = lisi
        operator.manager = dongdong

        # 4.销售部
        saler.leader = sunqi
        saler.manager = dongdong

        # 5.人事部
        hr.leader = wangwu
        hr.manager = duoduo

        # 6.财务部
        finance.leader = zhaoliu
        finance.manager = duoduo

        boarder.save()
        developer.save()
        operator.save()
        saler.save()
        hr.save()
        finance.save()

        self.stdout.write("初始用户创建成功！")
```

### 7.3运行自定义指令

```python
python manage.py inituser.py
```

### 7.4使用Naivcat查看

![image-20250728170158313](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250728170158313.png)

![image-20250728170212566](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250728170212566.png)

## 8.登录功能实现

### 8.1在oaauth下创建`authentications.py`用来实现JWT认证

```python
import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication,get_authorization_header
from rest_framework import exceptions
from django.contrib.auth import get_user_model
from jwt.exceptions import ExpiredSignatureError
MTUser = get_user_model()
import time
from .models import OAUser

def generate_jwt(user):
    expire_time = int(time.time() + 60*60*24*7)
    return jwt.encode({"userid":user.pk,"exp":expire_time},key=settings.SECRET_KEY)

class JWTAuthentication(BaseAuthentication):
    """
    Authorization: JWT 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Authorization不可用！'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Authorization不可用！应该提供一个空格！'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms="HS256")
            userid = jwt_info.get('userid')
            try:
                user = OAUser.objects.get(pk=userid)
                return (user, jwt_token)
            except Exception:
                msg = '用户不存在！'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'token格式错误！'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = 'token已过期！'
            raise exceptions.AuthenticationFailed(msg)
```

### 8.2在oaauth下的`Views.py`下实现登录功能

```python
from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializers import LoginSerializer
from .authentications import generate_jwt
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        # 1.验证数据是否可用
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = datetime.now()
            user.save()
            token = generate_jwt(user)
            return Response({'token': token})
        else:
            print(serializer.errors)
            return Response({"message": "参数验证失败！"},status=status.HTTP_400_BAD_REQUEST)


```

### 8.3配置路由

在oaauth下创建`urls.py`

```python
from django.urls import path
from . import  views

app_name = 'oaauth'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
]
```

在主路由下

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.oaauth.urls')),
]

```

### 8.4Postman验证

![image-20250729095055639](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729095055639.png)![image-20250729095036407](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729095036407.png)

## 9.返回用户信息

### 9.1序列化OAUser模型的数据，嵌套序列化用户的部门信息，排除敏感字段

```python
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
```

### 9.2Postman验证

![image-20250729100628515](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729100628515.png)

## 10.创建前端项目

### 10.1创建项目

在该项目的存放文件下进入`cmd`

```bash
npm create vue@3.10.3
```

![image-20250729101309241](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729101309241.png)

## 11.frame和login结构搭建

### 11.1删除不必要的页面和创建`login.vue`和`frame.vue`

![image-20250729103905207](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729103905207.png)

### 11.2安装vite-plugin-vue-setup-extend

```bash
npm install vite-plugin-vue-setup-extend --save-dev
```

配置:在`vite.config.js`中配置

```js
import VueSetupExtend from 'vite-plugin-vue-setup-extend'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VueSetupExtend()
  ],
})
```

### 11.3在router下`index.js`的路由配置

```js
import { createRouter, createWebHashHistory } from 'vue-router'
import login from '../views/login/login.vue'
import frame from '../views/main/frame.vue'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'frame',
      component: frame
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})

export default router

```

## 12.登录页面实现

### 12.1将`css` `img`等文件放入`assets`中

![image-20250729111732749](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729111732749.png)

### 12.2在`login.vue`中添加`HTML`

```html
<div class="dowebok">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img :src="login_img" alt="IMG" />
                </div>

                <div class="login100-form validate-form">
                    <span class="login100-form-title"> 员工登陆 </span>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="text" name="email" placeholder="邮箱" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="password" name="password" placeholder="密码" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-lock" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn">
                            登陆
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
```

### 12.4在`VUE`中添加外部`css`

```vue
<style scoped src="@/assets/css/login.css"></style>
<style scoped src="@/assets/iconfont/iconfont.css"></style>
```

### 12.7解决浏览器自带样式

在`APP.vue`下进行修改

```vue
<style>
*{
  margin: 0;
  padding: 0;
}
</style>

```



### 12.6启动`VUE`浏览界面

```bash
npm run dev
```

![image-20250729112133008](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729112133008.png)

## 13.前段登录功能实现

### 13.1安装axios

```bash
npm install axios@1.6.8
```

### 13.2修改`login.vue`

```vue
<script setup name="login">
import login_img from '@/assets/image/login.jpg'
import { reactive } from 'vue';
import axios from 'axios';

let form = reactive({
    email: '',
    password: ''
})

const onSubmit = () => {
    let pwdRgx = /^[0-9a-zA-Z]{6,20}/
    let emailRgx = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9]+)+/
    if(!(emailRgx.test(form.email))){
        alert('邮箱格式错误');
        return;
    }
    if(!(pwdRgx.test(form.password))){
        alert('密码格式错误');
        return;
    }
    // axios
    // promise
    axios.post("http://127.0.0.1:8000/auth/login",{
        email: form.email,
        password: form.password
    }).then(res => {
        // then:代表成功的情况（在这里，代表返回的状态码200）
        let data = res.data;
        let token = data.token;
        let user = data.user;
        console.log(token);
        console.log(user);
        
    }).catch((err) =>{
        // catch:代表失败的情况（在这里，代表返回的状态码不是200）
        let detail = err.response.data.detail
        alert(detail)
    })
}

</script>

<template>
    <div class="dowebok">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img :src="login_img" alt="IMG" />
                </div>

                <div class="login100-form validate-form">
                    <span class="login100-form-title"> 员工登陆 </span>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="text" name="email" placeholder="邮箱" v-model="form.email" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="password" name="password" placeholder="密码" v-model="form.password" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-lock" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn" @click="onSubmit">
                            登陆
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped src="@/assets/css/login.css"></style>
<style scoped src="@/assets/iconfont/iconfont.css"></style>

```

### 13.3浏览器验证登录

输入正确的邮箱和密码，浏览器返回

![image-20250729144801089](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729144801089.png)

## 14.用户和token信息管理

### 14.1在stores下创建`auth.js`文件

```js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const USER_KEY = "OA_USER_KEY";
const TOKEN_KEY = "OA_TOKEN_KEY";

export const useAuthStore = defineStore('auth', () => {
    let _user = ref({});
    let _token = ref({});

    function setUerToken(user, token) {
        // 保存到对象上(内存中)
        _user.value = user;
        _token.value = token;

        // 存储到浏览器的localStorge(硬盘上)
        localStorage.setItem(USER_KEY, JSON.stringify(user));
        localStorage.setItem(TOKEN_KEY, token);
    }

    // 计算属性
    let user = computed(() => {
        // 如果_user是一个空对象，那么就视图从localStorge中获取
        if(!_user.value){
            _user.value = localStorage.getItem(USER_KEY);
        }
        return _user.value;
    });
    // 计算属性
    let token = computed(() => {
        // 如果_token是一个空对象，那么就视图从localStorge中获取
        if(!_token.value){
            _token.value = localStorage.getItem(TOKEN_KEY);
        }
        return _token.value;
    });
    // 想要让外面访问，就必须要返回
    return {setUerToken,user,token}
})

```

### 14.2修改`login.vue`

```vue
<script setup name="login">
import login_img from '@/assets/image/login.jpg'
import { reactive } from 'vue';
import axios from 'axios';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

let form = reactive({
    email: '',
    password: ''
})

const onSubmit = () => {
    let pwdRgx = /^[0-9a-zA-Z]{6,20}/
    let emailRgx = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9]+)+/
    if(!(emailRgx.test(form.email))){
        alert('邮箱格式错误');
        return;
    }
    if(!(pwdRgx.test(form.password))){
        alert('密码格式错误');
        return;
    }
    // axios
    // promise
    axios.post("http://127.0.0.1:8000/auth/login",{
        email: form.email,
        password: form.password
    }).then(res => {
        // then:代表成功的情况（在这里，代表返回的状态码200）
        let data = res.data;
        let token = data.token;
        let user = data.user;
        authStore.setUerToken(user,token);
        // 登陆成功，跳转到OA系统的首页
        router.push({name:"frame"});
    }).catch((err) =>{
        // catch:代表失败的情况（在这里，代表返回的状态码不是200）
        let detail = err.response.data.detail
        alert(detail)
    })
}

</script>

<template>
    <div class="dowebok">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img :src="login_img" alt="IMG" />
                </div>

                <div class="login100-form validate-form">
                    <span class="login100-form-title"> 员工登陆 </span>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="text" name="email" placeholder="邮箱" v-model="form.email" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="password" name="password" placeholder="密码" v-model="form.password" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-lock" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn" @click="onSubmit">
                            登陆
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped src="@/assets/css/login.css"></style>
<style scoped src="@/assets/iconfont/iconfont.css"></style>

```

成功登录后会跳转到frame页面

![image-20250729152352060](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729152352060.png)

![image-20250729152404311](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250729152404311.png)

## 15.使用async和await改写Ajax请求

### 15.1创建生产环境和开发环境

在`vue`目录下创建`.env.development`和`.env.production`两个文件

在`.env.development`下写入开发环境的URL

```mariadb
VITE_BASE_URL = "http://127.0.0.1:8000"
```

### 15.2在src下创建api文件夹，在该目录下创建`authHttp.js`和`http.js`

在`http.js`下写入

```js
import axios from 'axios';

class Http {
    constructor() {
        this.instance = axios.create({
            baseURL: import.meta.env.VITE_BASE_URL,
            timeout: 10000,
        });
    }

    post(path, data) {
        // path: /auth/login
        // url: http://127.0.0.1:8000/auth/login
        // return this.instance.post(path, data);
        return new Promise(async (resolve, reject) => {
            // 网络请求发送出去后，线程会挂起这个等待
            // 等网络数据到达后，线程又会回到当前位置开始后执行
            // 如果在某个函数中使用了await，那么这个函数就必须要定义成async
            // axios底层也是使用promise对象，在响应的状态码不是200时，会调用reject
            // 调用reject的结果是，外层的函数会抛出异常
            try {
                let result = await this.instance.post(path, data)
                // 如果走到下面代码，说明上面await函数没有抛出异常，就肯定说明返回的状态码是200
                resolve(result.data);
            } catch (err) {
                let detial = err.response.data.detail;
                reject(detial)
            }
        })
    }

    get(path, params) {
        return this.instance.get(path, { params });
    }
}
export default new Http();
```

在`authHttp.js`下写入

```js
import http from './http';

const login = (email,password) =>{
    const path = '/auth/login';
    return http.post(path,{email,password});
}
export default {
    login,
}
```

### 15.3优化`login.vue`

```vue
<script setup name="login">
import login_img from '@/assets/image/login.jpg'
import { reactive } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import authHttp from '@/api/authHttp';

const authStore = useAuthStore();
const router = useRouter();

let form = reactive({
    email: '',
    password: ''
})

const onSubmit = async () => {
    let pwdRgx = /^[0-9a-zA-Z]{6,20}/
    let emailRgx = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9]+)+/
    if(!(emailRgx.test(form.email))){
        alert('邮箱格式错误');
        return;
    }
    if(!(pwdRgx.test(form.password))){
        alert('密码格式错误');
        return;
    }
    // axios
    // promise
    // 第一个版本，直接使用axios
    // axios.post("http://127.0.0.1:8000/auth/login",{
    //     email: form.email,
    //     password: form.password
    // }).then(res => {
    //     // then:代表成功的情况（在这里，代表返回的状态码200）
    //     let data = res.data;
    //     let token = data.token;
    //     let user = data.user;
    //     authStore.setUerToken(user,token);
    //     // 登陆成功，跳转到OA系统的首页
    //     router.push({name:"frame"});
    // }).catch((err) =>{
    //     // catch:代表失败的情况（在这里，代表返回的状态码不是200）
    //     let detail = err.response.data.detail
    //     alert(detail)
    // })
    
    // 第二个版本，对axios进行了一层封装
    // authHttp.login(form.email,form.password).then(res => {
    //      let data = res.data;
    //     let token = data.token;
    //     let user = data.user;
    //     authStore.setUerToken(user,token);
    //     // 登陆成功，跳转到OA系统的首页
    //     router.push({name:"frame"});
    // }).catch((err) =>{
    //     // catch:代表失败的情况（在这里，代表返回的状态码不是200）
    //     let detail = err.response.data.detail
    //     alert(detail)
    // })

    // 第三个版本，改成了异步调用的方式
    try{
        let data = await authHttp.login(form.email,form.password);
        let token = data.token;
        let user = data.user;
        authStore.setUerToken(user,token);
        // 登陆成功，跳转到OA系统的首页
        router.push({name:"frame"});
    }catch(detail){
        alert(detail)
    }
}

</script>

<template>
    <div class="dowebok">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img :src="login_img" alt="IMG" />
                </div>

                <div class="login100-form validate-form">
                    <span class="login100-form-title"> 员工登陆 </span>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="text" name="email" placeholder="邮箱" v-model="form.email" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input">
                        <input class="input100" type="password" name="password" placeholder="密码" v-model="form.password" />
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="iconfont icon-fa-lock" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn" @click="onSubmit">
                            登陆
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped src="@/assets/css/login.css"></style>
<style scoped src="@/assets/iconfont/iconfont.css"></style>

```

## 16.集成ElementPlus

### 16.1 安装配置ElementPlus

官网：https://element-plus.org/zh-CN/

```bash
npm install element-plus --save
```

在`main.js`中配置

```js

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)

app.mount('#app')

```

### 16.2使用ElementPlus

在`frame.vue`下添加一个按钮

```vue
<script setup name="frame">

</script>

<template>
<h1>这是frame页面</h1>
<el-button>这是一个按钮</el-button>
</template>

<style scoped>

</style>

```

## 17.优化登录失败提示

### 17.1 替换原本的提示

修改`login.vue`

```vue
import { ElMessage } from 'element-plus';

const onSubmit = async () => {
    let pwdRgx = /^[0-9a-zA-Z]{6,20}/
    let emailRgx = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(.[a-zA-Z0-9]+)+/
    if(!(emailRgx.test(form.email))){
        // alert('邮箱格式错误');
        ElMessage.info('邮箱格式错误');
        return;
    }
    if(!(pwdRgx.test(form.password))){
        // alert('密码格式错误');
        ElMessage.info('密码格式错误');
        return;
    }
    // axios
    // promise
    // 第一个版本，直接使用axios
    // axios.post("http://127.0.0.1:8000/auth/login",{
    //     email: form.email,
    //     password: form.password
    // }).then(res => {
    //     // then:代表成功的情况（在这里，代表返回的状态码200）
    //     let data = res.data;
    //     let token = data.token;
    //     let user = data.user;
    //     authStore.setUerToken(user,token);
    //     // 登陆成功，跳转到OA系统的首页
    //     router.push({name:"frame"});
    // }).catch((err) =>{
    //     // catch:代表失败的情况（在这里，代表返回的状态码不是200）
    //     let detail = err.response.data.detail
    //     alert(detail)
    // })
    
    // 第二个版本，对axios进行了一层封装
    // authHttp.login(form.email,form.password).then(res => {
    //      let data = res.data;
    //     let token = data.token;
    //     let user = data.user;
    //     authStore.setUerToken(user,token);
    //     // 登陆成功，跳转到OA系统的首页
    //     router.push({name:"frame"});
    // }).catch((err) =>{
    //     // catch:代表失败的情况（在这里，代表返回的状态码不是200）
    //     let detail = err.response.data.detail
    //     alert(detail)
    // })

    // 第三个版本，改成了异步调用的方式
    try{
        let data = await authHttp.login(form.email,form.password);
        let token = data.token;
        let user = data.user;
        authStore.setUerToken(user,token);
        // 登陆成功，跳转到OA系统的首页
        router.push({name:"frame"});
    }catch(detail){
        // alert(detail)
        ElMessage.error(detail)
    }
}
```

### 17.2优化登录失败提示

修改`serializers.py`

```python
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={'required': '请输入邮箱！'})
    password = serializers.CharField(max_length=20, min_length=6)
```

修改`views.py`

```python
class LoginView(APIView):
    def post(self, request):
        # 1.验证数据是否可用
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = datetime.now()
            user.save()
            token = generate_jwt(user)
            return Response({'token': token,'user': UserSerializer(user).data})
        else:
            detial = list(serializer.errors.values())[0][0]
            return Response({"detail": detial}, status=status.HTTP_400_BAD_REQUEST)

```

## 18.Frame页面结构搭建

在`frame.vue`下进行搭建

```vue
<script setup name="frame">

</script>

<template>
    <el-container class="container">
        <el-aside class="aside" width="250px">
            <router-link to="/" class="brand">Hiiaen OA</router-link>
        </el-aside>
        <el-container>
            <el-header class="header">Header</el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;

}
.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1xp solid #e6e6e6;
}
</style>

```

效果：

![image-20250730134009853](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250730134009853.png)

## 19.侧栏菜单实现

### 19.1修改`frame.vue`文件

```vue
<script setup name="frame">

</script>

<template>
    <el-container class="container">
        <el-aside class="aside" width="250px">
            <router-link to="/" class="brand">Hiiaen OA</router-link>
            <el-menu default-active="1" class="el-menu-vertical-demo" background-color="#343a40" text-color="#fff">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">Header</el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;

}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1xp solid #e6e6e6;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}
</style>
```

### 19.2 使用icon图标

安装icon包

```bash
npm install @element-plus/icons-vue
```

在`main.js`下进行配置

```js
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// 注册所有图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
```

### 19.3侧边菜单栏效果

![image-20250730145201110](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250730145201110.png)

##  20.折叠和展开菜单栏功能

修改`frame.vue`文件

```vue
<script setup name="frame">
import { ref, computed } from 'vue'
import {
    Expand,
    Fold,
} from '@element-plus/icons-vue'

let isCollapse = ref(false);
let asidWidth = computed(() => {
    if (isCollapse.value) {
        return '64px'
    } else {
        return '250px'
    }
})

const onCollapseAside = () => {
    isCollapse.value = !isCollapse.value;
}
</script>

<template>
    <el-container class="container">
        <el-aside class="aside" :width="asidWidth">
            <router-link to="/" class="brand">
                <strong>Hiiaen</strong>
                <transition name="fade">
                    <span v-show="!isCollapse" class="brand-text">OA</span>
                </transition>
            </router-link>
            <el-menu 
                default-active="1" 
                class="el-menu-vertical-demo" 
                background-color="#343a40" 
                text-color="#fff"
                :collapse="isCollapse"
                :collapse-transition="false">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">
                <el-button 
                    class="collapse-btn" 
                    :icon="isCollapse ? Expand : Fold" 
                    @click="onCollapseAside"
                    circle />
            </el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
    transition: width 0.3s ease-in-out;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    white-space: nowrap;
}

.brand-text {
    margin-left: 4px;
}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    align-items: center;
    padding: 0 20px;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
    transition: all 0.3s ease;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}

.collapse-btn {
    font-size: 18px;
    border: none;
    background: transparent;
    color: #606266;
    cursor: pointer;
    transition: all 0.3s ease;
}

.collapse-btn:hover {
    color: #409eff;
    transform: scale(1.1);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

```

## 21.header组件布局

修改`frame.vue`文件内容

```vue
<script setup name="frame">
import { ref, computed } from 'vue'
import {
    Expand,
    Fold,
} from '@element-plus/icons-vue'

let isCollapse = ref(false);
let asidWidth = computed(() => {
    if (isCollapse.value) {
        return '64px'
    } else {
        return '250px'
    }
})

const onCollapseAside = () => {
    isCollapse.value = !isCollapse.value;
}
</script>

<template>
    <el-container class="container">
        <el-aside class="aside" :width="asidWidth">
            <router-link to="/" class="brand">
                <strong>Hiiaen</strong>
                <transition name="fade">
                    <span v-show="!isCollapse" class="brand-text">OA</span>
                </transition>
            </router-link>
            <el-menu default-active="1" class="el-menu-vertical-demo" background-color="#343a40" text-color="#fff"
                :collapse="isCollapse" :collapse-transition="false">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">
                <div class="header-left">
                    <el-button class="collapse-btn" :icon="isCollapse ? Expand : Fold" @click="onCollapseAside" />
                </div>
                <el-dropdown>
                    <span class="el-dropdown-link">
                        <el-avatar :size="30" icon="UserFilled" />
                        <span style="margin-left: 4px;">Hiiaen</span>
                        <el-icon class="el-icon--right">
                            <arrow-down />
                        </el-icon>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item>修改密码</el-dropdown-item>
                            <el-dropdown-item divided>退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
    transition: width 0.3s ease-in-out;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    white-space: nowrap;
}

.brand-text {
    margin-left: 4px;
}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.header-left {
    display: flex;
    align-items: center;

}

.el-dropdown-link{
    display: flex;
    align-items: center;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
    transition: all 0.3s ease;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}

.collapse-btn {
    font-size: 18px;
    border: none;
    background: transparent;
    color: #606266;
    cursor: pointer;
    transition: all 0.3s ease;
}

.collapse-btn:hover {
    color: #409eff;
    transform: scale(1.1);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

```

## 22.auth.js 小bug

修改`auth.js`

```js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const USER_KEY = "OA_USER_KEY";
const TOKEN_KEY = "OA_TOKEN_KEY";

export const useAuthStore = defineStore('auth', () => {
    let _user = ref({});
    let _token = ref({});

    function setUerToken(user, token) {
        // 保存到对象上(内存中)
        _user.value = user;
        _token.value = token;

        // 存储到浏览器的localStorge(硬盘上)
        localStorage.setItem(USER_KEY, JSON.stringify(user));
        localStorage.setItem(TOKEN_KEY, token);
    }

    // 计算属性
    let user = computed(() => {
        // 如果_user是一个空对象，那么就视图从localStorge中获取
        if (Object.keys(_user.value).length == 0) {
            let user_str = localStorage.getItem(USER_KEY);
            if (user_str) {
                _user.value = JSON.parse(user_str);
            }
        }
        return _user.value;
    });
    // 计算属性
    let token = computed(() => {
        // 如果_token是一个空对象，那么就视图从localStorge中获取
        if (!_token.value) {
            let token_str = localStorage.getItem(TOKEN_KEY);
           if(token_str){
            _token.value = token_str;
           }
        }
        return _token.value;
    });
    // 想要让外面访问，就必须要返回
    return { setUerToken, user, token }
})

```

## 23.未登录限制访问

## 23.1修改`auth.js`

```js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const USER_KEY = "OA_USER_KEY";
const TOKEN_KEY = "OA_TOKEN_KEY";

export const useAuthStore = defineStore('auth', () => {
    let _user = ref({});
    let _token = ref({});

    function setUerToken(user, token) {
        // 保存到对象上(内存中)
        _user.value = user;
        _token.value = token;

        // 存储到浏览器的localStorge(硬盘上)
        localStorage.setItem(USER_KEY, JSON.stringify(user));
        localStorage.setItem(TOKEN_KEY, token);
    }

    // 计算属性
    let user = computed(() => {
        // 如果_user是一个空对象，那么就视图从localStorge中获取
        if (Object.keys(_user.value).length == 0) {
            let user_str = localStorage.getItem(USER_KEY);
            if (user_str) {
                _user.value = JSON.parse(user_str);
            }
        }
        return _user.value;
    });
    // 计算属性
    let token = computed(() => {
        // 如果_token是一个空对象，那么就视图从localStorge中获取
        if (!_token.value) {
            let token_str = localStorage.getItem(TOKEN_KEY);
           if(token_str){
            _token.value = token_str;
           }
        }
        return _token.value;
    });

    let  is_logined = computed(() =>{
      if(Object.keys(user.value).length>0 && token.value){
        return true;
      }
      return false;
    })

    // 想要让外面访问，就必须要返回
    return { setUerToken, user, token,is_logined }
})

```

### 23.2修改`index.js`

```js
router.beforeEach((to, from) =>{
  const authStore = useAuthStore();
  if(!authStore.is_logined && to.name != 'login'){
    return {name:'login'}
  }
})
```

这样就实现了，没有登录无法访问frame页面。

## 24.退出登录功能实现

24.1在`auth.js`构造退出登录的函数

```js
function clearUerToken(){
        _user.value = {};
        _token.value = '';
        localStorage.removeItem(USER_KEY);
        localStorage.removeItem(TOKEN_KEY);
    }
```

### 24.2添加按钮以及显示真实信息

在`frame.vue`中修改

```vue
<script setup name="frame">
import { ref, computed } from 'vue'
import {
    Expand,
    Fold,
} from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

let isCollapse = ref(false);
let asidWidth = computed(() => {
    if (isCollapse.value) {
        return '64px'
    } else {
        return '250px'
    }
})

const onCollapseAside = () => {
    isCollapse.value = !isCollapse.value;
}

const onExit = () =>{
    authStore.clearUerToken();
    router.push({name:'login'});
}
</script>

<template>
    <el-container class="container">
        <el-aside class="aside" :width="asidWidth">
            <router-link to="/" class="brand">
                <strong>Hiiaen</strong>
                <transition name="fade">
                    <span v-show="!isCollapse" class="brand-text">OA</span>
                </transition>
            </router-link>
            <el-menu default-active="1" class="el-menu-vertical-demo" background-color="#343a40" text-color="#fff"
                :collapse="isCollapse" :collapse-transition="false">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">
                <div class="header-left">
                    <el-button class="collapse-btn" :icon="isCollapse ? Expand : Fold" @click="onCollapseAside" />
                </div>
                <el-dropdown>
                    <span class="el-dropdown-link">
                        <el-avatar :size="30" icon="UserFilled" />
                        <span style="margin-left: 4px;">[{{ authStore.user.department.name }}]{{authStore.user.realname}}</span>
                        <el-icon class="el-icon--right">
                            <arrow-down />
                        </el-icon>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item>修改密码</el-dropdown-item>
                            <el-dropdown-item divided @click="onExit">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
    transition: width 0.3s ease-in-out;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    white-space: nowrap;
}

.brand-text {
    margin-left: 4px;
}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.header-left {
    display: flex;
    align-items: center;

}

.el-dropdown-link{
    display: flex;
    align-items: center;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
    transition: all 0.3s ease;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}

.collapse-btn {
    font-size: 18px;
    border: none;
    background: transparent;
    color: #606266;
    cursor: pointer;
    transition: all 0.3s ease;
}

.collapse-btn:hover {
    color: #409eff;
    transform: scale(1.1);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

```

## 25.中间件实现登录校验

### 25.1实现中间件

在`oaauth`下创建`middlewares.py`

```python
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from rest_framework.status import HTTP_403_FORBIDDEN
from jwt.exceptions import ExpiredSignatureError
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import reverse

OAUser = get_user_model()


class LoginCheckMiddleware(MiddlewareMixin):
    keyword = "JWT"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 对于那些不需要登录就能访问的接口，可以写在这里
        self.white_list = [reverse("oaauth:login")]  # 只保留存在的URL

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 1. 如果返回None，那么会正常执行（包括执行视图、执行其他中间件的代码）
        # 2. 如果返回一个HttpResponse对象，那么将不会执行视图，以及后面的中间件代码
        if request.path in self.white_list or request.path.startswith(settings.MEDIA_URL):
            request.user = AnonymousUser()
            request.auth = None
            return None
        try:
            auth = get_authorization_header(request).split()

            if not auth or auth[0].lower() != self.keyword.lower().encode():
                raise exceptions.ValidationError("请传入JWT！")

            if len(auth) == 1:
                msg = "不可用的JWT请求头！"
                raise exceptions.AuthenticationFailed(msg)
            elif len(auth) > 2:
                msg = '不可用的JWT请求头！JWT Token中间不应该有空格！'
                raise exceptions.AuthenticationFailed(msg)

            try:
                jwt_token = auth[1]
                jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms='HS256')
                userid = jwt_info.get('userid')
                try:
                    # 绑定当前user到request对象上
                    user = OAUser.objects.get(pk=userid)
                    # HttpRequest对象：是Django内置的
                    request.user = user
                    request.auth = jwt_token
                except:
                    msg = '用户不存在！'
                    raise exceptions.AuthenticationFailed(msg)
            except ExpiredSignatureError:
                msg = "JWT Token已过期！"
                raise exceptions.AuthenticationFailed(msg)
        except Exception as e:
            print(e)
            return JsonResponse(data={"detail": "请先登录！"}, status=HTTP_403_FORBIDDEN)
```

### 25.2修改`settings.py`

```python
"""
Django settings for HiiaenOAback project.

Generated by 'django-admin startproject' using Django 4.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import re


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$r+q3fq6^%z)cotx1*$)3+0#navy#duxv^j2!)9hnky#h88cge'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    # 安装rest_framework
    'rest_framework',
    # 安装django-cors-headers
    'corsheaders',
    # 安装项目的app
    'apps.oaauth'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 跨域中间件配置，一定要在CommonMiddleware前
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    # 关闭CSRF保护
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自定义中间件
    'apps.oaauth.middlewares.LoginCheckMiddleware',
]

ROOT_URLCONF = 'HiiaenOAback.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'HiiaenOAback.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hiiaenoa',
        'USER': 'root',
        'PASSWORD': '8737',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# 语言编码
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 允许所有域名跨域访问
CORS_ALLOW_ALL_ORIGINS = True

# 覆盖Django自带的User模型
# 'app.User模型名'
# 下面写法是不对的
# AUTH_USER_MODEL = 'apps.oaauth.models.OAUser'
AUTH_USER_MODEL = 'oaauth.OAUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.oaauth.authentications.JWTAuthentication',
    ]
}

```

### 25.3修改`authentications.py`

```python 
class UserTokenAuthmentication(BaseAuthentication):
    def authenticate(self, request):
        return request._request.user,request._request.auth
```

### 25.4修改路由

在主路由下添加

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('admin/', admin.site.urls),  # 注释掉这行
    path('auth/', include('apps.oaauth.urls')),
]

```

在apps路由下添加

```python
from django.urls import path
from . import  views

app_name = 'oaauth'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('resetpassword', views.RestPasswordView.as_view(), name='resetpassword'),  # 修改这里
]
```

## 26.修改密码功能后端实现

### 26.1定义密码序列化

```python
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
```

### 26.2视图实现

```python
class ResetPasswordView(APIView):  
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data,context={'request':request})
        if serializer.is_valid(): 
            newpwd = serializer.validated_data.get('newpwd')
            request.user.set_password(newpwd)
            request.user.save()
            return Response()
        else:
            print(serializer.errors)
            detail = list(serializer.errors.values())[0][0]  
            return Response({'detail': detail}, status=status.HTTP_400_BAD_REQUEST)

```

### 26.3测试

![image-20250731112949518](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250731112949518.png)

![image-20250731112959344](C:\Users\ArT\AppData\Roaming\Typora\typora-user-images\image-20250731112959344.png)

## 27.修改密码对话框实现

修改`frame.vue`文件

```vue
<script setup name="frame">
import { ref, computed, reactive } from 'vue'
import {
    Expand,
    Fold,
} from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

let dialogVisible = ref(false);
let resetPwdForm = reactive({
    oldpwd: '',
    newpwd: '',
    newpwd1: '',
});

let resetPwdFormRef = ref(null);

let formLabelWidth = ref('100px');

let rules = reactive({
    oldpwd: [
        { required: true, message: '请输入旧密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度必须在6到20位之间', trigger: 'blur' },
    ],
    newpwd: [
        { required: true, message: '请输入新密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度必须在6到20位之间', trigger: 'blur' },
    ],
    newpwd1: [
        { required: true, message: '请确认新密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度必须在6到20位之间', trigger: 'blur' },
    ],
})

let isCollapse = ref(false);
let asidWidth = computed(() => {
    if (isCollapse.value) {
        return '64px'
    } else {
        return '250px'
    }
})

const onCollapseAside = () => {
    isCollapse.value = !isCollapse.value;
}

const onExit = () => {
    authStore.clearUerToken();
    router.push({ name: 'login' });
}

const onContorlResetPwdDialog = () => {
    resetPwdForm.oldpwd = '';
    resetPwdForm.newpwd = '';
    resetPwdForm.newpwd1 = '';
    dialogVisible.value = true;
}

const onSubmit = () => {
    resetPwdFormRef.value.validate((valid,fields) => {
        if (valid) {
            console.log('字段校验成功!');
        } else {
            console.log('字段校验失败!');
        }
        console.log(fields);
    })
    console.log('点击了提交');
    

}
</script>

<template>
    <el-container class="container">
        <el-aside class="aside" :width="asidWidth">
            <router-link to="/" class="brand">
                <strong>Hiiaen</strong>
                <transition name="fade">
                    <span v-show="!isCollapse" class="brand-text">OA</span>
                </transition>
            </router-link>
            <el-menu default-active="1" class="el-menu-vertical-demo" background-color="#343a40" text-color="#fff"
                :collapse="isCollapse" :collapse-transition="false">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">
                <div class="header-left">
                    <el-button class="collapse-btn" :icon="isCollapse ? Expand : Fold" @click="onCollapseAside" />
                </div>
                <el-dropdown>
                    <span class="el-dropdown-link">
                        <el-avatar :size="30" icon="UserFilled" />
                        <span style="margin-left: 4px;">[{{ authStore.user.department.name
                        }}]{{ authStore.user.realname }}</span>
                        <el-icon class="el-icon--right">
                            <arrow-down />
                        </el-icon>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item @click="onContorlResetPwdDialog">修改密码</el-dropdown-item>
                            <el-dropdown-item divided @click="onExit">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
    <el-dialog v-model="dialogVisible" title="修改密码" width="500">

        <el-form :model="resetPwdForm" :rules="rules" ref="resetPwdFormRef">
            <el-form-item label="旧密码" :label-width="formLabelWidth" prop="oldpwd">
                <el-input v-model="resetPwdForm.oldpwd" autocomplete="off" type="password" />
            </el-form-item>
            <el-form-item label="新密码" :label-width="formLabelWidth" prop="newpwd">
                <el-input v-model="resetPwdForm.newpwd" autocomplete="off" type="password" />           
            </el-form-item>
            <el-form-item label="确认密码" :label-width="formLabelWidth" prop="newpwd1">
                <el-input v-model="resetPwdForm.newpwd1" autocomplete="off" type="password" />
            </el-form-item>

        </el-form>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="onSubmit">
                    确认
                </el-button>
            </div>
        </template>
    </el-dialog>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
    transition: width 0.3s ease-in-out;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    white-space: nowrap;
}

.brand-text {
    margin-left: 4px;
}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.header-left {
    display: flex;
    align-items: center;

}

.el-dropdown-link {
    display: flex;
    align-items: center;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
    transition: all 0.3s ease;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}

.collapse-btn {
    font-size: 18px;
    border: none;
    background: transparent;
    color: #606266;
    cursor: pointer;
    transition: all 0.3s ease;
}

.collapse-btn:hover {
    color: #409eff;
    transform: scale(1.1);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

```

## 29.修改密码前端实现

### 29.1修改`frame.vue`文件

```vue
<script setup name="frame">
import { ref, computed, reactive } from 'vue'
import {
    Expand,
    Fold,
} from '@element-plus/icons-vue'
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';
import authHttp from '@/api/authHttp';
import { ElMessage } from 'element-plus';

const authStore = useAuthStore();
const router = useRouter();

let dialogVisible = ref(false);
let resetPwdForm = reactive({
    oldpwd: '',
    newpwd: '',
    newpwd2: '',
});

let resetPwdFormRef = ref(null);

let formLabelWidth = ref('100px');

let rules = reactive({
    oldpwd: [
        { required: true, message: '请输入旧密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度必须在6到20位之间', trigger: 'blur' },
    ],
    newpwd: [
        { required: true, message: '请输入新密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度必须在6到20位之间', trigger: 'blur' },
    ],
    newpwd2: [
        { required: true, message: '请确认新密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度必须在6到20位之间', trigger: 'blur' },
    ],
})

let isCollapse = ref(false);
let asidWidth = computed(() => {
    if (isCollapse.value) {
        return '64px'
    } else {
        return '250px'
    }
})

const onCollapseAside = () => {
    isCollapse.value = !isCollapse.value;
}

const onExit = () => {
    authStore.clearUerToken();
    router.push({ name: 'login' });
}

const onContorlResetPwdDialog = () => {
    resetPwdForm.oldpwd = '';
    resetPwdForm.newpwd = '';
    resetPwdForm.newpwd2 = '';
    dialogVisible.value = true;
}

const onSubmit = () => {
    resetPwdFormRef.value.validate(async (valid,fields) => {
        if (valid) {
            try{
                await authHttp.resetPwd(resetPwdForm.oldpwd,resetPwdForm.newpwd,resetPwdForm.newpwd2);
                ElMessage.success('密码修改成功');
                dialogVisible.value = false;
            }catch(detial){
                ElMessage.error(detial);    
            }
        } else {
            ElMessage.info('请按要求填写字段');
        }
        console.log(fields);
    })
}
</script>

<template>
    <el-container class="container">
        <el-aside class="aside" :width="asidWidth">
            <router-link to="/" class="brand">
                <strong>Hiiaen</strong>
                <transition name="fade">
                    <span v-show="!isCollapse" class="brand-text">OA</span>
                </transition>
            </router-link>
            <el-menu default-active="1" class="el-menu-vertical-demo" background-color="#343a40" text-color="#fff"
                :collapse="isCollapse" :collapse-transition="false">
                <el-menu-item index="1">
                    <el-icon>
                        <HomeFilled />
                    </el-icon>
                    <span>首页</span>
                </el-menu-item>
                <el-sub-menu index="2">
                    <template #title>
                        <el-icon>
                            <Checked />
                        </el-icon>
                        <span>考勤管理</span>
                    </template>
                    <el-menu-item index="2-1">
                        <el-icon>
                            <UserFilled />
                        </el-icon>
                        <span>个人考勤</span>
                    </el-menu-item>
                    <el-menu-item index="2-2">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>下属考勤</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="3">
                    <template #title>
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>通知管理</span>
                    </template>
                    <el-menu-item index="3-1">
                        <el-icon>
                            <BellFilled />
                        </el-icon>
                        <span>发布通知</span>
                    </el-menu-item>
                    <el-menu-item index="3-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>通知列表</span>
                    </el-menu-item>
                </el-sub-menu>
                <el-sub-menu index="4">
                    <template #title>
                        <el-icon>
                            <Avatar />
                        </el-icon>
                        <span>员工管理</span>
                    </template>
                    <el-menu-item index="4-1">
                        <el-icon>
                            <Plus />
                        </el-icon>
                        <span>新增员工</span>
                    </el-menu-item>
                    <el-menu-item index="4-2">
                        <el-icon>
                            <Tickets />
                        </el-icon>
                        <span>员工列表</span>
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-container>
            <el-header class="header">
                <div class="header-left">
                    <el-button class="collapse-btn" :icon="isCollapse ? Expand : Fold" @click="onCollapseAside" />
                </div>
                <el-dropdown>
                    <span class="el-dropdown-link">
                        <el-avatar :size="30" icon="UserFilled" />
                        <span style="margin-left: 4px;">[{{ authStore.user.department.name
                        }}]{{ authStore.user.realname }}</span>
                        <el-icon class="el-icon--right">
                            <arrow-down />
                        </el-icon>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item @click="onContorlResetPwdDialog">修改密码</el-dropdown-item>
                            <el-dropdown-item divided @click="onExit">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </el-header>
            <el-main class="main">Main</el-main>
        </el-container>
    </el-container>
    <el-dialog v-model="dialogVisible" title="修改密码" width="500">

        <el-form :model="resetPwdForm" :rules="rules" ref="resetPwdFormRef">
            <el-form-item label="旧密码" :label-width="formLabelWidth" prop="oldpwd">
                <el-input v-model="resetPwdForm.oldpwd" autocomplete="off" type="password" />
            </el-form-item>
            <el-form-item label="新密码" :label-width="formLabelWidth" prop="newpwd">
                <el-input v-model="resetPwdForm.newpwd" autocomplete="off" type="password" />           
            </el-form-item>
            <el-form-item label="确认密码" :label-width="formLabelWidth" prop="newpwd2">
                <el-input v-model="resetPwdForm.newpwd2" autocomplete="off" type="password" />
            </el-form-item>

        </el-form>
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="onSubmit">
                    确认
                </el-button>
            </div>
        </template>
    </el-dialog>
</template>

<style scoped>
.aside {
    background-color: #343a40;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22) !important;
    transition: width 0.3s ease-in-out;
}

.container {
    height: 100vh;
    background-color: #f4f6f9;
}

.aside .brand {
    color: #fff;
    text-decoration: none;
    border-bottom: 1px solid #434a50;
    background-color: #232631;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    white-space: nowrap;
}

.brand-text {
    margin-left: 4px;
}

.header {
    height: 60px;
    background-color: #fff;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-between;
    align-items: center;

}

.header-left {
    display: flex;
    align-items: center;

}

.el-dropdown-link {
    display: flex;
    align-items: center;
}

.el-menu {
    border-right: none;
}

.el-menu-item,
.el-sub-menu__title {
    color: #fff !important;
    transition: all 0.3s ease;
}

.el-menu-item:hover,
.el-sub-menu__title:hover {
    background-color: #364781 !important;
}

.collapse-btn {
    font-size: 18px;
    border: none;
    background: transparent;
    color: #606266;
    cursor: pointer;
    transition: all 0.3s ease;
}

.collapse-btn:hover {
    color: #409eff;
    transform: scale(1.1);
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>

```

### 29.2修改`http.js`文件

```js
this.instance.interceptors.request.use((config) => {
            const authStore = useAuthStore();
            const token = authStore.token;
            if(token){
                config.headers['Authorization'] = 'JWT ' + token;
            }
            return config;
        })
```

### 29.3修改`authHttp.js`文件

```js
import http from './http';

const login = (email,password) =>{
    const path = '/auth/login';
    return http.post(path,{email,password});
}

const resetPwd = (oldpwd,newpwd,newpwd2) => {
    const path = '/auth/resetpassword';
    return http.post(path,{oldpwd,newpwd,newpwd2});
}

export default {
    login,
    resetPwd
}
```

## 30.考勤相关模型创建

### 30.1创建考勤app

```bash
python manager.py startapp absent
```

### 30.2修改app路径

在`absent`下修改`apps.py`

```python
from django.apps import AppConfig


class AbsentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.absent'  # 修改为完整的应用路径

```

### 30.3注册考勤app

在`settings.py`中注册

```python
INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    # 安装rest_framework
    'rest_framework',
    # 安装django-cors-headers
    'corsheaders',
    # 安装项目的app
    'apps.oaauth',
    'apps.absent'
]
```

### 30.4考勤模型

```python

from django.db import models
from django.contrib.auth import get_user_model  # 修正导入方式

OAUser = get_user_model()

class AbsentStatusChoices(models.IntegerChoices):
    # 审批中
    AUDITING = 1
    # 通过
    PASS = 2
    # 审核拒绝
    REJECT = 3


class AbsentType(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    
    
class Absent(models.Model):  # 修正拼写错误
    # 1. 标题
    title = models.CharField(max_length = 200)
    # 2. 请假详细内容
    request_content = models.TextField()
    # 3. 请假类型(事假，婚假)
    absent_type = models.ForeignKey(AbsentType, on_delete=models.CASCADE, related_name='absents', related_query_name='absents')
    # 4. 发起人
    requester = models.ForeignKey(OAUser, on_delete=models.CASCADE, related_name='my_absents', related_query_name='my_absents')  # 修正外键引用和字段名
    # 5. 审批人（可以为空）
    responder = models.ForeignKey(OAUser, on_delete=models.CASCADE, related_name='sub_absents', related_query_name='sub_absents', null=True)  # 修正外键引用
    # 6. 状态
    status = models.IntegerField(choices=AbsentStatusChoices.choices, default=AbsentStatusChoices.AUDITING)
    # 7. 请假开始日期
    start_date = models.DateField()
    # 8. 请假结束日期
    end_date = models.DateField()
    # 9. 请假发起时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 10.审批回复内容
    responder_content = models.TextField()
```

30.5生成迁移文件，完成迁移

```bash
python manager.py makemigrations
python manager.py migrate
```

## 31.考勤视图集和序列化(1)

### 31.1处理考勤请假相关的API接口

```python
from django.shortcuts import render
from rest_framework import viewsets
from .models import Absent, AbsentType, AbsentStatusChoices
from rest_framework import mixins,generics
# Create your views here.
"""
    1. 发起考勤(create)
    2. 处理考勤(update)
    3. 查看自己的考勤列表(list?who=my)
    4. 查看下属的考勤列表(list?who=sub
    
"""

class AbsenttViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Absent.objects.all()
    serializer_class = None

```

### 31.2创建`serializers.py`文件，处理数据的序列化和反序列化

```python
from rest_framework import serializers
from .models import Absent, AbsentType, AbsentStatusChoices
from apps.oaauth.serializers import UserSerializer

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
        
    
    # create
    def create(self, validated_data):
        pass
    
    
    # update
    def update(self, instance, validated_data):
        pass
```

### 31.3创建`urls.py`定义考勤模块的API路由

```python
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'absent'

router = DefaultRouter()
router.register(r'absent',views.AbsnetViewSet, basename='absent')

urlpatterns = [] + router.urls
```

## 32.考勤视图集和序列化(2)

### 32.1完善`serializers.py`逻辑

```python
from rest_framework import serializers
from .models import Absent, AbsentType, AbsentStatusChoices
from apps.oaauth.serializers import UserSerializer
from rest_framework import exceptions

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
            raise exceptions.ValidationError(detial='请假类型不存在！')
        return value
        
    
    # create
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        # 获取审批者
        # 1.如果是部门leader
        if user.department.leader.uid == user.uid:
            # 1.1 如果是董事会
            if  user.department.name == '董事会':
                responder = None
            else:
                responder = user.department.manager
        
        
        # 2. 如果不是部门leader
        else:
            responder = user.department.leader
            
        # 如果是董事会的leader，请假就直接通过
        if responder is None:
            validated_data['status'] = AbsentStatusChoices.PASS
        return Absent.objects.create(**validated_data, request = user, responder = responder)
    
    
    # update
    def update(self, instance, validated_data):
        if instance.status != AbsentStatusChoices.AUDITING:
            raise exceptions.ValidationError(detial='不能修改已经确定的请假数据！')
        request = self.context['request']
        user = request.user
        if instance.responder.uid != user.uid:
            raise exceptions.ValidationError(detial='您无权处理该考勤！')
        instance.status = validated_data['status']
        instance.responder_content = validated_data['responder_content']
        instance.save()
        return instance
```

### 32.2完善`views.py`

```python
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

class AbsenttViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Absent.objects.all()
    serializer_class = AbsentSerializer

```



## 33.考勤视图集和序列化(3) - 初始化考勤类型

在`absent`下创建`management`python包，再在`management`下创建`commands`python包，在该包下创建`initabsenttype.py`

```python
from django.core.management.base import BaseCommand
from apps.absent.models import AbsentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        absent_types = ["事假", "病假", "工伤假", "婚假", "丧假", "产假", "探亲假", "公假", "年休假"]
        absents = []
        for absent_type in absent_types:
            absents.append(AbsentType(name=absent_type))

        AbsentType.objects.bulk_create(absents)
        self.stdout.write("考勤类型数据初始化成功！")
```

在终端下执行`python manage.py initabsenttype`



