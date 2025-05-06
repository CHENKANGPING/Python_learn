# D&C  分而治之
# 1 找出简单的基线条件
# 2 确定如何缩小问题的规模，使其符合基线条件
def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])
    
print(sum([1,2,3,4,5,6,7,8]))

# 快排
def quicksort(array):
    if len(array) < 2: # 基线条件：数组为空或只含一个元素
        return array
    else:
        pivot = array[0] # 递归条件 pivot指的是基准值 这里的基准值为10 因为是array[0]
        less = [i for i in array[1:] if i <= pivot] # 遍历除pivot以外的元组 若小于pivot 则进入小于基准值的子数组 
        
        greater = [i for i in array[1:] if i > pivot] # 遍历除pivot以外的元素 若大于pivot则进入大于基准值的子数组
                
        return quicksort(less) + [pivot] + quicksort(greater)
# 从案例来看 10 为基准值 less = [5,2,3] greater 为空 这是第一次递归的结果
# 进行第二次递归 len(less) = 3 进行第二次递归  此时基准值为 less[0] = 5
# less = [2,3] greater 为空 这是第二次递归的结果
# 由于len(less)的值 = 2 进行第三次递归 此时基准值为 less[0] = 2
# 遍历剩下的元素 3 > 2 元素3 进入 greater中 less为空 这是第三次递归的结果
# 此时 less[2] 为单个元素 无需排序 进行递归回溯
# quicksort([5, 2, 3]) = quicksort([2, 3]) + [5] + quicksort([]) = [2, 3] + [5] + [] = [2, 3, 5]
# 最终结果 quicksort([10, 5, 2, 3]) = quicksort([2, 3, 5]) + [10] + quicksort([]) = [2, 3, 5] + [10] + [] = [2, 3, 5, 10]
    
print(quicksort([10,5,2,3]))       
        


