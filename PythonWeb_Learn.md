# PythonWeb

##  前端开发

```python
目的: 开发一个平台
	- 前端开发: HTML CSS JavaScript
	- 接收请求并处理
	- Mysql数据库: 存储数据

快速上手: 
	基于Flask Web框架快速搭建一个网站
深入学习:
	基于Django框架
```

### 1.快速开发网站

python 安装 Flask web 框架

```python
pip install flask
```

> 创建Flask的python目录

```shell
[root@hecs-33592 ~]# mkdir -p /root/python/FlaskWeb
[root@hecs-33592 ~]# cd /root/python/FlaskWeb
[root@hecs-33592 FlaskWeb]# pwd
/root/python/FlaskWeb
```

创建一个名为`web.py`的python文件

```python
from flask import Flask

app = Flask(__name__)

## 创建了网址 /show/info 和 函数index 的对应关系
## 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    return "中国联通"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)  
123456789101112
```

运行

```shell
[root@hecs-33592 ~]# /usr/bin/python3 /root/python/FlaskWeb/web.py
1
```

![run_flask_web](https://img-blog.csdnimg.cn/1a49d8bb6e81442da6b148bae8f13c61.png)
浏览器进行访问: http://[你的ip]:5100/show/info
![web1](https://img-blog.csdnimg.cn/3fcab5cb79fd4f39b3bc0f8a4323656d.png)

> 这种 return 方式返回 HTML 内容的方式不方便进行管理,因此我们会引入`templates`模板

```python
from flask import Flask, render_template

app = Flask(__name__)

## 创建了网址 /show/info 和 函数index 的对应关系
## 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    # 默认去当前目录的 templates 文件夹中找
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)
12345678910111213
```

创建`templates`目录

```shell
mkdir /root/python/FlaskWeb/templates/
1
```

![img](https://img-blog.csdnimg.cn/4891720ee2d549429c84a1c62c00701b.png)
编写`index.html`文件
![在这里插入图片描述](https://img-blog.csdnimg.cn/536ac80188d2446aa4692418dc6259b5.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>中国联通</h1>
</body>
</html>
123456789101112
```

重新运行Flask,浏览器刷新访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/f3647614c5684d03815d5a219d617293.png)

> 当然这个`templates`目录也可以自定义名称

```python
## 例如目录名称为"xxx"
app = Flask(__name__, template_folder="xxx")
```

### 2.标签

#### 2.1 编码

```html
<meta charset="UTF-8">
```

#### 2.2 title

```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
```

#### 2.3 标题

```html
<body>
    <h1>一级标题</h1>
    <h2>二级标题</h1>
    <h3>三级标题</h1>
    <h4>四级标题</h1>
    <h5>五级标题</h1>
</body>
```

#### 2.4 div和span



+

```html
<div>内容</div>

<span>asd</span>
```

- div: 占一整行(块级标签)
- span: 用多少占多少(行内标签/内联标签)
  - 两个 span 标签不在同一行,页面显示时会在同一行,中间以一个空格分隔
  - 两个 span 标签在同一行,页面显示时会在同一行,中间没有空格,连着

#### 2.5 超链接

> 这里就很有意思了,你可以选择跳转自己网站的地址,或者跳转外部的网站

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的联通</title>
</head>
<body>
    <a href="/get/news">点击跳转自己的网站</a></br>
    <a href="http://www.baidu.com">点击跳转别人的网站百度</a>
</body>
</html>
```

然后需要修改`web.py`文件

```python
from flask import Flask, render_template

app = Flask(__name__)

## 创建了网址 /show/info 和 函数index 的对应关系
## 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    # 默认去当前目录的 templates 文件夹中找
    return render_template("index.html")

## 新添加如下配置
@app.route("/get/news")
def get_news():
    # 默认去当前目录的 templates 文件夹中找
    return render_template("get_news.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)
```

在`templates`目录下新添加一个 `get_news.html` 文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>我是内部链接</h1>
</body>
</html>
```

重新运行Flask,刷新页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/c34740381d574cf1953aef30e7418e3a.png)
点击第一行后,跳转到如下页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/5a40f7323f314537a75a8b6ff14e2bdc.png)点击点击第二行后,跳转到百度

> 自行脑补百度页面哈

**在新的 Tab 标签页打开链接**

> 添加 target=“_blank”

```html
<body>
    <a href="https://www.mi.com/shop/buy/detail?product_id=16642" target="_blank">
        <img src="https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210262033_ef39fca0e37395d07682124770fd3ad9.png" style="width: 150px;"/>
    </a>
</body>
```

#### 2.6 图片

```html
<body>
    <h1>我是内部链接</h1>
    <img src="https://t7.baidu.com/it/u=848096684,3883475370&fm=193&f=GIF"/>
</body>
1234
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/998fb4c3564047f1810c2a804741e58d.png)
刷新浏览器
![在这里插入图片描述](https://img-blog.csdnimg.cn/661a1a93c39e428688b725ab76ff6312.png)

> 尝试访问服务器本地图片

在`/root/python/FlaskWeb/`下新建目录`static`
放入一张图片`dog.jpg`
![在这里插入图片描述](https://img-blog.csdnimg.cn/03c0cd62cc3e42ecb78492516f5a20a5.png)
修改`get_news.html`

```html
<body>
    <h1>我是内部链接</h1>
    <img src="/static/dog.jpg"/>
</body>
```

刷新浏览器
![在这里插入图片描述](https://img-blog.csdnimg.cn/fc3782da6df3409c85645b6ed729cd0a.png)

> 跟刚才一样

然后可以调整一下图片的高度与宽度

```html
<body>
    <h1>我是内部链接</h1>
    <img style="height: 100px; width: 200px;" src="/static/dog.jpg"/>
</body>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/9b2d9ce6d60d4e3ebd81bd4c784d20f0.png)

#### 小结

```html
- 块级标签
	- <h1></h1>
	- <div></div>

- 行内标签
	- <span></span>
	- <a></a>
	- <img />
```

#### 标签的嵌套

> 实现: 点击图片,跳转至指定页面

修改`web.py`,增加`get_product`

```python
from flask import Flask, render_template

app = Flask(__name__)

## 创建了网址 /show/info 和 函数index 的对应关系
## 以后用户在浏览器上访问 /show/info, 网站自动执行
@app.route("/show/info")
def index():
    # 默认去当前目录的 templates 文件夹中找
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("get_news.html")

@app.route("/get/product")
def get_product():
    return render_template("get_product.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)
```

在`templates`下新增一个`get_product.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="https://www.mi.com/shop/buy/detail?product_id=16642">
        <img src="https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210262033_ef39fca0e37395d07682124770fd3ad9.png" style="width: 150px;"/>
    </a>
</body>
</html>
```

访问页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/9434889dbf594e6597c3f317ca2f8187.png)
点击图片进行url跳转
![在这里插入图片描述](https://img-blog.csdnimg.cn/9a71d037eafc471785a9d3fb20c1cf45.png)

#### 2.7 列表

> 无序列表

```html
<ul>
	<li>中国移动</li>
	<li>中国联通</li>
	<li>中国电信</li>
</ul>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/615d4e3f906e4e1c8cad7156dd984f02.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/9286744c9e454d2f9fab6b88f00578bf.png)

> 有序列表

```html
<ol>
	<li>中国移动</li>
	<li>中国联通</li>
	<li>中国电信</li>
</ol>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/06288806f3c84d5284f19249f6b89609.png)

#### 2.8 表格

修改`web.py`新增一个访问路径

```python
@app.route("/get/table")
def get_table():
    return render_template("get_table.html")
123
```

在`templates`页面下新建`get_table.html`文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table>
        <thead>
            <tr><th>ID</th><th>姓名</th><th>年龄</th></tr>
        </thead>
        <tbody>
            <tr><td>10</td><td>张三</td><td>20</td></tr>
            <tr><td>11</td><td>李四</td><td>20</td></tr>
            <tr><td>12</td><td>王五</td><td>20</td></tr>
            <tr><td>13</td><td>赵六</td><td>20</td></tr>
        </tbody>
    </table>
</body>
</html>
```

重新运行并访问页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/b36e6a1a2b2e48a1af28aa1441eab6c3.png)

> 为表格增加边框

```html
<table border="1">
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0cb315152f924b8889cfc79475140aa5.png)

#### 2.9 input系列

```html
<!-- 文本与密码 -->
<input type="text" />
<input type="password" />

<!-- 选择文件 -->
<input type="file" />

<!-- 单选框 -->
<input type="radio" name="n1" />男
<input type="radio" name="n1" />女

<!-- 复选框 -->
<input type="checkbox" />唱
<input type="checkbox" />跳
<input type="checkbox" />Rap
<input type="checkbox" />篮球

<!-- 按钮 -->
<input type="button" value="提交"/>	普通按钮
<input type="submit" value="提交"/>	提交表单
1234567891011121314151617181920
```

#### 2.10 下拉框

```html
<select>
	<option>北京</option>
	<option>上海</option>
	<option>深圳</option>
</select>
```

#### 2.11 多行文本

```html
<textarea></textarea>
```

#### 用户注册

修改`web.py`

```python
@app.route("/register")
def register():
    return render_template("login.html")
```

在`templates`下新建`register.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>用户注册</h1>
    <div>
        用户名: <input type="text" />
    </div>
    <div>
        密码: <input type="password" />
    </div>
    <div>
        性别: <input type="radio" name="sex"/>男 <input type="radio" name="sex"/>女
    </div>
    <div>
        爱好:
        <input type="checkbox">唱
        <input type="checkbox">跳
        <input type="checkbox">Rap
        <input type="checkbox">篮球
    </div>
    <div>
        城市:
        <select>
            <option>北京</option>
            <option>上海</option>
            <option>深圳</option>
        </select>
    </div>
    <div>
        备注: <textarea cols="30" rows="10"></textarea>
    </div>
    <div>
        <input type="button" value="button提交">
        <input type="submit" value="submit提交">
    </div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/df2c248e81964b2980f7dbc484ad5edc.png)

> 顺便说一下 GET 方法与 POST 方法的区别
> GET: 可通过`URL/表单`提交
> POST: 只能通过`表单`提交,提交数据不在URL而是在`请求体`中

#### 案例: 用户注册

新建项目
在`/root/python`下新建目录:

- `account`
- `template`

在`account`下新建`app.py`文件

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=False)
```

在`templates`下新建`register.html`文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>用户注册</h1>
</body>
</html>
12345678910111
```

运行,浏览器进行访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/ec3ac4605d9c48299196ea2432991386.png)

表单可以提交的前提条件:

- 提交方式: method=“get”
- 提交地址: action=“/xxx/xxx/xxx”
- 在`form`标签里面必须有一个`submit`标签
- 每个标签有`name`属性

接下来尝试接收用户提交的表单数据

##### GET 方式

修改`app.py`,导入`request`方法,使用`/do/register`接收用户数据并展示

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET'])
def register():
    return render_template('login.html')

@app.route("/do/register", methods=['GET'])
def do_register():
    get_info = request.args
    return get_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
123456789101112131415
```

修改`templates`下的`register.html`

> 点击注册后跳转至路由`/do/register`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>用户注册</h1>
    <form action="/do/register" method="get">
        <div>
            用户名: <input type="text" name="username">
        </div>
        <div>
            密码: <input type="password" name="passwd">
        </div>
        
        <input type="submit" value="提交">
    </form>
</body>
</html>
12345678910111213141516171819202122
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/22f219eafd7644d097947e7139cc2fbb.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/95c694157df34ffbb78d656f928ee9e0.png)

##### POST 方式

修改`app.py`

```python
@app.route("/post/register", methods=['POST'])
def post_register():
    get_info = request.form
    return get_info
1234
```

修改`register.html`

> ```
> <form action="/post/register" method="post">
> ```

```html
<body>
    <h1>用户注册</h1>
    <form action="/post/register" method="post">
        <div>
            用户名: <input type="text" name="username">
        </div>
        <div>
            密码: <input type="password" name="passwd">
        </div>
        <input type="submit" value="提交">
    </form>
</body>
123456789101112
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/9503978ed2c04f26a6f32aa13db2bbb5.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/e550759c284447d099dfbe66c8054b13.png)
可以发现,跟上面的`GET`方法不同的是, 提交后跳转的页面的`URL`后并没有我们提交的参数,而是提交到了后台

##### 表单数据提交优化

修改`register.html`

> 添加 `name` 与 `value` 属性

![在这里插入图片描述](https://img-blog.csdnimg.cn/ae7f25063f6247cf8ac425bea05e898e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/fe1a5aaec3a14091adfafd6a4323ba95.png)

> 在控制台输出数据

修改`app.py`

```python
@app.route("/post/register", methods=['POST'])
def post_register():
    get_info = request.form

    username = request.form.get("username")
    passwd = request.form.get("passwd")
    sex = request.form.get("sex")
    hobby_list = request.form.getlist("hobby")
    city = request.form.get("city")
    more = request.form.getlist("textarea")

    print(username, passwd, sex, hobby_list, city, more)

    return get_info
1234567891011121314
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/d6f4634cc62248fcb53009c88bbd612e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/4753e57c3e034383850efaa3c3f143bd.png)

> 整合`GET`与`POST`方法

![在这里插入图片描述](https://img-blog.csdnimg.cn/ea0679ddcf084771a08055e4c6bf9ad1.png)
将上面图片中的内容整合
![在这里插入图片描述](https://img-blog.csdnimg.cn/dcbb0e9f37674ed6a0c16eceea5da176.png)

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('login.html')
    else:
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        sex = request.form.get("sex")
        hobby_list = request.form.getlist("hobby")
        city = request.form.get("city")
        more = request.form.getlist("textarea")

        print(username, passwd, sex, hobby_list, city, more)

        get_info = request.args
        return get_info
```

### 3.CSS样式

css , 专门用来美化标签

#### 3.1 快速上手

```html
<img src="..." stype="height: 100px">
```

#### 3.2 CSS应用方式

##### 1. 在标签上

```html
<img src="..." stype="height: 100px">
```

##### 2. 在 head 标签的 style 上

```html
...
<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <style>
        .c1 {
            color: red;
        }
    </style>

</head>
<body>
    <h1 class="c1">用户注册</h1>
    ...
```

##### 3. 写到文件中

- common.css

```html
.c1 {
	color: red;
}
 .c2{
	color:blue;
}

```

调用`common.css`

```html
...
<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="common.css" />

</head>
<body>
    <h1 class="c1">用户注册</h1>
    ...
1234567891011
```

### 3.3 选择器

#### 1. ID选择器

==id 唯一==

```html
##c1 {
	color: red;
}

<div id='c1'></div>
```

#### 2. 类选择器

```html
.c1 {
	color: red;
}

<div class='c1'></div>
```

#### 3. 标签选择器

```html
div{
	color: red;
}

<div>xxx</div>
```

#### 4. 属性选择器

> 下面的例子中,所有的`text`类型的`input`都会生效

```html
<head>
    <title>Document</title>
    <link rel="stylesheet" href="/static/commons.css">
    <style>
        input[type="text"]{
        border: 1px solid red;
    }
    </style>
</head>
```



![在这里插入图片描述](https://img-blog.csdnimg.cn/b13a09f158be4e5aacd666403d477e18.png)

> 还有另一种方式,看下面的例子

```html
<style>
    .v1[xx="456"]{
        color: gold;	<!-- 橙色 -->
    }
</style>

...

<body>
...
    <div class="v1" xx="123">a</div>
    <div class="v1" xx="456">b</div>
    <div class="v1" xx="789">c</div>
...
</body>
123456789101112131415
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/32b83bace48848649d23f099342f5fb4.png)

#### 5. 后代选择器

> 这个选择器很有意思,你可以指定标签让它下面对应的标签全部生效,也可以指定标签让他下面的n级标签生效,具体看例子

```html
<style>
    .zz h2{
        color:chartreuse;
    }
</style>
</head>

<body>

    <div class="zz" >
        <div>
            <h2>我是div里面的h2</h2>
        </div>
        <h2>我是div外面的h2</h2>
...
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7084e74a80404198aeadee719d0c7ab2.png)

> 如果只想让第一层的`h1`生效,可以添加`>`号

```html
<style>
    .zz > h2{
        color:chartreuse;
    }
</style>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/6809b78b88ad4a43b64c73f7ea60c376.png)

#### 关于样式的覆盖问题

当一个标签引用了多个 css 样式时,可能会遇到样式属性重复的问题

```html
<style>
    .c2 {
        color: darkgoldenrod;
    }

    .c3 {
        color:hotpink;
    }
</style>

<body>
    <div class="c2 c3">我是天才</div>
</body>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4056d8d7787f4fb8aaf09cb20c5850bd.png)

> 观察到,c3生效,而c2没有生效,这是因为c3在c2的下面,会将上面的c2属性覆盖掉
> 如果不想让上面的被覆盖掉怎么办呢?
> 可以在对应的属性后面添加`!important`

```html
<style>
    .c2 {
        color: darkgoldenrod !important;
    }

    .c3 {
        color:hotpink;
    }
</style>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/1b6e0ed2816c4a798baf3e0089c9064a.png)

### 3.4 样式

#### 1. 高度和宽度

```html
.c4 {
        height: 300px;
        width: 500px;
    }
```

注意事项:

- 支持百分比
- 行内标签: 默认无效
- 块级标签: 默认有效(右边的剩余空白区域也会被占用)

#### 2. 块级和行内标签

> `display:inline-block` 使行内标签对 **height** 和 **width** 生效

```html
<style>
.c4 {
        display: inline-block;
        height: 300px;
        width: 500px;
        border: 1px solid red;
    }
</style>

...

<body>
	<span class="c4">联通</span>
</body>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/210bd1237f44451cb9c12a53d8b9bed7.png)

> 块级与行内标签的转换

```html
## 转化为 行内标签
<div style="display: inline;">移动</div> 
## 转化为 块级标签
<span style="display: block;">联通</span>

```

注意:

- 块级标签 + 块级&行内标签

#### 3. 字体和对齐方式

> 设置字体颜色/大小/粗细/字体样式

```html
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .c1 {
            color: #00FF7F;                   /* 字体颜色 */
            font-size: 20px;                  /* 字体大小 */
            font-weight: 600;                 /* 字体粗细 */
            font-family: Microsoft Yahei;     /* 字体样式 */
            text-align: center;               /* 水平方向居中 */
            line-height: 50px;                /* 垂直方向居中 */
            border: 1px solid red;            /* 边框 */
        }
    </style>
</head>
```

#### 4. 浮动

> 如果在块级标签中，加入了`float`属性，那么这个块级标签奖不会再占用一整行，而是自己有多大就占用多大

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .item {
            float: left;
            width: 280px;
            height: 170px;
            border: 1px solid red;
        }

    </style>
</head>
<body>
    <div>
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
    </div>
</body>
</html>
1234567891011121314151617181920212223
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2714195774ec4ab5bf1ee7b90f01e022.png)

> 如果你让标签浮动起来之后，就会脱离文档流。
> 例如下面的例子中，我们给div的父标签赋予了一个蓝色的背景，但是你不会看到蓝色背景。因为他被浮动的div字标签挡住了。

```html
<body>
    <div style="background-color: blue;">
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
    </div>
</body>
```

> 解决办法: 在同级子标签的最下面添加 `style="clear: both;"`

```html
<body>
    <div style="background-color: blue;">
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
        <div style="clear: both;"></div>
    </div>
</body>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0a7e67f158da404fb24758b1d1539aa2.png)

#### 5. 内边距

> `padding-top | padding-left | padding-right | padding-botton`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .outer {
            border: 1px solid red;
            height: 200px;
            width: 200px;

            padding-top: 20px;
            padding-left: 20px;
            padding-right: 20px;
            padding-bottom: 20px;
        }

    </style>
</head>
<body>
    <div class="outer">
        <div>hello</div>
        <div>world</div>
        
    </div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0974caf8020248e19dc375afd423cffc.png)
其实上面的四个上下左右的padding可以简写为`padding: 20px 20px 20px 20px`,顺序为上右下左(顺时针方向)

#### 6. 外边距

> margin

```html
<body>
    <div style="height: 200px; background-color: aquamarine;"></div>
    <div style="height: 200px; background-color:blueviolet; margin-top: 20px;"></div>
</body>
1234
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f125808c48c74d4ba6c72b83f9cbb3d4.png)

#### 7. hover( 伪类 )

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .c1 {
            color:brown;
        }
        .c1:hover {
            color: green;
            font-size: 20px;
        }

        .c2 {
            width: 300px;
            height: 300px;
            border: 3px solid red;
        }
        .c2:hover {
            border: 3px solid green;
        }

        .download {
            display: none;
        }

        .app:hover .download {
            display: block;
        }

    </style>
</head>
<body>
    <div class="c1">字体碰到鼠标变成绿色</div>
    <div class="c2">边框碰到鼠标变成绿色</div>
    <div class="app">
        <div>鼠标放我这里触发显示二维码</div>
        <div class="download">
            <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/78c30d4f259ed43ab20e810a522a6249.png" alt="">
        </div>
    </div>
</body>
</html>
```

#### 8. after ( 伪类 )

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .c1:after {
            content: "大帅比"
        }
    </style>
</head>
<body>
    <div class="c1">张三</div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/73ba30286262404cb4b55ac7798d63b5.png)

> after一般像下面这样用,不用每次都写`stype="clear: both;"`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .clearfix:after {
            content: "";
            display: block;
            clear: both;
        }

        .item {
            float: left;
        }

    </style>
</head>
<body>
    <div class="clearfix">
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
    </div>
</body>
</html>
```

#### 9. position

- fixed
- relative
- absolute

##### 9.1 fixed

固定在窗口的某个位置。

> 返回顶部

```css
.back {
     position: fixed;
     width: 60px;
     height: 60px;
     border: 1px solid red;

     right: 50px;
     bottom: 50px;
 }
```

> 对话框

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        
        body {
            margin: 0;
        }

        .dialog {
            position: fixed;
            height: 300px;
            width: 500px;
            background-color: white;

            /* 居中 */
            
            left: 0;
            right: 0;
            margin: 0 auto;
            
            top: 200px;

            z-index: 1000;  /* 防止对话框被mask遮住 */
        }

        .mask {
            background-color: black;
            position: fixed;
            left: 0;
            right: 0;
            top: 0;
            bottom: 0;
            opacity: 0.7;

            z-index: 999;   /* 防止对话框被mask遮住  z-index 越大 优先级越高*/ 
        }

    </style>
</head>
<body>
    <div style="height: 1000px;"></div>
    <!-- 如果css中不加 z-index 设置优先级的话 -->
    <!-- 那么下面的 dialog 如果在 mask 的上面,对话框就显示不出来了 -->
    <!-- 设置优先级可以解决此问题 -->
    	
    
    <div class="dialog"></div>
    <div class="mask"></div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/9f3e4dd7039e4f318aeda438b9cd86e4.png)



##### 9.2 relative和absolute

> 在`小米商城`案例的基础上进行测试

```html
...
        .app{
            position: relative;
        }

        .app .download {
            position: absolute;
            display: none;
            height: 100px;
            width: 100px;
        }

        .app:hover .download {
            display: block;
        }

    </style>

</head>
<body>
    <div class="header">
        <div class="container">
            <div class="menu">
                <a href="https://www.mi.com">小米商城</a>
                <a href="https://www.mi.com">MIUI</a>
                <a href="https://www.mi.com">云平台</a>
                <a href="https://www.mi.com">有品</a>
                <a href="https://www.mi.com">小爱开放平台</a>
                <a href="https://www.mi.com" class="app">app下载
                    <div class="download">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/78c30d4f259ed43ab20e810a522a6249.png" alt="">
                    </div>
                </a>
            </div>
            <div class="account">
                <a href="https://www.mi.com">登录</a>
                <a href="https://www.mi.com">注册</a>
                <a href="https://www.mi.com">消息通知</a>
            </div>'
            <div style="clear: both;"></div>
        </div>
    </div>
...
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/8f8333012d29473f9a250fecfa1b61dc.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/09b4a80ac03340a9a27d6dc47f1e1008.png)

#### 10. border

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>

        .left {
            float: left;
        }

        .c1 {
            height: 200px;
            width: 300px;
            border: 3px dotted red;
            margin: 50px;
        }

        .c2 {
            height: 200px;
            width: 300px;
            border: 3px solid red;
            border-left: 3px solid green;
            margin: 50px;
        }

        .c3 {
            height: 200px;
            width: 300px;
            margin: 50px;
            background-color: bisque;
            border-left: 2px solid transparent;  /* 透明色 */
        }

        .c3:hover {
            border-left: 2px solid rgb(35, 211, 19);
        }

    </style>
</head>
<body>
    <div class="c1 left">我是虚线~</div>
    <div class="c2 left">我是实线~左边框是绿色,上下右边框是红色</div>
    <div class="c3 left">我是透明色,鼠标碰到我边框会变色哦~</div>
    <div style="clear: both;"></div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/6381207db4de4770bfb9b87785ee4cad.png)

#### 11. 背景色

> background-color: bisque;
> 无需多言☺

------

> 注意: 以上不是所有的CSS样式,这些是最常用的标签

### 总结

- body 标签，默认有一个边距，造成页面四边都有白色间隙，如何去除呢？

```html	
body{
	margin:0;
}
```

- 内容居中

  - 文本居中

    ```HTML
    <div style="width:200px; text-align:center;">学习Django</div>
    ```

  - 区域居中，自己要有宽度 + margin -left:auto ; margin-right:auto

    ```html
    .container{
    	width:980px;
    	margin:0 auto;
    }
    
    <div class="container">
        adsfaf
    </div>
    ```

    

- 父亲没有宽度或者高度，被孩子支撑起来
- 关于布局 不知道如何下手





### 4.案例: 小米商城

#### 4.1 小米顶部

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>小米商城</title>
    <style>
        /* 去掉body的边距 */
        body {
            margin: 0;
        }

        .header {
            background-color: #333;
        }

        /* 让中间内容居中 */
        .container {
            width: 1226px;
            margin: 0 auto;     /* 上下为0, 左右为auto */
        }

        /* header class 下的标签 a 自动应用这个样式 */
        .header a {
            color: #b0b0b0;
            line-height: 40px;
            display: inline-block;
            font-size: 12px;
        }

        .header .menu {
            float: left;
            color: white;
        }

        .header .account {
            float: right;
            color: white;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="container">
            <div class="menu">
                <a>小米商城</a>
                <a>MIUI</a>
                <a>云平台</a>
                <a>有品</a>
                <a>小爱开放平台</a>
            </div>
            <div class="account">
                <a>登录</a>
                <a>注册</a>
                <a>消息通知</a>
            </div>'
            <div style="clear: both;"></div>
        </div>
    </div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/aa98b77c70c74cb0ab76e6fbba4aea73.png)

#### 4.2 二级菜单

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>小米商城</title>
    <style>
        /* 去掉body的边距 */
        body {
            margin: 0;
        }

        .header {
            background-color: #333;
        }

        /* 让中间内容居中 */
        .container {
            width: 1226px;
            margin: 0 auto;     /* 上下为0, 左右为auto */
        }

        /* header class 下的标签 a 自动应用这个样式 */
        .header a {
            color: #b0b0b0;
            line-height: 40px;
            display: inline-block;
            font-size: 12px;
        }

        .header .menu {
            float: left;
            color: white;
        }

        .header a {
            text-decoration: none;
        }

        .header a:hover {
            color: white;
        }

        .header .account {
            float: right;
            color: white;
        }

        .sub-header {
            height: 100px;
        }

        .sub-header .hw {
            width: 234px;
            height: 100px;
        }

        .sub-header .logo {
            float: left;
        }

        /* a标签是行内标签,默认不支持设置高度与边距 因此设置padding是不起作用的,因此可以加上 inline-block */
        .sub-header .logo a {
            padding-top: 22px;
            padding-bottom: 22px;
            display: inline-block;
        }

        /* 设置logo的图片像素大小 */
        .sub-header .logo img {
            height: 56px;
            width: 56px;
        }

        .sub-header .menu {
            width: 400px;
            float:left;
            line-height: 100px;     /* 与行高度保持一致 */
        }

        .sub-header .menu a {
            text-decoration: none;  /* 去掉 a 标签的下划线 */
            color: #333;
            font-size: 16px;
            padding: 0 10px;        /* 设置字体的左右外边距 */
            display: inline-block;
        }

        /* 鼠标放到字体时,使字体变红 */
        .sub-header .menu a:hover {
            color: #ff6700;
        }

        .sub-header .search {
            float: right;
        }

    </style>

</head>
<body>
    <div class="header">
        <div class="container">
            <div class="menu">
                <a href="https://www.mi.com">小米商城</a>
                <a href="https://www.mi.com">MIUI</a>
                <a href="https://www.mi.com">云平台</a>
                <a href="https://www.mi.com">有品</a>
                <a href="https://www.mi.com">小爱开放平台</a>
            </div>
            <div class="account">
                <a href="https://www.mi.com">登录</a>
                <a href="https://www.mi.com">注册</a>
                <a href="https://www.mi.com">消息通知</a>
            </div>'
            <div style="clear: both;"></div>
        </div>
    </div>
    <div class="sub-header">
        <div class="container">
            <div class="hw logo">
                <a href="https://www.mi.com">
                    <img src="https://s02.mifile.cn/assets/static/image/logo-mi2.png" alt="小米官网">
                </a>
            </div>
            <div class="hw menu">
                <a href="https://www.mi.com">Xiaomi手机</a>
                <a href="https://www.mi.com">Redmi手机</a>
                <a href="https://www.mi.com">电视</a>
                <a href="https://www.mi.com">笔记本</a>
                <a href="https://www.mi.com">平板</a>
            </div>
            <div class="hw search"></div>
            <div style="clear: both;"></div>
        </div>
    </div>
</body>
</html>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/96de14e323504a8cbdf115daa9713ff7.png)

#### 4.3 推荐区域

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>小米商城</title>
    <style>
        /* 去掉body的边距 */
        body {
            margin: 0;
        }

        img {
            width: 100%;
            height: 100%;
        }

        .left {
            float: left;
        }

        .margin_left {
            margin-left: 14.5px;
        }

        .header {
            background-color: #333;
        }

        /* 让中间内容居中 */
        .container {
            width: 1226px;
            margin: 0 auto;     /* 上下为0, 左右为auto */
        }

        /* header class 下的标签 a 自动应用这个样式 */
        .header a {
            color: #b0b0b0;
            line-height: 40px;
            display: inline-block;
            font-size: 12px;
        }

        .header .menu {
            float: left;
            color: white;
        }

        .header a {
            text-decoration: none;
        }

        .header a:hover {
            color: white;
        }

        .header .account {
            float: right;
            color: white;
        }

        .sub-header {
            height: 100px;
        }

        .sub-header .hw {
            width: 234px;
            height: 100px;
        }

        .sub-header .logo {
            float: left;
        }

        /* a标签是行内标签,默认不支持设置高度与边距 因此设置padding是不起作用的,因此可以加上 inline-block */
        .sub-header .logo a {
            padding-top: 22px;
            padding-bottom: 22px;
            display: inline-block;
        }

        /* 设置logo的图片像素大小 */
        .sub-header .logo img {
            height: 56px;
            width: 56px;
        }

        .sub-header .menu {
            width: 400px;
            float:left;
            line-height: 100px;     /* 与行高度保持一致 */
        }

        .sub-header .menu a {
            text-decoration: none;  /* 去掉 a 标签的下划线 */
            color: #333;
            font-size: 16px;
            padding: 0 10px;        /* 设置字体的左右外边距 */
            display: inline-block;
        }

        /* 鼠标放到字体时,使字体变红 */
        .sub-header .menu a:hover {
            color: #ff6700;
        }

        .sub-header .search {
            float: right;
        }

        .slider {
            height: 460px;
        }

        .news{
            margin-top: 14px;
        }

        .news .channel {
            width: 228px;
            height: 164px;
            background-color: #5f5750;
            padding: 3px;
        }

        .news .channel .item {
            width: 76px;
            height: 82px;
            float: left;
            text-align: center;
        }

        .news .channel .item img {
            width: 24px;
            height: 24px;
            display: block;         /* 让图片自已占一整行 */
            margin: 0 auto;         /* 让图片垂直居中 */
            margin-bottom: 4px;     /* 设置图片与下方字体的间距 */
        }

        .news .channel .item a {
            display: inline-block;
            font-size: 12px;        /* 设置字体大小 */
            text-decoration: none;  /* a标签去掉下划线 */
            padding-top: 18px;  
            color: #fff;          /* 设置字体为白色 */
            opacity: 0.7;           /* 设置透明度 */
        }

        .news .channel .item a:hover {
            opacity: 1;           /* 设置透明度 */
        }


        .news .list-item {
            width: 316px;
            height: 170px;
        }



    </style>

</head>
<body>
    <div class="header">
        <div class="container">
            <div class="menu">
                <a href="https://www.mi.com">小米商城</a>
                <a href="https://www.mi.com">MIUI</a>
                <a href="https://www.mi.com">云平台</a>
                <a href="https://www.mi.com">有品</a>
                <a href="https://www.mi.com">小爱开放平台</a>
            </div>
            <div class="account">
                <a href="https://www.mi.com">登录</a>
                <a href="https://www.mi.com">注册</a>
                <a href="https://www.mi.com">消息通知</a>
            </div>'
            <div style="clear: both;"></div>
        </div>
    </div>
    <div class="sub-header">
        <div class="container">
            <div class="hw logo">
                <a href="https://www.mi.com">
                    <img src="https://s02.mifile.cn/assets/static/image/logo-mi2.png" alt="小米官网">
                </a>
            </div>
            <div class="hw menu">
                <a href="https://www.mi.com">Xiaomi手机</a>
                <a href="https://www.mi.com">Redmi手机</a>
                <a href="https://www.mi.com">电视</a>
                <a href="https://www.mi.com">笔记本</a>
                <a href="https://www.mi.com">平板</a>
            </div>
            <div class="hw search"></div>
            <div style="clear: both;"></div>
        </div>
    </div>
    <div class="slider">
        <div class="container">
            <div>
                <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/454c1da2c5b64a3f2c07c5a4c01aa9c4.jpg?thumb=1&w=1533&h=575&f=webp&q=90" alt="推荐商品">
            </div>
        </div>
    </div>
    <div class="news">
        <div class="container">
            <div class="channel left">
                <div class="item">
                    <a href="https://www.mi.com">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/82abdba456e8caaea5848a0cddce03db.png?w=48&h=48" alt="">
                        <div>保障服务</div>
                    </a>
                </div>
                <div class="item">
                    <a href="https://www.mi.com">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/806f2dfb2d27978e33fe3815d3851fa3.png?w=48&h=48" alt="">
                        <div>企业团购</div>
                    </a>
                </div>
                <div class="item">
                    <a href="https://www.mi.com">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/eded6fa3b897a058163e2485532c4f10.png?w=48&h=48" alt="">
                        <div>F码通道</div>
                    </a>
                </div>
                <div class="item">
                    <a href="https://www.mi.com">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/43a3195efa6a3cc7662efed8e7abe8bf.png?w=48&h=48" alt="">
                        <div>米粉卡</div>
                    </a>
                </div>
                <div class="item">
                    <a href="https://www.mi.com">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/f4846bca6010a0deb9f85464409862af.png?w=48&h=48" alt="">
                        <div>以旧换新</div>
                    </a>
                </div>
                <div class="item">
                    <a href="https://www.mi.com">
                        <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/9a76d7636b08e0988efb4fc384ae497b.png?w=48&h=48" alt="">
                        <div>话费充值</div>
                    </a>
                </div>
                <div style="clear: both;"></div>
            </div>
            <div class="list-item left margin_left">
                <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/d0c515086acb3c3a3e976ad20901aac5.jpg?w=632&h=340" alt="">
            </div>
            <div class="list-item left margin_left">
                <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/254c711cc71facf156ac955b8719dffa.jpg?w=632&h=340" alt="">
            </div>
            <div class="list-item left margin_left">
                <img src="https://cdn.cnbj1.fds.api.mi-img.com/mi-mall/2b120c0dddc056dcb36e847269fb92cd.jpg?w=632&h=340" alt="">
            </div>
            <div style="clear: both;"></div>
        </div>
    </div>
</body>
</html>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/fc5ebb5c2fe947f5abda7d0500f076e8.png)

### 5. Bootstrap

> 别人已经帮忙写好的CSS样式

使用方式:

- 下载Bootstrap
- 使用:
  - 在页面上引入 Bootstrap
  - 编写HTML时,按照Bootstrap的规定来编写或者自定制

> 由于我没有下载Pycharm,无法本地实时测试,我使用的VSCode进行的编辑,所以我继续使用Flaskweb进行页面的访问测试

![在这里插入图片描述](https://img-blog.csdnimg.cn/8e46a398ae2647c3824c4e192a55af6b.png)

#### 5.1 初识Bootstrap

下载地址: https://v3.bootcss.com/
![在这里插入图片描述](https://img-blog.csdnimg.cn/a5c6688a7821447d98383a2f08c5f345.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/646e48dcec744b39ba9c8db99e3169eb.png)

```
BaiDuNetDisk Download:
链接：https://pan.baidu.com/s/1rcZldkNHrpC11f2plUv-rg?pwd=mh5b 
提取码：mh5b 
123
```

下载完成后解压,目录如下:
![在这里插入图片描述](https://img-blog.csdnimg.cn/aafadde30ffa4f5cb5bbb28502164449.png)
在服务器中创建必要的目录

```shell
[root@hecs-33592 python]# cd bootstrap/
[root@hecs-33592 bootstrap]# ls
main.py  templates
[root@hecs-33592 bootstrap]# mkdir static
[root@hecs-33592 bootstrap]# cd static/
[root@hecs-33592 static]# ls
[root@hecs-33592 static]# mkdir css
[root@hecs-33592 static]# mkdir js
[root@hecs-33592 static]# mkdir img
[root@hecs-33592 static]# mkdir plugins



