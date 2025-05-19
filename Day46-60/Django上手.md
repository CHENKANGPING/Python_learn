# Django快速上手

## 术语解释

1. URL/URI ： 统一资源定位符/统一资源标识符，网络资源的唯一标识

2. 域名 ： 与Web服务器地址对应的一个易于记忆的字符串名字

3. DNS ： 域名解析服务， 可以域名转换为对应的IP地址

4. IP地址 ： 网络上的主机的身份标识， 通过IP地址可以区分不同的主机

5. HTTP ： 超文本传输协议， 构建在TCP之上的应用级协议，万维网数据通信的基础

6. 反向代理 ： 代理客户端向服务器发出请求，然后将服务器返回的资源返回给客户端

7. Web服务器 ： 接受HTTP请求， 然后返回HTML文件、纯文本文件、图像等资源给请求者看

8. Nginx ： 高性能的Web服务器，也可以用作反向代理，负载均衡和HTTP缓存


## 第一个Django项目

安装Django环境

```Shell
pip install Django
```

检查Django环境并使用`django-admin`命令创建Django项目

```Shell
django-admin --version
django-admin startproject hellodjango
```

Django项目文件夹其中包括了`__init__py`、`settings.py`、`urls.py`、`wsgi.py`、`asgi.py`五个文件，还有一个于`hellodjango`同级的名为`manage.py`的文件

这些文件的作用如下

1. `hellodjango/__init__.py` : 空文件，告诉Python解释器这个目录应该被视为一个python包

2. `hellodjango/setting.py` : Django项目的配置文件

3. `hellodjango/urls.py` : Django项目的URL映射声明，就像是网站的“目录”

4. `hellodjango/wsgi.py` : 项目运行在WSGI兼容Web服务器上的入口文件

5. `hellodjangp/asgi.py` :  Django项目能够以异步方式运行，支持异步视图和 WebSockets等功能.

6. `manag.py` : 管理Django项目的脚本程序

终端中通过命令运行项目

```Shell
python manage.py runsever
```

修改项目的配置文件`settings.py`

```Python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Chongqing'
```

## 创建自己的应用

如果要开发自己的Web应用，需要在Django项目中创建“应用”，一个Django项目可以包含一个或多个应用。

1.创建名为`first`的应用

```Shell
python manage.py startapp first
```

执行上面的命令会在当前路径下创建`first`目录，结构如下：

- `___init__.py` : 一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。

- `admin.py` : 可以用来注册模型，用于在Django框架自带的管理后台中管理模型。

- `apps.py` : 当前应用的配置文件。

- `migrations` : 存放与模型有关的数据库迁移信息。

    - `__init__.py` : 一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。

- `models.py` : 存放应用的数据模型(MTV中的M)。

- `test.py` : 包含测试应用各项功能的测试类和测试函数。

- `views.py` : 处理用户HTTP请求并返回HTTP响应的函数或类(MTV中的V).

2.修改应用下的视图文件`views.py`。

```Python
from django.http import HttpResponse

def show_index(request):
    return HttpResponse('<h1>Hello, Django!</h1>')
```

3.修改Django项目目录下的`urls.py`文件，将视图函数和用户在浏览器中请求的路径对应。

```Python
from django.contrib import admin
from django.urls import path, include

from first.views import show_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', show_index),
]
```

4.重新运行项目。

5.修改`views.py`文件添加如下代码。

```Python
from random import sample
from django.http import HttpResponse

def show_index(request):
    fruits  = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    content = '<h3>今天推荐的水果是：</h3>'
    content +='<hr>'
    content +='<ul>'
    for fruit in selected_fruits:
        content += f'<li>{fruit}</li>'
    content += '</ul>'
    return HttpResponse(content)
```

6.刷新页面查看程序运行结果，每次刷新网页内容不一样。


## 使用模板

上面的通过拼接HTML代码的方式，生成页面在实际开发中是无法接受的，为了解决这个问题，我们可以提前准备一个模板页(MTV中的T)，所谓模板就是一个带有占位符和模板指令的HTML页面。

Django框架中与一个名为`render`的便捷函数，可以来完成渲染模板的操作。

使用模板页的步骤如下：

1.在项目目录下创建名为templates的文件架。

2.添加模板页`index_html`

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>首页</title>
        <style>
            #fruits {
                font-size: 1.25em;
            }
        </style>
    </head>
    <body>
        <h1>今天推荐的水果是：</h1>
        <hr>
        <ul id="fruits">
            {% for fruit in fruits %}
            <li>{{ fruit }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

3.修改`views.py`文件，调用`render`函数模板渲染页

```Python
from random import sample

from django.shortcuts import render


def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})
```

`render`函数

第一个参数是请求对象request。

第二个参数是我们要渲染的模板页的名字。

第三个参数是要渲染到页面上的数据，我们通过一个字典将数据交给模板页，字典中的键就是模板页中使用的模板指令或占位符中的变量名。

4.到此为止，视图函数中的`render`还无法找到模板文件`index.html`，需要修改`settings.py`文件，配置模板文件所在的路径，修改`settings.py`文件，找到`TEMPLATES`配置，修改其中`DIRS`配置。

```Python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```