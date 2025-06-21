-- 更新员工职位和工资

update emp set salary = 99990 where name = 'bob';

-- 更改部门名称
update emp
set dep = 'python开发部门'
where dep = '技术部';


update emp
set salary = salary * 0.9
where age > 25;

-- 薪资最高的五个人降薪百分之30
update emp
set salary = salary * 0.7
order by  salary desc limit 5;

-- 删除指定员工 bob
delete
from emp
where name = 'bob';


-- 删除薪资最高的五个人，相同薪资按年龄优先
delete
from emp
order by salary desc ,age desc  limit 5;


