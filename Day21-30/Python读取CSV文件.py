# 将数据写入CSV文件
import csv
import random

with open('scores.csv', 'w') as file:
    # writer = csv.writer(file)
    writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名','语文','数学', '英语'])
    names = ['ckp', 'hyf', 'zj','xxx']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)
        

# 从CSV文件读取数据
import csv

with open('scores.csv','r') as file:
    reader = csv.reader(file,delimiter='|')
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem,end='\t')
    print()