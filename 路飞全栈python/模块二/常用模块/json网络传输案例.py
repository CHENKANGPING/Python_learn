"""
JS实现的序列化对对象处理

data  = {user:"ckp", pwd:"123"}
{user:'ckp', pwd:'123'}

data
{user:'ckp', pwd:'123'}

// 序列化
JSON.stringify(data)
'{user:"ckp", pwd:"123"}'



"""
import json


s = '{"user":"ckp", "pwd":"123"}'

# 反序列化
data = json.loads(s)

print(data, type(data))

user = data.get("user")
pwd = data.get("pwd")

# 数据过滤
user = {
    "naem" : "ckp",
    "email" : "4123",
    "gender" : "male"
}

res = json.dumps(user)
print(repr(res),type(res))
