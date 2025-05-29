from django.core.management.base import ALL_CHECKS

## Cookie和Session

### 用户登录的准备工作

1.创建用户模型，通过Django的ORM实现从二维表到模型的转换，这次我们尝试把模型
转换为二维表。

```python
class User(models.Model):
    """用户"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    tel = models.CharField(max_length=20, verbose_name='手机号')
    reg_data  = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    last_visit = models.DateTimeField(null=True, verbose_name='最后登录时间')
    
    class Meta:
        db_table = 'tb_user'
        verbose_name='用户'
        verbose_name_plural = '用户'
```

2.使用下面的命令生成迁移文件并执行，将`User`模型直接变成
关系型数据库中的二维表`tb_user`。

```shell
python manage.py makemigrations polls
python manage.py migrate polls
```

3.用下面的SQL语句直接插入两条测试数据。

```sql
insert into `tb_user`
        ('username', 'password', 'tel', 'reg_data')
values 
    ('HiiAen', '7BBC968271BFEA11D9F012B769572F21', '11111111111', now())
    ('miku', 'AA58E777C749B232DCBC911C2486BB04', '18693298737', now())
```

4.我们在应用下增加一个名为`utils.py`模块用来保存需要使用的工具函数，
使用`hashlib`中的`md5`类将字符串处理称MD5摘要的函数。

```python
import hashlib

def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()
```

5.编写用户登录的视图函数和模板页。

添加渲染登录页面的视图函数：

```python
def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    return render(request, 'login.html', {'hint': hint})
```