[root@hecs-33592 static]# tree /root/python/bootstrap/
/root/python/bootstrap/
├── main.py
├── static
│   ├── css
│   ├── img
│   ├── js
│   └── plugins
└── templates

1234567891011121314151617181920212223
```

我会把刚刚下载好的`bootstrap-3.4.1-dist.zip`解压放到`plugins`下

```shell
[root@hecs-33592 plugins]# ls
bootstrap-3.4.1-dist.zip
[root@hecs-33592 plugins]# unzip bootstrap-3.4.1-dist.zip
[root@hecs-33592 plugins]# mv bootstrap-3.4.1-dist bootstrap-3.4.1
[root@hecs-33592 plugins]# tree bootstrap-3.4.1
bootstrap-3.4.1
├── css
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   ├── bootstrap-theme.min.css
│   └── bootstrap-theme.min.css.map
├── fonts
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   └── glyphicons-halflings-regular.woff2
└── js
    ├── bootstrap.js
    ├── bootstrap.min.js
    └── npm.js

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/5becafc5da304cfeb7a2496e1545c624.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <!-- 开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">

    <!-- 生产版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css">

</head>
<body>
    <input type="button" value="提交">
    <input type="button" value="提交" class="btn btn-primary">
    <input type="button" value="提交" class="btn btn-success">
    <input type="button" value="提交" class="btn btn-danger">
    <input type="button" value="提交" class="btn btn-danger btn-xs">
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f0c2b689f012470e943571b42912b360.png)
接下来使用已经写好的导航栏
链接地址: https://v3.bootcss.com/components/
![在这里插入图片描述](https://img-blog.csdnimg.cn/bf94f0ee77d74dd5870133399ad9079b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/cb53a5549999478bb0475f7ab67fc60f.png)
复制上面的代码

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <!-- 开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">

    <!-- 生产版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css">

</head>

<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                    <li><a href="#">Link</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">One more separated link</a></li>
                        </ul>
                    </li>
                </ul>
                <form class="navbar-form navbar-left">
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Search">
                    </div>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Link</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
</body>

</html>
```

访问效果如下:
![在这里插入图片描述](https://img-blog.csdnimg.cn/9148ca0d41bc49cf8b23c5fcf17b1549.png)
其实你仔细看会发现这个导航栏是有`圆角`的
接下来我们去掉`圆角`
`F12`调试页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/8ceafe52d86042d7b19bfbe24dbc3a42.png)
覆盖`.navbar`样式

```html
<style>
    .navbar {
        border-radius: 0;
    }
</style>
12345
```

再次访问就没有圆角了

> 可以在相应的位置进行修改,代码部分自己测试修改哈

![在这里插入图片描述](https://img-blog.csdnimg.cn/c8304bb5a4d44135b70e42ba3ef18dcf.png)

#### 5.2 栅格系统

[栅格系统介绍](https://v3.bootcss.com/css/#grid)

> 整体划分为了`12`格

大致分为四种风格

> .col-xs-
> .col-sm-
> .col-md-
> .col-lg-

![在这里插入图片描述](https://img-blog.csdnimg.cn/d9b2a0564f9e4034a715f9f8e26d5f39.png)

响应式:根据页面的宽度,动态的改变布局

- .col-sm- : 750px
- .col-md- : 970px
- .col-lg- : 1170px

非响应式:

- .col-xs-

```html
<div class="col-xs-2" style="background-color: brown; height: 20px;"></div>
<div class="col-xs-10" style="background-color: green;height: 20px;"></div>
12
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/8161ef0ecd1346ea8ac1a40411ba37aa.png)
列偏移

> col-sm-offset-

```html
<div class="col-sm-offset-3 col-sm-2" style="background-color: brown; height: 20px;"></div>
<div class="col-sm-7" style="background-color: green;height: 20px;"></div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/3d38c831f61e40cf898b039dc448b066.png)

#### 5.3 container

- container

```html
<div class="container clearfix">
    <div class="col-sm-9">左边</div>
    <div class="col-sm-3">右边</div>
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/88328a48dbfe42d5b734b29b6976825e.png)

- container-fluid

```html
<div class="container-fluid clearfix">
    <div class="col-sm-9">左边</div>
    <div class="col-sm-3">右边</div>
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/81924a7d0d464bfca31ed611b46e7f3e.png)

#### 5.4 面板

地址: https://v3.bootcss.com/components/#panels
![在这里插入图片描述](https://img-blog.csdnimg.cn/8ad6b0a5286e4a87bfdfa9a41e766092.png)

```html
<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">我的导航</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                    <li><a href="#">联通</a></li>
                    <li><a href="#">移动</a></li>
                    <li><a href="#">电信</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">One more separated link</a></li>
                        </ul>
                    </li>
                </ul>
                <form class="navbar-form navbar-left">
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Search">
                    </div>
                    <button type="submit" class="btn btn-default">Submit</button>
                </form>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Link</a></li>
                    <li><a href="#">登录</a></li>
                    <li><a href="#">注册</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
    <div class="container clearfix">
        <div class="col-sm-9">左边</div>
        <div class="col-sm-3">
            <div class="panel panel-default">
                <div class="panel-heading">Panel heading without title</div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
            <div class="panel panel-primary">
                <div class="panel-heading">Panel heading without title</div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
            <div class="panel panel-warning">
                <div class="panel-heading">Panel heading without title</div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
        </div>
    </div>

</body>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2c0a60b5aa00424197b1e2a975bac01c.png)

#### 5.5 媒体对象

添加媒体对象
![在这里插入图片描述](https://img-blog.csdnimg.cn/bf809a51c4244143978ffa3a213c4a12.png)

> 由于官方文档给的示例代码不全,所以可以F12查看源码,复制页面中的样式

![在这里插入图片描述](https://img-blog.csdnimg.cn/f73cc6d80e9b4407982f1114bd9fa83e.png)

```html
<div class="col-sm-9">
    <div class="media">
        <div class="media-left media-middle">
            <a href="#">
                <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                    style="width: 64px; height: 64px;"
                    src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                    data-holder-rendered="true">
            </a>
        </div>
        <div class="media-body">
            <h4 class="media-heading">Middle aligned media</h4>
            <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
            <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
        </div>
    </div>
    <div class="media">
        <div class="media-left media-middle">
            <a href="#">
                <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                    style="width: 64px; height: 64px;"
                    src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                    data-holder-rendered="true">
            </a>
        </div>
        <div class="media-body">
            <h4 class="media-heading">Middle aligned media</h4>
            <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
            <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
        </div>
    </div>
    <div class="media">
        <div class="media-left media-middle">
            <a href="#">
                <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                    style="width: 64px; height: 64px;"
                    src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                    data-holder-rendered="true">
            </a>
        </div>
        <div class="media-body">
            <h4 class="media-heading">Middle aligned media</h4>
            <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
            <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
        </div>
    </div>
    <div class="media">
        <div class="media-left media-middle">
            <a href="#">
                <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                    style="width: 64px; height: 64px;"
                    src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                    data-holder-rendered="true">
            </a>
        </div>
        <div class="media-body">
            <h4 class="media-heading">Middle aligned media</h4>
            <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
            <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
        </div>
    </div>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f445849f2f044bbe907c669d1bb71865.png)

#### 5.6 分页

链接: https://v3.bootcss.com/components/#pagination
![在这里插入图片描述](https://img-blog.csdnimg.cn/983d055ac1fd413aae07737290d5d32a.png)

```html
<ul class="pagination">
                <li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">«</span></a></li>
                <li class="active"><a href="#">1 <span class="sr-only">(current)</span></a></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#">5</a></li>
                <li><a href="#" aria-label="Next"><span aria-hidden="true">»</span></a></li>
            </ul>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/1d77c7fd8fba4c5891c260112a169eec.png)

#### 案例: 登录

![在这里插入图片描述](https://img-blog.csdnimg.cn/8faa056ccb59431a97e68ae5278cb138.png)

- 宽度 + 区域居中
- 内边距

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">

    <style>
        .ct {
            margin-left: auto;                  /* 设置水平居中 */
            margin-right: auto;
            margin-top: 200px;
            width: 500px;
            height: 350px;
            border: 2px solid black;
            padding: 20px 40px;                 /* 设置内边距 */
            border-radius: 10px;                /* 设置圆角*/
            box-shadow: 5px 5px 10px #aaa;    /* 设置阴影 水平 垂直 厚度 颜色*/
            background-color:bisque;
        }

        .ct h1 {
            text-align: center;
            margin-top: 10px;
        }

        .ct button {
            margin: 20px;
        }
    </style>

</head>

<body>
    <div class="ct">
        <div>
            <h1>用户登录</h1>
        </div>
        <div>
            <form>
                <div class="form-group">
                    <label for="exampleInputEmail1">用户名</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="请输入用户名">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword1">密码</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                </div>
                <div style="text-align: center">
                    <button type="submit" class="btn btn-primary">登 录</button>
                    <button type="submit" class="btn btn-default">注 册</button>
                </div>
            </form>
        </div>
    </div>
</body>

</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/1b407c266b5e405c8b513b5c6efd5b4f.png)

#### 案例: 后台管理

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <!-- 开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">

    <!-- 生产版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css">

    <style>
        .bt {
            margin: 20px;
        }
    </style>

</head>

<body>
    <div class="container">
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">我的导航</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                        <li><a href="#">联通</a></li>
                        <li><a href="#">移动</a></li>
                        <li><a href="#">电信</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Another action</a></li>
                                <li><a href="#">Something else here</a></li>
                                <li role="separator" class="divider"></li>
                                <li><a href="#">Separated link</a></li>
                                <li role="separator" class="divider"></li>
                                <li><a href="#">One more separated link</a></li>
                            </ul>
                        </li>
                    </ul>
                    <form class="navbar-form navbar-left">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Search">
                        </div>
                        <button type="submit" class="btn btn-default">Submit</button>
                    </form>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#">Link</a></li>
                        <li><a href="#">登录</a></li>
                        <li><a href="#">注册</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Another action</a></li>
                                <li><a href="#">Something else here</a></li>
                                <li role="separator" class="divider"></li>
                                <li><a href="#">Separated link</a></li>
                            </ul>
                        </li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>

        <div class="panel panel-info">
            <div class="panel-heading">
                <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>
                表单区域
            </div>
            <div class="panel-body">
                <form class="form-inline">
                    <div class="form-group">
                        <label for="exampleInputName2">Name</label>
                        <input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
                    </div>
                    <div class="form-group">
                        <label for="exampleInputEmail2">Email</label>
                        <input type="email" class="form-control" id="exampleInputEmail2"
                            placeholder="jane.doe@example.com">
                    </div>
                    <button type="submit" class="btn btn-success">
                        <span class="glyphicon glyphicon-file" aria-hidden="true"></span> 保 存
                    </button>
                </form>
            </div>
        </div>

        <div class="panel panel-info">
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                数据列表
            </div>
            <div class="panel-body">
                注意: 以下内容是筛选出来的
            </div>
            <div>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">1</th>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>
                                <a class="btn btn-primary btn-xs">编辑</a>
                                <a class="btn btn-danger btn-xs">删除</a>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">2</th>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>
                                <a class="btn btn-primary btn-xs">编辑</a>
                                <a class="btn btn-danger btn-xs">删除</a>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">3</th>
                            <td>Larry</td>
                            <td>the Bird</td>
                            <td>
                                <a class="btn btn-primary btn-xs">编辑</a>
                                <a class="btn btn-danger btn-xs">删除</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>


        <nav aria-label="Page navigation">
            <ul class="pagination">
              <li>
                <a href="#" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              <li><a href="#">1</a></li>
              <li><a href="#">2</a></li>
              <li><a href="#">3</a></li>
              <li><a href="#">4</a></li>
              <li><a href="#">5</a></li>
              <li>
                <a href="#" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </nav>
    </div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/68323b5b10a24bc4a3b70135343352d7.png)

#### 5.7 图标

上面的后台管理案例中,Bootstrap提供的图标不是太够用,我们需要一个专业做图标的网站

> 地址: https://fontawesome.dashgame.com/

下载
![在这里插入图片描述](https://img-blog.csdnimg.cn/56a4695d6bf647cda63f614d01069c5d.png)
下载好后,上传至服务器的`static/plugins`下并解压
![在这里插入图片描述](https://img-blog.csdnimg.cn/c2b6984fc80a4c3490426804966132ed.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/f39f74da6d2d46bbaf981ab4e0f4e814.png)
打开网址https://fontawesome.dashgame.com/
![在这里插入图片描述](https://img-blog.csdnimg.cn/ec415bcfc2354773a5b838791ba98e1d.png)
放在代码的这里
![在这里插入图片描述](https://img-blog.csdnimg.cn/f7e2453baf1741f78ea762f293bca507.png)
访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/ccd82ccf19da4d13be3299b405590484.png)
以此类推,很简单

#### 优化

> 针对前面的导航页面进行优化

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <!-- 开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">

    <!-- 生产版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css">

    <link rel="stylesheet" href="static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <style>
        .distance {
            margin-left: 40px;
        } 
    </style>

</head>

<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">我的导航</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                    <li><a href="#">联通</a></li>
                    <li><a href="#">移动</a></li>
                    <li><a href="#">电信</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">One more separated link</a></li>
                        </ul>
                    </li>
                </ul>
                <form class="navbar-form navbar-left">
                    <div class="form-group">
                        <input type="text" class="form-control" placeholder="Search">
                    </div>
                    <button type="submit" class="btn btn-default">
                        <i class="fa fa-search" aria-hidden="true"></i>
                    </button>
                </form>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">Link</a></li>
                    <li><a href="#">登录</a></li>
                    <li><a href="#">注册</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
    <div class="container clearfix">
        <div class="col-sm-9">
            <div class="media">
                <div class="media-left media-middle">
                    <a href="#">
                        <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                            style="width: 64px; height: 64px;"
                            src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                            data-holder-rendered="true">
                    </a>
                </div>
                <div class="media-body">
                    <h4 class="media-heading">Middle aligned media</h4>
                    <div>
                        <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                        <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                        <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                        <i class="fa fa-star" aria-hidden="true" style="color: #f0ad4e;"></i>
                        <i class="fa fa-star" aria-hidden="true"></i>
                    </div>
                    <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                        commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                        nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                    <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                        penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
                    <div>
                        <i class="fa fa-calendar" aria-hidden="true"></i> 2022-12-07
                        <i class="fa fa-user distance" aria-hidden="true"></i> poker 
                        <i class="fa fa-comment distance" aria-hidden="true"></i> 1234
                    </div>
                </div>
            </div>
            <div class="media">
                <div class="media-left media-middle">
                    <a href="#">
                        <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                            style="width: 64px; height: 64px;"
                            src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                            data-holder-rendered="true">
                    </a>
                </div>
                <div class="media-body">
                    <h4 class="media-heading">Middle aligned media</h4>
                    <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                        commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                        nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                    <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                        penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
                </div>
            </div>
            <div class="media">
                <div class="media-left media-middle">
                    <a href="#">
                        <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                            style="width: 64px; height: 64px;"
                            src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                            data-holder-rendered="true">
                    </a>
                </div>
                <div class="media-body">
                    <h4 class="media-heading">Middle aligned media</h4>
                    <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                        commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                        nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                    <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                        penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
                </div>
            </div>
            <div class="media">
                <div class="media-left media-middle">
                    <a href="#">
                        <img class="media-object" data-src="holder.js/64x64" alt="64x64"
                            style="width: 64px; height: 64px;"
                            src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+PCEtLQpTb3VyY2UgVVJMOiBob2xkZXIuanMvNjR4NjQKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRlYTE3NjE2OSB0ZXh0IHsgZmlsbDojQUFBQUFBO2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjEwcHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGVhMTc2MTY5Ij48cmVjdCB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIGZpbGw9IiNFRUVFRUUiLz48Zz48dGV4dCB4PSIxMy4xNzUyMTg1ODIxNTMzMiIgeT0iMzYuNTU5OTk5OTQyNzc5NTQiPjY0eDY0PC90ZXh0PjwvZz48L2c+PC9zdmc+"
                            data-holder-rendered="true">
                    </a>
                </div>
                <div class="media-body">
                    <h4 class="media-heading">Middle aligned media</h4>
                    <p>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                        commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum
                        nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                    <p>Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                        penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
                </div>
            </div>
            <ul class="pagination">
                <li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">«</span></a></li>
                <li class="active"><a href="#">1 <span class="sr-only">(current)</span></a></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#">5</a></li>
                <li><a href="#" aria-label="Next"><span aria-hidden="true">»</span></a></li>
            </ul>
        </div>
        <div class="col-sm-3">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <i class="fa fa-fire" aria-hidden="true" style="color: red;"></i> 最新推荐
                </div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
            <div class="panel panel-primary">
                <div class="panel-heading">Panel heading without title</div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
            <div class="panel panel-warning">
                <div class="panel-heading">Panel heading without title</div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
        </div>
    </div>
</body>
</html>
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134135136137138139140141142143144145146147148149150151152153154155156157158159160161162163164165166167168169170171172173174175176177178179180181182183184185186187188189190191192193194195196197198199200201202203204205206207
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/89a9fa0306b145c9ba8df6d1ae3f818a.png)

#### 5.8 Bootstrap实现动态效果



依赖:

- JQuery
- Javascript

> JQuery 是 Javascript 的类库

下载JQuery: https://jquery.com/download/
![在这里插入图片描述](https://img-blog.csdnimg.cn/03a0db69536842f2bd6b6ea65a916c92.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2b002c989d24490a85ee1074d859ced4.png)
因为我的项目在服务器中,所以我可以在服务器中使用`wget`命令直接下载
放在`static/js`下

```shell
[root@hecs-33592 js]# pwd
/root/python/bootstrap/static/js
[root@hecs-33592 js]# wget https://code.jquery.com/jquery-3.6.1.min.js
--2022-12-07 14:08:39--  https://code.jquery.com/jquery-3.6.1.min.js
Resolving code.jquery.com (code.jquery.com)... 69.16.175.42, 69.16.175.10, 2001:4de0:ac18::1:a:1a, ...
Connecting to code.jquery.com (code.jquery.com)|69.16.175.42|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 89664 (88K) [application/javascript]
Saving to: ‘jquery-3.6.1.min.js’

100%[========================================================================================================================================================================>] 89,664       209KB/s   in 0.4s   

2022-12-07 14:08:40 (209 KB/s) - ‘jquery-3.6.1.min.js’ saved [89664/89664]
```

以之前的导航页面做演示

> 放在`body`标签中的最下面

```html
<body>
...
    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script src="static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
</body>
```

浏览器刷新访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/342b3c345a1b4efebf4b9dc07deab7e1.png)
接下来看一下Javascript
地址: https://v3.bootcss.com/javascript/
![在这里插入图片描述](https://img-blog.csdnimg.cn/67e7a483af254eeb901f472ea083de15.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/d3b390b0c8b64a41b94552f22fcc77d0.png)

```html
<div class="container">
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
        Launch demo modal
    </button>

    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">Modal title</h4>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/01a4770b94a4461891f074db82b31532.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/ff8cd2d1484a4cd1842a1d847002a218.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/afbd7b0db2594e5a9e4aa511b1e66578.png)

> 可以观察一下这个是怎么实现点击跳出窗口的

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
    Launch demo modal
</button>
1234
```

上面的代码中,`data-toggle="modal" data-target="#myModal"`,点击按钮后会寻找带有`id=myModal`的标签

```html
<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="myModalLabel">Modal title</h4>
            </div>
            <div class="modal-body">
                ...
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
            </div>
        </div>
    </div>
</div>
```

因此我们可以知道,使用其他的标签一样可以触发点击跳转

> 将右上角的注册按钮设置为点击跳转窗口

```html
<li><a href="#" data-toggle="modal" data-target="#myModal">注册</a></li>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4ac1948a139548df857ba78037e6f4c4.png)



### 6. Javascript

- JavaScript 是一门编程语言，浏览器就是 JacaScript 语言的解释器。

- DOM 和 BOM

  ```html
  相当于编程语言的内置模块
  例如：python中的re、random、time、json模块等
  ```

- JQuery

  ```html
  相当于是编程语言的第三方模块
  例如：requests	openpyxl
  ```

  

> **意义:** 实现动态效果

先准备基础目录,拷贝之前的`bootstrap`目录

```shell
[root@hecs-33592 python]# cp -r bootstrap javascript
```

删除`javascript`中无用的`html`文件

```shell
[root@hecs-33592 python]# cd javascript/
[root@hecs-33592 javascript]# ls
main.py  static  templates
[root@hecs-33592 javascript]# cd templates/
[root@hecs-33592 templates]# ls
01.html  02.html  03.html  04.html  05.html
[root@hecs-33592 templates]# rm -rf ./*
```

首先编写一个小样例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        .menus {
            width: 200px;
            border: 1px solid red;
        }

        .menus .header {
            background-color: gold;
            padding: 20px 10px;
        }

    </style>
</head>
<body>
    <div class="menus">
        <div class="header" onclick="myFunc()">大标题</div>
        <div class="item">内容</div>
    </div>

    <script type="text/javascript">
        function myFunc() {
            alert("hello")
        }
    </script>

</body>
</html>
```

访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/2ab4e7f27fdd4fdd99b56bc4dab59a65.png)
跳出对话框
![在这里插入图片描述](https://img-blog.csdnimg.cn/c5cad061545d4341b8888caec4d5c6fb.png)
更改,使用`confirm`

```html
<script type="text/javascript">
    function myFunc() {
        // alert("hello")
        confirm("是否要继续?")
    }
</script>
123456
```

浏览器刷新访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/944dc381355944bbbbd57f61b6bd8d22.png)

#### 6.1 代码位置

**js代码的存在形式:**

- 在当前HTML文件中

  - head中
  - body中(推荐)

  > 注意: 如果写在了`head`中,`body`的`html`代码不会执行,会先执行`head`中的`javascript`之后,才会显示`html`代码

- 在其他js文件中,导入使用(一般放在 body 中)
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/391ac594ab18435586ad6e26d75e678f.png)

```html
<body>
	<script src="static/js/my.js"></script>
</body>
123
```

#### 6.2 注释

- HTML的注释

```html
<!-- 注释内容 -->
```

- CSS的注释

```css
/* 注释内容 */
```

- Javascript的注释

```javascript
// 注释内容

/* 注释内容 */
```

#### 6.3 变量

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <script type="text/javascript">
        var name = "poker";
        console.log(name);   //打印变量
    </script>
</body>
</html>·
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7bcd359c7ac34db08a5c2e5a94d137d4.png)

##### 6.3.1 字符串类型

```javascript
//声明
var name = "helloworld";
var name = String("helloworld");
```

常见功能

```javascript
var name = "中国联通"
var v1 = name.length;
var v2 = name[0];
var v3 = name.trim();			//去除空白
var v4 = name.substring(0,2)	//切片, 前取后不取
12345
```

##### 案例: 跑马灯

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>

    <div id="txt">欢迎中国联通领导poker莅临指导</div>

    <script type="text/javascript">

        function show() {
            //1.去HTML中找到某个标签并获取他的内容 (DOM)
            var tag = document.getElementById("txt");
            var dataString = tag.innerText;

            //2.动态起来,把文本中的第一个字符放在字符串的最后面
            var firstChar = dataString[0];
            var otherString = dataString.substring(1, dataString.length);
            var newText = otherString + firstChar;

            //3.在HTML标签中更新内容
            tag.innerText = newText;
        }

        //Javascript中的定时器
        //每秒钟执行这个show函数
        setInterval(show, 1000);    //毫秒
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/94b19ae09a1848d7b5f9d8f388ad54e0.png)

##### 6.3.2 数组

```javascript
var v1 = [11,22,33,44];
var v2 = Array([11,22,33,44]);

//操作
var v1 = [11,22,33,44];

v1[1]
v1[0] = "poker"

//追加
v1.push("联通");			//尾部追加 [11,22,33,44,"联通"]
v1.unshift("联通");		//头部追加 ["联通",11,22,33,44]
v1.splice(索引,0,元素);
v1.splice(1,0,"中国");	//指定位置追加 [11,"中国",22,33,44]

//删除
v1.pop();				//尾部删除
v1.shift();				//头部删除
v1.splice(索引位置,1);
v1.splice(2,1);			//索引为 2 的元素删除 [11,22,44]



//循环
var v1 = [11,22,33,44];
//循环的是索引
for(var index in v1){
	//data=v1[index]
	...
}


for(var i=0; i<v1.length; i++){
	...
}
```

##### 案例: 动态数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title> 
</head>
<body>
    
    <ul id="city">
        <!-- <li>北京</li>
        <li>天津</li>
        <li>上海</li> -->
    </ul>

    <script type="text/javascript">
        var cityList = ["北京","天津","上海"];
        for(var idx in cityList) {
            var text = cityList[idx];

            //创建 <li></li> 标签
            var tag = document.createElement("li");
            //在 li 标签中写入内容
            tag.innerText = text;

            //添加到 id=city 那个标签的里面 DOM
            var parentTag = document.getElementById("city");
            parentTag.appendChild(tag);
        }
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7bcc32463cae431d951ce06871645af6.png)

##### 6.3.3 对象(字典)

```javascript
info = {
	"name":"poker",
	"age":18,
}

info = {
	name:"poker",
	age:18
}

info.age;
info.name = "toker"

info["age"]
info["name"] = "toker";

delete info["age"]

//循环
for(var key in info){
	//key值 data=info[key]
	...
}
	
```

##### 案例: 动态表格

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>年龄</th>
            </tr>
        </thead>
        <tbody id="body">
            <tr>
                <!-- <td>1</td>
                <td>poker</td>
                <td>25</td> -->
            </tr>
        </tbody>
    </table>

    <script type="text/javascript">

        var dataList = [
            { id: 1, name: "poker", age: 25 },
            { id: 1, name: "poker", age: 25 },
            { id: 1, name: "poker", age: 25 },
            { id: 1, name: "poker", age: 25 },
            { id: 1, name: "poker", age: 25 },
            { id: 1, name: "poker", age: 25 },
        ];

        for (var idx in dataList) {
            var info = dataList[idx]
            //1.创建 tr 标签
            var tr = document.createElement("tr")
            for (var key in info) {
                var text = info[key];
                //2.创建 td 标签
                var td = document.createElement("td");
                td.innerText = text;
                tr.appendChild(td);
            }
            //3. 追加数据
            var bodyTag = document.getElementById("body");
            bodyTag.appendChild(tr);
        }
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/aee0107f1c3640d682e196379314a847.png)

#### 6.4 条件语句

```javascript
if (条件) {
	...
}else{
	...
}

if (条件) {
	...
else if (条件){
	...
}else{
	...
}
```

#### 6.5 函数

```javascript
function func(){
	...
}

//执行
func()
```

#### 6.6 DOM

> DOM 是一个模块,模块可以对HTML页面中的标签进行操作

```javascript
//根据 ID 获取标签
var tag = doucment.getElementById("xx");

//获取标签中的文本
tag.innerText

//修改标签中的文本
tag.innerText = "hhhhhhh";

// 创建标签
var tag = document.createElement("div")

// 标签写内容
tag.innerText = "xxx"
```

如标题 6.3.2 中的案例

```html
<body> 
    
    <ul id="city">
        <!-- <li>北京</li>
        <li>天津</li>
        <li>上海</li> -->
    </ul>

    <script type="text/javascript">
        var cityList = ["北京","天津","上海"];
        for(var idx in cityList) {
            var text = cityList[idx];

            //创建 <li></li> 标签
            var tag = document.createElement("li");
            //在 li 标签中写入内容
            tag.innerText = text;

            //添加到 id=city 那个标签的里面 DOM
            var parentTag = document.getElementById("city");
            parentTag.appendChild(tag);
        }
    </script>
</body>
123456789101112131415161718192021222324
```

