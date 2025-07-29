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
