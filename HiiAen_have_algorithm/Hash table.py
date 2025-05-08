book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)
print(book["avocado"])

"""
    散列表由键和值组成
    适合用于
    模拟映射关系
    防止重复
    缓存/记住数据 以免服务器在通过处理来生成它们
    
"""
voted = {}
def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')
        
check_voter('tom')
check_voter('jack')
check_voter('jack')