##### 事件的绑定

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>

    <input type="text" placeholder="请输入内容" id="content">
    <input type="button" value="点击添加" onclick="addCityInfo()">

    <ul id="city">
    </ul>

        <script type="text/javascript">
        function addCityInfo() {
            //1.找到标签
            var userContent = document.getElementById("content");
            //2.获取input中用户输入的内容
            var newString = userContent.value;
            //判断用户输入是否为空
            if (newString.length > 0) {
                //3.创建 li 标签,传入用户输入的内容
                var newTag = document.createElement("li");
                newTag.innerText = newString;
                //4.标签添加到 ul 中
                var parentTag = document.getElementById("city");
                parentTag.appendChild(newTag);
                //5.将 input text 内容清空
                userContent.value = "";
            }else{
                alert("输入不能为空!")
            }
        }
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/b15752075e2b4e8989875ad33181a09a.png)

> 还有很多的`DOM`操作没有介绍,我们后面会使用`JQuery`来实现`DOM`的功能,所以这里的内容了解即可

#### 6.7知识总结

'

- 数据类型

  ```ht	ml
  常见的数据类型：int bool str list tuple dict set float None
  	- 哪些转化弄成布尔类型为 False: 空 None 0
  	- 可变和不可变划分，可变的有哪些:list set dict
  	- 可哈希和不可哈希，不可哈希的有哪些：list set dict
  	- 字典的键/集合的元素，必须是可哈希的类型( list set dict 不能做字典的键和集合元素 )
  
  主要数据类型：
  	- str
  		- 独有功能：upper / lowwer / startswitch / split / strip / join
  		注意：str 不可变 不会对原字符串进行修改 新的内容
  		- 公共功能：len / 索引 / 切片 / for循环 / 判断是否包含
  	- list 
  		- 独有功能：append insert remove pop...
  		注意：list 可变 功能很多都是对原数据操作
  		- 公共功能：len / 索引 / 切片 / for循环 / 判断是否包含
  	- dict
  		- 独有功能：get keys items values
  		- 公共功能：len / 索引 / 切片 / for循环 / 判断是否包含
  ```

  

- 函数编程

  ```html
  函数的基础指数：
  	- 定义
  	- 参数、概念：位置传参 / 关键字传参 / 参数默认值 / 动态参数 *args **kwargs
  	- 返回值
  		- 函数中一旦遇到 return 九立即返回，后续代码不再执行
  函数的进阶：
  	- python 中是为函数为作用域
  	- 全局变量和局部变量、规范：全局变量( 大写 ) 、 局部变量( 小写 )
  	- 在局部变量中可以使用 global 关键字，global 的作用？引用全局的那个变量 ( 不是在局部创建 )
  内置函数：
  	- bin/hex/odc/max/min/dicmod/sorted/open 文件操作
  
  文件操作：
  	- 基本操作：打开 操作 关闭 为了防止忘记关闭文件 `with`
  	- 打开文件时有模式：
  		- r / rb 读 			 【文件不存在，报错】				  【文件不存在，报错】
  		- w / wb 写( 清空 ) 	【文件不存在 自动创建】			【文件不存在，报错】
  		- a / ab 追加			【文件不存在 自动创建】			 【文件不存在，报错】
  
  		注意：os.mkdirs / os,path.exsits 是否存在 不存在 创建新建目录
  ```

- 模块

  ```html
  模块的分类：
  	- 自定义模块
  		- os.path 导入模块时 python 内部都回去那个目录先
  		- 自己写 py 文件时，不要与python内置模块同名
  		- import / from xx import xxx
  	- 内置模块：time datatime json re random os...
  	- 第三方模块：request openpyxl python-docx flask bs4
  查看当前目录下的所有文件：os.listdir / os.walk
  关于时间模块：时间戳 / datetime格式 / 字符串，三种时间格式可以互相转化。
  关于 Json 模块：
  	- JSON 本质是字符串，有一些自己格式的要求，例如：无元组 / 无单引
  关于 re 正则模块：
  	- 正则：\d \w
  	- 贪婪匹配和非贪婪匹配( 默认 )，想让他不贪婪 个数后面？
  	- re.search / re.match / re.findall
  第三方模块：都有哪些可以让我们安装第三方模块。
  	- pip 安装工具‘
  	- 源码
  	- wheel 包
  
  ```

- 面向对象

  ```htl
  目标：不是为了用面向对象编程
  面向对象三大特性：封装	继承	多态
  ```

- 前端开发

  ```html
  - 前端知识分为三部分：
  	- HTML 标签具有模式特点
  	- CSS  修改标签的特点
  	- JacaScript  动态
  - HTML 标签
  	- div / span / a / img / input / form / table /ul...
  	- 块级和行内标签，例如：div span 默认谁是块级标签？ div
   		注意：CSS 样式，发现行内标签设置高度，宽度，内边距，外边距都是无效
  	- form 表单 + input/selecet/textarea 数据框
  		- action 递交地址
  		- method 提交方式
  	 	- form 标签中一个 submit 标签
  		- 内部标签都需要设置name属性
  - CSS 样式
  	- 局部一定会用到的样式：div + float( 脱离文档流，clear;both;clearfix )
  	- 高度和狂赌
  	- 边距
  		- 内边距 padding
  		- 外边距 margin
  	- 字体大小 / 颜色
  	- 边框
  	- 背景颜色
  	- hover 鼠标放上去就会触发 CSS 的样式。
  	
  ```

### 7. JQuery

JQuery是一个JavaScript的第三方模块(第三方类库)

- 基于JQuery自己开发一个功能
- 现成的工具依赖JQuery, 例如: Bootstrap动态效果

JQuery的安装方式参考本文的 [5.8 Bootstrap实现动态效果](https://blog.csdn.net/qq_43139145/article/details/128073474#JQuery)

#### 7.1 快速上手

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

    <h1 id="txt">中国联通</h1>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script type="text/javascript">
        //使用JQuery修改内容
        $("#txt").text("广西移动");
    </script>

</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/9ec8552541f447ecbba224654f48e293.png)

#### 7.2 寻找标签(直接)

##### 7.2.1 ID选择器

```html
<h1 id="txt">中国联通</h1>
<h1>中国联通</h1>
<h1>中国联通</h1>
```

JQuery操作:

```javascript
$("#txt")
```

##### 7.2.2 样式选择器

```html
<h1 class="c1">中国联通</h1>
<h1 class="c2">中国联通</h1>
<h1 class="c3">中国联通</h1>
```

JQuery操作:

```javascript
$(".c1")
```

##### 7.2.3 标签选择器

```html
<h1 class="c1">中国联通</h1>
<h1 class="c2">中国联通</h1>
<h1 class="c3">中国联通</h1>
```

JQuery操作:

```javascript
$("h1")
```

##### 7.2.4 层级选择器

```html
<div class="c1">
	<div class="c2">
		<h1>123</h1>
	</div>
</div>
```

JQuery操作:

```javascript
$(".c1 .c2 h1")
```

##### 7.2.5 多选择器

```html
<div class="c1">
	<div class="c2">
		<h1>123</h1>
	</div>
</div>
<div class="c3">
	<div class="c4">
		<h1>123</h1>
		<li>456</li>
	</div>
</div>
```

JQuery操作:

```javascript
$("#c1,#c2,li")
```

##### 7.2.6 属性选择器

```html
<input type="text" name="n1" />
<input type="text" name="n2" />
<input type="text" name="n3" />
```

JQuery操作:

```javascript
$("input[name='n1']")
```

#### 7.3 寻找标签(间接)

##### 7.3.1 找到兄弟

```html
<div>
	<div>北京</div>
	<div id="c1">上海</div>
	<div>深圳</div>
	<div>广州</div>
</div>
```

JQuery操作:

```javascript
$("#c1").prev()			//上一个 <div>北京</div>
$("#c1")				// <div id="c1">上海</div>
$("#c1").next()			//下一个 <div>深圳</div>
$("#c1").next().next()	//下一个的下一个 <div>广州</div>
$("#c1").siblings()		//所有的兄弟
```

##### 7.3.2 找父子

```html
<div>
	<div>
		<div>北京</div>
		<div id="c1">
			<div>浦东新区</div>
			<div class="p10">静安区</div>
			<div>奉贤区</div>
		</div>
		<div>深圳</div>
		<div>广州</div>
	</div>
	<div>
		<div>北京</div>
		<div>上海</div>
		<div>深圳</div>
		<div>广州</div>
	</div>
</div>
```

JQuery操作:

```javascript
$("#c1").parent()			//父亲
$("#c1").parent().parent()	//父亲的父亲

$("#c1").children()			//所有的儿子
$("#c1").children(".p10")	//所有的儿子中寻找class=p10

$("#c1").find(".p10")		//所有的子孙中寻找class=p10
$("#c1").children("div")	//所有的儿子中寻找标签 div
```

#### 案例: 菜单的切换

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <style>
        .menus {
            width: 200px;
            height: 1000px;
            border: 1px solid red;
        }

        .menus .header {
            background-color: royalblue;
            padding: 5px 5px;
            border-bottom: 1px dotted gray;
            cursor: pointer;
        }

        .menus .content a {
            display: block;
            padding: 5px 5px;
            border-bottom: 1px dotted gray;
        }

        .hide {
            display: none;
        }
    </style>
</head>

<body>

    <div class="menus">
        <div class="item">
            <div class="header" onclick="clickMe(this);">天津</div>
            <div class="content hide">
                <a>静海区</a>
                <a>东丽区</a>
                <a>西青区</a>
                <a>宝坻区</a>
                <a>滨海新区</a>
            </div>
        </div>
        <div class="item">
            <div class="header" onclick="clickMe(this);">上海</div>
            <div class="content hide">
                <a>静安区</a>
                <a>奉贤区</a>
                <a>浦东新区</a>
                <a>徐汇区</a>
                <a>青浦区</a>
            </div>
        </div>
    </div>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script type="text/javascript">
        function clickMe(self) {
            var hasHide = $(self).next().hasClass("hide");
            if (hasHide) {
                $(self).next().removeClass("hide");
            } else {
                $(self).next().addClass("hide");
            }
        }
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/984e030a3cb24918b34758e553f3c51e.png)

> 功能升级: 只允许有一个是展开的

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <style>
        .menus {
            width: 200px;
            height: 1000px;
            border: 1px solid red;
        }

        .menus .header {
            background-color: royalblue;
            padding: 5px 5px;
            border-bottom: 1px dotted gray;
            cursor: pointer;
        }

        .menus .content a {
            display: block;
            padding: 5px 5px;
            border-bottom: 1px dotted gray;
        }

        .hide {
            display: none;
        }
    </style>
</head>

<body>

    <div class="menus">
        <div class="item">
            <div class="header" onclick="clickMe(this);">天津</div>
            <div class="content">
                <a>静海区</a>
                <a>东丽区</a>
                <a>西青区</a>
                <a>宝坻区</a>
                <a>滨海新区</a>
            </div>
        </div>
        <div class="item">
            <div class="header" onclick="clickMe(this);">上海</div>
            <div class="content hide">
                <a>静安区</a>
                <a>奉贤区</a>
                <a>浦东新区</a>
                <a>徐汇区</a>
                <a>青浦区</a>
            </div>
        </div>
        <div class="item">
            <div class="header" onclick="clickMe(this);">上海1</div>
            <div class="content hide">
                <a>静安区</a>
                <a>奉贤区</a>
                <a>浦东新区</a>
                <a>徐汇区</a>
                <a>青浦区</a>
            </div>
        </div>
        <div class="item">
            <div class="header" onclick="clickMe(this);">上海2</div>
            <div class="content hide">
                <a>静安区</a>
                <a>奉贤区</a>
                <a>浦东新区</a>
                <a>徐汇区</a>
                <a>青浦区</a>
            </div>
        </div>
    </div>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script type="text/javascript">
        function clickMe(self) {
            //1.让菜单展示出来
            $(self).next().removeClass("hide");

            //2.找父亲,父亲的所有兄弟,再去每个兄弟的子孙中寻找 class="content", 添加 hide 样式
            $(self).parent().siblings().find(".content").addClass("hide");
        }
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/b6fedcefb804461ca8cdedc21f1fc66a.png)

#### 7.4 值的操作

```html
<div id="c1">内容</div>
<input type="text " id="c2"/>
12
```

JQuery操作:

```javascript
$("#c1").text()				//获取文本内容
$("#c1").text("abc")		//设置文本内容

$("#c2").val()				//获取用户输入的值
$("#c2").val("嘿嘿嘿")		//设置值
```

#### 案例: 动态创建数据

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>

    <input type="text" id="txtUser" placeholder="用户名">
    <input type="text" id="txtEmail" placeholder="密码">
    <input type="button" value="提交" onclick="getInfo()">

    <ul id="view">
    </ul>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script>

        function getInfo() {
            //1.获取用户输入的用户名与密码
            var username = $("#txtUser").val();
            var email = $("#txtEmail").val();

            dataString = username + ":" + email

            //2.创建li标签, 在li内部写入内容
            var newLi = $("<li>").text(dataString);

            //3.把新创建的li标签添加到ul里面
            $("#view").append(newLi);
        }

    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c23b656b914a4949804342bfa658795b.png)

#### 7.5 事件

```html
<body>

    <ul>
        <li>百度</li>
        <li>谷歌</li>
        <li>搜狗</li>
    </ul>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script>
        $("li").click(function(){
            // 点击li标签时,自动执行这和函数
            // $(this) 当前你点击的是哪个标签
        });
    </script>
</body>
```

在JQuery可以删除指定的标签

```javascript
<script src="static/js/jquery-3.6.1.min.js"></script>
<script>
    $("li").click(function(){
        // 点击li标签时,自动执行这和函数
        // $(this) 当前你点击的是哪个标签
        $(this).remove();
    });
</script>
```

当页面框架加载完成之后执行代码

#### 案例: 表格操作

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>

    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>年龄</th>
            </tr>
        </thead>
        <tbody id="body">
            <tr>
                <td>1</td>
                <td>poker</td>
                <td>
                    <input type="button" value="删除" class="delete" />
                </td>
            </tr>
            <tr>
                <td>1</td>
                <td>poker</td>
                <td>
                    <input type="button" value="删除" class="delete" />
                </td>
            </tr>
            <tr>
                <td>1</td>
                <td>poker</td>
                <td>
                    <input type="button" value="删除" class="delete" />
                </td>
            </tr>
            <tr>
                <td>1</td>
                <td>poker</td>
                <td>
                    <input type="button" value="删除" class="delete" />
                </td>
            </tr>
        </tbody>
    </table>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script>
        $(
            function () {
                $(".delete").click(function () {
                    $(this).parent().parent().remove();
                });
            }
        )
    </script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0db419fa5c094055ace785ed54ff418e.png)

### 8. 前端整合

- HTML
- CSS
- JavaScript、jQuery
- BootStrap ）( 动态效果依赖 jQuery )

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <!-- 开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <!-- 生产版本 -->
    <!-- <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css"> -->

    <style>
        /* 去除导航栏圆角 */
        .navbar {
            border-radius: 0;
        }
    </style>

</head>

<body>


    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-9" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-9">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Home</a></li>
                    <li><a href="#">Link</a></li>
                    <li><a href="#">Link</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">One more separated link</a></li>
                        </ul>
                    </li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">登录</a></li>
                    <li><a href="#">注册</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">poker <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">个人资料</a></li>
                            <li><a href="#">我的账户</a></li>
                            <li><a href="#">个性设置</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>



    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
        Launch demo modal
    </button>

    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">Modal title</h4>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>

    <div>
        <button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="bottom"
            title="Tooltip on left">Tooltip on left</button>

        <button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="top"
            title="Tooltip on top">Tooltip on top</button>

        <button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="bottom"
            title="Tooltip on bottom">Tooltip on bottom</button>

        <button type="button" class="btn btn-default" data-toggle="tooltip" data-placement="right"
            title="Tooltip on right">Tooltip on right</button>
    </div>

    <div>
        <a id="tab" tabindex="0" class="btn btn-lg btn-danger" role="button" data-toggle="popover" data-trigger="focus" title="Dismissible popover" data-content="And here's some amazing content. It's very engaging. Right?">可消失的弹出框</a>
    </div>

    <script src="static/js/jquery-3.6.1.min.js"></script>
    <script src="static/plugins/bootstrap-3.4.1/js/bootstrap.js"></script>


    <div class="container" style="width: 800px;height:600px">
        <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li data-target="#carousel-example-generic" data-slide-to="0" class=""></li>
              <li data-target="#carousel-example-generic" data-slide-to="1" class=""></li>
              <li data-target="#carousel-example-generic" data-slide-to="2" class="active"></li>
            </ol>
            <div class="carousel-inner" role="listbox">
              <div class="item">
                <img data-src="holder.js/900x500/auto/#777:#555/text:First slide" alt="First slide [900x500]" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iOTAwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDkwMCA1MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiPjwhLS0KU291cmNlIFVSTDogaG9sZGVyLmpzLzkwMHg1MDAvYXV0by8jNzc3OiM1NTUvdGV4dDpGaXJzdCBzbGlkZQpDcmVhdGVkIHdpdGggSG9sZGVyLmpzIDIuNi4wLgpMZWFybiBtb3JlIGF0IGh0dHA6Ly9ob2xkZXJqcy5jb20KKGMpIDIwMTItMjAxNSBJdmFuIE1hbG9waW5za3kgLSBodHRwOi8vaW1za3kuY28KLS0+PGRlZnM+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48IVtDREFUQVsjaG9sZGVyXzE4NGY0NjIyODJjIHRleHQgeyBmaWxsOiM1NTU7Zm9udC13ZWlnaHQ6Ym9sZDtmb250LWZhbWlseTpBcmlhbCwgSGVsdmV0aWNhLCBPcGVuIFNhbnMsIHNhbnMtc2VyaWYsIG1vbm9zcGFjZTtmb250LXNpemU6NDVwdCB9IF1dPjwvc3R5bGU+PC9kZWZzPjxnIGlkPSJob2xkZXJfMTg0ZjQ2MjI4MmMiPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNTAwIiBmaWxsPSIjNzc3Ii8+PGc+PHRleHQgeD0iMzA4LjI4NzQ5MDg0NDcyNjU2IiB5PSIyNzAuMTYwMDAxMzczMjkxMDQiPkZpcnN0IHNsaWRlPC90ZXh0PjwvZz48L2c+PC9zdmc+" data-holder-rendered="true">
              </div>
              <div class="item">
                <img data-src="holder.js/900x500/auto/#666:#444/text:Second slide" alt="Second slide [900x500]" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iOTAwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDkwMCA1MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiPjwhLS0KU291cmNlIFVSTDogaG9sZGVyLmpzLzkwMHg1MDAvYXV0by8jNjY2OiM0NDQvdGV4dDpTZWNvbmQgc2xpZGUKQ3JlYXRlZCB3aXRoIEhvbGRlci5qcyAyLjYuMC4KTGVhcm4gbW9yZSBhdCBodHRwOi8vaG9sZGVyanMuY29tCihjKSAyMDEyLTIwMTUgSXZhbiBNYWxvcGluc2t5IC0gaHR0cDovL2ltc2t5LmNvCi0tPjxkZWZzPjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+PCFbQ0RBVEFbI2hvbGRlcl8xODRmNDYxZjZhOCB0ZXh0IHsgZmlsbDojNDQ0O2ZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1mYW1pbHk6QXJpYWwsIEhlbHZldGljYSwgT3BlbiBTYW5zLCBzYW5zLXNlcmlmLCBtb25vc3BhY2U7Zm9udC1zaXplOjQ1cHQgfSBdXT48L3N0eWxlPjwvZGVmcz48ZyBpZD0iaG9sZGVyXzE4NGY0NjFmNmE4Ij48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjUwMCIgZmlsbD0iIzY2NiIvPjxnPjx0ZXh0IHg9IjI2NC45NDM3NDA4NDQ3MjY1NiIgeT0iMjcwLjE2MDAwMTM3MzI5MTA0Ij5TZWNvbmQgc2xpZGU8L3RleHQ+PC9nPjwvZz48L3N2Zz4=" data-holder-rendered="true">
              </div>
              <div class="item active">
                <img data-src="holder.js/900x500/auto/#555:#333/text:Third slide" alt="Third slide [900x500]" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9InllcyI/PjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iOTAwIiBoZWlnaHQ9IjUwMCIgdmlld0JveD0iMCAwIDkwMCA1MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89Im5vbmUiPjwhLS0KU291cmNlIFVSTDogaG9sZGVyLmpzLzkwMHg1MDAvYXV0by8jNTU1OiMzMzMvdGV4dDpUaGlyZCBzbGlkZQpDcmVhdGVkIHdpdGggSG9sZGVyLmpzIDIuNi4wLgpMZWFybiBtb3JlIGF0IGh0dHA6Ly9ob2xkZXJqcy5jb20KKGMpIDIwMTItMjAxNSBJdmFuIE1hbG9waW5za3kgLSBodHRwOi8vaW1za3kuY28KLS0+PGRlZnM+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48IVtDREFUQVsjaG9sZGVyXzE4NGY0NjFmMTEyIHRleHQgeyBmaWxsOiMzMzM7Zm9udC13ZWlnaHQ6Ym9sZDtmb250LWZhbWlseTpBcmlhbCwgSGVsdmV0aWNhLCBPcGVuIFNhbnMsIHNhbnMtc2VyaWYsIG1vbm9zcGFjZTtmb250LXNpemU6NDVwdCB9IF1dPjwvc3R5bGU+PC9kZWZzPjxnIGlkPSJob2xkZXJfMTg0ZjQ2MWYxMTIiPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNTAwIiBmaWxsPSIjNTU1Ii8+PGc+PHRleHQgeD0iMjk4LjMxMjUiIHk9IjI3MC4xNjAwMDEzNzMyOTEwNCI+VGhpcmQgc2xpZGU8L3RleHQ+PC9nPjwvZz48L3N2Zz4=" data-holder-rendered="true">
              </div>
            </div>
            <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
              <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
              <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
    </div>

    <script>
        $(function () {
            $('[data-toggle="tooltip"]').tooltip()
        });
        $('#tab').popover('hide').popover({trigger: "click", placement: "bottom"});
    </script>
</body>
</html>	
```

#### 案例: 添加数据页面

> 人员信息录入功能,需要提供用户信息:
>
> - 用户名
> - 年龄
> - 薪资
> - 部门
> - 入职时间
>   …

对于时间的选择: 插件(datetimepicker),或者可以直接使用`<input type="date" class="form-control" placeholder="入职时间">`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <!-- 开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <!-- 生产版本 -->
    <!-- <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css"> -->

    <style>

    </style>

</head>

<body>


    <div class="container">
        <form class="form-horizontal" style="margin-top: 30px;">
            <!-- 引入栅格系统 -->
            <!-- 姓名和年龄 -->
            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">姓名</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" placeholder="姓名">
                        </div>
                    </div>
                </div>
                <div class="col-xs-6">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">年龄</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" placeholder="年龄">
                        </div>
                    </div>
                </div>
            </div>

            <!-- 部门和薪资 -->
            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">部门</label>
                        <div class="col-sm-10">
                            <select class="form-control">
                                <option>IT部</option>
                                <option>运营部</option>
                                <option>销售部</option>
                                <option>售前部</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div class="col-xs-6">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">薪资</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" placeholder="薪资">
                        </div>
                    </div>
                </div>
            </div>

            <!-- 入职时间和密码 -->
            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">入职时间</label>
                        <div class="col-sm-10">
                            <input type="date" class="form-control" placeholder="入职时间">
                        </div>
                    </div>
                </div>
                <div class="col-xs-6">
                    <div class="form-group">
                        <label for="inputPassword3" class="col-sm-2 control-label">密码</label>
                        <div class="col-sm-10">
                            <input type="password" class="form-control" placeholder="密码">
                        </div>
                    </div>
                </div>
            </div>

            <div class="row clearfix">
                <div class="col-xs-6">
                    <div class="form-group">
                        <div class="col-sm-offset-2 col-sm-10">
                            <button type="submit" class="btn btn-primary">Sign in</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>

</body>
</html>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/dd2423c3696f4e7fbf932cfba0b384e1.png)

#### Python管理数据库

##### 添加数据

代码实现

> Python 代码实现:
>
> - 添加用户
> - 删除用户
> - 查看用户
> - 更新用户信息

安装pymysql包

```shell
pip3 install pymysql
1
```

编辑python文件

```python
##!/usr/bin/env python3

import pymysql

## 1.连接Mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Syz123!@#', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令
cursor.execute("insert into admin(username, password, mobile) values('poker', '123456', '12345678912');")
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

运行

```shell
/bin/python3 /root/python/Mysql/createData.py
```

验证

```sql
mysql> select * from admin;
+----+----------+----------+-------------+
| id | username | password | mobile      |
+----+----------+----------+-------------+
|  3 | poker    | 123456   | 12345678912 |
+----+----------+----------+-------------+
1 row in set (0.00 sec)

```

> 优化

```python
##!/usr/bin/env python3

import pymysql

## 1.连接Mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Syz123!@#', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令
sql = "insert into admin(username, password, mobile) values(%s, %s, %s);"
cursor.execute(sql, ['toker', '123456', '12355674325'])
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

> 注意: sql语句不要使用字符串格式化,有会SQL注入的风险,需要使用 cursor.execute(sql, [参数1, 参数2, …])

##### 查询数据

```python
##!/usr/bin/env python3

import pymysql

## 1.连接Mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='Syz123!@#', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令
sql = "select * from admin where id > %s"
cursor.execute(sql, [2, ])
## data_list = cursor.fetchall()		查询一条数据,为字典
data_list = cursor.fetchall()		# 查询所有符合条件的数据,为列表套多个
字典
for row_dict in data_list:
    print(row_dict)

## 3.关闭
cursor.close()
conn.close()
```

输出结果如下

```shell
[root@hecs-33592 ~]# /bin/python3 /root/python/Mysql/searchData.py 
{'id': 3, 'username': 'poker', 'password': '123456', 'mobile': '12345678912'}
{'id': 4, 'username': 'toker', 'password': '123456', 'mobile': '12355674325'}
```

##### 删除数据

> 删除 `id` 大于 3 的行

```python
##!/usr/bin/env python3

import pymysql

## 1.连接Mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='Syz123!@#', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令
sql = "delete from admin where id > %s"
cursor.execute(sql, [3, ])
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

##### 修改数据

```python
##!/usr/bin/env python3

import pymysql

## 1.连接Mysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='Syz123!@#', charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令
sql = "update admin set mobile=%s where id = %s"
cursor.execute(sql, ['12332145665', 3])
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

#### 强调

- 在进行 新增 删除 修改时，一定要记得 commit 不然数据库没有数据

  cursor.execurte(sql)

  conn.commit()

- 在查询时，不需要 commit，执行 fetchall / fetchone

  ```python
  cursor.exceccute("...")
  
  # 第一条数据 字典 无数据时是空列表
  v1 = cursor,fetchone()
  # 所有数据 列表套字典 无数据时是 None
  v1 = cursor.fetchall()
  ```

- 对于 sql 语句不要使用 python 的字符串格式化( 会被 sql 注入 )，一定要使用 execute( )+参数

  ```python
  cursor.execute("%s....%s",["xx","xxx"]) 
  ```

  

### 案例: Flask + Mysql

main.py

```python
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/add/user", methods=['GET', 'POST'])
def addUser():
    if request.method == 'GET':
        return render_template("addUser.html")
    else:
        username = request.form.get('user')
        password = request.form.get('pwd')
        mobile = request.form.get('mobile')

        # 1.连接Mysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                            passwd='Syz123!@#', charset='utf8', db='unicom')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 2.发送指令
        sql = "insert into admin(username, password, mobile) values(%s, %s, %s);"
        cursor.execute(sql, [username, password, mobile])
        conn.commit()

        # 3.关闭
        cursor.close()
        conn.close()

        return "添加成功"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
```

编写一个简单的前端页面添加数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>添加用户</h1>
    <form method="post" action="/add/user">
        <input type="text" name="user" placeholder="用户名">
        <input type="text" name="pwd" placeholder="密码">
        <input type="text" name="mobile" placeholder="手机号">
        <input type="submit" value="提 交">
    </form>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/22bc418316e14793b4474e491b6be6fb.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/396ac74ddec64d3b94b9b99017ac7463.png)

```sql
mysql> select * from admin;
+----+----------+----------+-------------+
| id | username | password | mobile      |
+----+----------+----------+-------------+
|  3 | poker    | 123456   | 12332145665 |
|  5 | roker    | 123456   | 4563112345  |
+----+----------+----------+-------------+
1234567
```

### 案例: 查询所有用户

main.py

```python
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/add/user", methods=['GET', 'POST'])
def addUser():
    if request.method == 'GET':
        return render_template("addUser.html")
    else:
        username = request.form.get('user')
        password = request.form.get('pwd')
        mobile = request.form.get('mobile')

        # 1.连接Mysql
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                            passwd='Syz123!@#', charset='utf8', db='unicom')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 2.发送指令
        sql = "insert into admin(username, password, mobile) values(%s, %s, %s);"
        cursor.execute(sql, [username, password, mobile])
        conn.commit()

        # 3.关闭
        cursor.close()
        conn.close()

        return "添加成功"


@app.route("/show/user", methods=['GET', 'POST'])
def showUser():
    username = request.form.get('user')
    password = request.form.get('pwd')
    mobile = request.form.get('mobile')

    # 1.连接Mysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                        passwd='Syz123!@#', charset='utf8', db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2.发送指令
    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 3.关闭
    cursor.close()
    conn.close()
	// 返回到前端showUser.html 数据是data_list
    return render_template("showUser.html", data_list=data_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)

```

编写HTML文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>用户列表</h1>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>密码</th>
                <th>手机号</th>
            </tr>
        </thead>
        <tbody>
            {% for item in data_list %}
            <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.username }}</td>
                <td>{{ item.password }}</td>
                <td>{{ item.mobile }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/47208d415ead46139a397ad12df23896.png)
优化

> 加入 `bootstrap.css`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="../static/plugins/bootstrap-3.4.1/css/bootstrap.css">

</head>
<body>
    <div class="container">
        <h1>用户列表</h1>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>姓名</th>
                    <th>密码</th>
                    <th>手机号</th>
                </tr>
            </thead>
            <tbody>
                {% for item in data_list %}
                <tr>
                    <td>{{ item.id }}</td>
                    <td>{{ item.username }}</td>
                    <td>{{ item.password }}</td>
                    <td>{{ item.mobile }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    
</body>
</html>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/b9b9ec633e634e4590ef4905e9832902.png)

## Django

### 安装Django

```
c:/python39
	- python.exe
	- Scripts
		- pip.exe
		- django-admin.exe 	【工具，创建 django 项目】
	- Lib
		- 内置模块
		- site-packages
			- openpyxl
			- python-docx
			- flask
			- django 		【框架的源码】
```

#### 安装Python

```bash
## 安装依赖
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel gcc


wget https://www.python.org/ftp/python/3.8.15/Python-3.8.15.tgz
tar xf Python-3.8.15.tar.xz
cd Python-3.8.15
./configure --prefix=/usr/local/python3
make && make install

## 删除旧软链接
rm -rf /usr/bin/python3
rm -rf /usr/bin/pip3

## 新添加软链接
ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip3
```

#### pip加速

```bash
cd ~
mkdir .pip
vi .pip/pip.conf
## 增加如下内容
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

#### 安装Django

```bash
pip3 install django

## 新版跟老版不太一样,需要自己设置软链接
ln -s /usr/local/python3/bin/django-admin /usr/bin/django-admin
```

#### 创建项目

- 打开终端

- 进入某个目录

  ```
  /User/Django_learn/Django_
  ```

- 执行命令创建项目

  ```
  "c:\python39\Scripts\django-admin.exe" startproject 项目名称
  ```

  ```
  # 如果 c:\python39\Scripts 已经加入环境系统变量
  django-admin startproject 项目名称
  ```