增加`login.html`模板页

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>用户登录</title>
    <style>
        #container {
            width: 520px;
            margin: 10px auto;
        }
        .input {
            margin: 20px 0;
            width: 460px;
            height: 40px;
        }
        .input>label {
            display: inline-block;
            width: 140px;
            text-align: right;
        }
        .input>img {
            width: 150px;
            vertical-align: middle;
        }
        input[name=captcha] {
            vertical-align: middle;
        }
        form+div {
            margin-top: 20px;
        }
        form+div>a {
            text-decoration: none;
            color: darkcyan;
            font-size: 1.2em;
        }
        .button {
            width: 500px;
            text-align: center;
            margin-top: 20px;
        }
        .hint {
            color: red;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div id="container">
        <h1>用户登录</h1>
        <hr>
        <p class="hint">{{ hint }}</p>
        <form action="/login/" method="post">
            {% csrf_token %}
            <fieldset>
                <legend>用户信息</legend>
                <div class="input">
                    <label>用户名：</label>
                    <input type="text" name="username">
                </div>
                <div class="input">
                    <label>密码：</label>
                    <input type="password" name="password">
                </div>
                <div class="input">
                    <label>验证码：</label>
                    <input type="text" name="captcha">
                    <img id="code" src="/captcha/" alt="" width="150" height="40">
                </div>
            </fieldset>
            <div class="button">
                <input type="submit" value="登录">
                <input type="reset" value="重置">
            </div>
        </form>
        <div>
            <a href="/">返回首页</a>
            <a href="/register/">注册新用户</a>
        </div>
    </div>
</body>
</html>
```
注意，在上面的表单中，
我们使用了模板指令{% csrf_token %}为表单添加一个隐藏域（大家可以在浏览器中显示网页源代码就可以看到这个指令生成的type属性为hidden的input标签），
它的作用是在表单中生成一个随机令牌（token）来防范跨站请求伪造（简称为CSRF），
这也是Django在提交表单时的硬性要求。如果我们的表单中没有这样的令牌，那么提交表单时，Django框架会产生一个响应状态码为403的响应（禁止访问），
除非我们设置了免除CSRF令牌。

### 实现用户跟踪

要实现用户跟踪，
服务器端可以为每个用户会话创建一个session对象并将session对象的ID写入到浏览器的cookie中；用户下次请求服务器时，浏览器会在HTTP请求头中携带该网站保存的cookie信息，
这样服务器就可以从cookie中找到session对象的ID并根据此ID获取到之前创建的session对象；由于session对象可以用键值对的方式保存用户数据，
这样之前保存在session对象中的信息可以悉数取出，服务器也可以根据这些信息判定用户身份和了解用户偏好，为用户提供更好的个性化服务。


### Django框架对session的支持

在创建Django项目时，默认的配置文件`settings.py`文件中已经激活了一个名为`SessionMiddleware`的中间件（关于中间件的知识我们在后面的章节做详细讲解，这里只需要知道它的存在即可），因为这个中间件的存在，我们可以直接通过请求对象的`session`属性来操作会话对象。前面我们说过，`session`属性是一个像字典一样可以读写数据的容器对象，因此我们可以使用“键值对”的方式来保留用户数据。与此同时，`SessionMiddleware`中间件还封装了对cookie的操作，在cookie中保存了sessionid，这一点我们在上面已经提到过了。

在默认情况下，Django将session的数据序列化后保存在关系型数据库中，在Django 1.6以后的版本中，默认的序列化数据的方式是JSON序列化，而在此之前一直使用Pickle序列化。JSON序列化和Pickle序列化的差别在于前者将对象序列化为字符串（字符形式），而后者将对象序列化为字节串（二进制形式），因为安全方面的原因，JSON序列化成为了目前Django框架默认序列化数据的方式，这就要求在我们保存在session中的数据必须是能够JSON序列化的，否则就会引发异常。还有一点需要说明的是，使用关系型数据库保存session中的数据在大多数时候并不是最好的选择，因为数据库可能会承受巨大的压力而成为系统性能的瓶颈，在后面的章节中我们会告诉大家如何将session保存到缓存服务中以提升系统的性能。

### 实现用户登录验证

首先，在`polls/utils.py`中编写生成随机验证码的函数`gen_random_code`。

```python
import random

ALL_CHECKS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gen_random_code(length = 4):
    return ''.join(random.choices(ALL_CHECKS, k = length))
```

编写生成验证码图片的类`Captcha`

```python
"""
图片验证码
"""
import os
import random
from io import BytesIO

from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype


class Bezier:
    """贝塞尔曲线"""

    def __init__(self):
        self.tsequence = tuple([t / 20.0 for t in range(21)])
        self.beziers = {}

    def make_bezier(self, n):
        """绘制贝塞尔曲线"""
        try:
            return self.beziers[n]
        except KeyError:
            combinations = pascal_row(n - 1)
            result = []
            for t in self.tsequence:
                tpowers = (t ** i for i in range(n))
                upowers = ((1 - t) ** i for i in range(n - 1, -1, -1))
                coefs = [c * a * b for c, a, b in zip(combinations,
                                                      tpowers, upowers)]
                result.append(coefs)
            self.beziers[n] = result
            return result


class Captcha:
    """验证码"""

    def __init__(self, width, height, fonts=None, color=None):
        self._image = None
        self._fonts = fonts if fonts else \
            [os.path.join(os.path.dirname(__file__), 'fonts', font)
             for font in ['Arial.ttf', 'Georgia.ttf', 'Action.ttf']]
        self._color = color if color else random_color(0, 200, random.randint(220, 255))
        self._width, self._height = width, height

    @classmethod    
    def instance(cls, width=200, height=75):
        """用于获取Captcha对象的类方法"""
        prop_name = f'_instance_{width}_{height}'
        if not hasattr(cls, prop_name):
            setattr(cls, prop_name, cls(width, height))
        return getattr(cls, prop_name)

    def _background(self):
        """绘制背景"""
        Draw(self._image).rectangle([(0, 0), self._image.size],
                                    fill=random_color(230, 255))

    def _smooth(self):
        """平滑图像"""
        return self._image.filter(ImageFilter.SMOOTH)

    def _curve(self, width=4, number=6, color=None):
        """绘制曲线"""
        dx, height = self._image.size
        dx /= number
        path = [(dx * i, random.randint(0, height))
                for i in range(1, number)]
        bcoefs = Bezier().make_bezier(number - 1)
        points = []
        for coefs in bcoefs:
            points.append(tuple(sum([coef * p for coef, p in zip(coefs, ps)])
                                for ps in zip(*path)))
        Draw(self._image).line(points, fill=color if color else self._color, width=width)

    def _noise(self, number=50, level=2, color=None):
        """绘制扰码"""
        width, height = self._image.size
        dx, dy = width / 10, height / 10
        width, height = width - dx, height - dy
        draw = Draw(self._image)
        for i in range(number):
            x = int(random.uniform(dx, width))
            y = int(random.uniform(dy, height))
            draw.line(((x, y), (x + level, y)),
                      fill=color if color else self._color, width=level)

    def _text(self, captcha_text, fonts, font_sizes=None, drawings=None, squeeze_factor=0.75, color=None):
        """绘制文本"""
        color = color if color else self._color
        fonts = tuple([truetype(name, size)
                       for name in fonts
                       for size in font_sizes or (65, 70, 75)])
        draw = Draw(self._image)
        char_images = []
        for c in captcha_text:
            font = random.choice(fonts)
            c_width, c_height = draw.textsize(c, font=font)
            char_image = Image.new('RGB', (c_width, c_height), (0, 0, 0))
            char_draw = Draw(char_image)
            char_draw.text((0, 0), c, font=font, fill=color)
            char_image = char_image.crop(char_image.getbbox())
            for drawing in drawings:
                d = getattr(self, drawing)
                char_image = d(char_image)
            char_images.append(char_image)
        width, height = self._image.size
        offset = int((width - sum(int(i.size[0] * squeeze_factor)
                                  for i in char_images[:-1]) -
                      char_images[-1].size[0]) / 2)
        for char_image in char_images:
            c_width, c_height = char_image.size
            mask = char_image.convert('L').point(lambda i: i * 1.97)
            self._image.paste(char_image,
                              (offset, int((height - c_height) / 2)),
                              mask)
            offset += int(c_width * squeeze_factor)

    @staticmethod
    def _warp(image, dx_factor=0.3, dy_factor=0.3):
        """图像扭曲"""
        width, height = image.size
        dx = width * dx_factor
        dy = height * dy_factor
        x1 = int(random.uniform(-dx, dx))
        y1 = int(random.uniform(-dy, dy))
        x2 = int(random.uniform(-dx, dx))
        y2 = int(random.uniform(-dy, dy))
        warp_image = Image.new(
            'RGB',
            (width + abs(x1) + abs(x2), height + abs(y1) + abs(y2)))
        warp_image.paste(image, (abs(x1), abs(y1)))
        width2, height2 = warp_image.size
        return warp_image.transform(
            (width, height),
            Image.QUAD,
            (x1, y1, -x1, height2 - y2, width2 + x2, height2 + y2, width2 - x2, -y1))

    @staticmethod
    def _offset(image, dx_factor=0.1, dy_factor=0.2):
        """图像偏移"""
        width, height = image.size
        dx = int(random.random() * width * dx_factor)
        dy = int(random.random() * height * dy_factor)
        offset_image = Image.new('RGB', (width + dx, height + dy))
        offset_image.paste(image, (dx, dy))
        return offset_image

    @staticmethod
    def _rotate(image, angle=25):
        """图像旋转"""
        return image.rotate(random.uniform(-angle, angle),
                            Image.BILINEAR, expand=1)

    def generate(self, captcha_text='', fmt='PNG'):
        """生成验证码(文字和图片)
        :param captcha_text: 验证码文字
        :param fmt: 生成的验证码图片格式
        :return: 验证码图片的二进制数据
        """
        self._image = Image.new('RGB', (self._width, self._height), (255, 255, 255))
        self._background()
        self._text(captcha_text, self._fonts,
                   drawings=['_warp', '_rotate', '_offset'])
        self._curve()
        self._noise()
        self._smooth()
        image_bytes = BytesIO()
        self._image.save(image_bytes, format=fmt)
        return image_bytes.getvalue()


def pascal_row(n=0):
    """生成毕达哥拉斯三角形（杨辉三角）"""
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n // 2 + 1):
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n & 1 == 0:
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result))
    return result


