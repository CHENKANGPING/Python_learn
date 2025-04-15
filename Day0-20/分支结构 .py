# 分支结构
# 使用if和else构造分支
# BMI计算器 
height = float(input('身高（cm）： '))
weight = float(input('体重（kg）： '))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')
    
print('--------------------------------------------------')

# 使用match和case构造分支结构 match - case 语句支持Python 3.10 以上版本
# status_code = int(input('相应状态码：'))
# match status_code:
#     case 400 | 405: descripiton = ' Invalid Request '
#     case 401 | 403 | 404: descripiton = ' not allowed '
#     case 418: descripiton = ' i an a teapot '
#     case 429: descripiton = ' too many requests '
#     case _: descripiton = ' unknow status code'
# print('状态码描述： ', descripiton) 


# 分支结构应用
# 1.分段函数求值
x = float(input(' x = '))
if x > 1:
    y = 3 * x -5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')

print('--------------------------------------------------')

# 2.分数转等级
score = float(input('请输入成绩： '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade = }') 

print('--------------------------------------------------')

# 2.计算三角形的周长和面积
# 要求：输入三条边的长度，如能构成三角形计算周长和面积，如不能返回无法构成三角形
# 分析构成三角形要求，任意两边之和大于第三边即可构成
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a :
    circumference = a + b + c
    print(f'周长：{circumference}')
    s = circumference / 2
    area = (s *( s - a ) * ( s - b ) * ( s - c )) ** 0.5
    print(f'面积: {area}')
else:
    print("无法构成三角形！")
    
    
    





    


    
    