- 特殊说明

  - 命令行，创建的项目是标准的

  - pycharm 在标准的基础上默认加了点东西

    - 创建了一个 temlpates目录 [删除]

    - settings.py 中 [删除]

      ![image-20230811100020411](https://imgtroage-1317162111.cos.ap-nanjing.myqcloud.com/img/image-20230811100020411.png)

**Linux**

```bash
django-admin startproject web
```

报错

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/usr/local/python3/lib/python3.8/site-packages/django/db/backends/base/base.py", line 282, in ensure_connection

  ...           

  File "/usr/local/python3/lib/python3.8/site-packages/django/db/backends/sqlite3/_functions.py", line 45, in register
    create_deterministic_function("django_date_extract", 2, _sqlite_datetime_extract)
pysqlite3.dbapi2.NotSupportedError: deterministic=True requires SQLite 3.8.3 or higher

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/python3/lib/python3.8/threading.py", line 932, in _bootstrap_inner
  
    ...

  File "/usr/local/python3/lib/python3.8/site-packages/django/db/backends/sqlite3/_functions.py", line 45, in register
    create_deterministic_function("django_date_extract", 2, _sqlite_datetime_extract)
django.db.utils.NotSupportedError: deterministic=True requires SQLite 3.8.3 or higher
```

解决办法

```bash
pip3 install pysqlite3
pip3 install pysqlite3-binary

vim /usr/local/python3/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py
## 修改内容
## from sqlite3 import dbapi2 as Database (注释掉这段)
from pysqlite3 import dbapi2 as Database # 启用pysqlite3
## :wq 保存即可
```

再次运行

```bash
[root@hecs-33592 web]# python3 manage.py runserver 0.0.0.0:8000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
November 24, 2022 - 09:16:47
Django version 4.1.3, using settings 'web.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/d58443de6f6c4fe091894c03a4e324a1.png)
报错了,修改ALLOWED_HOSTS
![在这里插入图片描述](https://img-blog.csdnimg.cn/25977721dc764022adad529a33c9796c.png)
后面我们直接使用`VSCode`进行项目的编辑与运行,有条件的同学可以考虑使用`Pycharm`

#### 文件介绍

```shell
web
├── db.sqlite3
├── manage.py			# 项目的管理,包括: 启动项目,创建app, 数据管理
└── web
    ├── asgi.py			# 接收网络请求
    ├── __init__.py
    ├── settings.py		# 项目配置(模板配置,数据库配置,注册app)
    ├── urls.py			# url和函数的对应关系
    └── wsgi.py			# 接收网络请求
    
    
Django_
├── manage.py			# 项目的管理,包括: 启动项目,创建app, 数据管理
└── Django_
    ├── __init__.py
    ├── settings.py		# 项目配置(模板配置,数据库配置,注册app)
    ├── urls.py			# url和函数的对应关系
    └── wsgi.py			# 接收网络请求 同步
    ├── asgi.py			# 接收网络请求 异步
    
```

#### 简单访问

在 `/root/python/web/web`下新增一个 `views.py` 文件

```python
from django.http import HttpResponse
def index(req):
    return HttpResponse('<h1>welcome to Django</h1>')
```

配置`/root/python/web/web` 下的`urls.py` 文件

```python
from django.contrib import admin
from django.urls import path
from . import views    # 导入我们刚刚创建的views.py文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # 新增这一行,''为空表示默认访问 ip:端口
]
```

启动

```shell
cd /root/python/web/
python3 manage.py runserver 0.0.0.0:5900
```

浏览器访问测试

![img](https://img-blog.csdnimg.cn/aec928edcbad454fab7170171a2786f1.png)

### APP

```
- 项目
	- app，用户管理 【表结构，函数，HTML模板，CSS】
	- app，订单管理 【表结构，函数，HTML模板，CSS】
	- app，后台管理 【表结构，函数，HTML模板，CSS】
	- app，网站	【表结构，函数，HTML模板，CSS】
	- app，API	  【表结构，函数，HTML模板，CSS】
	....
```



#### 添加新的app

进入linux命令行,执行以下命令

```bash
[root@hecs-33592 web]# pwd
/root/python/web
[root@hecs-33592 web]# django-admin startapp blog
[root@hecs-33592 web]# ls
blog  db.sqlite3  manage.py  web
[root@hecs-33592 web]# tree blog/

Django_learn
├── Django_	
    ├── admin.py		# 【固定不用动】 django 默认提供了 admin 后台管理 
    ├── apps.py			# 【固定不用动】app 启动类
    ├── __init__.py
    ├── migrations		# 【固定不用动】数据库变更记录
    │    └── __init__.py	
    ├── models.py		# 【**重要**】对数据库操作
    ├── tests.py		# 单元测试
    └── views.py		# 【**重要**】函数
├── manage.py			# 项目的管理,包括: 启动项目,创建app, 数据管理
└── Django_learn
    ├── __init__.py
    ├── settings.py		# 项目配置(模板配置,数据库配置,注册app)
    ├── urls.py			# url和函数的对应关系
    └── wsgi.py			# 接收网络请求 同步
    ├── asgi.py			# 接收网络请求 异步
```

应用【blog】中各个目录作用：

- **migrations:** 用于记录models中数据的变更。
- **admin.py:** 映射models中的数据到Django自带的admin后台。
- **apps.py:** 在新的Django版本中新增，用于应用程序的配置。
- **models.py:** 创建应用程序数据表模型（对应数据库的相关操作)。
- **test.py:** 创建Django测试。
- **views.py:** 控制向前端显示那些数据

#### 注册app

修改`/root/python/web/web` 下的`settings.py`
![在这里插入图片描述](https://img-blog.csdnimg.cn/d60e0d9b2dc74a379b92247b81b0cd85.png)

#### 创建blog的页面

编辑`/root/python/web/blog` 下的`views.py` 视图函数

```python
from django.shortcuts import render
from django.http import HttpResponse
def index_app(req):
    return HttpResponse('welcome to Django blog!')
```

编辑`/root/python/web/web` 下的`urls.py` 来指定访问路由

```python
from django.contrib import admin
from django.urls import path
from blog.views import index_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', index_app),
]
```

命令行启动Django应用

```shell
cd /root/python/web/
python3 manage.py runserver 0.0.0.0:5900
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/425f958d8df54d67a690efe088789d3b.png)

> 再来一个

编辑`/root/python/web/blog` 下的`views.py` 视图函数

```python
from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    return HttpResponse("用户列表")

def index_app(req):
    return HttpResponse('<h1>welcome to Django blog!</h1>')
12345678
```

编辑`/root/python/web/web` 下的`urls.py` 来指定访问路由

```python
from django.contrib import admin
from django.urls import path
from blog.views import index_app
from blog.views import user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', index_app),
    path('user_list/', user_list),
]
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/33641363f9cc4b07b23a4fc53b4d282f.png)

### templates模板

> 为了使用HTML,这里开始引入templates模板

**注意:** 可以在app下创建`templates`目录,也可以在主目录下创建`templates`目录

接下来可以做个测试

编辑`/root/python/web/blog` 下的`views.py` 视图函数

```python
from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    # 1.优先去项目的根目录下寻找
    # 2.根据app的注册顺序去app的目录下templates下寻找
    return render(request, "user_list.html")
```

编辑`/root/python/web/blog/templates`下的`user_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <h1>用户列表</h1>
</body>
</html>
```

编辑`/root/python/web/templates`下的`user_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <h1>根目录,用户列表</h1>
</body>
</html>
```

浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/4d7d9aa0326e43028114777346c41ca7.png)

> 1.优先去项目的根目录`templates`下寻找
> 2.根据`app`的注册顺序去项目`app`的目录下的`templates`下寻找

### templates模板语法

创建一个新的模板页面
编辑`web`下的`urls.py`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
]
```

编辑APP`blog`下的`views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    # 1.优先去项目的根目录下寻找
    # 2.根据app的注册顺序去app的目录下templates下寻找
    return render(request, "user_list.html")

def index_app(req):
    return HttpResponse('<h1>welcome to Django blog!</h1>')

## 新增下面的内容
def tpl(request):
    return render(request, "tpl.html")
```

在`blog/templates`下新建`tpl.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>templates模板语法</h1>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/1205d600e8b74494af9822ca775acdbb.png)

#### 单一变量

> 如果说我们从数据库中取到了数据,如何在`html`页面中进行展示呢,这里需要用到templates的基本语法

修改`blog`下的`views.py`

```python
def tpl(request):
    name = "poker"
    return render(request, "tpl.html", {"name":name})
```

修改`blog/templates`下的`tpl.html`

```html
<body>
    <h1>templates模板语法</h1>
    <li>姓名: {{ name }}</li>
</body>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c824c72e91b843b2acf56d45633fe326.png)

> 这样,`name`参数就被传到HTML页面中展示了出来

#### 列表

```python
def tpl(request):
    
    name = "poker"
    roles_list = ['服务员1', '服务员2', '服务员3']
    
    return render(request, "tpl.html", {"name":name, "roles_list":roles_list})
<body>
    <h1>templates模板语法</h1>
    <li>姓名: {{ name }}</li>
    <li>服务员:{{ roles_list }}</li>
    <li>服务员:{{ roles_list.0 }}</li>
    <li>服务员:{{ roles_list.1 }}</li>
    <li>服务员:{{ roles_list.2 }}</li>
</body>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4a12a20abf25445da6d0cd415211319d.png)

#### 循环(列表)

修改`blog/templates`下的`tpl.html`

```html
<div>
    列表循环:
    {% for item in roles_list %}
        <span>{{ item }}</span>
    {% endfor %}
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e9ee08c86ced4ebab72d44ede528dc60.png)

#### 字典

修改`blog`下的`views.py`

```python
def tpl(request):

    name = "poker"
    roles_list = ['服务员1', '服务员2', '服务员3']
    user_info = {"name": "张三", "age": 25, "sex": "男"}

    return render(request, "tpl.html", {"name": name, "roles_list": roles_list, "user_info": user_info})
```

修改`blog/templates`下的`tpl.html`

```html
<div>
    {{ user_info }}<br>
    {{ user_info.name }}
    {{ user_info.age }}
    {{ user_info.sex }}
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/3cae9996cbf54d2c83de9dd86f5bd0dc.png)

#### 循环(字典)

修改`blog/templates`下的`tpl.html`

> 获取值 `values`

```html
<div>
    {% for v in user_info.values %}
        <li>{{ v }}</li>
    {% endfor %}
</div>
```

> 获取键 `keys`

```html
    <div>
        {% for k in user_info.keys %}
            <li>{{ k }}</li>
        {% endfor %}
    </div>
```

> 获取键和值 `items`

```html
<div>
    {% for k,v in user_info.items %}
        <li>{{ k }} = {{ v }}</li>
    {% endfor %}
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e62ca12a693b443990ddf5c7577c65d7.png)

#### 列表套字典

修改`blog`下的`views.py`

```python
def tpl(request):

    name = "poker"
    roles_list = ['服务员1', '服务员2', '服务员3']
    user_info = {"name": "张三", "age": 25, "sex": "男"}

    date_list = [
        {"name": "张三", "age": 25, "sex": "男"},
        {"name": "李四", "age": 18, "sex": "男"},
        {"name": "王五", "age": 22, "sex": "女"},
    ]

    return render(request, "tpl.html", {"name": name, "roles_list": roles_list, "user_info": user_info, "data_list":date_list})
```

修改`blog/templates`下的`tpl.html`

```html
<div>
    {% for item in data_list %}
        <div>{{ item.name }} {{ item.age }} {{ item.sex }}</div>
    {% endfor %}
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/da00812ba83d43168da4e694133dfd81.png)

#### 条件判断

修改`blog/templates`下的`tpl.html`

```html
{%  if name == "poker" %}
    <h3>嘿嘿嘿</h3>
{% elif name == "toker" %}
    <h3>哈哈哈</h3>
{% else %}
    <h3>呵呵呵</h3>
{% endif %}
```

> 先介绍这些常用的语法,其实还有很多的语法,感兴趣的可自行百度.

### 请求和响应

**重定向:** 浏览器向某个网站发送请求,网站返回给浏览器一个新的URL,浏览器去访问这个新的URL地址
修改`blog`下的`views.py`, 根据情况去掉下面代码的注释进行测试

```python
## 导入 redirect 包
from django.shortcuts import render, redirect
...

## 增加新函数
def something(request):
    # request 是一个对象,封装了用户发送过来的所有请求相关数据

    # 1.[请求]获取请求的方式
    print("用户请求的方式: " + request.method)

    # 2.[请求]在URL上传递值, 例如: http://123.249.26.154:5900/something/?n1=1&n2=2
    print(request.GET)

    # 3.[请求]在请求体中提交数据,目前是空值
    print(request.POST)

    # 4.[响应]HttpResponse("返回内容"), 内容字符串内容返回给请求者
    # return HttpResponse("返回内容")

    # 5.[响应]读取HTML的内容 + 渲染(替换) => 字符串,返回给用户浏览器
    # 需要在 blog/templates 下新建`something.html`
    #return render(request, 'something.html', {"title": "hello"})

    # 6.[响应] 让浏览器重定向到其他的页面 
    return redirect("http://www.baidu.com")
```

修改`web/web/urls.py`,增加`something`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
]
```

#### 案例: 用户登录

修改`blog`下的`views.py`,新增`login`函数

```python
def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是 POST 请求,获取用户提交的数据
    print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("password")
    if username == "poker" and password == "123":
        return HttpResponse("登录成功") 

    #return HttpResponse("登录失败")
    return render(request, "login.html", {"error_msg": "用户名或密码错误"})
```

修改`web/web/urls.py`,增加`login`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
]
```

在`blog/templates`下新建`login.html`

> {% csrf_token %} 必须加上

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <h1>用户登录</h1>
    <form method="post" action="/login/">

        {% csrf_token %}

        <input type="text" name="user", placeholder="用户名">
        <input type="password" name="password", placeholder="密码">
        <input type="submit" value="提交"> 
        <span style="color: red;">{{ error_msg }}</span>
    </form>
</body>
</html>
```

浏览器访问,输入错误的用户名和密码
![在这里插入图片描述](https://img-blog.csdnimg.cn/08281fd0a0c54eea922d4ec2c828e93e.png)

### 数据库操作

Django开发操作数据库更简单,内部提供了ORM框架

#### 安装第三方模块

> mysqlclient

直接安装可能会报错
![在这里插入图片描述](https://img-blog.csdnimg.cn/6b02fd9305e84e0f9f15f5f8e16cfae8.png)
**解决办法**
参考链接: https://blog.csdn.net/m0_67155975/article/details/123138225

```shell
yum -y install mysql-devel
yum -y install python-devel
pip3 install mysqlclient
```

#### ORM

ORM可以帮助我们做两件事;

- 创建/修改/删除数据库中的表(无法创建数据库)
- 操作表中的数据

##### 创建数据库

```sql
create database mydb DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/45d1e747a5b84bac9a57b26e7954f6bd.png)

##### Django连接数据库

修改`web/web/settings.py`
![在这里插入图片描述](https://img-blog.csdnimg.cn/ad5e7c4c4faf4ee3a52746e23e98df06.png)
增加如下内容

```python
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'mydb',
        'USER':'root',
        'PASSWORD':'Syz123!@#',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

##### Django操作表

- 创建表
- 删除表
- 修改表

配置`blog`下的`models.py`

> 会根据自定义的类创建跟app同名的表

```python
from django.db import models

## Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()

"""
create table UserInfo(
    id bigint auto_increment primary key,
    name varchar(20),
    password varchar(20),
    age int
)
"""
```

在服务器中项目根目录下执行命令

> 如果不想要某个表了,将[class类](https://so.csdn.net/so/search?q=class类&spm=1001.2101.3001.7020)注释后,重新执行下面的命令即可

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

注意: app需要提前注册
![在这里插入图片描述](https://img-blog.csdnimg.cn/d74b70e0aaf346dfa1f606638e15b0aa.png)
查看Mysql数据库
![在这里插入图片描述](https://img-blog.csdnimg.cn/136a1ca514544c769cdbb3c176225ee5.png)
修改表的话,如果原表中存有数据,此时如果增加一个新的列,需要设定一个默认值

- 手动设定

```python
age = models.IntegerField(default=2)
```

- 允许为空

```python
data = models.IntegerField(null=True, blank=True)
```

##### Django操作表数据

- 添加数据

修改`blog`下的`views.py`

```python
from blog.models import UserInfo
...

def orm(request):
    # 新建数据
    UserInfo.objects.create(name="poker", password="123", age=25)
    UserInfo.objects.create(name="roker", password="456", age=30)

    return HttpResponse("成功")

```

修改`web/web/urls.py`,增加`orm`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
]
```

浏览器访问页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/103b66bbe54343b48f5d734002364576.png)
查看Mysql数据库
![在这里插入图片描述](https://img-blog.csdnimg.cn/1c5306636d94469193592ddad18fc4d2.png)

- 删除数据

```python
	# 删除数据
    UserInfo.objects.filter(id=2).delete()
    # 删除表中所有数据
    UserInfo.objects.all().delete()
```

- 获取数据

```python
## data_list = [行,行,行] QuerySet 类型 每一行都是对象
data_list = UserInfo.objects.all()
print(data_list)
for obj in data_list:
    print(obj.id, obj.name, obj.password, obj.age)
## 获取第一行的数据    
row_obj = UserInfo.objects.filters(id=1).first()
```

浏览器刷新访问,观察工作台输出
![在这里插入图片描述](https://img-blog.csdnimg.cn/04cc285ab9994510b7458ba3ec0e87a0.png)

- 更新数据

```python
UserInfo.objects.filter(name="roker").update(age=35)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c285f7dd3aa741229ade66a9dfae5f16.png)

#### 案例:用户管理

##### 展示用户列表

修改`web/web/urls.py`,增加`info/list`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list)
]
```

修改`blog`下的`views.py`

```python
from blog.models import UserInfo
...

def info_list(request):
    data_list = UserInfo.objects.all()

    return render(request, "info_list.html", {"data_list": data_list})
```

在`blog/templates`下新增`info_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>密码</th>
                <th>年龄</th>
            </tr>
        </thead>
        <tbody>
            {% for obj in data_list %}
                <tr>
                    <td>{{ obj.id }}</td>
                    <td>{{ obj.name }}</td>
                    <td>{{ obj.password }}</td>
                    <td>{{ obj.age }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/fb4b0e12fc794b3db92f33aed5817fba.png)

##### 添加用户

修改`web/web/urls.py`,增加`info/list`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
]
```

修改`blog`下的`views.py`

```python
def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')

    # 获取用户提交的数据
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")

    # 添加到数据库
    UserInfo.objects.create(name=name, password=password, age=age)

    # 自动跳转
    return redirect("/info/list/")
```

在`blog/templates`下新增`info_add.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <form action="/info/add/" method="post">

        {% csrf_token %}

        <input type="text" name="name" placeholder="用户名">
        <input type="text" name="password" placeholder="密码">
        <input type="text" name="age" placeholder="年龄">
        <input type="submit" value="提交">
    </form>
</body>
</html>
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/eba6ee3613fa4591827e17f83f19a07d.png)
点击"提交"
![在这里插入图片描述](https://img-blog.csdnimg.cn/83cbcde3a4ce438baa853f666f7aca96.png)
在`info/list`页面增加"添加"按钮
修改`blog/templates`下`info_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <a href="/info/add">添加</a>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>密码</th>
                <th>年龄</th>
            </tr>
        </thead>
        <tbody>
            {% for obj in data_list %}
                <tr>
                    <td>{{ obj.id }}</td>
                    <td>{{ obj.name }}</td>
                    <td>{{ obj.password }}</td>
                    <td>{{ obj.age }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c9a0632759e54af1808a1e5c4be54939.png)
点击"添加"后,即可跳转回添加页面

##### 删除用户

修改`web/web/urls.py`,增加`info/list`

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_app/', views.index_app),
    path('user_list/', views.user_list),
    path('tpl/', views.tpl),
    path('something/', views.something),
    path('login/', views.login),
    path('orm/', views.orm),
    path('info/list/', views.info_list),
    path('info/add/', views.info_add),
    path('info/delete/', views.info_delete)
]
```

修改`blog`下的`views.py`

```python
def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
1234
```

修改`blog/templates`下的`info_list.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <a href="/info/add">添加</a>
    <table border="1">
        <thead>
            <tr>
                <th>ID</th>
                <th>姓名</th>
                <th>密码</th>
                <th>年龄</th>
                <th>操作</th>
            </tr>
        </thead>
        <tbody>
            {% for obj in data_list %}
                <tr>
                    <td>{{ obj.id }}</td>
                    <td>{{ obj.name }}</td>
                    <td>{{ obj.password }}</td>
                    <td>{{ obj.age }}</td>
                    <td>
                        <a href="/info/delete?nid={{ obj.id }}">删除</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

浏览器访问,点击"删除"即可将对应的行删除
![在这里插入图片描述](https://img-blog.csdnimg.cn/5f01978b91d646f5889340d7ec1e9209.png)

## 部门管理

### 部门列表

修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
]
```

设计数据库表结构

```python
from django.db import models
class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=2)
    create_time = models.DateTimeField(verbose_name="入职时间")
	
    # 有约束
    # 外键约束
    # Django 自动
    #   - 写的 depart
    #   - 生成数据列 depart_id on_delete = models.CASCADE 删除级联
    depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    # 删除置空
    # depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.SET_NULL,null=True,blank=True)
    # 在 Django 中做的约束
    gender_choices = (
        (1:'男'),
        (2:'女'),
    )

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


```



修改`myproject/employee_management/views.py`

```python
from turtle import title
from django.shortcuts import render, redirect
from employee_management.models import Department,UserInfo

## Create your views here.
def depart_list(request):
    """部门列表"""

    depart_list = Department.objects.all()

    return render(request, "depart_list.html", {"depart_list": depart_list})
```

在`myproject/employee_management/templates`下新建`depart_list.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <style>
        .navbar {
            border-radius: 0;
        }
    </style>
</head>

<body>

    <!-- 导航条, https://v3.bootcss.com/components/#navbar -->
    <nav class="navbar navbar-default">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">员工管理系统</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li><a href="#">部门管理</a></li>
                    <li><a href="#">部门管理</a></li>

                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">注册</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">poker <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
    <!-- 新建区域 -->
    <div>
        <div class="container">
            <div style="margin-bottom: 10px">
                <a class="btn btn-primary" href="/depart/add/" target="_blank">新建部门</a>
            </div>
            <div>
                <div class="panel panel-default">
                    <!-- Default panel contents -->
                    <div class="panel-heading">
                        <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                        <span>部门列表</span>
                    </div>

                    <!-- Table -->
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>名称</th>
                                <th>操作</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for obj in depart_list %}
                            <tr>
                                <th>{{ obj.id }}</th>
                                <td>{{ obj.title }}</td> 
                                <td>
                                    <button type="button" class="btn btn-primary btn-xs">编辑</button>
                                    <button type="button" class="btn btn-danger btn-xs">删除</button>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script src="/static/js/jquery-3.6.1.min.js"></script>
    <script src="/static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/5ed88fd2d2a246eb9fbe574191674b15.png)

### 部门添加

修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
]
```

修改`myproject/employee_management/views.py`

```python
def depart_add(request):
    """部门添加"""
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 获取用户提交的部门数据
    depart_title = request.POST.get("depart_title")

    # 保存到数据库
    Department.objects.create(title=depart_title)

    return redirect("/depart/list/")
```

在`myproject/employee_management/templates`下新建`depart_list.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <style>
        .navbar {
            border-radius: 0;
        }
    </style>

</head>

<body>
    <div>
        <!-- 导航条, https://v3.bootcss.com/components/#navbar -->
        <nav class="navbar navbar-default">
            <div class="container">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">员工管理系统</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li><a href="#">部门管理</a></li>
                        <li><a href="#">部门管理</a></li>

                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#">注册</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                aria-haspopup="true" aria-expanded="false">poker <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Another action</a></li>
                                <li><a href="#">Something else here</a></li>
                                <li role="separator" class="divider"></li>
                                <li><a href="#">Separated link</a></li>
                            </ul>
                        </li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>
    </div>
    <div class="container">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">新建部门</h3>
            </div>
            <div class="panel-body">
                <form action="/depart/add/" method="post">
                    {% csrf_token %}
                    <div class="form-group">
                        <label>部门名称</label>
                        <input type="text" class="form-control" placeholder="部门名称" name="depart_title">
                    </div>

                    <button type="submit" class="btn btn-primary">保存</button>

                </form>
            </div>
        </div>
    </div>
</body>
</html>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e31dab99a99240239c9a5c9113fe3ed7.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/c4ca5172699744409b96c0c2ff42b32a.png)

### 部门删除

修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
]
```

修改`myproject/employee_management/views.py`

```python
def depart_delete(request):
    """部门删除"""

    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/depart/list/")
```

修改`myproject/employee_management/templates/depart_list.html`

```html
<tbody>
    {% for obj in depart_list %}
    <tr>
        <th>{{ obj.id }}</th>
        <td>{{ obj.title }}</td> 
        <td>
            <a class="btn btn-primary btn-xs">编辑</a>
            <a class="btn btn-danger btn-xs" href="/depart/delete/?nid={{ obj.id }}">删除</a>
        </td>
    </tr>
    {% endfor %}
</tbody>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/8070d6f6b73344ba9c2f501534baf312.png)

### 部门编辑

修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
]
```

修改`myproject/employee_management/views.py`

```python
def depart_edit(request, nid):
    """部门编辑"""

    if request.method == "GET":
        # 根据nid,获取数据
        row_object = Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {"row_object": row_object})
    
    # 如果是POST请求,保存修改
    depart_title = request.POST.get('depart_title')
    Department.objects.filter(id=nid).update(title=depart_title)

    # 重定向回部门列表
    return redirect('/depart/list/')
```

新建`myproject/employee_management/templates/depart_edit.html`

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <style>
        .navbar {
            border-radius: 0;
        }
    </style>

</head>

<body>
    <div>
        <!-- 导航条, https://v3.bootcss.com/components/#navbar -->
        <nav class="navbar navbar-default">
            <div class="container">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">员工管理系统</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li><a href="#">部门管理</a></li>
                        <li><a href="#">部门管理</a></li>

                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#">注册</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                aria-haspopup="true" aria-expanded="false">poker <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">Action</a></li>
                                <li><a href="#">Another action</a></li>
                                <li><a href="#">Something else here</a></li>
                                <li role="separator" class="divider"></li>
                                <li><a href="#">Separated link</a></li>
                            </ul>
                        </li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>
    </div>
    <div class="container">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">编辑部门</h3>
            </div>
            <div class="panel-body">
                <form action="/depart/{{ row_object.id }}/edit/" method="post">
                    {% csrf_token %}
                    <div class="form-group">
                        <label>部门名称</label>
                        <input type="text" class="form-control" placeholder="部门名称" name="depart_title" value="{{ row_object.title }}">
                    </div>
                    <button type="submit" class="btn btn-primary">保存</button>
                </form>
            </div>

        </div>
    </div>
</body>
</html>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f7519eea8fdd4c4b8df408fe02767142.png)
修改`myproject/employee_management/templates/depart_list.html`

```html
<tbody>
    {% for obj in depart_list %}
    <tr>
        <th>{{ obj.id }}</th>
        <td>{{ obj.title }}</td> 
        <td>
            <a class="btn btn-primary btn-xs" href="/depart/{{ obj.id }}/edit/">编辑</a>
            <a class="btn btn-danger btn-xs" href="/depart/delete/?nid={{ obj.id }}">删除</a>
        </td>
    </tr>
    {% endfor %}
</tbody>
```

浏览器访问`/depart/list/`,点击"编辑"
![在这里插入图片描述](https://img-blog.csdnimg.cn/23587f73a79649b79e2950e6ea336f11.png)

修改后"保存"观察数据变化

### 模板继承

定义模板:`layout.html`

> {% block content %}{% endblock %}

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">

    <style>
        .navbar {
            border-radius: 0;
        }
    </style>
</head>

<body>

    <!-- 导航条, https://v3.bootcss.com/components/#navbar -->
    <nav class="navbar navbar-default">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">员工管理系统</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li><a href="#">部门管理</a></li>
                    <li><a href="#">部门管理</a></li>

                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#">注册</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                            aria-expanded="false">poker <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
    <!-- 新建区域 -->
    <div>
        {% block content %}{% endblock %}
    </div>

    <script src="/static/js/jquery-3.6.1.min.js"></script>
    <script src="/static/plugins/bootstrap-3.4.1/js/bootstrap.min.js"></script>
</body>

</html>
```

继承模板:

```html
{% extends 'layout.html' %}

{% block content %}
	<h1>首页</h1>
{% endblock %}
```

例如,可以将`myproject/employee_management/templates/depart_list.html`改成

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
    <div style="margin-bottom: 10px">
        <a class="btn btn-primary" href="/depart/add/" target="_blank">新建部门</a>
    </div>
    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>部门列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>名称</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in depart_list %}
                    <tr>
                        <th>{{ obj.id }}</th>
                        <td>{{ obj.title }}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="/depart/{{ obj.id }}/edit/">编辑</a>
                            <a class="btn btn-danger btn-xs" href="/depart/delete/?nid={{ obj.id }}">删除</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

{% endblock %}
```

其余页面以此类推,请自行修改

> 如果有个别页面不需要用到指定的css样式,可以这么做

```html
{% block css %}{% endblock %}
```

在`layout.html`模板中将css区域独立出来



## 用户管理

```
mysql> desc employee_management_userinfo;
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| id          | bigint(20)    | NO   | PRI | NULL    | auto_increment |
| name        | varchar(16)   | NO   |     | NULL    |                |
| password    | varchar(64)   | NO   |     | NULL    |                |
| age         | int(11)       | NO   |     | NULL    |                |
| account     | decimal(10,2) | NO   |     | NULL    |                |
| create_time | datetime(6)   | NO   |     | NULL    |                |
| gender      | smallint(6)   | NO   |     | NULL    |                |
| depart_id   | bigint(20)    | NO   | MUL | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
```

向用户数据表中插入几行数据方便后面进行测试

```
insert into employee_management_userinfo(name,password,age,account,create_time,gender,depart_id) values("李云龙","123456",45,50000,"2020-03-24",1,2);
insert into employee_management_userinfo(name,password,age,account,create_time,gender,depart_id) values("张三丰","123456",45,60000,"2021-03-24",1,3);
insert into employee_management_userinfo(name,password,age,account,create_time,gender,depart_id) values("周杰伦","123456",45,70000,"2022-03-24",1,4);
```

### 用户列表

修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('user/list/', views.user_list),
]
```

修改`myproject/employee_management/views.py`

```python
def user_list(request):

    # 获取所有用户列表
    user_data = UserInfo.objects.all()

    # 用 python 的语法获取数据
    """
    for obj in user_data:
        # obj.get_gender_display() 表示匹配 男/女,原始字段名为gender,obj.get_字段名称_display()
        # obj.create_time.strftime("%Y-%m-%d") 表示将时间格式转换成固定格式的字符串
        # obj.depart.title 表示获取depart_id对应的部门名称,因为我们在models中定义表时与另外一张表设置了级联关系,有外键
        print(obj.id, obj.name, obj.password, obj.age, obj.account, obj.get_gender_display(), obj.depart.title, obj.create_time.strftime("%Y-%m-%d"))
    """
    
    return render(request, "user_list.html", {"user_data": user_data})

```

新建`myproject/employee_management/templates/user_list.html`

> 注意: HTML 中获取数据的方式与 Python 中有些不同
> 例如:
> 1.HTML中引入函数不能带括号, obj.get_gender_display()
> 2.日期类型转字符串有Django自己的格式, obj.create_time|date:“Y-m-d”

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
    <div style="margin-bottom: 10px">
        <a class="btn btn-primary" href="/depart/add/" target="_blank">新建用户</a>
    </div>
    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>用户列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>姓名</th>
                        <th>密码</th>
                        <th>年龄</th>
                        <th>性别</th>
                        <th>账户余额</th>
                        <th>入职时间</th>
                        <th>部门</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in user_data %}
                    <tr>
                        <th>{{ obj.id }}</th>
                        <td>{{ obj.name }}</td>
                        <td>{{ obj.password }}</td>
                        <td>{{ obj.age }}</td>
                        <td>{{ obj.get_gender_display }}</td>
                        <td>{{ obj.account }}</td>
                        <td>{{ obj.create_time|date:"Y-m-d" }}</td>
                        <td>{{ obj.depart.title }}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="/user/{{ obj.id }}/edit/">编辑</a>
                            <a class="btn btn-danger btn-xs" href="/user/delete/?nid={{ obj.id }}">删除</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

{% endblock %}
```

浏览器进行访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/1a251b46074147dea5552643ff831d56.png)

### 用户添加

> 这里不演示最无脑原始的方式,漏洞百出,因为:
>
> - 数据校验较麻烦
> - 页面没有错误提示
> - 页面上每一个字段都需要重新写一遍
> - 关联的数据,需要手动获取并循环展示在页面

Django组件:

- Form组件(简便)
- ModelForm组件(最简便)

#### 初识Form

- views.py

```python
class MyForm(Form):
	user = forms.CharField(widget=forms.Input)
	pwd = forms.CharField(widget=forms.Input)
	email = forms.CharField(widget=forms.Input)

def user_add(request):
	if request.method == "GET":
	form = MyForm()
		return render(request, "user_add.html", {"form": form})
```

- user_add.html

> {{ form.xxx }} 可以自动生成前端代码

```html
<form method="post">
	{{ form.user }}
	{{ form.pwd }}
	{{ form.email }}
</form>
```

> 也可以不指定,自动生成全部

```html
<form method="post">
	{% for field in form %}
		{{ field }}
	{% endfor %}
</form>
```

#### ModelForm

- models.py

```python
from django.db import models

## Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='标题')


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(max_length=16, verbose_name="姓名")
    password = models.CharField(max_length=64, verbose_name="密码")
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE, verbose_name="部门")
    
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(choices=gender_choices,verbose_name="性别")

```

- views.py

```python
class MyForm(ModelForm):
	class Meta:
		field = ["name", "password", "age"]
 
def user_add(request):
	if request.method == "GET":
	form = MyForm()
		return render(request, "user_add.html", {"form": form})
```

- user_add.html

> {{ form.xxx }} 可以自动生成前端代码

```html
<form method="post">
	{{ form.user }}
	{{ form.pwd }}
	{{ form.email }}
</form>
```

> 也可以不指定,自动生成全部

```html
<form method="post">
	{% for field in form %}
		{{ field }}
	{% endfor %}
