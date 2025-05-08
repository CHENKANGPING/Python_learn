"""
    是一种用于图的查找算法 
    回答两类问题
    从节点A出发 有前往节点B的路径吗
    从节点A出发 前往节点B的哪条路径最短
    
    
    队列 FIFO
    队列是一种先进先出的数据结构
    
    运行时间至少为O(边数)
    由于用到了队列
    所以BFS的运行时间为O(边数 + 人数)
"""
from collections import deque
# 使用字典创建图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 判断水果经销商 名字的最后一个字母是'm'
def person_is_seller(name):
    return name[-1] =='m'


def search(name):
    """
    使用广度优先搜索查找是否存在名字以'm'结尾的芒果销售商。
    :param name: 起始搜索的节点名称
    :return: 如果找到芒果销售商 返回True 否则返回False
    """
    search_queue = deque() # 使用deque创建一个双端队列
    search_queue += graph[name] # 将起始节点的所有朋友加入双端队列
    searched = [] # 创建一个空数组 用来记录被搜索过的节点
    while search_queue: # 进入循环
        person = search_queue.popleft() # 依次从已经创建的双端队列取人名进行判断
        if not person in searched: # 如果这个人名不在searched中
            if person_is_seller(person): # 如果符合person_is_seller 就输出 person + is a mango seller!
                print(person + ' is a mango seller!')
                return True
            else: # 否则 将该人名下的所有节点加入双端队列
                search_queue += graph[person]
                searched.append(person) #将刚才查找的人名加入searched 用于记录 避免重复
    return False

search('you')
    

        