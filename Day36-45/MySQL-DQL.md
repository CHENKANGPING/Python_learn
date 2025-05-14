查询操作

```SQL
USE school;

-- 查询所有学生的所有信息
SELECT stu_id,
       stu_name,
       stu_sex,
       stu_birth,
       stu_addr,
       col_id
  FROM tb_student;

-- 查询学生的学号、姓名和籍贯(投影和别名)
SELECT stu_id AS 学号,
       stu_name AS 姓名,
       stu_addr AS 籍贯
  FROM tb_student;

-- 查询所有课程的名称及学分(投影和别名)
SELECT cou_name AS 课程名称,
       cou_credit AS 学分
  FROM tb_course;

-- 查询所有女学生的姓名和出生日期(数据筛选)
SELECT stu_name,
       stu_birth
  FROM tb_student
 WHERE stu_sex = 0;

-- 查询籍贯为“四川成都”的女学生的姓名和出生日期(数据筛选)
SELECT stu_name,
       stu_birth
  FROM tb_student
 WHERE stu_sex = 0
       AND stu_addr = '四川成都';

-- 查询籍贯为“四川成都”或者性别是女的学生(数据筛选)
SELECT stu_name,
       stu_birth
  FROM tb_student
 WHERE stu_sex = 0
       OR stu_addr = '四川成都';

-- 查询所有80后学生的姓名、性别和出生日期(数据筛选)
SELECT stu_name,
       stu_sex,
       stu_birth
  FROM tb_student
 WHERE '1980-1-1' <= stu_birth 
       AND stu_birth <= '1989-12-31';
       
SELECT stu_name,
       stu_sex,
       stu_birth
  FROM tb_student
 WHERE stu_birth BETWEEN '1980-1-1' AND '1989-12-31';

-- 查询学分大于2的课程的名称和学分(数据筛选)
SELECT cou_name,
	   cou_credit
  FROM tb_course
 WHERE cou_credit > 2;

-- 查询学分是奇数的课程的名称和学分(数据筛选)
SELECT cou_name,
	   cou_credit
  FROM tb_course
 WHERE cou_credit MOD 2 <> 0;

-- 查询选择选了1111的课程考试成绩在90分以上的学生学号(数据筛选)
SELECT stu_id
  FROM tb_record
 WHERE cou_id = 1111
       AND score > 90;

-- 查询名字叫“杨过”的学生的姓名和性别(数据筛选)
SELECT stu_name AS 姓名, 
       CASE stu_sex WHEN 1 THEN '男' ELSE '女' END AS 性别
  FROM tb_student
 WHERE stu_name = '杨过';
 
SELECT stu_name AS 姓名, 
       IF(stu_sex, '男', '女') AS 性别
  FROM tb_student
 WHERE stu_name = '杨过';
    
-- 查询姓“杨”的学生姓名和性别(模糊匹配)
-- 通配符 % 匹配零个或任意多个字符
SELECT stu_name AS 姓名, 
       CASE stu_sex WHEN 1 THEN '男' ELSE '女' END AS 性别
  FROM tb_student
 WHERE stu_name LIKE '杨%';

-- 查询姓“杨”名字两个字的学生姓名和性别(模糊匹配)
-- 通过符 _ 匹配一个字符
SELECT stu_name AS 姓名, 
       CASE stu_sex WHEN 1 THEN '男' ELSE '女' END AS 性别
  FROM tb_student
 WHERE stu_name LIKE '杨_';

-- 查询姓“杨”名字三个字的学生姓名和性别(模糊匹配)
SELECT stu_name AS 姓名, 
       CASE stu_sex WHEN 1 THEN '男' ELSE '女' END AS 性别
  FROM tb_student
 WHERE stu_name LIKE '杨__';
 
-- 查询学号最后一位是3的学生的学号和姓名(模糊匹配)
SELECT stu_id,
       stu_name
  FROM tb_student
 WHERE stu_id LIKE '%3';

-- 查询名字中有“不”字或“嫣”字的学生的学号和姓名(模糊匹配和并集运算)
SELECT stu_id,
       stu_name
  FROM tb_student
 WHERE stu_name LIKE '%不%'
       OR stu_name LIKE '%嫣%';
       
SELECT stu_id,
       stu_name
  FROM tb_student
 WHERE stu_name LIKE '%不%'
 UNION
SELECT stu_id,
       stu_name
  FROM tb_student
 WHERE stu_name LIKE '%嫣%';

-- 查询姓“杨”或姓“林”名字三个字的学生的学号和姓名(正则表达式模糊匹配)
SELECT stu_id,
       stu_name
  FROM tb_student
 WHERE stu_name REGEXP '[林杨][\\u4e00-\\u9fa5]{2}';

-- 查询没有录入籍贯的学生姓名(空值处理)
SELECT stu_name
  FROM tb_student
 WHERE TRIM(stu_addr) = ''
       OR stu_addr is null;
 
-- 查询录入了籍贯的学生姓名(空值处理)
SELECT stu_name
  FROM tb_student
 WHERE TRIM(stu_addr) <> ''
       AND stu_addr is not null;

-- 查询学生选课的所有日期(去重)
SELECT DISTINCT sel_date
  FROM tb_record;

-- 查询学生的籍贯(去重)
SELECT DISTINCT stu_addr
  FROM tb_student
 WHERE TRIM(stu_addr) <> ''
       AND stu_addr is not null;

-- 查询男学生的姓名和生日按年龄从大到小排列(排序)
SELECT stu_name,
       stu_birth
  FROM tb_student
 WHERE stu_sex = 1
 ORDER BY stu_birth ASC;
 
-- 补充：将上面的生日换算成年龄(日期函数、数值函数)
SELECT stu_name AS 姓名,
       FLOOR(DATEDIFF(CURDATE(), stu_birth) / 365) AS 年龄
  FROM tb_student
 WHERE stu_sex = 1
 ORDER BY 年龄 DESC;

-- 查询年龄最大的学生的出生日期(聚合函数)
SELECT MIN(stu_birth)
  FROM tb_student;

-- 查询年龄最小的学生的出生日期(聚合函数)
SELECT MAX(stu_birth)
  FROM tb_student;

-- 查询编号为1111的课程考试成绩的最高分(聚合函数)
SELECT MAX(score)
  FROM tb_record
 WHERE cou_id = 1111;

-- 查询学号为1001的学生考试成绩的最低分、最高分、平均分、标准差、方差(聚合函数)
SELECT MIN(score) AS 最低分,
       MAX(score) AS 最高分,
	   ROUND(AVG(score), 1) AS 平均分,
       STDDEV(score) AS 标准差,
       VARIANCE(score) AS 方差
  FROM tb_record
 WHERE stu_id = 1001;

-- 查询学号为1001的学生考试成绩的平均分，如果有null值，null值算0分(聚合函数)
SELECT ROUND(SUM(score) / COUNT(*), 1) AS 平均分
  FROM tb_record
 WHERE stu_id = 1001;

-- 查询男女学生的人数(分组和聚合函数)
SELECT CASE stu_sex WHEN 1 THEN '男' ELSE '女' END AS 性别,
       COUNT(*) AS 人数
  FROM tb_student
 GROUP BY stu_sex;

-- 查询每个学院学生人数(分组和聚合函数)
SELECT col_id AS 学院编号,
       COUNT(*) AS 人数
  FROM tb_student
 GROUP BY col_id
  WITH ROLLUP;

-- 查询每个学院男女学生人数(分组和聚合函数)
SELECT col_id AS 学院编号,
       CASE stu_sex WHEN 1 THEN '男' ELSE '女' END AS 性别,
       COUNT(*) AS 人数
  FROM tb_student
 GROUP BY col_id, stu_sex;

-- 查询每个学生的学号和平均成绩(分组和聚合函数)
SELECT stu_id AS 学号,
	   ROUND(AVG(score), 1) AS 平均分
  FROM tb_record
 GROUP BY stu_id;

-- 查询平均成绩大于等于90分的学生的学号和平均成绩(分组后的数据筛选)
SELECT stu_id AS 学号,
	   ROUND(AVG(score), 1) AS 平均分
  FROM tb_record
 GROUP BY stu_id
HAVING 平均分 >= 90;

-- 查询1111、2222、3333三门课程平均成绩大于等于90分的学生的学号和平均成绩(分组前后的数据筛选)
SELECT stu_id AS 学号,
	   ROUND(AVG(score), 1) AS 平均分
  FROM tb_record
 WHERE cou_id in (1111, 2222, 3333)
 GROUP BY stu_id
HAVING 平均分 >= 90
 ORDER BY 平均分 ASC;

-- 查询年龄最大的学生的姓名(子查询)
SELECT stu_name
  FROM tb_student
 WHERE stu_birth = (SELECT MIN(stu_birth)
                      FROM tb_student);

-- 查询选了两门以上的课程的学生姓名(子查询和集合运算)
SELECT stu_name
  FROM tb_student
 WHERE stu_id in (SELECT stu_id
				    FROM tb_record
				   GROUP BY stu_id
				  HAVING COUNT(*) > 2);

-- 查询学生的姓名、生日和所在学院名称(表连接)
SELECT stu_name,
       stu_birth,
       col_name
  FROM tb_student AS t1, tb_college AS t2
 WHERE t1.col_id = t2.col_id;
 
SELECT stu_name,
       stu_birth,
	   col_name
  FROM tb_student INNER JOIN tb_college
       ON tb_student.col_id = tb_college.col_id;

SELECT stu_name,
       stu_birth,
	   col_name
  FROM tb_student NATURAL JOIN tb_college;
  
SELECT stu_name,
       stu_birth,
	   col_name
  FROM tb_student CROSS JOIN tb_college;

-- 查询学生姓名、课程名称以及成绩(表连接)
SELECT stu_name,
       cou_name,
	   score
  FROM tb_student, tb_course, tb_record
 WHERE tb_student.stu_id = tb_record.stu_id
       AND tb_course.cou_id = tb_record.cou_id
       AND score is not null;

SELECT stu_name,
       cou_name,
	   score
  FROM tb_student 
       INNER JOIN tb_record
	       ON tb_student.stu_id = tb_record.stu_id
	   INNER JOIN tb_course
	       ON tb_course.cou_id = tb_record.cou_id
 WHERE score is not null;
 
SELECT stu_name,
       cou_name,
       score
  FROM tb_student 
	   NATURAL JOIN tb_record
       NATURAL JOIN tb_course
 WHERE score is not null;

-- 补充：上面的查询结果取前5条数据(分页查询)
SELECT stu_name,
       cou_name,
       score
  FROM tb_student 
	   NATURAL JOIN tb_record
       NATURAL JOIN tb_course
 WHERE score is not null
 ORDER BY cou_id ASC, score DESC
 LIMIT 5;

-- 补充：上面的查询结果取第6-10条数据(分页查询)
SELECT stu_name,
       cou_name,
       score
  FROM tb_student 
	   NATURAL JOIN tb_record
       NATURAL JOIN tb_course
 WHERE score is not null
 ORDER BY cou_id ASC, score DESC
 LIMIT 5
OFFSET 5;

-- 补充：上面的查询结果取第11-15条数据(分页查询)
SELECT stu_name,
       cou_name,
       score
  FROM tb_student 
	   NATURAL JOIN tb_record
       NATURAL JOIN tb_course
 WHERE score is not null
 ORDER BY cou_id ASC, score DESC
 LIMIT 10, 5;

-- 查询选课学生的姓名和平均成绩(子查询和表连接)
-- Error Code: 1248. Every derived table must have its own alias
SELECT stu_name,
	   avg_score
  FROM tb_student
       NATURAL JOIN (SELECT stu_id,
                            ROUND(AVG(score), 1) AS avg_score
                       FROM tb_record
                      GROUP BY stu_id) as tmp;

-- 查询学生的姓名和选课的数量(子查询和表连接)
SELECT stu_name,
	   total
  FROM tb_student
       NATURAL JOIN (SELECT stu_id,
                            COUNT(*) AS total
                       FROM tb_record
                      GROUP BY stu_id) as tmp;

-- 查询每个学生的姓名和选课数量(子查询和左外连接)
SELECT stu_name AS 姓名,
	   COALESCE(total, 0) AS 选课数量
  FROM tb_student AS t1
	   LEFT JOIN (SELECT stu_id,
			             COUNT(*) AS total
		            FROM tb_record
				   GROUP BY stu_id) AS t2
	       ON t1.stu_id = t2.stu_id;

```