</form>
```

>获取标签

```html
<form method="post">
    {% csrf_token %}
    {{ form.name.label }}:{{ form.name }}
    {{ form.password.label }}:{{ form.password }}
    {{ form.age.label }}:{{ form.age }}
</form>
```



### 用户添加(ModelForm)

修改`myproject/employee_management/views.py`

```python
########################### ModelForm 演示 #############################

from django import forms

class UserModelForm(forms.ModelForm):

    ### 自定义数据校验
    # 例如: 用户名最小三个字符
    #name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # 逐一控制标签的样式
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        # }
        
        # 这里让日期可以手动点击鼠标选择,所以单独拎出来,加上日期插件
        widgets = {
            "create_time": forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'myDate'}),
        }

    # 循环找到所有的插件,添加 "class": "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # 可以排除指定的字段
            if name == "create_time":
                continue
            print(name, field)
            field.widget.attrs = {"class": "form-control"}


def user_model_form_add(request):
    """添加用户(ModelForm版本)"""
    if request.method == "GET": 
        form = UserModelForm()
        return render(request, "user_model_form_add.html", {"form": form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/user/list/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "user_model_form_add.html", {"form": form})
```

修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('user/list/', views.user_list),
    path('user/model/form/add/', views.user_model_form_add),
]
```

新建`myproject/employee_management/templates/user_model_form_add.html`

```python
{% extends 'layout.html' %}

{% block content %}
<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">添加用户</h3>
        </div>
        <div class="panel-body">
            <form action="/user/model/form/add/" method="post" novalidate>
                {% csrf_token %}
                
                {% for field in form %}
                    <div class="form-group">
                        <label>{{ field.label }}: </label>
                        {{ field }}
                        <!-- 数据校验,显示错误信息 -->
                        <span style="color: red;">{{ field.errors.0 }}</span>
                    </div>
                {% endfor %}

                <button type="submit" class="btn btn-primary">保存</button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
</body>
</html>
```

>form 默认保存的是用户输入的所有数据 如果想要再用户输入以外增加一点值

```python
form.instance.字段值 = 值
```

修改`myproject/employee_management/models.py`

> 目的是让自动生成的部门字段不显示"对象"本身,显示对象对应的"title"

```python
class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='标题')

    def __str__(self):
        return self.title
123456
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/a69ddb65da684cec9f7441e53c00b3a1.png)
修改后再次刷新
![在这里插入图片描述](https://img-blog.csdnimg.cn/b60fce024b0c41ffbb57dd843fc1aafc.png)

#### 日期设置

目前日期只能手动输入,如果想要鼠标点击选择,需要调用`datetimepicker`插件

插件下载地址：
链接：https://pan.baidu.com/s/1yN-L7bhwdSXwfYfh2MUj2A
提取码：yyds

> 下载完成后,我将插件放在了`/root/python/myproject/static/`下

![在这里插入图片描述](https://img-blog.csdnimg.cn/4103d73a9940403e848792e538c47450.png)
修改`myproject/employee_management/templates/layout.html`引入`datetimepicker`插件

> 调用方法: 在对应的标签中加入"id=myDate"

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>

    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugins/font-awesome-4.7.0/css/font-awesome.css">


    <!--JQUERY-->
    <script type="text/javascript" src="/static/jquery/jquery-1.11.1-min.js"></script>
    <!--BOOTSTRAP框架-->
    <link rel="stylesheet" type="text/css" href="/static/jquery/bootstrap_3.3.0/css/bootstrap.min.css">
    <script type="text/javascript" src="/static/jquery/bootstrap_3.3.0/js/bootstrap.min.js"></script>
    <!--BOOTSTRAP_DATETIMEPICKER插件-->
    <link rel="stylesheet" type="text/css" href="/static/jquery/bootstrap-datetimepicker-master/css/bootstrap-datetimepicker.min.css">
</head>
<body>

	<!-- 此处省略一部分代码 -->

    <script type="text/javascript">
        $(function () {
            //当容器加载完成，对容器调用工具函数
            $("#myDate").datetimepicker({
                language: 'zh-CN', //语言
                format: 'yyyy-mm-dd',//日期的格式
                minView: 'month', //可以选择的最小视图
                initialDate: new Date(),//初始化显示的日期
                autoclose: true,//设置选择完日期或者时间之后，日否自动关闭日历
                todayBtn: true,//设置自动显示为今天
                clearBtn: false//设置是否清空按钮，默认为false
            });
        });
    </script>
</body>
</html>
123456789101112131415161718192021222324252627282930313233343536373839
```

如何使用呢
其实在上面的代码中我已经提前写上了
下图是Django中ModelForm修改标签属性的方式,在`widgets`字典中定义
`attrs={'class': 'form-control', 'id': 'myDate'}`
![在这里插入图片描述](https://img-blog.csdnimg.cn/c30582222e914d5d8d0ed4138171ea3f.png)
最终效果
![在这里插入图片描述](https://img-blog.csdnimg.cn/8db65a9479c943d99519054c0c61b802.png)

#### 数据校验错误提示

修改`myproject/myproject/settings.py`

> 改为中文,目的是为了让页面提示错误信息时显示中文,否则会显示英文

```python
##LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'
12
```

如果我们没有写入任何内容直接点击"保存",那么页面会提示错误
![在这里插入图片描述](https://img-blog.csdnimg.cn/19ae785f405c4027aac50f2d206fe100.png)
因为我们在`/root/python/myproject/employee_management/templates/user_model_form_add.html`中加入了`{{ field.errors.0 }}`字段
![在这里插入图片描述](https://img-blog.csdnimg.cn/18ba1de56bf34dbc8bfcbaf111e3f120.png)

### 编辑用户

修改`myproject/employee_management/views.py`

```python
def user_edit(request, nid):
    """编辑用户"""
    
    row_obj = UserInfo.objects.filter(id=nid).first()
    
    # GET请求
    if request.method == "GET":
        form = UserModelForm(instance=row_obj)
        return render(request, "user_edit.html", {"form": form})
    
    # POST请求
    form = UserModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")

    return render(request, "user_edit.html", {"form": form})    
```

修改`/root/python/myproject/myproject/urls.py`

```python
path('user/<int:nid>/edit/', views.user_edit),
```

加`/root/python/myproject/employee_management/templates/user_edit.html`

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">编辑用户</h3>
        </div>
        <div class="panel-body">
            <form method="post" novalidate>
                {% csrf_token %}
                
                {% for field in form %}
                    <div class="form-group">
                        <label>{{ field.label }}: </label>
                        {{ field }}
                        <!-- 数据校验,显示错误信息 -->
                        <span style="color: red;">{{ field.errors.0 }}</span>
                    </div>
                {% endfor %}

                <button type="submit" class="btn btn-primary">保存</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
</body>
</html>
```

浏览器访问测试,点击"编辑"
![在这里插入图片描述](https://img-blog.csdnimg.cn/4cadd3a8a10141369490af19a2438cba.png)
但是发现上面的时间有些问题,应该只显示年月日就可以了,不应该显示时分秒
需要修改数据库models
![在这里插入图片描述](https://img-blog.csdnimg.cn/cb6cb0fa63164bd3a0d98027d30b9f9f.png)
更新[数据库表结构](https://so.csdn.net/so/search?q=数据库表结构&spm=1001.2101.3001.7020)

```shell
python3 manage.py makemigrations
python3 manage.py migrate
12
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/366d9554365443e79106bf3fffaa974a.png)
此时还需要更改一个地方
![在这里插入图片描述](https://img-blog.csdnimg.cn/8f19feb090df4a4585db6896069070c8.png)
浏览器刷新
![在这里插入图片描述](https://img-blog.csdnimg.cn/e1c0f0e0e4534e5d98d4696d1a2e1e99.png)

### 删除用户

修改`myproject/employee_management/views.py`

```python
def user_delete(request, nid):
    """用户删除"""
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
```

修改`myproject/myproject/urls.py`

```python
path('user/<int:nid>/delete/', views.user_delete),
```

修改`myproject/employee_management/templates/user_list.html`

```html
<td>
    <a class="btn btn-primary btn-xs" href="/user/{{ obj.id }}/edit/">编辑</a>
    <a class="btn btn-danger btn-xs" href="/user/{{ obj.id }}/delete/">删除</a>
</td>
```

浏览器测试

## 靓号管理

### 表结构

修改`myproject/employee_management/models.py`

```python
class PrettyNum(models.Model):
    """靓号表"""
    # 如果想要为空 null=True blank=True
    mobile = models.CharField(verbose_name="手机号", max_length=32)
    price = models.IntegerField(verbose_name="价格", default=0)

    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)

    status_choices = (
        (1, "已占用"),
        (2, "未使用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)
```

生成数据库表

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2e45639d14ab45158ba4746fc7f3f463.png)
手动模拟添加一些数据

```shell
insert into employee_management_prettynum(mobile, price, level, status) values("15811223344", 500, 2, 2);
insert into employee_management_prettynum(mobile, price, level, status) values("13846783361", 100, 3, 2);
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/dffabde7d5f84139a87cc9cae22c8245.png)

### 靓号列表

> 相信到这里大家可以做到这里,可以说是已经轻车熟路了

修改`myproject/employee_management/views.py`增加`pretty_list`函数

```python
def pretty_list(request):
    """靓号列表"""

    # select * from 表 by level desc;
    pretty_data = PrettyNum.objects.all().order_by("-level")

    return render(request, "pretty_list.html", {"pretty_data": pretty_data})
```

修改`myproject/myproject/urls.py`

```python
path('pretty/list/', views.pretty_list),
```

新建`myproject/employee_management/templates/pretty_list.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
    <div style="margin-bottom: 10px">
        <a class="btn btn-primary" href="/user/model/form/add/" target="_blank">新建靓号</a>
    </div>
    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>靓号列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>号码</th>
                        <th>价格</th>
                        <th>级别</th>
                        <th>状态</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in pretty_data %}
                    <tr>
                        <th>{{ obj.id }}</th>
                        <td>{{ obj.mobile }}</td>
                        <td>{{ obj.price }}</td>
                        <td>{{ obj.get_level_display }}</td>
                        <td>{{ obj.get_status_display }}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="/user/{{ obj.id }}/edit/">编辑</a>
                            <a class="btn btn-danger btn-xs" href="/user/{{ obj.id }}/delete/">删除</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

{% endblock %}
```

运行,浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/80fd66703fd44125a991d8012465e0da.png)

> 这里在导航栏中增加一个"靓号管理"的标签

修改`myproject/employee_management/templates/layout.html`

```html
<li><a href="/pretty/list/">靓号管理</a></li>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/5ed5acf152e247a7960c9bf7163ed79d.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/f74fb5c462164968a8576f914185671c.png)

### 靓号添加

修改`myproject/employee_management/views.py`

```python
from django.core.validators import RegexValidator

class PrettyModelForm(forms.ModelForm):

    # 数据校验
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'),],
    )

    class Meta:
        model = PrettyNum
        # fields = "__all__"    表示取表中所有的字段
        fields = ['mobile', 'price', 'level', 'status']
        # exclude = ['level']   表示取除了表中的某个字段的所有字段

    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control"}

def pretty_add(request):
    """添加靓号"""

    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {"form": form})

    # 用户POST请求提交数据,需要进行数据校验
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/pretty/list/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "pretty_add.html", {"form": form})
```

修改`/root/python/myproject/myproject/urls.py`

```python
path('pretty/add/', views.pretty_add),
```

修改`myproject/employee_management/templates/pretty_list.html`

> 修改 href

```html
<a class="btn btn-primary" href="/pretty/add/" target="_blank">新建靓号</a>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/3f26ed0831be429892d318bba95fd0f8.png)
新建`myproject/employee_management/templates/pretty_add.html`

```html
{% extends 'layout.html' %}

{% block content %}


<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">添加靓号</h3>
        </div>
        <div class="panel-body">
            <form action="/pretty/add/" method="post" novalidate>
                {% csrf_token %}
                
                {% for field in form %}
                    <div class="form-group">
                        <label>{{ field.label }}: </label>
                        {{ field }}
                        <!-- 数据校验,显示错误信息 -->
                        <span style="color: red;">{{ field.errors.0 }}</span>
                    </div>
                {% endfor %}

                <button type="submit" class="btn btn-primary">保存</button>
            </form>
        </div>
    </div>
</div>

{% endblock %}

```

浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/8ec92799dbb34a97b1be5a7de3e3f097.png)
格式只能11位手机号
![在这里插入图片描述](https://img-blog.csdnimg.cn/3fbdc1f71ff44dc7af74577ac4675a51.png)
点击保存
![在这里插入图片描述](https://img-blog.csdnimg.cn/2f07855a630f44d28bf85bc4e51186aa.png)

> 数据校验的方式还有另外一种,更为复杂的

修改`myproject/employee_management/views.py`

```python
from django.core.exceptions import ValidationError

class PrettyModelForm(forms.ModelForm):

	# 此处省略中间内容
	...

    # 数据校验: 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError('格式错误')

        # 验证通过
        return txt_mobile
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f93682f12f2247f2af676663ae304e2e.png)
同样的效果,选择其中一种方式即可

### 靓号编辑

> **重新复习一下编辑实现的逻辑:**
>
> 1. 列表页面点击"编辑"按钮
> 2. 匹配`urls.py`中的定义的path
> 3. `views.py`中定义的函数接收到POST请求提交的`nid`
> 4. 函数根据`nid`找到对应的数据行
> 5. `templates`模板下的HTML文件根据Django的方法展示数据

修改`myproject/employee_management/views.py`

```python
def pretty_edit(request, nid):
    """编辑靓号"""
    row_obj = PrettyNum.objects.filter(id=nid).first()
    
    # GET请求
    if request.method == "GET":
        form = PrettyModelForm(instance=row_obj)
        return render(request, "pretty_edit.html", {"form": form})
    
    # POST请求
    form = PrettyModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")

    return render(request, "pretty_edit.html", {"form": form})
```

修改`myproject/myproject/urls.py`

```python
path('pretty/<int:nid>/edit/', views.pretty_edit),
```

新建`/root/python/myproject/employee_management/templates/pretty_edit.html`

```html
{% extends 'layout.html' %}

{% block content %}


<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">编辑靓号</h3>
        </div>
        <div class="panel-body">
            <form method="post" novalidate>
                {% csrf_token %}
                
                {% for field in form %}
                    <div class="form-group">
                        <label>{{ field.label }}: </label>
                        {{ field }}
                        <!-- 数据校验,显示错误信息 -->
                        <span style="color: red;">{{ field.errors.0 }}</span>
                    </div>
                {% endfor %}

                <button type="submit" class="btn btn-primary">保存</button>
            </form>
        </div>
    </div>
</div>

{% endblock %}

```

修改`/root/python/myproject/employee_management/templates/pretty_list.html`
![在这里插入图片描述](https://img-blog.csdnimg.cn/d53f0ccb030d4cd5a312df513ed329f9.png)
浏览器点击"编辑"更改[数据测试](https://so.csdn.net/so/search?q=数据测试&spm=1001.2101.3001.7020)即可

> 现在有一个新的需求,不想让用户编辑手机号字段,该怎么做?
> 其实我们可以单独新增一个class,去掉`mobile`字段

修改`myproject/employee_management/views.py`

```python
class PrettyEditModelForm(forms.ModelForm):

    class Meta:
        model = PrettyNum
        # fields = "__all__"    表示取表中所有的字段
        fields = ['price', 'level', 'status']
        # exclude = ['level']   表示取除了表中的某个字段的所有字段

    # 循环找到所有的插件,加入css样式,添加 "class": "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control"}


def pretty_edit(request, nid):
    """编辑靓号"""
    row_obj = PrettyNum.objects.filter(id=nid).first()
    
    # GET请求
    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_obj)
        return render(request, "pretty_edit.html", {"form": form})
    
    # POST请求
    form = PrettyEditModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")

    return render(request, "pretty_edit.html", {"form": form})
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/176fc4951f9d44bca0107251204cc271.png)
浏览器访问,可以发现没有手机号了
![在这里插入图片描述](https://img-blog.csdnimg.cn/aad925720312440d8d0ff23459feb6fc.png)

> 这时可能有人会说,我就是想要加上手机号字段,但是不想让他可编辑
> 这个当然也可以实现哈

修改`myproject/employee_management/views.py`

```python
mobile = forms.CharField(disabled=True, label="手机号")
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/6f4f3b3f1b764327aea0166e12e7195d.png)
浏览器刷新
![在这里插入图片描述](https://img-blog.csdnimg.cn/6b776973b2574535b279c1170a58143e.png)

> 那如果也允许编辑手机号字段呢
> 那么这样会有一个问题,如果手机号已经存在怎么办?
> 这里就涉及到了手机号的重复性问题

#### 不允许手机号重复

- 添加: 如果手机号已存在,提示"手机号已存在"
- 编辑: 如果手机号除了当前手机号以外已存在,提示"手机号已存在"

> 添加和编辑的逻辑不太一样,编辑需要将它自己先排除然后再做判断

**首先实现"添加"功能的手机号重复验证**
修改`myproject/employee_management/views.py`中`class PrettyModelForm`的`clean_mobile`函数

```python
## 数据校验：验证方式1
	mobile = forms.CharFIeld(
    	label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$',"手机号格式错误"),],
    )
## 数据校验: 验证方式2
def clean_mobile(self):
    txt_mobile = self.cleaned_data['mobile']

    if len(txt_mobile) != 11:
        # 验证不通过
        raise ValidationError('格式错误')
    exists_data = PrettyNum.objects.filter(mobile=txt_mobile).exists()
    if exists_data:
        raise ValidationError("手机号已存在")

    # 验证通过
    return txt_mobile
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4ea96fd72805424b9adfa6302ee8c672.png)
浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/ffcdddd68f2543f38595e2580a463123.png)
**实现"编辑"功能的手机号重复验证**

> 注意: 下面修改的是`PrettyEditModelForm`类下面的函数

修改`myproject/employee_management/views.py`中`class PrettyEditModelForm`的`clean_mobile`函数

```python
## 数据校验: 验证方式2
def clean_mobile(self):
    txt_mobile = self.cleaned_data['mobile']

    if len(txt_mobile) != 11:
        # 验证不通过
        raise ValidationError('格式错误')

    # exclude 表示排除哪一个数据
    # self.instance.pk 表示当前编辑的哪一行 id
    exists_data = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
    if exists_data:
        raise ValidationError("手机号已存在")

    # 验证通过
    return txt_mobile
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/32df921b46544c6f96fd357240bdff9c.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/7c911e65cdf143e08716fb4866ad196b.png)
不更改直接保存,正常
将手机号更改为已经存在的其他电话号码,保存,则提示"手机号已存在"
![在这里插入图片描述](https://img-blog.csdnimg.cn/5f04ac0bc809462c93fb826fd816c8e5.png)

### 靓号删除

修改`myproject/employee_management/views.py`

```python
def pretty_delete(request, nid):
    """删除靓号"""
    PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')
```

修改`myproject/myproject/urls.py`

```python
path('pretty/<int:nid>/delete/', views.pretty_delete),
```

修改`/root/python/myproject/employee_management/templates/pretty_list.html`
![在这里插入图片描述](https://img-blog.csdnimg.cn/c5ce0a5d02e343b2a513fa8f77328259.png)
浏览器测试即可
![在这里插入图片描述](https://img-blog.csdnimg.cn/5d2b6f53eac1469f9b7e8402c2d674a1.png)

### 手机号搜索

```python
query1 = PrettyNum.objects.filter(mobile=15576547933, id=4)
print(query1)

## 如果是空字典,表示获取所有
query_dict = {"mobile": "15576547933", "id": 4}
query2 = PrettyNum.objects.filter(**query_dict)
print(query2)
PrettyNum.objects.filter(id=4)			# 等于4
PrettyNum.objects.filter(id__gt=4)		# 大于4
PrettyNum.objects.filter(id__gte=4)		# 大于等于4
PrettyNum.objects.filter(id__lt=4)		# 小于4
PrettyNum.objects.filter(id__lte=4)		# 小于等于4

PrettyNum.objects.filter(mobile__startswith="1999")		# 筛选出以"1999"开头的
PrettyNum.objects.filter(mobile__endswith="1999")		# 筛选出以"1999"结尾的
PrettyNum.objects.filter(mobile__contains="1999")		# 筛选出包含"1999"开头的
```

> 接下来我们来实现这个功能

修改`myproject/employee_management/views.py`

```python
def pretty_list(request):
    """靓号列表"""

    data_dict = {}
    
    search_data = request.GET.get('query', "")  # 不加后面的 "", 首次访问浏览器,搜索框中不会显示前端页面中的 placeholder="Search for..." 属性
    if search_data:
    	# mobile_contains  表示筛选出字段 mobile 包含 search_data 数据的行
        data_dict["mobile__contains"] = search_data

    # select * from 表 by level desc;
    # data_dict 如果是空字典,表示获取所有
    pretty_data = PrettyNum.objects.filter(**data_dict).order_by("-level")

	# 加入search_data的目的是,当搜索后,搜索框内的值不会置为空
    return render(request, "pretty_list.html", {"pretty_data": pretty_data, "search_data": search_data})
```

修改`myproject/employee_management/templates/pretty_list.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">

    <div>
        <div style="margin-bottom: 10px; ">
            <a class="btn btn-primary" href="/pretty/add/" target="_blank">新建靓号</a>

            <div style="float: right; width: 300px;">
                <form method="get">
                    <div class="input-group">
                        <input type="text" name="query" class="form-control" placeholder="Search for..."
                            value="{{ search_data }}">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">
                                <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                            </button>
                        </span>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>靓号列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>号码</th>
                        <th>价格</th>
                        <th>级别</th>
                        <th>状态</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in pretty_data %}
                    <tr>
                        <th>{{ obj.id }}</th>
                        <td>{{ obj.mobile }}</td>
                        <td>{{ obj.price }}</td>
                        <td>{{ obj.get_level_display }}</td>
                        <td>{{ obj.get_status_display }}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="/pretty/{{ obj.id }}/edit/">编辑</a>
                            <a class="btn btn-danger btn-xs" href="/pretty/{{ obj.id }}/delete/">删除</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>

{% endblock %}
```

浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/47dab631ed564283adb942f9dca88be4.png)
进行搜索
![在这里插入图片描述](https://img-blog.csdnimg.cn/aed8b457ebf14e718a71b9ab04cc8f2b.png)

### 分页

```
quertset = PrettyNum.objects.filter(id=1)[0:10]
quertset = PrettyNum.objects.all()[0:10]			# 取0到10行数据
```

> 先使用最原始的代码方式实现分页
> 内容较多,仔细看,有很多的细节

修改`myproject/employee_management/views.py`

```python
from django.utils.safestring import mark_safe

def pretty_list(request):
    """靓号列表"""

    ################### 纯代码实现分页 ###################
    # 插入一些演示数据,使用完注释掉
    # for i in range(300):
    #     PrettyNum.objects.create(mobile="13811223344", price=100, level=3, status=1)

    page_now = int(request.GET.get('page', 1))

    page_range = 5  # 当前页面前后留几个页码
    start = (page_now - 1) * 10
    end = page_now * 10 + 2

    # 总数据行数
    data_num = PrettyNum.objects.all().count()

    # 总页码
    page_num, div = divmod(data_num, 10)
    if div:
        page_num += 1

    page_show = 5
    # 如果总页码数量大于 11
    if page_num > page_show * 2 + 1:
        # 如果当前页面页码位置小于等于5
        if page_now <= 5:
            start_page = 1
            end_page = page_show * 2 + 2
        # 否则,当前页面页码位置大于5时
        else:
            # 防止页码超出范围
            if page_now >= page_num - page_show:
                start_page = page_num - page_show * 2
                end_page = page_num + 1
            else:
                # 计算出当前页的前5页和后5页
                start_page = page_now - page_show
                end_page = page_now + page_show + 1

    else:
        start_page = 1
        end_page = page_num + 1


    ######## 创建页码 ########
    # 页码
    page_str_list = []

    # 跳到首页
    head_page = '?page={}'.format(1)
    
    # 跳到上10页
    # 如果当前页面小于 11, 防止超过最小页数
    if page_now < page_show * 2 + 1:
        prev = '<li><a href="?page={}">{}</a></li>'.format(1, "<<")
        page_str_list.append(prev)
    else:
        prev = '<li><a href="?page={}">{}</a></li>'.format(page_now - 10, "<<")
        page_str_list.append(prev)

    for i in range(start_page, end_page):

        # 如果是当前页,高亮显示页码颜色
        if page_now == i:
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)

    ### 跳到下10页
    # 如果当前页面页数 大于 最大页面数量减去(page_show*2+1),则直接跳到最后一页,防止超过最大页数
    if page_now >= page_num - page_show * 2 + 1:
        next = '<li><a href="?page={}">{}</a></li>'.format(page_num, ">>")
        page_str_list.append(next)
    else:
        next = '<li><a href="?page={}">{}</a></li>'.format(page_now + 10, ">>")
        page_str_list.append(next)

    page_string = mark_safe("".join(page_str_list))

    # 跳到尾页
    end_page = '?page={}'.format(page_num)

    ################### 代码实现分页结束 ###################

    data_dict = {}
    # 如果是空字典,表示获取所有
    search_data = request.GET.get('query', "")  # 不加后面的 "", 首次访问浏览器,搜索框中不会显示前端页面中的 placeholder="Search for..." 属性
    if search_data:
        data_dict["mobile__contains"] = search_data

    # select * from 表 by level desc;
    pretty_data = PrettyNum.objects.filter(**data_dict).order_by("-level")[start:end]

    return render(request, "pretty_list.html", {"pretty_data": pretty_data, "search_data": search_data, "page_string": page_string, "head_page": head_page, "end_page": end_page})

```

修改`myproject/employee_management/templates/pretty_list.html`

```html
<ul class="pagination">
    <li><a href="{{ head_page }}" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>
    {{ page_string }}
    <li><a href="{{ end_page }}" aria-label="Next"><span aria-hidden="true">尾页</span></a></li>

</ul>
<br>

<form method="get">
    <div style="display:inline-block; width: 150px;">
        <div class="input-group">
            <span> <input type="text" class="form-control" placeholder="请输入页码" name="page"></span>
            <span class="input-group-btn">
                <button class="btn btn-primary" type="submit">跳转</button>
            </span>
        </div>
    </div>
</form>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/347e7879c123479ab8873df4f0c7473e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/b619ae3963d54b388dc03fe5c9736a8e.png)

### 封装分页

> 实现分页代码的封装,方便以后其他代码的调用

在`myproject/employee_management`目录下新建`utils`目录
在`utils`下新建`pagination.py`文件

```python
"""
自定义的分页组件
"""
from django.utils.safestring import mark_safe

class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", page_show=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据(根据此数据进行分页处理)
        :param page_size: 每页显示多少条数据
        :param page_param: 获取在URL中传递的分页参数, 例如: /pretty/list/?page=21
        :param page_show: 页码显示前几页后几页
        """
        page = int(request.GET.get(page_param, 1))

        # 如果不是整数
        if type(page) != int:
            # 强制让页码为1
            page = 1
            
        self.page = page

        self.start = (page - 1) * page_size
        self.end = page * page_size

        # 每页展示的数据行数
        self.page_queryset = queryset[self.start:self.end]

        total_data_count = queryset.count()     # 数据行数
        total_page_count, div = divmod(total_data_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count    # 总页码数量
        self.page_show = page_show  # 当前页前后展示的页码数量
        self.request = request


    def html(self):
        # 如果总页码数量大于 11
        if self.total_page_count > self.page_show * 2 + 1:
            # 如果当前页面页码位置小于等于5
            if self.page <= 5:
                start_page = 1
                end_page = self.page_show * 2 + 2
            # 否则,当前页面页码位置大于5时
            else:
                # 防止页码超出范围
                if self.page >= self.total_page_count - self.page_show:
                    start_page = self.total_page_count - self.page_show * 2
                    end_page = self.total_page_count + 1
                else:
                    # 计算出当前页的前5页和后5页
                    start_page = self.page - self.page_show
                    end_page = self.page + self.page_show + 1

        else:
            start_page = 1
            end_page = self.total_page_count + 1

        ######## 创建页码 ########
        # 页码
        page_str_list = []

        # 跳到首页
        self.head_page = '?page={}'.format(1)

        # 跳到上10页
        # 如果当前页面小于 11, 防止超过最小页数
        if self.page < self.page_show * 2 + 1:
            prev = '<li><a href="?page={}">{}</a></li>'.format(1, "<<")
            page_str_list.append(prev)
        else:
            prev = '<li><a href="?page={}">{}</a></li>'.format(self.page - 10, "<<")
            page_str_list.append(prev)

        for i in range(start_page, end_page):

            # 如果是当前页,高亮显示页码颜色
            if self.page == i:
                ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)

        # 跳到下10页
        # 如果当前页面页数 大于 最大页面数量减去(page_show*2+1),则直接跳到最后一页,防止超过最大页数
        if self.page >= self.total_page_count - self.page_show * 2 + 1:
            next = '<li><a href="?page={}">{}</a></li>'.format(self.total_page_count, ">>")
            page_str_list.append(next)
        else:
            next = '<li><a href="?page={}">{}</a></li>'.format(self.page + 10, ">>")
            page_str_list.append(next)

        self.page_string = mark_safe("".join(page_str_list))

        # 跳到尾页
        self.end_page = '?page={}'.format(self.total_page_count)
```

修改`myproject/employee_management/views.py`

```python
def pretty_list(request):
    """靓号列表"""

    data_dict = {}
    # 如果是空字典,表示获取所有
    # 不加后面的 "", 首次访问浏览器,搜索框中不会显示前端页面中的 placeholder="Search for..." 属性
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict["mobile__contains"] = search_data 
    
    queryset = PrettyNum.objects.filter(**data_dict).order_by("-level")

    ### 引入封装的 Pagination 类并初始化
    # 初始化
    page_object = Pagination(request, queryset, page_size=10, page_param="page")
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string
    head_page = page_object.head_page
    end_page = page_object.end_page

    context = {
        "pretty_data": page_queryset,   # 分页的数据
        "search_data": search_data,     # 搜索的内容
        "page_string": page_string,     # 页码
        "head_page": head_page,         # 首页
        "end_page": end_page,           # 尾页
    }

    return render(request, "pretty_list.html", context)
```

浏览器刷新访问,你会发现效果和之前一样

### 解决小BUG

> 当我们进行搜索后,可以展示出搜索的对应数据
> 但是如果此时我们进行翻页,搜索数据将清空,重新展示所有的数据
> 这样是不符合逻辑的

***下面的代码对之前的代码进行了优化:***

- 将首页和尾页加入到了`page_str_list`列表中,方便后续其他页面进行调用

修改`myproject/employee_management/utils/pagination.py`

```python
"""
自定义的分页组件

"""

from django.utils.safestring import mark_safe
import copy


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", page_show=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据(根据此数据进行分页处理)
        :param page_size: 每页显示多少条数据
        :param page_param: 获取在URL中传递的分页参数, 例如: /pretty/list/?page=21
        :param page_show: 页码显示前几页后几页
        """

        # 防止搜索出结果进行翻页时,URL参数没有了搜索参数
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        self.page_param = page_param

        page = int(request.GET.get(page_param, 1))

        # 如果不是整数
        if type(page) != int:
            # 强制让页码为1
            page = 1

        self.page = page

        self.start = (page - 1) * page_size
        self.end = page * page_size

        # 每页展示的数据行数
        self.page_queryset = queryset[self.start:self.end]

        total_data_count = queryset.count()     # 数据行数
        total_page_count, div = divmod(total_data_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count    # 总页码数量
        self.page_show = page_show  # 当前页前后展示的页码数量
        self.request = request

    def html(self):
        # 如果总页码数量大于 11
        if self.total_page_count > self.page_show * 2 + 1:
            # 如果当前页面页码位置小于等于5
            if self.page <= 5:
                start_page = 1
                end_page = self.page_show * 2 + 2
            # 否则,当前页面页码位置大于5时
            else:
                # 防止页码超出范围
                if self.page >= self.total_page_count - self.page_show:
                    start_page = self.total_page_count - self.page_show * 2
                    end_page = self.total_page_count + 1
                else:
                    # 计算出当前页的前5页和后5页
                    start_page = self.page - self.page_show
                    end_page = self.page + self.page_show + 1

        else:
            start_page = 1
            end_page = self.total_page_count + 1

        ######## 创建页码 ########
        # 页码
        page_str_list = []

        # self.query_dict.setlist(self.page_param, [1])
        # page_str_list.append('<li><a href="?page={}">{}</a></li>'.format(self.query_dict.urlencode()))

        # 跳到首页
        self.query_dict.setlist(self.page_param, [1])
        self.head_page = '<li><a href="?{}" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(self.head_page)

        # 跳到上10页
        # 如果当前页面小于 11, 防止超过最小页数
        if self.page < self.page_show * 2 + 1:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">{}</a></li>'.format(
                self.query_dict.urlencode(), "<<")
            page_str_list.append(prev)
        else:
            self.query_dict.setlist(self.page_param, [self.page - 10])
            prev = '<li><a href="?{}">{}</a></li>'.format(
                self.query_dict.urlencode(), "<<")
            page_str_list.append(prev)

        for i in range(start_page, end_page):
            # 如果是当前页,高亮显示页码颜色
            if self.page == i:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(
                    self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 跳到下10页
        # 如果当前页面页数 大于 最大页面数量减去(page_show*2+1),则直接跳到最后一页,防止超过最大页数
        if self.page >= self.total_page_count - self.page_show * 2 + 1:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next = '<li><a href="?{}">{}</a></li>'.format(
                self.query_dict.urlencode(), ">>")
            page_str_list.append(next)
        else:
            self.query_dict.setlist(self.page_param, [self.page + 10])
            next = '<li><a href="?page={}">{}</a></li>'.format(
                self.query_dict.urlencode(), ">>")
            page_str_list.append(next)

        # 跳到尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        self.end_page = '<li><a href="?{}" aria-label="Next"><span aria-hidden="true">尾页</span></a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(self.end_page)

        self.page_string = mark_safe("".join(page_str_list))
```

**对上面一段代码的解析:**

```python
query_dict = copy.deepcopy(request.GET)
query_dict._mutable = True
self.query_dict = query_dict
```

上面这一段代码是获取保留目前已有的URL参数
`query_dict._mutable = True`表示将URL改为参数可拼接

```python
self.query_dict.setlist(self.page_param, [self.page + 10])
    next = '<li><a href="?page={}">{}</a></li>'.format(self.query_dict.urlencode(), ">>")
```

上面这一段代码表示在原来URL参数的基础上进行拼接,不是像原来一样直接覆盖URL参数
`setlist`表示增加URL参数
`self.query_dict.urlencode()`表示将`self.page_param`与数值`self.page + 10`拼接起来,不会讲原来已有的URL参数覆盖
例如`setlist(page, [10])`表示`page=10`
修改`myproject/employee_management/templates/pretty_list.html`

```html
<ul class="pagination">
    {{ page_string }}
</ul>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/cafb4358bd0a4495b5cf0862626c31af.png)

> 浏览器访问测试

![在这里插入图片描述](https://img-blog.csdnimg.cn/c3242052bc874de1a036b6d96bdd8b0f.png)
但是目前`输入页码跳转到指定页`的功能还是有这个问题,现在还无法解决,需要使用到ajax

### 用户列表增加分页

修改`myproject/employee_management/views.py`

```python
def user_list(request):
    """用户列表"""
    # 获取所有用户列表
    queryset = UserInfo.objects.all()

    page_object = Pagination(request, queryset, page_size=2)

    # 用 python 的语法获取数据
    """
    for obj in user_data:
        # obj.get_gender_display() 表示匹配 男/女,原始字段名为gender,obj.get_字段名称_display()
        # obj.create_time.strftime("%Y-%m-%d") 表示将时间格式转换成固定格式的字符串
        # obj.depart.title 表示获取depart_id对应的部门名称,因为我们在models中定义表时与另外一张表设置了级联关系,有外键
        print(obj.id, obj.name, obj.password, obj.age, obj.account, obj.get_gender_display(), obj.depart.title, obj.create_time.strftime("%Y-%m-%d"))
    """

    page_object.html()

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.page_string,
    }

    return render(request, "user_list.html", context)
```

修改`myproject/employee_management/templates/user_list.html`

```html
{% for obj in queryset %}

...

<ul class="pagination">
    {{ page_string }}
</ul>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/8df4551ac62643ccb1b323676f89e840.png)
浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/1bb0f828d99540acbb6a9e251027543a.png)

### 部门列表增加分页

修改`myproject/employee_management/views.py`

```python
def depart_list(request):
    """部门列表"""

    queryset = Department.objects.all()
    page_object = Pagination(request, queryset, page_size=2)

    page_object.html()

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.page_string,
    }

    return render(request, "depart_list.html", context)
```

修改`myproject/employee_management/templates/depart_list.html`

```html
{% for obj in queryset %}

...
            
<ul class="pagination">
    {{ page_string }}
</ul>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/fe8945a6e3384df4abaa4b6bb442eadd.png)
浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/b4e46ff99e114eca85bbdc2d24df5475.png)

## 项目代码优化

### ModelForm优化

新建`myproject/employee_management/utils/modelform.py`

```python
from django import forms

class BootStrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for _, field in self.fields.items():
            # 字段中有属性,保留原来的属性,没有属性,才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
            else:
                field.widget.attrs = {
                    "class": "form-control",
                }
```

修改`myproject/employee_management/views.py`

> 将目前的三个class类改为继承`BootStrapModelForm`自定义类

```python
class UserModelForm(BootStrapModelForm):
class PrettyModelForm(BootStrapModelForm):
class PrettyEditModelForm(BootStrapModelForm):
```

> 删除三个class的`init函数`

刷新浏览器查看效果,你会发现和以前一样,没有变化

### 整合form

新建`myproject/employee_management/form`目录
新建`myproject/employee_management/form/form.py`文件,将`/root/python/myproject/employee_management/views.py`文件中的相关class移动到此文件中

```python
from employee_management.utils.modelform import BootStrapModelForm
from employee_management.models import UserInfo, PrettyNum
from django.core.exceptions import ValidationError
from django import forms

class UserModelForm(BootStrapModelForm):

    ### 自定义数据校验
    # 例如: 用户名最小三个字符
    #name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # 逐一控制标签的样式
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        # }
        
        # 这里让日期可以手动点击鼠标选择,所以单独拎出来,加上日期插件
        widgets = {
            # "create_time": forms.DateInput(attrs={'class': 'form-control', 'id': 'myDate'}),
            "create_time": forms.DateInput(attrs={'id': 'myDate'}),
        }


class PrettyModelForm(BootStrapModelForm):

    # 数据校验: 验证方式1
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'),],
    # )

    class Meta:
        model = PrettyNum
        # fields = "__all__"    表示取表中所有的字段
        fields = ['mobile', 'price', 'level', 'status']
        # exclude = ['level']   表示取除了表中的某个字段的所有字段

    # 数据校验: 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError('格式错误')

        exists_data = PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists_data:
            raise ValidationError("手机号已存在")

        # 验证通过
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):

    # mobile = forms.CharField(disabled=True, label="手机号")

    # 数据校验: 验证方式1
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'),],
    # )

    class Meta:
        model = PrettyNum
        # fields = "__all__"    表示取表中所有的字段
        fields = ['mobile', 'price', 'level', 'status']
        # exclude = ['level']   表示取除了表中的某个字段的所有字段

    # 数据校验: 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError('格式错误')

        # exclude 表示排除哪一个数据
        # self.instance.pk 表示当前编辑的哪一行 id
        exists_data = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists_data:
            raise ValidationError("手机号已存在")

        # 验证通过
        return txt_mobile
```

整理之后的`views.py`文件是这样的
![在这里插入图片描述](https://img-blog.csdnimg.cn/413e7baa4aa14ebeacfeb6351e631089.png)

### 优化views.py

> 我们也可以将`/root/python/myproject/employee_management/views.py`进行拆分
> 按照部门进行拆分

新建`/root/python/myproject/employee_management/views`目录
然后在其下依次新建`user.py` `depart.py` `pretty.py`

> depart.py

```python
from django.shortcuts import render, redirect
from employee_management.models import Department
from employee_management.utils.pagination import Pagination


def depart_list(request):
    """部门列表"""

    queryset = Department.objects.all()
    page_object = Pagination(request, queryset, page_size=2)

    page_object.html()

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.page_string,
    }

    return render(request, "depart_list.html", context)

def depart_add(request):
    """部门添加"""
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 获取用户提交的部门数据
    depart_title = request.POST.get("depart_title")

    # 保存到数据库
    Department.objects.create(title=depart_title)

    # 重定向回部门列表
    return redirect("/depart/list/")

def depart_delete(request):
    """部门删除"""

    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()

    # 重定向回部门列表
    return redirect("/depart/list/")

def depart_edit(request, nid):
    """部门编辑"""

    if request.method == "GET":
        # 根据nid,获取数据
        row_object = Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {"row_object": row_object})
    
    # 如果是POST请求,保存修改
    depart_title = request.POST.get('depart_title')
    Department.objects.filter(id=nid).update(title=depart_title)

    # 重定向回部门列表
    return redirect('/depart/list/')
```

> user.py

```python
from django.shortcuts import render, redirect
from employee_management.models import UserInfo
from employee_management.utils.pagination import Pagination
from employee_management.form.form import UserModelForm


def user_list(request):
    """用户列表"""
    # 获取所有用户列表
    queryset = UserInfo.objects.all()

    page_object = Pagination(request, queryset, page_size=2)

    # 用 python 的语法获取数据
    """
    for obj in user_data:
        # obj.get_gender_display() 表示匹配 男/女,原始字段名为gender,obj.get_字段名称_display()
        # obj.create_time.strftime("%Y-%m-%d") 表示将时间格式转换成固定格式的字符串
        # obj.depart.title 表示获取depart_id对应的部门名称,因为我们在models中定义表时与另外一张表设置了级联关系,有外键
        print(obj.id, obj.name, obj.password, obj.age, obj.account, obj.get_gender_display(), obj.depart.title, obj.create_time.strftime("%Y-%m-%d"))
    """

    page_object.html()

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.page_string,
    }

    return render(request, "user_list.html", context)

def user_model_form_add(request):
    """添加用户(ModelForm版本)"""
    if request.method == "GET": 
        form = UserModelForm()
        return render(request, "user_model_form_add.html", {"form": form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/user/list/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "user_model_form_add.html", {"form": form})

def user_edit(request, nid):
    """编辑用户"""
    
    row_obj = UserInfo.objects.filter(id=nid).first()
    
    # GET请求
    if request.method == "GET":
        form = UserModelForm(instance=row_obj)
        return render(request, "user_edit.html", {"form": form})
    
    # POST请求
    form = UserModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")

    return render(request, "user_edit.html", {"form": form})    

def user_delete(request, nid):
    """用户删除"""
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")
```

> pretty.py

```python
from django.shortcuts import render, redirect
from employee_management.models import PrettyNum
from employee_management.utils.pagination import Pagination
from employee_management.form.form import PrettyModelForm, PrettyEditModelForm
 

def pretty_list(request):
    """靓号列表"""


    print(request.GET)
    print(request.GET.urlencode())

    data_dict = {}
    # 如果是空字典,表示获取所有
    # 不加后面的 "", 首次访问浏览器,搜索框中不会显示前端页面中的 placeholder="Search for..." 属性
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict["mobile__contains"] = search_data 
    
    queryset = PrettyNum.objects.filter(**data_dict).order_by("-level")

    ### 引入封装的 Pagination 类并初始化
    # 初始化
    page_object = Pagination(request, queryset, page_size=10, page_param="page")
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()

    page_string = page_object.page_string

    context = {
        "pretty_data": page_queryset,   # 分页的数据
        "search_data": search_data,     # 搜索的内容
        "page_string": page_string,     # 页码
    }

    

    return render(request, "pretty_list.html", context)

def pretty_add(request):
    """添加靓号"""

    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {"form": form})

    # 用户POST请求提交数据,需要进行数据校验
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/pretty/list/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "pretty_add.html", {"form": form})

def pretty_edit(request, nid):
    """编辑靓号"""
    row_obj = PrettyNum.objects.filter(id=nid).first()
    
    # GET请求
    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_obj)
        return render(request, "pretty_edit.html", {"form": form})
    
    # POST请求
    form = PrettyEditModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")

    return render(request, "pretty_edit.html", {"form": form})

def pretty_delete(request, nid):
    """删除靓号"""
    PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')
```

重命名原来的`views.py`文件为`views_old.py`,不然会跟目前的views目录冲突
修改`myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management.views import depart,user,pretty

urlpatterns = [
    path('admin/', admin.site.urls),
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('user/list/', user.user_list),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),
]
```

刷新浏览器,效果还是一样,不同的是我们的代码更加规整

## 管理员管理

### 创建数据库表

```python
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

```

执行命令

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/f66e91e4428d4275bf05b43f1ecaa7cc.png)
像素数据库表中插入一条数据

```sql
mysql> use my_project;

mysql> insert into employee_management_admin(username, password) values("张三", "123456");
Query OK, 1 row affected (0.00 sec)

mysql> insert into employee_management_admin(username, password) values("李四", "456789");
Query OK, 1 row affected (0.00 sec)

mysql> insert into employee_management_admin(username, password) values("楚云飞", "qwe123");
Query OK, 1 row affected (0.01 sec)

mysql> insert into employee_management_admin(username, password) values("小日子", "123456");
Query OK, 1 row affected (0.00 sec)

mysql> insert into employee_management_admin(username, password) values("小瘪三", "123456");
Query OK, 1 row affected (0.00 sec)

mysql> insert into employee_management_admin(username, password) values("大狗", "123456");
Query OK, 1 row affected (0.00 sec)

mysql> insert into employee_management_admin(username, password) values("孙悟空", "123456");
Query OK, 1 row affected (0.00 sec)

1234567891011121314151617181920212223
```

### 增加管理员菜单

修改`/root/python/myproject/employee_management/templates/layout.html`

```html
<ul class="nav navbar-nav">
	<li><a href="/admin/list/">管理员账户</a></li>
	<li><a href="/depart/list/">部门管理</a></li>
	<li><a href="/user/list/">用户管理</a></li>
	<li><a href="/pretty/list/">靓号管理</a></li>
</ul>
123456
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/178c51e4f03e49c0b97c2ce5f8629b22.png)

### 管理员列表

新建`myproject/employee_management/templates/admin_list.html`

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">

    <div>
        <div style="margin-bottom: 10px; ">
            <a class="btn btn-primary" href="/pretty/add/" target="_blank">新建管理员</a>

            <div style="float: right; width: 300px;">
                <form method="get">
                    <div class="input-group">
                        <input type="text" name="query" class="form-control" placeholder="Search for..."
                            value="{{ search_data }}">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">
                                <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                            </button>
                        </span>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>管理员列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>姓名</th>
                        <th>密码</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in page_queryset %}
                    <tr>
                        <th>{{ obj.id }}</th>
                        <td>{{ obj.username }}</td>
                        <td>{{ obj.password }}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="/admin/{{ obj.id }}/edit/">编辑</a>
                            <a class="btn btn-danger btn-xs" href="/admin/{{ obj.id }}/delete/">删除</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <ul class="pagination">
        {{ page_string }}
    </ul>
    <br>

    <form method="get">
        <div style="display:inline-block; width: 150px;">
            <div class="input-group">
                <span> <input type="text" class="form-control" placeholder="请输入页码" name="page"></span>
                <span class="input-group-btn">
                    <button class="btn btn-primary" type="submit">跳转</button>
                </span>
            </div>
        </div>
    </form>
</div>

{% endblock %}

```

新建`myproject/employee_management/views/admin.py`

```python
from django.shortcuts import render
from employee_management.models import Admin
from employee_management.utils.pagination import Pagination


def admin_list(request):
    """管理员列表"""

    data_dict = {}
    # 不加后面的 "", 首次访问浏览器,搜索框中不会显示前端页面中的 placeholder="Search for..." 属性
    search_data = request.GET.get('query', "")
    if search_data:
        data_dict["username__contains"] = search_data 
    
    queryset = Admin.objects.filter(**data_dict).order_by("id")

    # queryset = Admin.objects.all()
    page_object = Pagination(request, queryset, page_size=2)
    page_queryset = page_object.page_queryset
    page_object.html()
    page_string = page_object.page_string

    context = {
        "page_queryset": page_queryset,
        "page_string": page_string,
        "search_data": search_data,
    }
```

修改`/root/python/myproject/myproject/urls.py`

```python
from django.contrib import admin
from django.urls import path
from employee_management.views import depart,user,pretty,admin

urlpatterns = [

    # path('admin/', admin.site.urls),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/model/form/add/', user.user_model_form_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

    # 管理员管理
    path('admin/list/', admin.admin_list),
]
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2c45705bfbec4d3da66619c96c3a8817.png)

### 管理员添加

修改`myproject/employee_management/views/admin.py`

```python
from employee_management.utils.modelform import BootStrapModelForm
from django import forms


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

def admin_add(request):
    """添加管理员"""

    form = AdminModelForm

    context = {
        "form": form,
        "title": "新建管理员",
    }

    return render(request, "change.html", context)
```

> 按照之前的套路,我应该会新建一个名为`admin_add.html`的HTML文件来展示添加界面
> 这次我们优化一下
> 不管是`pretty_add.html`或者`user_add.html`,除了标题不一样,其他的都是一样的
> 没有必要在创建一个单独的HTML页面,我们只需要在一个公共的HTML页面中传入各自的标题即可

新建`myproject/employee_management/templates/change.html`

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">{{ title }}</h3>
        </div>
        <div class="panel-body">
            <form method="post" novalidate>
                {% csrf_token %}
                
                {% for field in form %}
                    <div class="form-group">
                        <label>{{ field.label }}: </label>
                        {{ field }}
                        <!-- 数据校验,显示错误信息 -->
                        <span style="color: red;">{{ field.errors.0 }}</span>
                    </div>
                {% endfor %}

                <button type="submit" class="btn btn-primary">保存</button>
            </form>
        </div>
    </div>
</div>

{% endblock %}
</body>

</html>
```

修改`myproject/myproject/urls.py`

```python
path('admin/add/', admin.admin_add),
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/6debd73dac974655a0eb619305c4fae2.png)

> 将数据保存到数据库

修改`myproject/employee_management/views/admin.py`

```python
def admin_add(request):
    """添加管理员"""

    title = "新建管理员"

    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"form": form, "title": title})

    # 如果是POST请求
    form = AdminModelForm(data=request.POST)

    context = {
        "form": form,
        "title": title,
    }
    
    if form.is_valid():
        form.save()
        return redirect("/admin/list")


    return render(request, "change.html", context)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c2fe0f8c334e4d5981d9e15cf453e62a.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/d59a34d1a021494d8a0354dff6001df2.png)

> 但是现在还有一个问题,如果两次输入的密码不一致呢?

修改`myproject/employee_management/views/admin.py`,增加[钩子函数](https://so.csdn.net/so/search?q=钩子函数&spm=1001.2101.3001.7020)`clean_confirm_password`

```python
class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    # 钩子函数
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        if confirm != pwd:
            raise ValidationError("密码不一致!")
        return confirm
```

浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/bbd8b7ae9d134669afa457b8b077efac.png)
可以发现,[数据校验](https://so.csdn.net/so/search?q=数据校验&spm=1001.2101.3001.7020)成功了
但是还有个问题,当我们点击保存后,密码和密码确认框中的数据清空了
这样不是太友好,因此我们需要添加一个属性

修改`myproject/employee_management/views/admin.py`

```python
render_value=True
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/973e3ff3591f4047bcc720b21d3525ad.png)
然后测试,就不会出现自动清空的情况了

> 现在又出现一个问题
> 密码这样存储进数据库,很不安全
> 我们最好对其进行加密后,再进行保存

这里我们使用`md5`方式进行加密
新建`/root/python/myproject/employee_management/utils/encrypt.py`文件

```python
import hashlib
from django.conf import settings

def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()
```

修改`myproject/employee_management/views/admin.py`

```python
## clean_字段名
def clean_password(self):
    pwd = self.cleaned_data.get("password")
    # return什么.password字段保存什么
    return md5(pwd)

## 钩子函数
def clean_confirm_password(self):
    pwd = self.cleaned_data.get("password")
    confirm = self.cleaned_data.get("confirm_password")
    if md5(confirm) != pwd:
        raise ValidationError("密码不一致!")
    
    # return返回什么,字段 confirm_password 保存至数据库的值就是什么
    return md5(confirm)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/637339feff1048a18089c6a10e43a736.png)
浏览器添加新用户测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/774d493a884644b98b92d14d6ddd1463.png)

