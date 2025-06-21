/*
    -- 语法
CREATE TABLE table_name(
             field1 type[约束条件]，
             field2 type,
             ...
             fieldn type   -- 一定不要加逗号，否则报错。

)[character set utf8];
*/
-- 无约束版
create table student
(
    name   varchar(32),
    gender bit,
    age    int,
    birth  date,
    gpa    decimal(4, 2)

)character set=gbk;



 -- 有约束版
use db_day01;

CREATE TABLE student(
    id int primary key auto_increment,
    name varchar(20) not null,
    gender bit default 1,
    age int,
    birth date
)character set=utf8;

