# 验证输入用户名和qq号是否有效并给出对应的提示消息
"""
    用户名必须又字母 数字或下划线构成且长度在6 ~  20个字符之间
    qq号是5 ~ 12的数字且首位不能为0
    
"""
# import re
# username = input('请输入用户名：')
# qq = input('请输入qq：')

# m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
# if not  m1:
#     print('请输入有效的用户名.')
    
# m2 = re.fullmatch(r'[1-9]\d{4,11}',qq)
# if not m2:
#     print('请输入有效的qq号')
# if m1 and m2:
#     print('你输入的信息是有效的！')
    
    
print('--------------------------------------------------')


# 从一段文字中提取出国内手机号
import re
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765'''

# 方法1 查找所有匹配并保存到一个列表中
tel_list = re.findall(pattern, sentence)
for tel in tel_list:
    print(tel)
    
print('--------------------------------------------------')

# 方法2 通过迭代器去除匹配对象并获得匹配内容
for temp in pattern.finditer(sentence):
    print(temp.group())
    
print('--------------------------------------------------')

# 方法3 通过search函数指定搜索位置找出所有匹配
m = pattern.search(sentence)
while m :
    print(m.group())
    m = pattern.search(sentence, m.end())
    
    
print('--------------------------------------------------')


# 替换字符串中的不良内容
import re

sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
purified = re.sub('fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]',
                  '*', sentence, flags=re.IGNORECASE)
print(purified)  # Oh, *! 你是*吗? * you.


print('--------------------------------------------------')


# 拆分长短句
import re

poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)



    