### 管理员编辑

修改`myproject/employee_management/templates/admin_list.html`

```html
<a class="btn btn-primary btn-xs" href="/admin/{{ obj.id }}/edit/">编辑</a>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/851bb778b7154f72b013826aa2f2735a.png)
修改`myproject/myproject/urls.py`

```python
path('admin/<int:nid>/edit/', admin.admin_edit),
```

修改`myproject/employee_management/views/admin.py`

```python
## 如果不想让用户修改密码,只能修改用户名,那么使用下面这个AdminEditModelForm 
## 如果都可以修改,直接用上面的AdminModelForm即可
class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = Admin
        fields = ["username"]

def admin_edit(request, nid):

    # 判断 nid 是否存在
    row_object = Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, "error.html", {"msg": "数据不存在!"})

    """编辑管理员"""

    title = "编辑管理员"

    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    
    return render(request, "change.html", {"form": form, "title": title})
```

浏览器访问,修改`张三`为`张三啊`
![在这里插入图片描述](https://img-blog.csdnimg.cn/8fba8fe476624b75864af776e62d70d6.png)
点击"保存"
![在这里插入图片描述](https://img-blog.csdnimg.cn/787c66b5f721465399cb8c7283f07c43.png)

### 管理员删除

修改`myproject/employee_management/templates/admin_list.html`

```html
<a class="btn btn-danger btn-xs" href="/admin/{{ obj.id }}/delete/">删除</a>
```

修改`myproject/myproject/urls.py`

```python
path('admin/<int:nid>/delete/', admin.admin_delete),
```

修改`myproject/employee_management/views/admin.py`

```python
def admin_delete(request, nid):
    """删除管理员"""
    Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")
```

### 管理员重置密码

修改`myproject/employee_management/templates/admin_list.html`

```html
<th>重置密码</th>

...

<td>
    <a class="btn btn-primary btn-xs" href="/admin/{{ obj.id }}/edit/">编辑</a>
    <a class="btn btn-danger btn-xs" href="/admin/{{ obj.id }}/delete/">删除</a>
</td>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/69cdcbd564f54d39a86a4fcc05462051.png)
修改`myproject/myproject/urls.py`

```python
path('admin/<int:nid>/reset/', admin.admin_reset),
```

修改`myproject/employee_management/views/admin.py`

```python
class AdminResetModelForm(BootStrapModelForm):

    confirm_password = forms.CharField(
        label = "确认密码",
        widget = forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    # clean_字段名
    def clean_password(self):
        pwd = self.cleaned_data.get("password")

        # 校验当前数据库中的密码与用户输入的新密码是否一致
        exists = Admin.objects.filter(id=self.instance.pk, password=md5(pwd))
        if exists:
            raise ValidationError("密码不能与当前密码一致!")

        # return什么.password字段保存什么
        return md5(pwd)

    # 钩子函数
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        if md5(confirm) != pwd:
            raise ValidationError("密码不一致!")
        
        # return返回什么,字段 confirm_password 保存至数据库的值就是什么
        return md5(confirm)

def admin_reset(request, nid):
    """重置管理员密码"""

    # 判断 nid 是否存在
    row_object = Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, "error.html", {"msg": "数据不存在!"})

    title = "重置密码 - {}".format(row_object.username)

    if request.method == "GET":
        form = AdminResetModelForm(instance=row_object)
        
        return render(request, "change.html", {"title": title, "form": form})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")

    return render(request, "change.html", {"title": title, "form": form})
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c83621ae14b34071b0c11f2205864dff.png)

> 不知道为什么下面的"密码不一致错误也出来了",后面待解决

## 账户登录

### 登录界面

修改`myproject/employee_management/templates/layout.html`

```html
{% block css %}
<style>

    .navbar {
        border-radius: 0;
    }

</style>

{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/22eeb5aceea64dea8b5ff48754288052.png)
新建`myproject/employee_management/templates/login.html`

```html
{% extends 'layout.html' %}


{% block css %}
<style>
    .account {
        width: 400px;
        border: 1px solid #dddddd;
        border-radius: 5px;
        box-shadow: 5px 5px 20px #aaa;

        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
        padding: 20px 40px;
    }

    .account h2 {
        margin-top: 10px;
        text-align: center;
    }
</style>
{% endblock %}


{% block content %}
<div class="account">
    <h2>用户登录</h2>
    <div class="panel-body">
        <form method="post">
            {% csrf_token %}
            <div class="form-group">
                <label>用户名</label>
                <input type="text" class="form-control" placeholder="用户名" name="username">
            </div>
            <div class="form-group">
                <label>密码</label>
                <input type="password" class="form-control" placeholder="密码" name="password">
            </div>
            <button type="submit" class="btn btn-primary center-block" style="width: 80px;">登录</button>
        </form>
    </div>
</div>
{% endblock %}
```

修改`myproject/myproject/urls.py`

```python
## 登录
path('login/', account.login),
```

新建`myproject/employee_management/views/account.py`

```python
from django.shortcuts import render

def login(request):
    """登录"""

    return render(request, 'login.html')
```

浏览器简单访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/4ca3b8b87e2a4839874f7e98df6653f1.png)

### 用户名密码验证

修改`myproject/employee_management/templates/login.html`

```html
{% extends 'layout.html' %}


{% block css %}
<style>
    .account {
        width: 400px;
        border: 1px solid #dddddd;
        border-radius: 5px;
        box-shadow: 5px 5px 20px #aaa;

        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
        padding: 20px 40px;
    }

    .account h2 {
        margin-top: 10px;
        text-align: center;
    }
</style>
{% endblock %}


{% block content %}
<div class="account">
    <h2>用户登录</h2>
    <div class="panel-body">
        <form method="post" novalidate>
            {% csrf_token %}
            <div class="form-group">
                <label>用户名</label>
                {{ form.username }}
                <span style="color: red;">{{ form.errors.username.0 }}</span>
                
            </div>
            <div class="form-group">
                <label>密码</label>
                {{ form.password }}
                <span style="color: red;">{{ form.errors.password.0 }}</span>
            </div>
            
            <button type="submit" class="btn btn-primary center-block" style="width: 80px;">登录</button>
        </form>
    </div>
</div>
{% endblock %}
```

修改`myproject/employee_management/views/account.py`

```python
from django.shortcuts import render, HttpResponse
from django import forms
from employee_management.utils.modelform import BootStrapForm
from employee_management.utils.encrypt import md5
from employee_management.models import Admin

## 这一次不使用ModelForm,使用Form来实现
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="用户名",
        # render_value=True 表示当提交后,如果密码输入错误,不会自动清空密码输入框的内容
        widget=forms.PasswordInput(attrs={"class": "form-control"}, ),
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功, 获取到的用户名和密码
        # print(form.cleaned_data)
        # {'username': '123', 'password': '123'}
        # {'username': '456', 'password': '0f54af32f41a5ba8ef3a2d40cd6ccf25'}

        # 去数据库校验用户名和密码是否正确
        admin_object = Admin.objects.filter(**form.cleaned_data).first()
        # 如果数据库中没有查询到数据
        if not admin_object:
        	# 手动抛出错误显示在"password"字段下
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        return HttpResponse("登陆成功")

    return render(request, 'login.html', {"form": form})
```

浏览器进行测试
新建用户`toker`(必须为后来使用[md5加密](https://so.csdn.net/so/search?q=md5加密&spm=1001.2101.3001.7020)过密码的用户,不能是明文密码的用户)
![在这里插入图片描述](https://img-blog.csdnimg.cn/f11dee24b28c4be691e5fb1e2e4b1627.png)
输入错误的密码
![在这里插入图片描述](https://img-blog.csdnimg.cn/576da4db8c3d436aa43b5b57eff9b234.png)
输入正确的密码
![在这里插入图片描述](https://img-blog.csdnimg.cn/3a781a8f752f4449bc7a036745cf6688.png)

### 配置cookie与session

修改`myproject/employee_management/views/account.py`

```python
def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功, 获取到的用户名和密码
        print(form.cleaned_data)
        # {'username': '123', 'password': '123'}
        # {'username': '456', 'password': '0f54af32f41a5ba8ef3a2d40cd6ccf25'}

        # 去数据库校验用户名和密码是否正确
        admin_object = Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        # 如果用户名密码正确
        # 网站生成随机字符创,写到用户浏览器的cookie中,再写入到服务器的session中
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect("/admin/list/")

    return render(request, 'login.html', {"form": form})
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/717c94a4ae2747b996f987459ac7adab.png)
登录成功后,跳转到`管理员列表`界面
`session`信息保存在了服务器中的Mysql数据库`django_session`表中

```sql
mysql> use my_project;

mysql> show tables;
+--------------------------------+
| Tables_in_my_project           |
+--------------------------------+
| auth_group                     |
| auth_group_permissions         |
| auth_permission                |
| auth_user                      |
| auth_user_groups               |
| auth_user_user_permissions     |
| django_admin_log               |
| django_content_type            |
| django_migrations              |
| django_session                 |
| employee_management_admin      |
| employee_management_department |
| employee_management_prettynum  |
| employee_management_userinfo   |
+--------------------------------+

mysql> select * from django_session;
+----------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+
| session_key                      | session_data                                                                                    | expire_date                |
+----------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+
| zkgq26t7hqx3yu6xo04bws856002n5aj | eyJpbmZvIjp7ImlkIjoxMiwibmFtZSI6InRva2VyIn19:1pElim:Tus2mHaJUTNTfzhppuah8N0FVdLXQxyvRk_4n-4fP6g | 2023-01-23 06:33:24.373104 |
+----------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/3780462856934d59ac43fcfaaaee88b3.png)

> 当实现了这个功能后,我们需要对每个页面做验证,只有登陆的人才可以访问这些页面,这个功能在下一节的中间件中来实现

### 中间件实现登录验证

> 中间件会在视图函数下的每个方法执行前调用,不用在每个方法下面进行判断,不然函数太多,过于繁琐。

新建`myproject/employee_management/middleware`目录
在其下新建`myproject/employee_management/middleware/auth.py`文件

```python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 0.排除不需要的页面
        if request.path_info == "/login/":
            return

        # 1.读取当前访问的用户的session信息,如果能读到,说明已登录过,就可以继续向后走
        info_dict = request.session.get("info")
        if info_dict:
            return

        # 2.如果没有登录信息
        return redirect("/login/")
```

修改`myproject/myproject/setting.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'employee_management.middleware.auth.AuthMiddleware',
]
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7f01b78fda4545cd9dbb1e6baf40407e.png)

>如果方法中没有返回值 (返回 None) 继续向后走
>
>如果由返回值 HttpResponse render redirect 则不再继续向后执行

浏览器访问`/pretty/list/`进行测试
你会发现只要你没登录过,不管你访问什么页面,都会跳转到`login`登录界面

> 登录校验的功能算是实现了,但是登录的用户目前无法退出,下一节进行介绍

### 用户注销

> 小插曲: 我刚才整理代码的时候才发现,我因为之前使用了`datetimepicker`的日期插件,粘贴代码的时候,将我原来css样式给覆盖掉了,其实是我粘贴多了,需要先改一下,不然右上角的按钮无法展开,抱歉抱歉

![在这里插入图片描述](https://img-blog.csdnimg.cn/57f0e60f96b74439b4e9fccc63991a5c.png)
修改`myproject/employee_management/templates/layout.html`,将下面的几行注释掉
![在这里插入图片描述](https://img-blog.csdnimg.cn/af7748375f434c82a237025944d8d93f.png)
配置注销按钮的跳转URL地址
![在这里插入图片描述](https://img-blog.csdnimg.cn/afc7abf7b4ed45b187f4c682c7966c51.png)

然后保存就可以了

> 接下来实现注销功能

修改`myproject/employee_management/views/account.py`

```python
def logout(request):
    """ 注销 """

    # 清楚当前session
    request.session.clear()

    return redirect("/login/")
```

修改`myproject/myproject/urls.py`

```python
path('logout/', account.logout),
```

浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/3971a2d70d0f4e6fa77ac9c4bfac089b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/bcb9028787074685914d9e2656162fe9.png)登录成功后,右上角的用户名还不是目前登录的用户,所以我们还需要再做一次修改
![在这里插入图片描述](https://img-blog.csdnimg.cn/365f8248ede143a9b0c1a89126ba3f91.png)
因为在`login函数`中`request.session`中定义的username字段对应的名称为`name`,所以我们可以在前端代码中直接调用

```html
<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
aria-expanded="false">{{ request.session.info.name }}<span class="caret"></span></a>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e9a3e304ecaf49019bc4f4eceb37195e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/c45e4eb4c0fb403f9e39c2122730366f.png)

### 图片验证码

> 生成验证码参考链接: https://www.cnblogs.com/wupeiqi/articles/5812291.html

下载必要的软件

```shell
pip3 install pillow
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/075762f7f5c94ea8b1571ee34b7825cd.png)
下载字体

> 点击这里: [验证码字体下载](https://files.cnblogs.com/files/wupeiqi/验证码字体文件.zip)

新建`myproject/employee_management/utils/ttf`目录,将字体放在其下
![在这里插入图片描述](https://img-blog.csdnimg.cn/fb654c49901342338e04c71ff77cafab.png)
新建`myproject/employee_management/utils/code.py`,编辑验证码生成函数

```python
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
 

def check_code(width=120, height=30, char_length=5, font_file='employee_management/utils/ttf/Monaco.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')
 
    def rndChar():
        """
        生成随机字母   
        :return:
        """
        return chr(random.randint(65, 90))
 
    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))
 
    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())
 
    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
 
    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())
 
    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
 
        draw.line((x1, y1, x2, y2), fill=rndColor())
 
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img,''.join(code)


