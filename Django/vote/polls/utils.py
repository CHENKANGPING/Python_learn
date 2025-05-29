import hashlib
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.contrib.auth.hashers import make_password

def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()

def gen_random_code(length=4):
    """生成指定长度的随机验证码"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

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
    """验证码生成器"""
    _instance = None
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.width = 100
        self.height = 40
        self.font_size = 30
        self.font_path = 'arial.ttf'  # 请确保字体文件存在
    
    def generate(self, code):
        """生成验证码图片"""
        # 创建图片
        image = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # 添加干扰线
        for i in range(5):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0))
        
        # 添加干扰点
        for i in range(30):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            draw.point([x, y], fill=(0, 0, 0))
        
        # 添加验证码文字
        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
        except IOError:
            font = ImageFont.load_default()
        
        for i, char in enumerate(code):
            x = 10 + i * 20
            y = random.randint(5, 10)
            draw.text((x, y), char, font=font, fill=(0, 0, 0))
        
        # 保存图片到内存
        buffer = BytesIO()
        image.save(buffer, 'PNG')
        return buffer.getvalue()

def hash_password(password):
    """对密码进行加密"""
    return make_password(password)

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