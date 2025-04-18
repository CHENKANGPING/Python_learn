"""
    字符串的定义
    就是由零个或多个字符组成的有限数列
    在python中
    把单个或多个字符用单引号或双引号包围起来
    可以表示一个字符串
    中可以有特殊符号 英文字母
    中文字符 日文的平片假名
    希腊字符 Emoji等
"""
s1 = 'hello, world'
s2 = "你好，世界！ ❤"
s3 = '''hello,
wonderful
world
'''
print(s1)
print(s2)
print(s3)


print('---------------------------------------------------------------')


"""
    转义字符串
    \ 来表示转义 说明\后面的字符不再是它原来的定义
    \n 不是代表字符\和n 而是换行
    \t表示制表符
"""
s3 = '\'hello,world!\''
s4 = '\\hello, world!\\'
print(s3)
print(s4)


print('---------------------------------------------------------------')


"""
    原始字符串
    python中有一种以r或R开头的字符串
    被称为原始字符串
    意思是字符串中的每个字符都是它原来的含义
    没有所谓的转义字符
    如'hello\n' \n代表换行
    r'hello\n' \n不在表示换行
"""
s5 = '\it \is \time \to \read \now'
s6 = r'\it \is \time \to \read \now'
print(s5)
print(s6)
# s5 中的 \t是制表符(table) \n是换行符(new line) \r是回车符 相当于让输出回到了首行


print('---------------------------------------------------------------')


# 字符的特殊表示
# python 允许在 \后面可以跟一个八进制或者十六进制数来表示字符
# 另外一种是在 \u后跟Unicode字符编码

s7 = '\141\142\143\x61\x62\x63'
s8 = '\u9648\u5eb7\u5e73'
print(s7)
print(s8)


print('---------------------------------------------------------------')


# 字符串运算
# 拼接和重复
s9 = 'hello' + ',' + 'wold'
print(s9)
s10 = '!' * 3
print(s10)
s9 += s10
print(s9)
s9 *= 2
print(s9)


print('---------------------------------------------------------------')


# 比较运算
# 大小比较比较的是每个字符对应的编码大小
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '骆昊'
print(ord('骆'))            # 39558
print(ord('昊'))            # 26122
s4 = '王大锤'
print(ord('王'))            # 29579
print(ord('大'))            # 22823
print(ord('锤'))            # 38180
print(s3 >= s4)             # True
print(s3 != s4)             # True


print('---------------------------------------------------------------')


# 成员运算
# 可以用in和not in 判断一个字符串中是否包含另外一个字符或字符串
# in和not in 称为成员运算符 会产生布尔值True 或 False
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)
print('wo' not in s2)
print(s2 in s1)


print('---------------------------------------------------------------')


# 获取字符串长度
s = 'hello, world'
print(len(s))
print(len('goodbye, world'))


print('---------------------------------------------------------------')


# 切片和索引
# 字符串的索引和切片跟列表 元组 几乎没有区别
# 注：字符串是不可改变类型 所以不能通过索引运算修改字符串中的字符
s = 'abc123456'
n = len(s)
print(s[0], s[-n])
print(s[n-1], s[-1])
print(s[2], s[-7])
print(s[5], s[-4])
print(s[2:5])
print(s[-7:-4])
print(s[2:])
print(s[:2])
print(s[::2])
print(s[::-1])


print('---------------------------------------------------------------')


# 字符的遍历
# 方法一
s = 'hello'
for i in range(len(s)):
    print(s[i])
    
# 方法二
s = 'hello'
for elem in s :
    print(elem)


print('---------------------------------------------------------------')


# 大小写相关操作
s1 = 'hello, world'
# 字符串首字母大写
print(s1.capitalize())
# 字符串每个单词首字母大写
print(s1.title())
# 字符串大写
print(s1.upper())
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())
# 检查s1和s2的值
print(s1)
print(s2)


print('---------------------------------------------------------------')


# 查找操作
# 使用find 和 index
# find 和 index 可以通过方法的参数来指定查找的范围
# 注:find 方法找不到的字符串会返回-1 index方法找不到会引发错误
s = 'hello, world'
print(s.find('or'))
print(s.find('or', 9))
print(s.find('of'))
print(s.index('or'))
# print(s.index('or', 9))


print('---------------------------------------------------------------')


# 性质判断
# 通过startswich endswith 来判断字符串是否以某个字符串开头和结尾
# 还可以用 is 开头的方法判断字符串的特征
# 这些方法返回的都是布尔值
s1 = 'hello, world!'
print(s1.startswith('He'))
print(s1.startswith('hel'))
print(s1.endswith('!'))

s2 = 'qbc123456'
print(s2.isdigit())
# isdigit() 检查字符串是否只包含数字字符
print(s2.isalpha())
# isalpha() 检查字符串是否只包含字母字符（英文字母或其他语言的字母）
print(s2.isalnum())
# isalnum() 检查字符串是否只包含字母或数字字符（字母或数字的组合）


print('---------------------------------------------------------------')


# 格式化
# 可以用center ljust rjust方法做居中 左对齐 右对齐
# 如要在字符串左侧补0 可以用zfill方法
s = 'hello, world'
print(s.center(20, '*'))
print(s.rjust(20))
print(s.ljust(20, '~'))
print('33'.zfill(5))
print('-33'.zfill(5))


print('---------------------------------------------------------------')


# 剪切操作
# strip方法可以帮我们获得将原来字符串修剪掉左右两端指定字符之后的字符
# strip 方法还有lstrip 和 rstrip
s1 = '      4343242@qq.com   '
print(s1.strip())

s2 = '~你好, 世界~'
print(s2.lstrip('~'))
print(s2.rstrip('~'))


print('---------------------------------------------------------------')


# 替换操作
# 如果希望用新的内容替换字符串中指定的内容
# 可以使用replace方法
# replace方法的第一个参数是被替换的内容
# 第二个参数是替换后的内容
# 还可以通过第三个参数指定替换的次数
s = 'hello, good world'
print(s.replace('o', '@'))
print(s.replace('o', '@', 1))


print('---------------------------------------------------------------')


# 拆分和合并
# split方法将一个字符串拆分为多个字符串
# join方法将列表中的多个字符连接成一个字符串
s = 'i love you'
words = s.split()
print(words)
print('~'.join(words))


print('---------------------------------------------------------------')


# 编码和解码
a = '陈康平'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)
print(c)
print(b.decode('utf-8'))
print(c.decode('gbk'))