if __name__ == '__main__':
    img, code_str = check_code()
    print(code_str)

    with open('code.png', 'wb') as f:
        img.save(f, format='png')
```

修改`myproject/employee_management/views/account.py`,引入调用刚刚写的验证码生成函数

```python
from employee_management.utils.code import check_code
from django.shortcuts import HttpResponse
from io import BytesIO

def image_code(request):
    """ 生成图片验证码 """
    # 调用pillow函数,生成图片
    img, code_string = check_code()

	# 将图片保存到内存
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
```

修改`myproject/myproject/urls.py`

```python
path('image/code/', account.image_code),
```

还需要将该函数的URL加入访问白名单,使验证码链接可用
编辑`myproject/employee_management/middleware/auth.py`

```python
## 0.排除不需要的页面
if request.path_info in ["/login/", "/image/code/"]:
    return
```

修改`myproject/employee_management/templates/login.html`

```html
{% extends 'layout.html' %}


{% block css %}
<style>
    .account {
        width: 400px;
        border: 1px solid #dddddd;
        border-radius: 5px;
        box-shadow: 5px 5px 20px #aaa;

        margin-left: auto;
        margin-right: auto;
        margin-top: 100px;
        padding: 20px 40px;
    }

    .account h2 {
        margin-top: 10px;
        text-align: center;
    }
</style>
{% endblock %}


{% block content %}
<div class="account">
    <h2>用户登录</h2>
    <div class="panel-body">
        <form method="post" novalidate>
            {% csrf_token %}
            <div class="form-group">
                <label>用户名</label>
                {{ form.username }}
                <span style="color: red;">{{ form.errors.username.0 }}</span>
                
            </div>
            <div class="form-group">
                <label>密码</label>
                {{ form.password }}
                <span style="color: red;">{{ form.errors.password.0 }}</span>
            </div>
            <div class="form-group">
                <label for="id_code">图片验证码</label>
                <div class="row">
                    <div class="col-xs-7">
                        <input type="text" name="code" class="form-control" placeholder="请输入图片验证码" required="" id="id_code">
                        <span style="color: red;"></span>
                    </div>
                    <div class="col-xs-5">
                        <img src="/image/code/" alt="" id="image_code">
                    </div>
                </div>
            </div>
            <button type="submit" class="btn btn-primary center-block" style="width: 80px;">登 录</button>
        </form>
    </div>
</div>
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/c1d448f7b6d7416682caa35b3656e22c.png)
浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/dcfef539168944f1ae3d90665e529d32.png)

### 验证码的校验

> 接下来需要验证用户输入的验证码与生成的验证码是否一致

修改`myproject/employee_management/views/account.py`

- 第一处

```python
code = forms.CharField(
    label="验证码",
    widget=forms.TextInput(attrs={"class": "form-control"}),
    required=True,
)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/465f04ca9eb74029bb1a513182e7177e.png)

- 第二处

```python
def image_code(request):
    """ 生成图片验证码 """
    # 调用pillow函数,生成图片
    img, code_string = check_code()

    # 写入到自己的session中,以便于后续获取验证码再进行校验
    request.session['image_code'] = code_string
    # 给session设置 60s 超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/adcc71c1915f49a9aaecbf5ac98ceb2d.png)

- 第三处

```python
def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功, 获取到的用户名和密码
        print(form.cleaned_data)
        # {'username': '123', 'password': '123'}
        # {'username': '456', 'password': '0f54af32f41a5ba8ef3a2d40cd6ccf25'}

        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        image_code = request.session.get('image_code', "")
        print("user_input_code={}, image_code={}".format(user_input_code, image_code))
        if image_code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})

        # 去数据库校验用户名和密码是否正确
        admin_object = Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        # 如果用户名密码和验证码正确
        # 网站生成随机字符创,写到用户浏览器的cookie中,再写入到服务器的session中
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # 重新设置session的超时时间,因为之前设置的session的超时时间的 60s
        request.session.set_expiry(60 * 60 * 24)

        return redirect("/admin/list/")

    return render(request, 'login.html', {"form": form})
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/ec8be42f6d2e4c4fa0ee54931bbe44cc.png)
浏览器登录测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/b2264fbcd4b14472a53337253d3edaeb.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/f07eea8147f24a94a7f65ed9a218e2d0.png)

> 现在已经可以正常登录,但是还可以进行优化
> 我们想要点击验证码图片进行刷新验证码,很简单

修改`myproject/employee_management/templates/login.html`

```python
<img src="/image/code/" alt="" id="image_code" onclick="this.setAttribute('src','/image/code/?random='+Math.random())">
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/308ef794127544e081ff91cc3aa9258b.png)
点击验证码图片后,验证码可刷新



## 解决跨域问题



```python
pip3 install django-cors-headers
```



在 setting.py 中配置文件

![image-20230913085550556](https://imgtroage-1317162111.cos.ap-nanjing.myqcloud.com/img/image-20230913085550556.png)

```text
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
## CORS_ORIGIN_WHITELIST = (
##     'http://127.0.0.1:8080',
## )
CORS_ALLOWED_ORIGINS_REGEXES=[
    r'^http://.*?$',
]
## CORS_ORIGIN_REGEXES_WHITELIST = (
##         r'^http://.*?$',
## )
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
   )
```

添加中间件

1. 
   MIDDLEWARE = [
2. ​    'corsheaders.middleware.CorsMiddleware',
3. ​    ...
4. 

## Ajax

浏览器向网站发送请求时,URL 和 表单的形式提交

- GET
- POST

> 特点: [页面刷新](https://so.csdn.net/so/search?q=页面刷新&spm=1001.2101.3001.7020)

`Ajax可以实现向后台偷偷发送请求`

- 依赖JQuery （ 发送简单 ）
- 编写Ajax代码

```python
$.ajax({
	url:"发送的地址",
	type: "get",
	data:{
		n1:123,
		n2:456
	},
	success:function(res){
		console.log(res);
	}
})
```

### GET请求

新建`myproject/employee_management/views/task.py`

```python
from django.shortcuts import render,HttpResponse
def task_list(request):

    return render(request, "task_list.html")


def task_ajax(request):
    print(request.GET)
    return HttpResponse("成功了")
```

修改`myproject/myproject/urls.py`

```python
## 任务管理
path('task/list/', task.task_list),
path('task/ajax/', task.task_ajax),
```

新建`myproject/employee_management/templates/task_list.html`

```html
{% extends 'layout.html' %}

{% block content %}

    <div class="container">
        <h1>任务管理</h1>
        <h3>示例1</h3>
        <input type="button" value="点击" class="btn btn-primary" onclick="clickMe();">
    </div>

{% endblock %}

{% block script %}
    <script type="text/javascript">
        function clickMe() {
            $.ajax({
                url: '/task/ajax/',
                type: "get",
                data: {
                    n1:123,
                    n2:456
                },
                success: function(res) {
                    console.log(res);
                }
            })
        }
    </script>
{% endblock %}
```

修改`myproject/employee_management/templates/layout.html`

```html
<li><a href="/task/list/">任务管理</a></li>

...

{% block script %}
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/52759756c2d64446be0b76235c640fbd.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2cfcab193f694c9e888e7848e6773e9c.png)
浏览器访问测试,打开F12进入调试界面
![在这里插入图片描述](https://img-blog.csdnimg.cn/9884ed70ac9349149790b57d19f0ed20.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/1e5628c339a24b7b9900a06fa5493738.png)
查看后台输出
![在这里插入图片描述](https://img-blog.csdnimg.cn/9b3635ec3cf4416caa36a93583ade69a.png)

### POST请求

修改`myproject/employee_management/views/task.py`

> csrf_exempt可以免除在HTM中写[CSRF](https://so.csdn.net/so/search?q=CSRF&spm=1001.2101.3001.7020)

```python
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

def task_list(request):

    return render(request, "task_list.html")

@csrf_exempt
def task_ajax(request):
    print("get请求: ", request.GET)
    print("post请求: ", request.POST)
    return HttpResponse("成功了")
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/ab79089533f742f9ae37e4533f031fa3.png)
修改`myproject/employee_management/templates/task_list.html`
![在这里插入图片描述](https://img-blog.csdnimg.cn/b0a89e064122478bbd7a89eaf9e425cf.png)
浏览器访问测试,F12依然开启调试模式
![在这里插入图片描述](https://img-blog.csdnimg.cn/54f970dcd5184ded9fb5fa51e1d768a9.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/956390aaae1941418fd491ef63b921a2.png)
查看后台输出
![在这里插入图片描述](https://img-blog.csdnimg.cn/197534afe0944abfabccf88fb2e915c7.png)

> 对上面的Ajax代码进行优化: `绑定事件`

修改`myproject/employee_management/templates/task_list.html`

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">
    <h1>任务管理</h1>
    <h3>示例1</h3>
    <input id="btn1" type="button" value="点击" class="btn btn-primary">
</div>

{% endblock %}

{% block script %}
<script type="text/javascript">

    $(function () {
        // 页面框架加载完成之后代码自动执行
        bindBtn1Event();
    })

    function bindBtn1Event() {
        $("#btn1").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    n1: 123,
                    n2: 456
                },
                success: function (res) {
                    console.log(res);
                }
            })
        })

    }
</script>
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/310f07a4420a4f6591298d93416962d9.png)

### 返回值

> 以JSON的方式返回数据

修改`myproject/employee_management/templates/task_list.html`

```javascript
function bindBtn1Event() {
    $("#btn1").click(function () {
        $.ajax({
            url: '/task/ajax/',
            type: "post",
            data: {
                n1: 123,
                n2: 456
            },
            dataType: "JSON",
            success: function (res) {
                console.log(res);
                console.log(res.status);
                console.log(res.data);
            }
        })
    })
}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/878319d303274270939d2e24585db31b.png)
浏览器刷新访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/be8caaf1a77d4d06a9ebea7efd182bbe.png)

> 实现后台接收`输入框`中的内容

修改`myproject/employee_management/templates/task_list.html`

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">
    <h1>任务管理</h1>
    <h3>示例1</h3>
    <input id="btn1" type="button" value="点击" class="btn btn-primary">

    <h3>示例2</h3>
    <input type="text" id="txtuser" placeholder="姓名">
    <input type="text" id="txtpwd" placeholder="密码">
    <input id="btn2" type="button" value="点击" class="btn btn-primary">


</div>

{% endblock %}

{% block script %}
<script type="text/javascript">

    $(function () {
        // 页面框架加载完成之后代码自动执行
        bindBtn1Event();
        bindBtn2Event();
    })


    function bindBtn1Event() {
    $("#btn1").click(function () {
        $.ajax({
            url: '/task/ajax/',
            type: "post",
            data: {
                n1: 123,
                n2: 456
            },
            dataType: "JSON",
            success: function (res) {
                console.log(res);
                console.log(res.status);
                console.log(res.data);
            }
        })
    })
}

    function bindBtn2Event() {
        $("#btn2").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    name: $("#txtuser").val(),
                    password: $("#txtpwd").val()
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }
</script>
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/ca45c2e5762947198ec6604b2fe5db09.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/9e3953238116454b80635755815365fd.png)

浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/bf7fe4eefcb34682aab61a5a7c8e6f45.png)
查看后台
![在这里插入图片描述](https://img-blog.csdnimg.cn/0557cd53b32e45cb95c354fca15ec509.png)

> 假如前端代码过多,我们需要用更简单的方法[批量处理](https://so.csdn.net/so/search?q=批量处理&spm=1001.2101.3001.7020)

修改`myproject/employee_management/templates/task_list.html`

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">
    <h1>任务管理</h1>
    <h3>示例1</h3>
    <input id="btn1" type="button" value="点击1" class="btn btn-primary">

    <h3>示例2</h3>
    <input type="text" id="txtuser" placeholder="姓名">
    <input type="text" id="txtpwd" placeholder="密码">
    <input id="btn2" type="button" value="点击2" class="btn btn-primary">

    <form id="from3">
        <h3>示例2</h3>
        <input type="text" name="user" placeholder="姓名">
        <input type="text" name="age" placeholder="年龄">
        <input type="text" name="pwd" placeholder="密码">
        <input type="text" name="mobile" placeholder="电话">
    </form>
    <input id="btn3" type="button" value="点击3" class="btn btn-primary">



</div>

{% endblock %}

{% block script %}
<script type="text/javascript">

    $(function () {
        // 页面框架加载完成之后代码自动执行
        bindBtn1Event();
        bindBtn2Event();
        bindBtn3Event();
    })


    function bindBtn1Event() {
        $("#btn1").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    n1: 123,
                    n2: 456
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindBtn2Event() {
        $("#btn2").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    name: $("#txtuser").val(),
                    password: $("#txtpwd").val()
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindBtn3Event() {
        $("#btn3").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: $("#from3").serialize(),
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }
</script>
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/8bd9c8a85b1841acad158096b1414b62.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/357f4aff2dd948b18dc988ed64081446.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/e58ad77b993a482eb1f0c38aecae307c.png)
浏览器进行测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/5ce88f753b2346679bee98150403f359.png)
查看后台
![在这里插入图片描述](https://img-blog.csdnimg.cn/112d76ead2544ae68d47f3080de0a479.png)

> 这样,我们就学会了如何在浏览器页面不刷新的情况下,如何向后台提交数据

接下来正式开始Ajax的案例

### 任务添加(一)

> 首先为该页面创建一个表

编辑`myproject/employee_management/models.py`

```python
class Task(models.Model):
    """任务"""

    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to=Admin, on_delete=models.CASCADE)
123456789101112
```

更新信息

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

编辑`myproject/employee_management/views/task.py`

```python
from employee_management.utils.modelform import BootStrapModelForm
from employee_management.models import Task


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = Task
        fields = "__all__"


@csrf_exempt
def task_list(request):
    form = TaskModelForm()
    return render(request, "task_list.html", {"form": form})
1234567891011121314
```

编辑`myproject/employee_management/templates/task_list.html`

```html
<div class="panel panel-default">
   <div class="panel-heading">表单</div>
    <div class="panel-body">
        <form method="post" novalidate>
            {% for item in form %}
            <div class="form-group">
                <label>{{ item.label }}</label>
                {{ item }}
            </div>
            {% endfor %}
        </form>
    </div>
</div>

```

![在这里插入图片描述](https://img-blog.csdnimg.cn/658caac99fd4496ea0bce35c260d4df0.png)
浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/79002a733cdd44818dc5d6064760103a.png)
但是会有一个问题存在
![在这里插入图片描述](https://img-blog.csdnimg.cn/6c396287152c40ddae2df3d7efbd9116.png)
解决办法:编辑`myproject/employee_management/models.py`

> ```
> def __str__(self):`
> `return self.username
> ```

```python
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/70fdb708b0c0465ea371ea73097baf03.png)

> 接下来实现将添加的数据发送到后台

优化一下前端的展示样式
编辑`myproject/employee_management/templates/task_list.html`

> 注意: 下面前端代码中的`button`标签必须放在`form`表单的外面,不然`submit`的 Ajax 触发机制不会生效

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">

    <div class="panel panel-default">
        <div class="panel-heading">表单</div>
        <div class="panel-body">
            <form method="post" id="task_form" novalidate>
                <div>
                    {% for item in form %}
                    <div class="col-xs-6">
                        <div class="form-group">
                            <label>{{ item.label }}</label>
                            {{ item }}
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </form>
            <div class="col-xs-12">
                <input id="submit" type="submit" value="提 交" class="btn btn-primary center-block" style="width: 100px;">
            </div>
        </div>
    </div>

    <h1>任务管理</h1>
    <h3>示例1</h3>
    <input id="btn1" type="button" value="点击1" class="btn btn-primary">

    <h3>示例2</h3>
    <input type="text" id="txtuser" placeholder="姓名">
    <input type="text" id="txtpwd" placeholder="密码">
    <input id="btn2" type="button" value="点击2" class="btn btn-primary">

    <form id="from3">
        <h3>示例2</h3>
        <input type="text" name="user" placeholder="姓名">
        <input type="text" name="age" placeholder="年龄">
        <input type="text" name="pwd" placeholder="密码">
        <input type="text" name="mobile" placeholder="电话">
    </form>
    <input id="btn3" type="button" value="点击3" class="btn btn-primary">



</div>

{% endblock %}

{% block script %}
<script type="text/javascript">

    $(function () {
        // 页面框架加载完成之后代码自动执行
        bindBtn1Event();
        bindBtn2Event();
        bindBtn3Event();
        bindaddEvent();
    })


    function bindBtn1Event() {
        $("#btn1").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    n1: 123,
                    n2: 456
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindBtn2Event() {
        $("#btn2").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    name: $("#txtuser").val(),
                    password: $("#txtpwd").val()
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindBtn3Event() {
        $("#btn3").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: $("#from3").serialize(),
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindaddEvent() {
        $("#submit").click(function () {
            $.ajax({
                url: '/task/add/',
                type: "post",
                data: $("#task_form").serialize(),
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }
</script>
{% endblock %}
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127128129130131132133134
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/49efae892de84fdfb11b98232659f814.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/1ba90c37dbff4c90b4e4776894887e04.png)

### 任务添加(二)

编辑`myproject/employee_management/views/task.py`

```python
from django import forms

class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "detail": forms.TextInput,
        }

...

@csrf_exempt
def task_add(request):
    print(request.POST)
    data_dict = {"status": True}
    return HttpResponse(json.dumps(data_dict))
```

编辑`myproject/myproject/urls.py`

```python
path('task/add/', task.task_add),
```

浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/9ddc4534331c4061bd1896d241a7e38f.png)
后台查看输出内容
![在这里插入图片描述](https://img-blog.csdnimg.cn/3ef43d7ffe0c439db601345bcba3da8c.png)

> 接下来保存数据并进行数据校验

编辑`myproject/employee_management/views/task.py`

```python
@csrf_exempt
def task_add(request):
    print(request.POST)

    # 1.用户发送过来的数据进行校验(ModelForm进行数据校验)
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict))
```

编辑`myproject/employee_management/templates/task_list.html`

```html
{% extends 'layout.html' %}

{% block content %}

<div class="container">

    <div class="panel panel-default">
        <div class="panel-heading">表单</div>
        <div class="panel-body">
            <form method="post" id="task_form" novalidate>
                <div>
                    {% for item in form %}
                    <div class="col-xs-6">
                        <div class="form-group" style="position: relative; margin-top: 20px">
                            <label>{{ item.label }}</label>
                            {{ item }}
                            <span class="error_msg" style="color: red;position: absolute;"></span>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </form>
            <div class="col-xs-12" style="margin-top: 20px">
                <input id="submit" type="submit" value="提 交" class="btn btn-primary center-block" style="width: 100px;">
            </div>
        </div>
    </div>

    <h1>任务管理</h1>
    <h3>示例1</h3>
    <input id="btn1" type="button" value="点击1" class="btn btn-primary">

    <h3>示例2</h3>
    <input type="text" id="txtuser" placeholder="姓名">
    <input type="text" id="txtpwd" placeholder="密码">
    <input id="btn2" type="button" value="点击2" class="btn btn-primary">

    <form id="from3">
        <h3>示例2</h3>
        <input type="text" name="user" placeholder="姓名">
        <input type="text" name="age" placeholder="年龄">
        <input type="text" name="pwd" placeholder="密码">
        <input type="text" name="mobile" placeholder="电话">
    </form>
    <input id="btn3" type="button" value="点击3" class="btn btn-primary">



</div>

{% endblock %}

{% block script %}
<script type="text/javascript">

    $(function () {
        // 页面框架加载完成之后代码自动执行
        bindBtn1Event();
        bindBtn2Event();
        bindBtn3Event();
        bindaddEvent();
    })


    function bindBtn1Event() {
        $("#btn1").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    n1: 123,
                    n2: 456
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindBtn2Event() {
        $("#btn2").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: {
                    name: $("#txtuser").val(),
                    password: $("#txtpwd").val()
                },
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindBtn3Event() {
        $("#btn3").click(function () {
            $.ajax({
                url: '/task/ajax/',
                type: "post",
                data: $("#from3").serialize(),
                dataType: "JSON",
                success: function (res) {
                    console.log(res);
                    console.log(res.status);
                    console.log(res.data);
                }
            })
        })
    }

    function bindaddEvent() {
        $("#submit").click(function () {

            // 每次点击,将以前的错误信息清空
            $(".error_msg").empty();

            $.ajax({
                url: '/task/add/',
                type: "post",
                data: $("#task_form").serialize(),
                dataType: "JSON",
                success: function (res) {
                    // 如果数据校验正确
                    if(res.status){
                        alert("添加成功");
                    } else {
                        // 否则将错误信息显示在输入框下
                        $.each(res.error, function(name,data){
                            $("#id_" + name).next().text(data[0]);
                        })
                    }
                }
            })
        })
    }
</script>
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4501c22237ec4258adf477c217766911.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/63df6d98abe74682bf87ae962a2fa8d7.png)

> 在上面的 HTML 代码中,我在操作时很奇怪为什么错误信息会显示在输入框的下面,然后又看了一遍武佩奇老师的视频,发现原理是这样的

ModelForm 在生成页面标签时,会在 input 标签上自动加入`required id`,它的值由`id_` + `input标签的name属性的值`组成
![在这里插入图片描述](https://img-blog.csdnimg.cn/7be0da0dbaf240b2b3169f181be14410.png)
而在 HTML 中 Javascript 的一行代码,自动在下一行的标签中加入了数据

```javascript
$("#id_" + name).next().text(data[0]);
```

明白了吧?
ok

### 任务列表

> 在上面 HTML 代码的基础上进行添加,包括:
>
> - 添加数据后列表自动刷新
> - 分页
> - 搜索

- 实现添加数据后列表自动刷新

编辑`myproject/employee_management/templates/task_list.html`

```javascript
location.reload();
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/31634d6b14874bfbba7b6852a53c7996.png)

- 实现分页与搜索
  编辑`myproject/employee_management/templates/task_list.html`,在`<div class="container">`内加入如下代码

```html
<div>
    <div class="panel panel-default">
        <!-- Default panel contents -->
        <div class="panel-heading">
            <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
            <span>任务列表</span>
        </div>

        <!-- Table -->
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>标题</th>
                    <th>级别</th>
                    <th>负责人</th>
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
                {% for obj in queryset %}
                <tr>
                    <th>{{ obj.id }}</th>
                    <td>{{ obj.title }}</td>
                    <td>{{ obj.get_level_display }}</td>
                    <td>{{ obj.user.username }}</td>
                    <td>
                        <a class="btn btn-primary btn-xs" href="#">编辑</a>
                        <a class="btn btn-danger btn-xs" href="#">删除</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>

<ul class="pagination">
    {{ page_string }}
</ul>
<br>

<form method="get">
    <div style="display:inline-block; width: 150px;">
        <div class="input-group">
            <span> <input type="text" class="form-control" placeholder="请输入页码" name="page"></span>
            <span class="input-group-btn">
                <button class="btn btn-primary" type="submit">跳转</button>
            </span>
        </div>
    </div>
</form>
```

编辑`myproject/employee_management/views/task.py`

```python
from employee_management.utils.pagination import Pagination


@csrf_exempt
def task_list(request):
    """ 任务列表 """
    
    form = TaskModelForm()

    ##########################################################
    # >>>>>生成页码与搜索
    data_dict = {}
    search_data = request.GET.get('query', "")
    # title__ccontains 表示使用title作为搜索字段进行内容匹配
    if search_data:
        data_dict["title__contains"] = search_data 
    
    # 对搜索内容进行查询,为空表示获取所有数据
    queryset = Task.objects.filter(**data_dict).order_by('-id')

    page_object = Pagination(request, queryset, page_size=10, page_param="page")
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()
    page_string = page_object.page_string

    ##########################################################
    context = {
        "queryset": page_queryset,
        "form": form,
        "page_string": page_string,
        "search_data": search_data,
    }

    return render(request, "task_list.html", context)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/da47df21097e40079660c295d4deb9a5.png)

## 内容回顾

- 安装Django

  ```python
  pip install django
  ```

- 创建Django项目

  ```python
  >>>django-admin startproject mysite
  ```

  注意：Pycharm可以创建。如果用pycharm创建，记得 settings.py 中的 DIR templates 删除。

- 创建app & 注册

  ```python
  >>>python manage.py startapp app01
  >>>python manage.py startapp app02
  >>>python manage.py startapp app03
  ```

  ```python
  INSTALLED_APPS = [
  	···
      'APP01.apps.App01Config',
      'app02.apps.App02Config',
  ]
  ```

  注意：否则 app 下的models.py 写类时，无法在数据库中创建表。

- 配置 静态文件路径 & 模板的路径 ( 放在 app 目录下 )

- 配置数据库相关操作 ( MYSQL )

  - 第三方模块 ( django3版本 )

    ```python
    pip install mysqlclient
    ```

  - 自己先去 MySQL 创建一个数据库

  - 配置数据库连接 setting.py

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mydepartment',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    ```

  - 在 app 下的 models.py 中编写

    ```python
    from django.db import models
    
    
    class Department(models.Model):
        """部门表"""
        title = models.CharField(verbose_name="标题", max_length=32)
    
        def __str__(self):
            return self.title
    
    
    class UserInfo(models.Model):
        """员工表"""
        name = models.CharField(verbose_name="姓名", max_length=16)
        password = models.CharField(verbose_name="密码", max_length=64)
        age = models.IntegerField(verbose_name="年龄")
        account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
        # create_time = models.DateTimeField(verbose_name="入职时间",default=None)
        create_time = models.DateField(verbose_name="入职时间", default=None)
    
        # 有约束
        # 外键约束
        # Django 自动
        #   - 写的 depart
        #   - 生成数据列 depart_id on_delete = models.CASCADE 删除级联
        depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE,
                                   default=None)
        # 删除置空
        # depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.SET_NULL,null=True,blank=True)
    
        # 在 Django 中做的约束
        gender_choices = (
            (1, '男'),
            (2, '女'),
        )
    
        gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, default=None)
    ```

  - 执行两个命令：

    ```python
    >>>python manage.py makemigrations
    >>>python manage.py migrate
    ```

- 在 urls.py ，路由 ( URL 和函数的对应关系 )

- 在 views.py 视图函数 编写业务逻辑

- templates 目录，编写 HTML 模板 （含有模板语法 继承 {% static 'xx' %}）

- ModelForm & Form 组件，在我们开发增删改查的功能

  - 生成 HTML 标签 ( 生成默认值 )
  - 请求数据进行校验
  - 保存到数据库（ModelForm）
  - 获取错误信息

- Cookie 和 Session 用户登录信息保存下来

- 中间件，基于中间件实现用户认证


- ORM操作

  ```python
  models.User.objects.filter(id='XXX')
  models.User.objects.filter(id='XXX').order_by("-id")
  ```

- 分页组件



















## 项目:管理系统

> 以前的操作全部舍弃,我们从头复习操作一遍

### 新建项目

```shell
django-admin startproject myproject
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/bd61e90ed66540e8950393eaeecb51a6.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/cc9f97871a034e4ea8a40c0f543aacc6.png)

### 创建app

```shell
django-admin startapp employee_management
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/fa9d87672c8e42a6ac72d934a20fce92.png)

### 注册app

![在这里插入图片描述](https://img-blog.csdnimg.cn/6a76b0591eae4a1f910f74acc7918fe2.png)

### 连接数据库

创建数据库

```sql
create database my_project DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
1
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'my_project',
        'USER':'root',
        'PASSWORD':'Syz123!@#',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4b13a5f69ece4f5e8a46f301fac2f8b9.png)

### 设计表结构

修改`employee_management`下的`models.py`

```python
from django.db import models

## Create your models here.
class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=32, verbose_name='标题')


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(max_length=16, verbose_name="姓名")
    password = models.CharField(max_length=64, verbose_name="密码")
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    
    # 外键约束
    # to 表示与哪张表关联
    # to_field 表示表中的哪一列
    # 在django中,数据表中的名称自动加上_id,也就是depart_id
    # on_delete=models.CASCADE 表示级联删除(删除部门,部门下的所有员工都会被删除)
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE, verbose_name="部门")
    # on_delete=models.SET_NULL, null=True, blank=True 表示置空(删除部门,部门下的所有员工的部门字段置为空)
    #depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.SET_NULL, null=True, blank=True)

    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(choices=gender_choices,verbose_name="性别")
```

### 生成数据库表

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/826d4919c32042799b8062eb7f235406.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/42026154d3724c759f71c809cc2196f8.png)
查看Mysql
![在这里插入图片描述](https://img-blog.csdnimg.cn/5b86442286b943879d2d43c78d458f0e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/22185e00763940659a7b25061022807f.png)

### 静态文件管理

将以前做过的`static`目录拷贝到项目根目录一份
![在这里插入图片描述](https://img-blog.csdnimg.cn/085fdc8f1e6f43afb88716d81c78892c.png)

新建模板目录`templates`
![在这里插入图片描述](https://img-blog.csdnimg.cn/ca02deb34fa746c69bcf86ed1ac50371.png)
修改`settings.py`
![在这里插入图片描述](https://img-blog.csdnimg.cn/8142386ab41b4ff99089d3dcc5920224.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/e2d71320175a4701aab80778ee999c7a.png)

别忘了导入`os`

```python
import os
```



## 订单管理

### 表结构设计

编辑`myproject/employee_management/models.py`

```python
class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )

    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    admin = models.ForeignObject(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)
12345678910111213
```

生成数据库表

```python
python3 manage.py makemigrations
python3 manage.py migrate
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/6f9e26f7de3346f494870d9a4698c394.png)

### 订单添加

> 首先实现弹出对话框

编辑`myproject/myproject/urls.py`

```python
## 订单管理
    path('order/list/', order.order_list)
```

新建`myproject/employee_management/views/order.py`

```python
from django.shortcuts import render


def order_list(request):
    return render(request, 'order_list.html')
```

新建`myproject/employee_management/templates/order_list.html`

```html
{% extends 'layout.html' %}


{% block content %}

<div class="container">
    <div>
        <input type="button" value="新建订单1" class="btn btn-primary" data-toggle="modal" data-target="#myModal">
        <input id="btnAdd" type="button" value="新建订单2" class="btn btn-primary">
    </div>
</div>

<!-- 新建订单1 - 对话框 -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title" id="myModalLabel">Modal title</h4>
        </div>
        <div class="modal-body">
          ...
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>

{% endblock %}



{% block script %}
  <script type="text/javascript">
    $(function(){
        bindBtnAddEvent();
    })

    function bindBtnAddEvent(){
        $("#btnAdd").click(function(){
            $("#myModal").modal('show');
        });
    }
  </script>
{% endblock %}
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/b6f7be2693fa4761b72a9a080f0adb1d.png)

- 第一种方式: 官网自带方式
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/7ab3c74271a942ce882a05104b114e2c.png)
- 第二种方式: javascript实现

```javascript
{% block script %}
  <script type="text/javascript">
    $(function(){
        bindBtnAddEvent();
    })

    function bindBtnAddEvent(){
        $("#btnAdd").click(function(){
            $("#myModal").modal('show');
        });
    }
  </script>
{% endblock %}
12345678910111213
```

编辑`myproject/employee_management/templates/layout.html`

```html
<li><a href="/order/list/">订单管理</a></li>
1
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7949299ad8784ebfa89f572f15f411d6.png)
浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/e470d6ccb7e94cf8baa81477b7a2e488.png)

> 接下来编辑弹窗里的内容

编辑`myproject/employee_management/views/order.py`

```python
from employee_management.utils.modelform import BootStrapModelForm


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        # 排除 oid 订单号,让系统自动生成
        # 排除 admin 管理员, 默认使用当前登录用户为管理员 
        exclude = ["oid", "admin"]


def order_list(request):
    form = OrderModelForm()
    return render(request, 'order_list.html', {"form": form})
123456789101112131415
```

编辑`myproject/employee_management/templates/order_list.html`

```html
<form method="post" id="formSave" novalidate>
    <div>
        {% for item in form %}
        <div class="col-xs-6">
            <div class="form-group" style="position: relative; margin-top: 5px">
                <label>{{ item.label }}</label>
                {{ item }}
                <span class="error_msg" style="color: red;position: absolute;"></span>
            </div>
        </div>
        {% endfor %}
    </div>
</form>
12345678910111213
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/b7bf9af2ea874cacb1ddd9407a3187c7.png)
浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/20fb0437c3fe442ca2edd167b684411d.png)

> 接下来实现数据的提交
> 编辑`myproject/employee_management/templates/order_list.html`

```javascript
function bindBtnSaveEvent(){
  $("#btnSave").click(function(){
    // 清除错误信息
    $(".error_msg").empty();

    $.ajax({
      url: "/order/add/",
      type: "post",
      data: $("#formSave").serialize(),
      dataType: "JSON",
      success: function(res) {
        if(res.status){
          alert("创建订单成功");
        } else {
          $.each(res.error, function(name, errorlist){
            $("#id_" + name).next().text(errorlist[0]);
          })
        }
      }
    })
  });
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/1f0a8e637b8342028fcb04f6d2ccec13.png)
编辑`myproject/employee_management/views/order.py`

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def order_add(request):
    """ 新建订单 """
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse(json.dumps({"status": True}))

    return HttpResponse(json.dumps({"status": False, "error": form.errors}))
