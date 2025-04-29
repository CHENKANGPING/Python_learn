def findSmallest(arr):
    smallest = arr[0] # 假设第一个值为0
    smallest_index = 0 # 最小值的索引为0
    for i in range(1, len(arr)): #for 循环 从索引1 开始 因为索引0 已经被初始化
        if arr[i] < smallest:  # 如果 当前元素小于最小值
            smallest = arr[i]  # 让最小值变为当前元素
            smallest_index = i # 最小值索引变为当前循环下的 第 i 次
    return smallest_index # 返回最小值索引

def Selectionsort(arr):
    newArr = [] # 定义一个空列表 用于存放排序后的元素
    for i in range(len(arr)): # 遍历数组的长度次
        smallest = findSmallest(arr) # 寻找当前数组下的最小值
        newArr.append(arr.pop(smallest)) # 将最小值从原数组移除 添加到空数组中去
    return newArr # 返回排序后的数组

print(Selectionsort([5, 3, 6, 2, 10]))