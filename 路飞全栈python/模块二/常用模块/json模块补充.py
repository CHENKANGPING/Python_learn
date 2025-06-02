import json

# user = {
#     "name" : "参考平",
#     "email" : "4123",
#     "gender" : "male"
# }
#
# print(repr(json.dumps(user, ensure_ascii=False)))
#

# data = {
#     1000 : "apple",
#     2000 : "banana",
#     3000 : "peach"
#
# }
#
# print(repr(json.dumps(data)))
#
# with open("data.json","w") as f:
#     json.dump(data,f)


# with open("data.json") as f:
#     data = json.load(f)
#     print(data)
#
# print({int(k):v for k,v in data.items()})


user = {
    "name" : "参考平",
    "email" : "4123",
    "gender" : "male"
}

print(repr(json.dumps(user, ensure_ascii=False,separators=(',',':'))))
print(len(json.dumps(user, ensure_ascii=False,separators=(',',':'))))