1234567891011
```

浏览器进行测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/f2b004012d484ea5b4b083d74fbacbff.png)

> 优化弹出窗口:
>
> - 自动生成订单号
> - 使用当前登录用户为订单管理员
> - 添加完成后自动关闭弹出的窗口

编辑`myproject/employee_management/templates/order_list.html`

```javascript
function bindBtnSaveEvent(){
  $("#btnSave").click(function(){
    // 清除错误信息
    $(".error_msg").empty();

    $.ajax({
      url: "/order/add/",
      type: "post",
      data: $("#formSave").serialize(),
      dataType: "JSON",
      success: function(res) {
        if(res.status){
          alert("创建订单成功");
          // 清空表单
          $("#formSave")[0].reset();
          // 关闭对话框
          $("#myModal").modal('hide');
        } else {
          $.each(res.error, function(name, errorlist){
            $("#id_" + name).next().text(errorlist[0]);
          })
        }
      }
    })
  });
}
1234567891011121314151617181920212223242526
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/0649d9d11bcf47d788f08cfde5b9c5a7.png#pic_center)
编辑`myproject/employee_management/views/order.py`

```python
from datetime import datetime
from random import randint



class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        # 排除 oid 订单号,让系统自动生成
        # 排除 admin 管理员, 默认使用当前登录用户为管理员 
        exclude = ["oid", "admin"]


@csrf_exempt
def order_add(request):
    """ 新建订单 """
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 增加 oid 订单号
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(randint(1000,9000))

        # 设置当前登录用户为订单的管理员
        admin_user = request.session["info"]["id"]
        print(admin_user)
        form.instance.admin_id = admin_user

        form.save()
        return HttpResponse(json.dumps({"status": True}))

    return HttpResponse(json.dumps({"status": False, "error": form.errors}))
12345678910111213141516171819202122232425262728293031
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/7d922372b1844a65b60b343c2492aca3.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/d3a0681ef60e4def9a9db495e70c45fb.png)
浏览器访问测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/ad4078eaac834efea3186dccb768c75b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/917a9113972a43bdb521ef37e1c33dc5.png#pic_center)

### 订单列表

> 首先实现订单列表的数据展示和分页搜索

编辑`myproject/employee_management/views/order.py`

```python
def order_list(request):
    form = OrderModelForm()

    ##########################################################
    # >>>>>生成页码与搜索
    data_dict = {}
    search_data = request.GET.get('query', "")
    # title__ccontains 表示使用title作为搜索字段进行内容匹配
    if search_data:
        data_dict["title__contains"] = search_data 
    
    # 对搜索内容进行查询,为空表示获取所有数据
    queryset = models.Order.objects.filter(**data_dict).order_by('-id')

    page_object = Pagination(request, queryset, page_size=10, page_param="page")
    page_queryset = page_object.page_queryset

    # 调用对象的html方法,生成页码
    page_object.html()
    page_string = page_object.page_string

    ##########################################################
    context = {
        "queryset": page_queryset,
        "form": form,
        "page_string": page_string,
        "search_data": search_data,
    }

    return render(request, 'order_list.html', context)
123456789101112131415161718192021222324252627282930
```

编辑`myproject/employee_management/templates/order_list.html`

```html
<div class="container">
    <div style="margin-bottom: 20px;">
        <input type="button" value="新建订单1" class="btn btn-primary" data-toggle="modal" data-target="#myModal">
        <input id="btnAdd" type="button" value="新建订单2" class="btn btn-primary">
    </div>
    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>订单列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>订单号</th>
                        <th>名称</th>
                        <th>价格</th>
                        <th>状态</th>
                        <th>管理员</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in queryset %}
                    <tr>
                        <th>{{ obj.id }}</th>
                        <th>{{ obj.oid }}</th>
                        <th>{{ obj.title }}</th>
                        <td>{{ obj.price }}</td>
                        <td>{{ obj.get_status_display }}</td>
                        <td>{{ obj.admin.username }}</td>
                        <td>
                            <a class="btn btn-primary btn-xs" href="#">编辑</a>
                            <a class="btn btn-danger btn-xs" href="#">删除</a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <ul class="pagination">
        {{ page_string }}
    </ul>
    <br>

    <form method="get">
        <div style="display:inline-block; width: 150px;">
            <div class="input-group">
                <span> <input type="text" class="form-control" placeholder="请输入页码" name="page"></span>
                <span class="input-group-btn">
                    <button class="btn btn-primary" type="submit">跳转</button>
                </span>
            </div>
        </div>
    </form>
</div>

<!-- 新建订单 - 对话框 -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true">&times;</span></button>
                <h4 class="modal-title" id="myModalLabel">新建订单</h4>
            </div>
            <div class="modal-body">
                <form method="post" id="formSave" novalidate>
                    <div>
                        {% for item in form %}
                        <div class="col-xs-6">
                            <div class="form-group" style="position: relative; margin-top: 5px">
                                <label>{{ item.label }}</label>
                                {{ item }}
                                <span class="error_msg" style="color: red;position: absolute;"></span>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </form>
            </div>
            <div class="modal-footer bottom-right" style="margin-top: 250px;">
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                <button type="button" class="btn btn-primary" id="btnSave">保存</button>
            </div>
        </div>
    </div>
</div>
```

添加新订单后,让页面自动刷新

```javascript
// 刷新页面
location.reload();
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e111425e4f9d4bdf8706ec88e6defae1.png)
浏览器刷新
![在这里插入图片描述](https://img-blog.csdnimg.cn/d1fca8da36aa4340889ab30b60333443.png)

### 订单删除

> 目标:
> 实现点击`删除`按钮后,弹出`确认删除`的[弹出框](https://so.csdn.net/so/search?q=弹出框&spm=1001.2101.3001.7020),`确认`后再进行删除

编辑`myproject/employee_management/templates/order_list.html`,实现点击`删除`按钮后,弹出`确认删除`的对话框

```html
<!-- 删除 对话框 -->
<div class="modal fade" id="myModalDelete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-body">
            <div class="alert alert-danger alert-dismissible fade in" role="alert">
                <h4>是否确定删除?</h4>
                <p>删除后所有关联的相关数据都将被删除</p>
                <p>
                    <button id="btnConfirmDelete" type="button" class="btn btn-danger">确定</button>
                    <!-- data-dismiss="modal" 表示点击取消按钮后,关闭对话框 -->
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                </p>
            </div>
        </div>
    </div>
</div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/d68b37be55504f4cacc9f26c59ae8cd0.png)

> 下面是用 js 和 ajax的方式实现数据行的删除,注意下面的id与class绑定匹配, 例如:
> `$(".btn-delete")`对应HTML中的`class="btn-delete"`位置
> `$("#btnConfirmDelete")`对应HTML中的`id="btnConfirmDelete"`位置

```javascript
{% block script %}
<script type="text/javascript">

    var DELETE_ID;

    $(function () {
        bindBtnAddEvent();
        bindBtnSaveEvent();
        bindBtnDeleteEvent();
        bindBtnConfirmDeleteEvent();
    })

    function bindBtnAddEvent() {
        $("#btnAdd").click(function () {
            $("#myModal").modal('show');
        });
    }

    function bindBtnSaveEvent() {
        $("#btnSave").click(function () {
            // 清除错误信息
            $(".error_msg").empty();

            $.ajax({
                url: "/order/add/",
                type: "post",
                data: $("#formSave").serialize(),
                dataType: "JSON",
                success: function (res) {
                    if (res.status) {
                        alert("创建订单成功");
                        // 清空表单
                        $("#formSave")[0].reset();
                        // 关闭对话框
                        $("#myModal").modal('hide');
                        // 刷新页面
                        location.reload();
                    } else {
                        $.each(res.error, function (name, errorlist) {
                            $("#id_" + name).next().text(errorlist[0]);
                        })
                    }
                }
            })
        });
    }

    function bindBtnDeleteEvent() {

        $(".btn-delete").click(function () {
            // 显示删除对话框
            $("#myModalDelete").modal('show');

            //获取当前行的ID
            DELETE_ID = $(this).attr("uid");
        });
    }

    function bindBtnConfirmDeleteEvent(){
        $("#btnConfirmDelete").click(function(){
            // 点击确认删除按钮,将全局变量中设置的那个要删除的ID发送到后台
            $.ajax({
                url: "/order/delete/",      // => /order/delete/?uid=123 
                type: "GET",
                dataType: "JSON",
                data: {
                    uid: DELETE_ID
                },
                success: function(res) {
                    if(res.status) {
                        // alert("删除成功");
                        //隐藏删除框
                        // $("#myModalDelete").modal("hide");
                        //删除列表中的那一行
                        // $("tr[uid='" + DELETE_ID + "']").remove();
                        //将要删除的DELETE_ID置空
                        // DELETE_ID = 0;

                        //刷新页面列表
                        location.reload();
                    } else {
                        alert(res.error);
                    }
                }
            })
        });
    }
</script>
{% endblock %}
```

> `location.reload();` 表示删除完成后,让页面自动刷新
> 它上面注释掉的那一段,可以实现删除后,让页面删除的那一行清除,但是会有一个问题,第二页的数据不会顶上来,也就是说当前页面有 10 行数据,我们删除一行后,只剩下 9 行数据,不会自动刷新

![在这里插入图片描述](https://img-blog.csdnimg.cn/b25f9315209c4d92a05a50c597b2f1ba.png)
编辑`myproject/myproject/urls.py`

```python
path('order/delete/', order.order_delete),
```

编辑`myproject/employee_management/views/order.py`

```python
def order_delete(request):
    """ 删除订单 """
    uid = request.GET.get('uid')
	# 判断获取到的 id 数据行是否存在
    if models.Order.objects.filter(id=uid).exists():
        models.Order.objects.filter(id=uid).delete()
        return HttpResponse(json.dumps({"status": True}))
    else:
        return HttpResponse(json.dumps({"status": False, "error": "删除失败, 数据不存在,请刷新页面后重试!"}))
```

浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/64108d73644e49efb780cb360632bb8d.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/3148c41ba7664294afea740faf3d0a1f.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/b08c8f712aa5407f9381a241c16007de.png)

### 订单编辑

> 这个逻辑稍微复杂一些,慢慢理解

#### 获取数据库数据

```python
## 对象，当前行的    # 对象 当前行的所有数据
    row_object = models.Order.objects.filter(id=uid).first()
    row_object.id
    row_object.title
    
    # 字典 {"id":1."title":"xx"}
    row_dict = models.Order.objects.filter(id=uid).values("id","title").first()
    
    # queryset = [obj,obj,obj]
    queryset = models.Order.objects.all()
    
    # queryset = [{"id":1, "title":"xx"},obj,obj]
    queryset = models.Order.objects.all().values("id","title")
    
    # queryset = [(1,"xx"),(2,"xxx"),obj]
    queryset = models.Order.objects.all().values_list("id","title")
```



编辑`myproject/employee_management/templates/order_list.html`

```html
{% extends 'layout.html' %}


{% block content %}

<div class="container">
    <div style="margin-bottom: 20px;">
        <input type="button" value="新建订单1" class="btn btn-primary" data-toggle="modal" data-target="#myModal">
        <input id="btnAdd" type="button" value="新建订单2" class="btn btn-primary">
    </div>
    <div>
        <div class="panel panel-default">
            <!-- Default panel contents -->
            <div class="panel-heading">
                <span class="glyphicon glyphicon-th-list" aria-hidden="true" style="margin-right: 5px;"></span>
                <span>订单列表</span>
            </div>

            <!-- Table -->
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>订单号</th>
                        <th>名称</th>
                        <th>价格</th>
                        <th>状态</th>
                        <th>管理员</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    {% for obj in queryset %}
                    <tr uid="{{ obj.id }}">
                        <th>{{ obj.id }}</th>
                        <th>{{ obj.oid }}</th>
                        <th>{{ obj.title }}</th>
                        <td>{{ obj.price }}</td>
                        <td>{{ obj.get_status_display }}</td>
                        <td>{{ obj.admin.username }}</td>
                        <td>
                            <input uid="{{ obj.id }}" class="btn btn-primary btn-xs btn-edit" type="button" value="编辑">
                            <input uid="{{ obj.id }}" class="btn btn-danger btn-xs btn-delete" type="button" value="删除"
                                data-dismiss="alert" aria-label="Close">
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <ul class="pagination">
        {{ page_string }}
    </ul>
    <br>

    <form method="get">
        <div style="display:inline-block; width: 150px;">
            <div class="input-group">
                <span> <input type="text" class="form-control" placeholder="请输入页码" name="page"></span>
                <span class="input-group-btn">
                    <button class="btn btn-primary" type="submit">跳转</button>
                </span>
            </div>
        </div>
    </form>
</div>

<!-- 新建/编辑 订单 对话框 -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title" id="myModalLabel">新建订单</h4>
            </div>
            <div class="modal-body">
                <form method="post" id="formSave" novalidate>
                    <div>
                        {% for item in form %}
                        <div class="col-xs-6">
                            <div class="form-group" style="position: relative; margin-top: 5px">
                                <label>{{ item.label }}</label>
                                {{ item }}
                                <span class="error_msg" id="error_msg" style="color: red;position: absolute;"></span>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </form>
            </div>
            <div class="modal-footer bottom-right" style="margin-top: 150px;">
                <button type="button" class="btn btn-default" data-dismiss="modal" id="btn-cancel">取消</button>
                <button type="button" class="btn btn-primary" id="btnSave">保存</button>
            </div>
        </div>
    </div>

</div>

<!-- 删除 对话框 -->
<div class="modal fade" id="myModalDelete" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <div class="modal-body">
            <div class="alert alert-danger alert-dismissible fade in" role="alert">
                <h4>是否确定删除?</h4>
                <p>删除后所有关联的相关数据都将被删除</p>
                <p>
                    <button id="btnConfirmDelete" type="button" class="btn btn-danger">确定</button>
                    <!-- data-dismiss="modal" 表示点击取消按钮后,关闭对话框 -->
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                </p>
            </div>
        </div>
    </div>
</div>

{% endblock %}



{% block script %}
<script type="text/javascript">

    var DELETE_ID;
    var EDIT_ID;

    $(function () {
        bindBtnAddEvent();
        bindBtnSaveEvent();
        bindBtnDeleteEvent();
        bindBtnConfirmDeleteEvent();
        bindBtnEditEvent();
    })

    function bindBtnAddEvent() {
        $("#btnAdd").click(function () {
            // 将正在编辑的 ID 设置为空
            EDIT_ID = undefined;
            // 添加前先将对话框内容清空
            $("#formSave")[0].reset();
            // 修改标题
            $("#myModalLabel").text('新建');
            // 显示对话框
            $("#myModal").modal('show');
        });
    }

    function bindBtnSaveEvent() {
        $("#btnSave").click(function () {
            // 清除错误信息
            $(".error_msg").empty();

            if (EDIT_ID) {
                // 编辑
                doEdit();
            } else {
                // 添加
                doAdd();
            }
        });
    }

    function doAdd() {

        $.ajax({
            url: "/order/add/",
            type: "post",
            data: $("#formSave").serialize(),
            dataType: "JSON",
            success: function (res) {
                if (res.status) {
                    alert("创建订单成功");
                    // 清空表单
                    $("#formSave")[0].reset();
                    // 关闭对话框
                    $("#myModal").modal('hide');
                    // 刷新页面
                    location.reload();
                } else {
                    $.each(res.error, function (name, errorlist) {
                        $("#id_" + name).next().text(errorlist[0]);
                    })
                }
            }
        })
    }

    function doEdit() {

        $.ajax({
            url: "/order/edit/?uid=" + EDIT_ID,
            type: "post",
            data: $("#formSave").serialize(),
            dataType: "JSON",
            success: function (res) {
                if (res.status) {
                    // 清空表单
                    $("#formSave")[0].reset();
                    // 关闭对话框
                    $("#myModal").modal('hide');
                    // 刷新页面
                    location.reload();
                } else {
                    if (res.tips) {
                        alert(res.tips)
                    } else {
                        $.each(res.error, function (name, errorlist) {
                            $("#id_" + name).next().text(errorlist[0]);
                        })
                    }
                }
            }
        })
    }

    function bindBtnDeleteEvent() {

        $(".btn-delete").click(function () {
            // 显示删除对话框
            $("#myModalDelete").modal('show');

            //获取当前行的ID
            DELETE_ID = $(this).attr("uid");
        });
    }

    function bindBtnConfirmDeleteEvent() {
        $("#btnConfirmDelete").click(function () {
            // 点击确认删除按钮,将全局变量中设置的那个要删除的ID发送到后台
            $.ajax({
                url: "/order/delete/",      // => /order/delete/?uid=123 
                type: "GET",
                dataType: "JSON",
                data: {
                    uid: DELETE_ID
                },
                success: function (res) {
                    if (res.status) {
                        // alert("删除成功");
                        //隐藏删除框
                        // $("#myModalDelete").modal("hide");
                        //删除列表中的那一行
                        // $("tr[uid='" + DELETE_ID + "']").remove();
                        //将要删除的DELETE_ID置空
                        // DELETE_ID = 0;

                        //刷新页面列表
                        location.reload();
                    } else {
                        alert(res.error);
                    }
                }
            })
        });
    }

    function bindBtnEditEvent() {
        $(".btn-edit").click(function () {
			// 清除错误信息
            $(".error_msg").empty();
            var uid = $(this).attr("uid");
            EDIT_ID = uid;

            // 发送 Ajax 去后台获取当前行的相关数据
            $.ajax({
                url: "/order/detail/",
                type: "GET",
                data: {
                    uid: uid
                },
                dataType: "JSON",
                success: function (res) {
                    if (res.status) {
                        // 添加前先将对话框内容清空
                        $("#formSave")[0].reset();
                        // 展示当前行的数据
                        $.each(res.data, function (name, value) {
                            $("#id_" + name).val(value);
                        });
                        // 更改标题
                        $("#myModalLabel").text('编辑');
                        // 显示对话框
                        $("#myModal").modal('show');
                    } else {
                        alert(res.error);
                    }
                }
            });
        })
    }
</script>
{% endblock %}
```

在上面的代码中,进行了如下方面的操作:

- 编辑和新建订单共用一个对话框,使用`doEdit`和`doAdd`进行区分
- 编辑页面中自动填充已有数据
- 编辑的js代码分为`bindBtnEditEvent()`与`doEdit()`
- 编辑对话框中保存时,需要考虑到当前的数据行是否存在

编辑`myproject/employee_management/views/order.py`

```python
def order_detail(request):
    """ 根据id获取订单详情 """
    uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).values("title", "price", "status").first()
    if not row_object:
        return HttpResponse(json.dumps({"status": False, "error": "数据不存在!"}))

    # 从数据库中获取到一个对象 row_object
    result = {
        "status": True,
        "data": row_object,
    }

    return HttpResponse(json.dumps(result))


@csrf_exempt
def order_edit(request):
    """ 编辑订单 """
    uid = request.GET.get('uid')
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return HttpResponse(json.dumps({"status": False, "tips": "数据不存在!"}))

    # 获取编辑界面提交的数据
    data = request.POST
    # 判断编辑的内容是否跟以前一样
    if data["title"] != '' and data['price'] != '' and data['status'] != '':
        flag = 0
        if  row_object.title == data["title"]:
            flag += 1
        if  row_object.price == int(data["price"]):
            flag += 1
        if  row_object.status == int(data["status"]):
            flag += 1
        # 如果输入的内容与原有内容相同,则进行提示
        if flag == 3:
            return HttpResponse(json.dumps({"status": False, "tips": "您没有变更任何内容,无需修改!"}))

    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return HttpResponse(json.dumps({"status": True}))

    return HttpResponse(json.dumps({"status": False, "error": form.errors}))
```

编辑`myproject/myproject/urls.py`

```python
path('order/detail/', order.order_detail),
path('order/edit/', order.order_edit),
```

浏览器进行测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/4f620b45cf84495dbd85d09df77872a5.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/421ff1e0112a47cab7383e91e81a44ea.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/9fb87dc43aff41bb9ccb8bfa055f04cd.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/b714db5c3e334694a18ef68d5d6f4c4f.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/55bb5f958ebc4991844cdeb8858d5a0c.png)

- echarts 国内

获取方式: https://registry.npmjs.org/echarts/-/echarts-5.4.1.tgz
下载完成后
![在这里插入图片描述](https://img-blog.csdnimg.cn/6a2924216ed94470b56d29a960f9f50c.png)
将此文件放到项目静态文件目录下
![在这里插入图片描述](https://img-blog.csdnimg.cn/bbaae0935c2b44628f8ddaf7eaa081c4.png)
接下来,上手做

### [柱状图](https://so.csdn.net/so/search?q=柱状图&spm=1001.2101.3001.7020)

编辑`myproject/employee_management/templates/layout.html`

```html
<li><a href="/chart/list/">数据统计</a></li>
```

编辑`myproject/myproject/urls.py`

```python
from employee_management.views import depart,user,pretty,admin, account, task, order, chart

## 数据统计
    path('chart/list/', chart.chart_list),
```

新建`myproject/employee_management/views/chart.py`

```python
from django.shortcuts import render, HttpResponse


def chart_list(request):
    """ 数据统计 """
    return render(request, 'chart_list.html')
123456
```

新建`myproject/employee_management/templates/chart_list.html`

```html
{% extends 'layout.html'%}

{% block css %}

{% endblock %}


{% block content %}
<div class="container">
    <h1>数据统计</h1>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">折线图</h3>
        </div>
        <div class="panel-body">
            
        </div>
    </div>
    <div class="row">
        <div class="col-sm-8">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">柱状图</h3>
                </div>
                <div class="panel-body">
                    <div id="m2" style="width: 600px;height:400px;"></div>
                </div>
            </div>
        </div>
        <div class="col-sm-4">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">饼图</h3>
                </div>
                <div class="panel-body">
                    Panel content
                </div>
            </div>
        </div>

    </div>
</div>
{% endblock %}

{% block script %}
<script src="/static/js/echarts.min.js"></script>
<script type="text/javascript">
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('m2'));

    // 指定图表的配置项和数据
    var option = {
        title: {
            text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
            data: ['销量', '价格']
        },
        xAxis: {
            data: ['1月', '2月', '3月', '4月', '5月', '6月']
        },
        yAxis: {},
        series: [
            {
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            },
            {
                name: '价格',
                type: 'bar',
                data: [25, 40, 80, 65, 70, 50]
            }
        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
</script>
{% endblock %}
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/693b5c1118984f06b8e222272d24cb65.png)

> 调整一下文字和标题的位置

编辑`myproject/employee_management/templates/chart_list.html`

```javascript
textAlign: "auto",
   left: "center",
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/26d6e571ca6b48bcaab45628f0f2f96b.png)

```javascript
legend: {
    data: ['销量', '价格'],
    bottom: 0,
},
1234
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/6e93905ae0fd435b81e5ccb842ca36dd.png#pic_center)

> 模拟从后台获取数据

编辑`myproject/myproject/urls.py`

```python
path('chart/bar/', chart.chart_bar),
```

编辑`myproject/employee_management/views/chart.py`,新增`chart_bar`函数

```python
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


def chart_list(request):
    """ 数据统计 """
    return render(request, 'chart_list.html')


def chart_bar(request):
    """ 构造柱状图的数据 """

    # 数据可以去数据库中获取
    legend = ['销量', '价格']
    xAxis = ['1月', '2月', '3月', '4月', '5月', '6月']
    series_list = [
                {
                    "name": '销量',
                    "type": 'bar',
                    "data": [5, 20, 36, 10, 10, 20]
                },
                {
                    "name": '价格',
                    "type": 'bar',
                    "data": [25, 40, 80, 65, 70, 50]
                }
            ]

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "xAxis": xAxis,
            "series_list": series_list,
        }
    }

    return JsonResponse(result)
```

编辑`myproject/employee_management/templates/chart_list.html`

```javascript
<script type="text/javascript">

    $(function () {
        initBar();
    })

    function initBar() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('m2'));

        // 指定图表的配置项和数据
        var option = {
            title: {
                text: '员工业绩年度汇总信息',
                subtext: "xxx公司",
                textAlign: "auto",
                left: "center",
            },
            tooltip: {},
            legend: {
                data: [],   // 后台获取
                bottom: 0,
            },
            xAxis: {
                data: []    // 后台获取
            },
            yAxis: {},
            series: []      // 后台获取
        };

        $.ajax({
            url: "/chart/bar/",
            type: "get",
            dataType: "JSON",
            success: function(res){
                if(res.status){
                    // 将获取到的数据更新到 option 中
                    option.legend.data = res.data.legend;
                    option.xAxis.data = res.data.xAxis;
                    option.series = res.data.series_list;

                    // 使用刚指定的配置项和数据显示图表。
                    myChart.setOption(option);
                }
            }
        })
    }
</script>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/4a2cbbe2b88b4560baf94fe6f31de00c.png)

### [饼图](https://so.csdn.net/so/search?q=饼图&spm=1001.2101.3001.7020)

> 经过上面柱状图的测试,饼图就非常简单了

打开网址: https://echarts.apache.org/examples/zh/index.html#chart-type-pie
![在这里插入图片描述](https://img-blog.csdnimg.cn/35ff0ab73d2748389f358a5b29e69746.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/bb190f53a01a4a8690ee4514d6afebe8.png)
编辑`myproject/employee_management/templates/chart_list.html`,在复制代码的基础上进行修改

```javascript
<script type="text/javascript">

    $(function () {
        initBar();
        iniPie();
    })
	
	// 柱状图
    function initBar() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('m2'));

        // 指定图表的配置项和数据
        var option = {
            title: {
                text: '员工业绩年度汇总信息',
                subtext: "xxx公司",
                textAlign: "auto",
                left: "center",
            },
            tooltip: {},
            legend: {
                data: [],   // 后台获取
                bottom: 0,
            },
            xAxis: {
                data: []    // 后台获取
            },
            yAxis: {},
            series: []      // 后台获取
        };

        $.ajax({
            url: "/chart/bar/",
            type: "get",
            dataType: "JSON",
            success: function (res) {
                if (res.status) {
                    // 将获取到的数据更新到 option 中
                    option.legend.data = res.data.legend;
                    option.xAxis.data = res.data.xAxis;
                    option.series = res.data.series_list;

                    // 使用刚指定的配置项和数据显示图表。
                    myChart.setOption(option);
                }
            }
        })

    }

	// 饼图
    function iniPie() {
        var chartDom = document.getElementById('m3');
        var myChart = echarts.init(chartDom);
        var option;

        option = {
            title: {
                text: '部门预算占比',
                subtext: 'xxx公司',
                left: 'center'
            },
            tooltip: {
                trigger: 'item'
            },
            legend: {
                orient: 'vertical',
                bottom: 0,
            },
            series: [
                {
                    name: 'Access From',
                    type: 'pie',
                    radius: '50%',
                    data: [
                        { value: 1048, name: '销售部' },
                        { value: 735, name: '运营部' },
                        { value: 580, name: '财务部' },
                    ],
                    emphasis: {
                        itemStyle: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        };
        option && myChart.setOption(option);
    }
</script>
```

浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/eb4c75d4338f4988a19a5848a107996d.png)

> 接下来实现模拟获取后台数据,依然是上面的套路

编辑`myproject/myproject/urls.py`

```python
path('chart/pie/', chart.chart_pie),
```

编辑`myproject/employee_management/views/chart.py`

```python
def chart_pie(request):
    """ 构造饼图的数据 """
    data_list = [
                    { "value": 1048, "name": '销售部' },
                    { "value": 735, "name": '运营部' },
                    { "value": 580, "name": '财务部' },
                ]

    result = {
        "status": True,
        "data_list": data_list,
    }

    return JsonResponse(result)
```

编辑`myproject/employee_management/templates/chart_list.html`

```html
<div id="m3" style="width: 300px; height:400px;"></div>
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/281983623c5e4024a65b04149e66c533.png)

```javascript
function iniPie() {
    var chartDom = document.getElementById('m3');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        title: {
            text: '部门预算占比',
            subtext: 'xxx公司',
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            bottom: 0,
        },
        series: [
            {
                name: 'Access From',
                type: 'pie',
                radius: '50%',
                data: [],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    $.ajax({
        url: "/chart/pie/",
        type: "get",
        dataType: "JSON",
        success: function(res) {
            if(res.status){
                option.series[0].data = res.data_list;
                option && myChart.setOption(option);
            }
        }
    })
}
```

> **特别说明:**
>
> - 老版本的 echart 不会对 option 变量在局部声明,而是直接声明为全局变量,我是用的 echart 版本为5.4,已经提前帮我声明好了(不加 var 表示全局变量)

![在这里插入图片描述](https://img-blog.csdnimg.cn/30edd305368a4f60a40d59c9db1fdc69.png)
浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/782ec64e4ca9401ba53674dfec1c3c62.png)

### 折线图

编辑`myproject/employee_management/templates/chart_list.html`

```html
<div id="m1" style="width: 100%; height:300px;"></div>
1
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/520e0a797273436d996200006e4b71ab.png)
增加`initLine`函数

```javascript
$(function () {
    initBar();
    iniPie();
    initLine();
})

function initLine() {
    var chartDom = document.getElementById('m1');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        title: {
            text: '分公司业绩图',
            left: "center",
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['天津分公司', '北京分公司'],
            bottom: 0,
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '12%',
            containLabel: true
        },
        toolbox: {
            feature: {
                // saveAsImage: {}
                saveAsImage: false,
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: '天津分公司',
                type: 'line',
                stack: 'Total',
                data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
                name: '北京分公司',
                type: 'line',
                stack: 'Total',
                data: [220, 182, 191, 234, 290, 330, 310]
            },
        ]
    };

    option && myChart.setOption(option);
}
```

浏览器访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/0017c41f4e744eb4b3f55f0e5f8b5f7e.png)

> 实现获取后台数据

编辑`myproject/employee_management/templates/chart_list.html`

```javascript
function initLine() {
    var chartDom = document.getElementById('m1');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
        title: {
            text: '分公司业绩图',
            left: "center",
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: [],
            bottom: 0,
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '12%',
            containLabel: true
        },
        toolbox: {
            feature: {
                // saveAsImage: {}
                saveAsImage: false,
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: []
    };

    $.ajax({
        url: "/chart/line/",
        type: "get",
        dataType: "JSON",
        success: function(res) {
            if(res.status){
                option.legend.data = res.data.legend_list;
                option.xAxis.data = res.data.xAxis_list;
                option.series = res.data.series_list;

                option && myChart.setOption(option);
            }
        }
    })
}

```

编辑`myproject/myproject/urls.py`

```python
path('chart/line/', chart.chart_line),
```

编辑`myproject/employee_management/views/chart.py`

```python
def chart_line(request):
    """ 构造折线图的数据 """
    legend_list = ['天津分公司', '北京分公司']
    xAxis_list = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
    series_list = [
                {
                    "name": '天津分公司',
                    "type": 'line',
                    "stack": 'Total',
                    "data": [120, 132, 101, 134, 90, 230, 210]
                },
                {
                    "name": '北京分公司',
                    "type": 'line',
                    "stack": 'Total',
                    "data": [220, 182, 191, 234, 290, 330, 310]
                },
            ]

    result = {
        "status": True,
        "data": {
            "legend_list": legend_list,
            "xAxis_list": xAxis_list,
            "series_list": series_list,
        }
    }
    return JsonResponse(result)
```

浏览器测试
![在这里插入图片描述](https://img-blog.csdnimg.cn/3ea87981d82145188141b725e23d1fa3.png)



### 文件的上传



#### 基本操作

```html
    <div class="container">
        <form method="post" enctype="multipart/form-data">
            <input type="text" name="username"/>
            <input type="file" name="avatar"/>
            <input type="submit" value="提 交"/>
        </form>
    </div>
```

![image-20230924194358499](https://imgtroage-1317162111.cos.ap-nanjing.myqcloud.com/img/image-20230924194358499.png)

> ​	支持文件上传内容

```python
##{'username': ['xxx']}
print(request.POST) # 请求体中的数据
##  {'avatar': [ < TemporaryUploadedFile: wallhaven - rr7xjq.jpg(image / jpeg) >]}
print(request.FILES) # 请求发过来的文件
```

代码：

```python
def upload_list(request):
    if request.method == 'GET':
        return render(request, "upload_list.html")
    print(request.POST)  # 请求体中的数据
    #  {'avatar': [ < TemporaryUploadedFile: wallhaven - rr7xjq.jpg(image / jpeg) >]}
    print(request.FILES)  # 请求发过来的文件

    file_object = request.FILES.get("avatar")
    print(file_object.name)  # 文件名：wallhaven-rr7xjq.jpg
    
    # 上传文件保存到本地
    f = open(file_object.name, mode="wb")
    # 读取图片一块块的内容
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse("...")
```

























