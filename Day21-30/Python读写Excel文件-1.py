# pip install xlwt xlrd xlutils
# 写Excel文件
import random
import xlwt

student_names = ['ckp', 'hyf', 'zj', 'xxx']
scores = [[random.randrange(50, 100) for _ in range(3)] for _ in range(4)]

wb = xlwt.Workbook()

sheet = wb.add_sheet('22001')
titles = ('name', 'Chinese', 'Math', 'English')

for index, title in enumerate(titles):
    sheet.write(0, index, title)
    
for row in range(len(scores)):
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
        
wb.save('text.xls')