def random_color(start=0, end=255, opacity=255):
    """获得随机颜色"""
    red = random.randint(start, end)
    green = random.randint(start, end)
    blue = random.randint(start, end)
    if opacity is None:
        return red, green, blue
    return red, green, blue, opacity
```

完成提供验证码的视图函数。

```python
def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')
```

保存session中的验证码字符串和用户输入的验证码字符串进行对比，
如果用户输入了正确的验证码才能够执行后续的登录流程。

```python
def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {'hint': hint})
```
上面的代码中，我们设定了登录成功后会在session中保存用户的编号（userid）和用户名（username），
页面会重定向到首页。接下来我们可以稍微对首页的代码进行调整，
在页面的右上角显示出登录用户的用户名。我们将这段代码单独写成了一个名为header.html的HTML文件，
首页中可以通过在<body>标签中添加{% include 'header.html' %}来包含这个页面，代码如下所示。

```html
<div class="user">
    {% if request.session.userid %}
    <span>{{ request.session.username }}</span>
    <a href="/logout">注销</a>
    {% else %}
    <a href="/login">登录</a>&nbsp;&nbsp;
    {% endif %}
    <a href="/register">注册</a>
</div>
```
如果用户没有登录，页面会显示登录和注册的超链接；而用户登录成功后，
页面上会显示用户名和注销的链接，注销链接对应的视图函数如下所示，
URL的映射与之前讲过的类似。

```python
def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')
```
接下来，我们就可以限制只有登录用户才能为老师投票，
修改后的praise_or_criticize函数如下所示，
我们通过从request.session中获取userid来判定用户是否登录。

```python
def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise/'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 20000, 'mesg': '投票成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'mesg': '投票失败'}
    else:
        data = {'code': 20002, 'mesg': '请先登录'}
    return JsonResponse(data)
```






