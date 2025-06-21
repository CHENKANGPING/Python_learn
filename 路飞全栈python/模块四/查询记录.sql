 CREATE TABLE emp(
    id		int primary key auto_increment,
    name 	varchar(20),
    gender	ENUM('male','female','other'),
    age		TINYINT,
    dep		VARCHAR(20),
    province VARCHAR(20),
    salary	DOUBLE(7,2)
)character set=utf8;

insert into emp(name,gender,age,dep,province,salary)
values('george','male',24,'教学部','河北省',6000),
	  ('alice','female',22,'销售部','北京市',7000),
    ('bob','male',26,'技术部','上海市',8000),
    ('cindy','female',23,'市场部','广东省',6500),
    ('dave','male',28,'研发部','江苏省',9000),
    ('ellen','female',25,'客服部','浙江省',5500),
    ('frank','male',27,'财务部','四川省',7500),
    ('grace','female',24,'人力资源部','湖北省',6000),
    ('henry','male',29,'采购部','湖南省',6800),
    ('iris','female',21,'公关部','山东省',5800),
    ('james','male',30,'物流部','辽宁省',7200),
    ('kate','female',23,'编辑部','福建省',6300),
    ('larry','male',25,'设计部','安徽省',7800),
    ('molly','female',24,'策划部','河南省',6200),
    ('nathan','male',26,'运维部','陕西省',8500),
    ('olivia','female',22,'法务部','黑龙江省',7000),
    ('peter','male',28,'审计部','吉林省',6600),
    ('quinn','female',27,'培训部','山西省',5900),
    ('robert','male',29,'数据分析部','江西省',7100),
    ('sophie','female',25,'产品部','贵州省',6400),
    ('tom','male',30,'质量控制部','海南省',7300),
    ('ursula','female',23,'新媒体部','云南省',6100),
    ('victor','male',24,'智能科技部','甘肃省',7600),
    ('wanda','female',26,'电商部','青海省',6700),
    ('xavier','male',27,'游戏部','西藏自治区',7400),
    ('yvonne','female',28,'影视部','内蒙古自治区',6900),
    ('zack','male',22,'音乐部','广西壮族自治区',6000),
    ('amy','female',25,'教学部','河北省',6200),
    ('ben','male',26,'教学部','河南省',6300),
    ('carol','female',24,'教学部','山东省',6100),
    ('derek','male',27,'教学部','广东省',6400),
    ('emily','female',23,'教学部','江苏省',6000),
    ('frank','male',28,'教学部','浙江省',6500),
    ('gloria','female',22,'教学部','四川省',6200),
    ('howard','male',25,'教学部','湖南省',6300),
    ('ivory','female',24,'教学部','湖北省',6100),
    ('james','male',26,'教学部','福建省',6400),
    ('karen','female',23,'教学部','安徽省',6000),
    ('lucy','female',27,'教学部','辽宁省',6500),
    ('mike','male',28,'教学部','吉林省',6200),
    ('nancy','female',24,'教学部','黑龙江省',6300),
    ('os','male',25,'教学部','云南省',6100),
    ('pamela','female',26,'教学部','贵州省',6400),
    ('quentin','male',27,'教学部','海南省',6200),
    ('rachel','female',23,'教学部','山西省',6300),
    ('steven','male',24,'教学部','江西省',6100),
    ('tracy','female',25,'教学部','广西壮族自治区',6400),
    ('ulric','male',26,'教学部','西藏自治区',6200),
    ('vera','female',27,'教学部','内蒙古自治区',6300),
    ('william','male',28,'教学部','宁夏回族自治区',6100),
    ('xena','female',29,'教学部','新疆维吾尔自治区',6400),
    ('york','male',30,'教学部','香港特别行政区',6200),
    ('zoe','female',22,'教学部','澳门特别行政区',6300);

-- 查询字段
select * from emp;
select name,salary
from emp;
select  name, gender, age, dep, province, salary
from emp;

-- 条件过滤
-- 查询年龄大于30岁的员工
select *
from emp where age > 30;

-- 查询年龄在20-30之间的所有员工
select *
from emp where age between 20 and 30;

select *
from emp where  age in (10,20,30);

-- 查询所有员工姓名以b开头的
select *
from emp where  name like 'b%';

select *
from emp where  name like 'a_';

-- 正则
select *
from emp where  name regexp '^b'; # 以b开头

select *
from emp where  name regexp 'n$'; #以n结尾

select *
from emp where name regexp '.*b.*'; # 包含b

-- 正则函数
select *
from emp where regexp_like(name,'.*b.*','c');

-- 查询教学部的所有男老师信息
select *
from emp where gender = 'male' and dep = '教学部';

select *
from emp where gender = 'female' and dep = '教学部';

-- 查询名字以A开头的员工并且工资大于等于10000的员工姓名
select *
from emp where  regexp_like(name,'^a','c') and salary >=10000;

-- 查询年龄小于25或工资低于10000的员工
select *
from emp
where age < 25 or salary < 10000;

-- 日期相关查询
select *
from emp
where  birthday > '1990-1-1';

-- 查询1990年出身的所有员工
select *
from emp
where year(birthday) = 1990;


-- 查询12月出身的所有员工
select *
from emp
where month(birthday) = 12;

-- 查询所有摩羯座的员工
select *
from emp
where (month(birthday) = 12 and day(birthday) > 22)
    or (month(birthday) = 1 and day(birthday) < 19);


-- order by
select *
from emp order by  age desc ;

select *
from emp order by salary desc ;

select *
from emp order by salary desc limit 3;

select *
from emp order by salary,age,id;

select *
from emp where salary > 5000 order by salary;

-- 查询男女员工个有多少人
 select gender 性别,count(*) 人数
 from emp
 group by gender;

-- 查询年龄大于25的男女员工个有多少人
 select gender 性别,count(*) 人数
 from emp
 where age > 25
 group by gender;

-- 查询教学部的员工最高工资
 select dep,max(salary)
 from emp
 group by dep
 having dep ='教学部';

-- 查询公司所有员工的平均工资
 select avg(salary)
 from emp;

-- 查询平均薪水超过5000的部门
 select dep,avg(salary) 平均薪水
 from emp
 group by dep
 having 平均薪水 > 5000;

-- 查询薪水超过5000的所有员工的前提下部门的平均薪资
 select dep,avg(salary)
 from emp
 where salary > 5000
 group by dep;

-- 查询每个部门的所有员工姓名
 select dep,group_concat(name)
 from emp
 group by dep;

-- 查询公司一共有多少个员工
select count(*) from emp


-- 取前10条信息
 select *
 from emp
 limit  10;

-- 跨过前两条 显示4条
#  select *
#  from emp
#  limit 2,4;

-- 查询工资最高的前五人
 select *
 from emp
 order by salary desc,age desc
 limit  5;

-- 查询年龄最大的5个人
 select *
 from emp
 order by age desc
 limit  5;


-- 分页
-- 第一页
select * from  emp limit 10;

-- 第二页
select * from  emp limit 10,10;

-- 第三页
select * from  emp limit 20,10;



-- 查询去重
 select distinct name, age
 from emp;
