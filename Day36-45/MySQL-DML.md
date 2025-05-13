DML 可以帮助将数据插入到二维表(insert操作) 
从二维表删除数据(delete操作)
更新二维表的数据(update操作)

在执行DML之前使用use命令切换到 school 数据库
```SQL
USE `school`;
```

insert 操作
插入方式:插入完整的一行、插入行的一部分、 插入多行、 插入查询的结果

向学院表中添加一个学院

```SQL
INSERT INTO `tb_collage`
VALUSE
    (DEFAULT, '计算机学院', '学习计算机科学与技术的地方');
```
最佳插入
```SQL
INSERT INTO `tb_collage`
            (`col_name`, `col_inrtro`)
VALUSE 
    ('外国语学院', '学习外国人的语言的学院'),
    ('经济管理学院','经世济民, 治理国家; 管理科学, 兴国之道'),
    ('体育学院', '发展体育运动, 增强人民体质');
```