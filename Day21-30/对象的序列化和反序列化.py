"""
    如希望把一个列表
    或一个字典中的数据保存到文件中
    以JSON格式进行保存
    结构紧凑而且时纯文本
    任何操作系统和编程语言都能处理纯文本
    
"""

import json
my_dict = {
    'name' : 'ckp',
    'age': 23,
    'friends': ['hyf', 'zj'],
    'cars':[
        {"brand" : "BMW", "max_speed" : 240},
        {"brand" : "Benz", "max_speed" : 280},
        {"brand" : "Audi", "max_speed" : 280}
        
    ]
}
print(json.dumps(my_dict))



print('--------------------------------------------------')


my_dict = {
    'name' : 'ckp',
    'age': 23,
    'friends': ['hyf', 'zj'],
    'cars':[
        {"brand" : "BMW", "max_speed" : 240},
        {"brand" : "Benz", "max_speed" : 280},
        {"brand" : "Audi", "max_speed" : 280}
        
    ]
}
with open('data.json', 'w') as file:
    json.dump(my_dict, file)
    
"""
    json模块四个重要函数
    dump - 将python对象按照json格式序列化到文件中
    dumps - 将python对象处理成json格式的字符串
    load - 将文件中的json数据反序列化成对象
    loads - 将字符串的内容反序列化成python对象
    
"""

# 读取data.json文件 将json格式的数据还原成python中的字典
import json
with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
    
    
print('--------------------------------------------------')
    
    
#包管理工具pip
# pip install ujson
# pip install ujson -i https://pypi.tuna.tsinghua.edu.cn/simple 
# pip search 根据名字查找需要的第三方库
# pip list 查看已经安装过的第三方库
# pip install --U  或 pip install --upgrade 来更新第三方库
# pip uninstall 卸载某个第三方库


# 使用网络API获取数据
import requests
resp = requests.get('https://apis.tianapi.com/esports/?key=&num=10')
if resp.status_code == 200:
    data_modle = resp.json()
    for news in data_modle['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)



