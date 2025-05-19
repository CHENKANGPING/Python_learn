"""
    狄克斯塔拉算法找出的是总权数最小的路径
    狄克斯特拉算法4个步骤
    1.找出最便宜的节点 即可在最短时间内前往的节点
    2.对于该节点的邻居 检查是否有前往它们更短的路径 如果有 就更新其开销
    3.重复这个过程 直到对图中的每个节点都这样做了
    4.计算最终路径
    如有负边权就不能使用狄克斯特拉算法
    
"""

"""
Dijkstra算法完整实现示例
用于查找从起点到终点的最短路径
"""

# --------------------- 数据结构定义 ---------------------
# 使用邻接表表示图结构
# 格式：graph[节点] = {相邻节点: 边权重}
graph = {
    "start": {
        "a": 6,     # 从start到a的边权重为6
        "b": 2      # 从start到b的边权重为2
    },
    "a": {
        "fin": 1    # 从a到fin的边权重为1
    },
    "b": {
        "a": 3,     # 从b到a的边权重为3
        "fin": 5     # 从b到fin的边权重为5
    },
    "fin": {}        # 终点没有出边
}

# 初始化开销表（记录当前已知到达各节点的最小开销）
infinity = float("inf")
costs = {
    "a": 6,         # 初始路径：start → a
    "b": 2,         # 初始路径：start → b
    "fin": infinity  # 初始时无法直接到达终点
}

# 初始化父节点表（记录最短路径的节点关系）
parents = {
    "a": "start",   # a的父节点是起点
    "b": "start",    # b的父节点是起点
    "fin": None      # 终点没有父节点
}

# 记录已处理过的节点
processed = []

# --------------------- 工具函数 ---------------------
def find_lowest_cost_node(costs):
    """
    在未处理的节点中找出开销最小的节点
    时间复杂度：O(n)，可以使用优先队列优化为O(log n)
    """
    lowest_cost = infinity
    lowest_cost_node = None
    
    # 遍历所有节点
    for node in costs:
        cost = costs[node]
        # 如果当前节点开销更低且未被处理过
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
            
    return lowest_cost_node

# --------------------- 算法主体 ---------------------
# 查找当前最小开销节点（初始为b节点）
current_node = find_lowest_cost_node(costs)

# 主循环：当还有未处理的节点时继续
while current_node is not None:
    # 获取当前节点的开销和邻居信息
    current_cost = costs[current_node]
    neighbors = graph[current_node]
    
    print(f"\n正在处理节点 {current_node}，当前开销：{current_cost}")
    print("邻居节点:", list(neighbors.keys()))
    
    # 遍历所有邻居节点
    for neighbor, weight in neighbors.items():
        # 计算经过当前节点到达该邻居的新路径总开销
        new_cost = current_cost + weight
        
        print(f"  检查邻居 {neighbor}：旧开销 {costs[neighbor]} vs 新开销 {new_cost}")

        # 如果发现更便宜的路径
        if new_cost < costs[neighbor]:
            print(f"  ↘ 更新 {neighbor} 的开销：{costs[neighbor]} → {new_cost}")
            costs[neighbor] = new_cost       # 更新开销表
            parents[neighbor] = current_node # 更新父节点关系
    
    # 将当前节点标记为已处理
    processed.append(current_node)
    print(f"处理完成，已标记 {current_node} 为已处理")
    
    # 获取下一个最小开销节点
    current_node = find_lowest_cost_node(costs)

# --------------------- 结果输出 ---------------------
print("\n最终结果：")
print("开销表:", costs)        # {'a': 5, 'b': 2, 'fin': 6}
print("父节点表:", parents)    # {'a': 'b', 'b': 'start', 'fin': 'a'}

# 路径回溯函数
def build_path(target):
    """根据父节点表回溯生成路径"""
    path = []
    while target is not None:
        path.append(target)
        target = parents.get(target)
    return ' → '.join(reversed(path))

print("最短路径:", build_path("fin"))  # start → b → a → fin