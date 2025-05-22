## 静态资源和Ajax请求

### 加载静态资源

如果要在Django项目中使用静态资源，可以先创建一个用于保存静态资源的目录。
在vote项目中，我们将静态资源放置于`static`的文件架中，在该文件夹中包含三个
子文件夹：`css`、`js`和`images`。

为了能够找到保存静态资源的文件夹，修改`settings.py`。

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

### Ajax概述

接下来就可以实现“好评”和“差评”的功能了，很明显如果能够在不刷新页面的情况下实现这两个功能会带来更好的用户体验，因此我们考虑使用Ajax技术来实现“好评”和“差评”。Ajax是Asynchronous Javascript And XML的缩写 , 简单的说，使用Ajax技术可以在不重新加载整个页面的情况下对页面进行局部刷新。

对于传统的Web应用，每次页面上需要加载新的内容都需要重新请求服务器并刷新整个页面，如果服务器短时间内无法给予响应或者网络状况并不理想，那么可能会造成浏览器长时间的空白并使得用户处于等待状态，在这个期间用户什么都做不了，如下图所示。很显然，这样的Web应用并不能带来很好的用户体验。

对于使用Ajax技术的Web应用，浏览器可以向服务器发起异步请求来获取数据。异步请求不会中断用户体验，当服务器返回了新的数据，我们可以通过JavaScript代码进行DOM操作来实现对页面的局部刷新，这样就相当于在不刷新整个页面的情况下更新了页面的内容。

使用Ajax技术时，浏览器根据服务通常会交换XML或JSON格式的数据

XML时以前使用得非常多得一种数据格式，近年来几乎被JSON替代

格式对比

XML格式：
```xml
<?xml version="1.0" encoding="utf-8"?>
<message>
	<from>Alice</from>
    <to>Bob</to>
    <content>Dinner is on me!</content>
</message>
```

JSON格式：
```json
{
    "from": "Alice",
    "to": "Bob",
    "content": "Dinner is on me!"
}
```

### 用Ajax实现投票功能

下面我们实现投票功能，首先修改`urls.py`文件，为“好评”和“差评”功能映射对于得URL。

```python
from django.http import JsonResponse

from django.contrib import admin
from django.urls import path
from vote import views

from polls.views import  show_subjects, show_teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_subjects),
    path('teachers/', views.show_teachers, name='teachers'),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
]

def praise_or_criticize(request):
    """好评"""
    try:
        tno = int(request.GET('tno'))
        teacher = Teacher.objects.get(tno=tno)
        if request.path.startswith('/praise'):
            teacher.good_count += 1
            count = teacher.good_count
        else:
            teacher.bad_count += 1
            count = teacher.bad_count
        teacher.save()
        deta = {
            'code' : 20000,
            'mesg' : '操作成功',
            'count' : count
        }
    except (ValueError, Teacher.DoesNotExist):
        deta = {
            'code' : 20001,
            'mesg' : '操作失败',
        }
    return JsonResponse(deta)
```
修改老师模板页，映入jQuery库来实现事件处理、Ajax请求、DOM操作。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>老师信息</title>
    <style>
        #container {
            width: 80%;
            margin: 10px auto;
        }
        .teacher {
            width: 100%;
            margin: 0 auto;
            padding: 10px 0;
            border-bottom: 1px dashed gray;
            overflow: auto;
        }
        .teacher>div {
            float: left;
        }
        .photo {
            height: 140px;
            border-radius: 75px;
            overflow: hidden;
            margin-left: 20px;
        }
        .info {
            width: 75%;
            margin-left: 30px;
        }
        .info div {
            clear: both;
            margin: 5px 10px;
        }
        .info span {
            margin-right: 25px;
        }
        .info a {
            text-decoration: none;
            color: darkcyan;
        }
    </style>
</head>
<body>
    <div id="container">
        <h1>{{ subject.name }}学科的老师信息</h1>
        <hr>
        {% if not teachers %}
            <h2>暂无该学科老师信息</h2>
        {% endif %}
        {% for teacher in teachers %}
        <div class="teacher">
            <div class="photo">
                <img src="/static/images/{{ teacher.photo }}" height="140" alt="">
            </div>
            <div class="info">
                <div>
                    <span><strong>姓名：{{ teacher.name }}</strong></span>
                    <span>性别：{{ teacher.sex | yesno:'男,女' }}</span>
                    <span>出生日期：{{ teacher.birth }}</span>
                </div>
                <div class="intro">{{ teacher.intro }}</div>
                <div class="comment">
                    <a href="/praise/?tno={{ teacher.no }}">好评</a>&nbsp;&nbsp;
                    (<strong>{{ teacher.good_count }}</strong>)
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <a href="/criticize/?tno={{ teacher.no }}">差评</a>&nbsp;&nbsp;
                    (<strong>{{ teacher.bad_count }}</strong>)
                </div>
            </div>
        </div>
        {% endfor %}
        <a href="/">返回首页</a>
    </div>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
    <script>
        $(() => {
            $('.comment>a').on('click', (evt) => {
                evt.preventDefault()
                let url = $(evt.target).attr('href')
                $.getJSON(url, (json) => {
                    if (json.code == 20000) {
                        $(evt.target).next().text(json.count)
                    } else {
                        alert(json.mesg)
                    }
                })
            })
        })
    </script>
</body>
</html>
```
### 小结
到此为止，这个投票项目的功能已经完成，下一章会要求用户登录才能能进行投票，
没有账号的用户需要注册一个账号才能进行投票。
























