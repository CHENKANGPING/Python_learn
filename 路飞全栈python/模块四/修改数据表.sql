-- 修改表名
alter table student rename students;

-- 修改编码集
alter  table  students character set = gbk;

-- 表的字段增删改

-- （1）添加字段
alter table students add  class_name  varchar(32) not null;

-- (2) 删除字段
alter table students drop  class_name;

-- (3) 修改字段
alter  table  students modify  name varchar(32) not null;

-- (4) 修改字段名
alter  table  students change  birth birthday date;


-- 补充 first after：字段位置
alter table students add  class_name  varchar(32) not null after id;
alter table students modify  class_name  varchar(20) first;
alter table students change  class_name cls_name  varchar(20) after birthday;

