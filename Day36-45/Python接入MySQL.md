## Python接入MySQL数据库

使用第三方库 `pymysql`

如需要接入MySQL8.0


```Shell
pip install pymysql cryptography
```

使用 `pymysql` 操作MySQL的步骤

1. 创建连接 MySQL服务器启动后 提供了基于TPC的网络服务。我们可以通过 `pymysql` 模块的 `connect` 函数连接MySQL服务器。需要指定主机(`host`)、端口(`prot`)、用户名(`usr`)、口令(`password`)、数据库(`database`)、字符集(`charset`)等参数，该函数会返回一个`Connection`对象。

2. 获取游标。连接MySQL服务器成功后，接下来要做的就是向数据库服务器发送`SQL`语句，MySQL会执行接收到的SQL并执行结果通过网络返回。要实现这项操作，需要先通过连接对象的`cursor`方法获取游标(`Cursor`)对象。

3. 发出SQL。通过游标对象的`execute`方法，我们可以向数据库发出SQL语句。

4. 如果执行`insert`、`delete`或`update`操作，需要根据实际情况提交或回滚事务。因为创建连接时，默认开启了事务环境，在操作完成后，需要使用连接对象`commit`或`rollback`方法，实现事务的提交或回滚，`rollback`方法通常会放在异常捕获代码块`except`中。如果执行`select`操作，需要通过游标对象抓取查询记录的结果，对应的方法分别是`fetchone`、 `fetchmany`和`fetchall`。其中`fetchone`方法会抓取到一条记录，并以元组或字典的方式放回；`fetchone`、`fetchall`方法会抓取到多条记录，并嵌套元组或列表装字典的方式返回。

5. 关闭连接。在完成持久化操作后，请不要忘记关闭连接，释放外部资源。我们通常会在`finally`代码块中使用连接对象的`close`方法来关闭连接。


## 代码实操

插入数据

```Python
import pymysql

no = int(input('部门编号：'))
name = input('部门名称：')
location = input('部门所在地：')

# 1.建立连接(Connection)
conn = pymysql.connect(host = '127.0.0.1', port = 3306，
                       user = 'root', password = '123456',
                       database = 'hrs', charset = 'utf8mb4')

try:
    # 2. 获取游标对象(Course)
    with conn.cursor() as cursor:
        # 3. 通过游标对象数据库服务器发处SQL语句
        affected_rows = cursor.execute(
            'insert into `tb_dept` values(%s, %s, %s)',
            (no, name, location)
        )
        if affected_rows == 1:
            print('新增部门成功！！！')
    # 4. 提交事务(transaction)
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()
```

删除数据

```Python
import pymysql

no = int(input('部门编号：'))

# 1. 创建连接(Connection)
conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', password = '123456',
                       database = 'hrs', charset = 'utf8mb4',
                       autocommit = True)
try:
    # 2. 获取游标对象(Cursor)
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发送SQL语句
        affected_rows = cursor.execute(
            'delete from `tb_dept` where `dno` =%s',
            (no, )
        )
        if affected_rows == 1:
            print('删除部门成功!!!')
finally:
    # 5. 关闭连接释放资源
    conn.close()
```

更新数据

```Python
import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', password = '123456',
                       database = 'hrs', charset = 'utf8mb4')
        
try:
    with conn.cursor() as cursor:
        affected_rows = coursor.execute(
            'update `tb_dept` set `dnames` =%s, `dloc` =%s where `dno` = %s',
            (name, location, no)
        )
        if affected_rows == 1:
            print('更新部门信息成功！！！')
    
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)

finally:
    conn.close()
```

查询数据

1. 查询部门表的信息

```Python
import pymysql

conn = pymysql.connect(host = '127.0.0.1', port = 3306,
                       user = 'root', password = '123456',
                       database = 'hrs', charset = 'utf8mb4')

try:
    with conn.cursor() as cursor:
        cursor.execute('select `dno`, `dname`, `dloc` from `tb_dept`')
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    conn.close()
```

分页查询员工表的数据

```Python
import pymysql

page = int(input('页码：')
size = int(input('大小: '))

con = pymysql.connect(host = '127.0.0.1', port = 3306,
                      user = 'root', password = '123456',
                      database = 'hrs', charset = 'utf8')

try:
    with con.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(
            'select `eno`, `ename`, `job`, `sal` from `tb_emp` order by `sal` desc limit %s,%s',
            ((page - 1) * size, size)
        )

        for emp_dict in cursor.fetchall():
            print(emp_dict)

finally:
    con.close()
```

## 案例讲解

将数据库表导出到Excel文件，首先安装`openpyxl`三方库

```Shell
pip install openpyxl
```

将数据库`hrs`中所有员工的编号、姓名、职位、月薪、补贴、和部门名称导出到一个Excel中

```Python
import openpyxl
import pymysql

# 创建工作簿对象
workbook = openpyxl.Workbook()

# 获得默认的工作表
sheet = workbook.active

# 修改工作表的名称
sheet.title = '员工基本信息'

# 给工作表添加表头
sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='123456',
                       database='hrs', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        cursor.execute(
            'SELECT `eno`, `ename`, `job`, `sal`, COALESCE(`comm`, 0), `dname` '
            'FROM `tb_emp` NATURAL JOIN `tb_dept`'
        )
        # 使用 fetchall 获取所有数据
        rows = cursor.fetchall()
        for row in rows:
            sheet.append(row)
    
    # 保存工作簿
    workbook.save('hrs.xlsx')
    print("数据已成功导出到 hrs.xlsx 文件中。")
except pymysql.MySQLError as err:
    print("数据库操作失败：", err)
finally:
    conn.close()
```
