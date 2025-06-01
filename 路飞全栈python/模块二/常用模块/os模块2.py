import os
# os.system(command) : 执行操作系统命令
# os.system("dir")

# os.popen(command) : 执行操作系统命令，返回一个文件对象
# ret = os.popen('dir')
# print(ret.read())

# os.path.join(path1,path2....) : 将多个路径组合成一个路径

# print(os.path.join("a","b","c","d","e","f","g","h"))
# print(os.path.sep)

# os.path.split(path) : 将路径分隔成目录和文件名
# ret = os.path.split(r"C:\Users\ArT\Desktop\python_learn\路飞全栈python")
# print(ret)
# os.path.dirname(path) : 返回路径的目录部分
# path = r"C:\Users\ArT\Desktop\python_learn\路飞全栈python"
# print(os.path.basename(path))
# print(os.path.dirname(path))
# os.path.basename(path) : 返回路径的文件名部分



# os.path.exists(path) ： 检查路径是否存在
# print(os.path.exists(r"C:\Users\ArT\Desktop\python_learn\路飞全栈python"))

