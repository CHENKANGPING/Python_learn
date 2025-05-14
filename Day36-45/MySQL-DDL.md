MySQL基本命令

1.查看所有数据库
show databases;

2.查看所有字符集
show charater set;

3.查看所有非排序规则
show collation;

4.查看所有引擎
show engines;

5.查看所有日志文件
show binary logs;

6.查看数据库下的所有表
show tables;

SQL详解之DDL
DDL(数据定义语言),DML(数据操作语言),DCL(数据控制语言),TCL(事务控制语言)

DDL主要用于创建,删除,修改数据库中的对象, 比如创建,删除,和修改二维表,核心的关键字包括create, drop, alter;
DML主要负责数据的插入,删除,更新,和查询, 关键字包括insert, delete, update, select;
DCL主要用于授予和召回权限,核心的关键字是grant和revoke;
TCL通常用于事务控制

建库建表

数据库名：school

学院表(tb_collage)

学生表(tb_student)

教师表(tb_teacher)

课程表(tb_course)

选课记录表(tb_record)

```SQL
-- 如果存在名为school的数据库就删除它
DROP DATABASE IF EXISTS `school`;

-- 创建名为school的数据库并设置默认的字符集和排序方式
CREATE DATABASE `school` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- 切换到school数据库上下文环境
USE `school`;

-- 创建学院表
CREATE TABLE `tb_college`
(
`col_id`    int unsigned AUTO_INCREMENT      COMMENT '编号',
`col_name`  varchar(50)  NOT NULL            COMMENT '名称',
`col_intro` varchar(500) NOT NULL DEFAULT '' COMMENT '介绍',
PRIMARY KEY (`col_id`)
);

-- 创建学生表
CREATE TABLE `tb_student`
(
`stu_id`    int unsigned NOT NULL           COMMENT '学号',
`stu_name`  varchar(20)  NOT NULL           COMMENT '姓名',
`stu_sex`   boolean      NOT NULL DEFAULT 1 COMMENT '性别',
`stu_birth` date         NOT NULL           COMMENT '出生日期',
`stu_addr`  varchar(255) DEFAULT ''         COMMENT '籍贯',
`col_id`    int unsigned NOT NULL           COMMENT '所属学院',
PRIMARY KEY (`stu_id`),
CONSTRAINT `fk_student_col_id` FOREIGN KEY (`col_id`) REFERENCES `tb_college` (`col_id`)
);

-- 创建教师表
CREATE TABLE `tb_teacher`
(
`tea_id`    int unsigned NOT NULL                COMMENT '工号',
`tea_name`  varchar(20)  NOT NULL                COMMENT '姓名',
`tea_title` varchar(10)  NOT NULL DEFAULT '助教' COMMENT '职称',
`col_id`    int unsigned NOT NULL                COMMENT '所属学院',
PRIMARY KEY (`tea_id`),
CONSTRAINT `fk_teacher_col_id` FOREIGN KEY (`col_id`) REFERENCES `tb_college` (`col_id`)
);

-- 创建课程表
CREATE TABLE `tb_course`
(
`cou_id`     int unsigned NOT NULL COMMENT '编号',
`cou_name`   varchar(50)  NOT NULL COMMENT '名称',
`cou_credit` int          NOT NULL COMMENT '学分',
`tea_id`     int unsigned NOT NULL COMMENT '授课老师',
PRIMARY KEY (`cou_id`),
CONSTRAINT `fk_course_tea_id` FOREIGN KEY (`tea_id`) REFERENCES `tb_teacher` (`tea_id`)
);

-- 创建选课记录表
CREATE TABLE `tb_record`
(
`rec_id`   bigint unsigned AUTO_INCREMENT COMMENT '选课记录号',
`stu_id`   int unsigned    NOT NULL       COMMENT '学号',
`cou_id`   int unsigned    NOT NULL       COMMENT '课程编号',
`sel_date` date            NOT NULL       COMMENT '选课日期',
`score`    decimal(4,1)                   COMMENT '考试成绩',
PRIMARY KEY (`rec_id`),
CONSTRAINT `fk_record_stu_id` FOREIGN KEY (`stu_id`) REFERENCES `tb_student` (`stu_id`),
CONSTRAINT `fk_record_cou_id` FOREIGN KEY (`cou_id`) REFERENCES `tb_course` (`cou_id`),
CONSTRAINT `uk_record_stu_cou` UNIQUE (`stu_id`, `cou_id`)
);
```

删除表和修改表

```SQL
DROP TABLE `tb_student`;
```

修改表使用 alter table

给学生表添加一个联系电话的列
```SQL
ALTER TABLE `tb_student` ADD COLUMN `stu_tel` varchar(20) NOT NULL COMMENT '联系电话';
```

修改表删除指定的列 将上面添加的联系电话列删除掉
```SQL
ALTER TABLE `tb_student` DROP COLIMN `stu_tel`;
```

修改表，列的的数据类型 例如将学生表的 stu_sex修改为字符
```SQL
ALTER TABLE `tb_student` MODIFY COLIMN `stu_sex` char(1) NOT NULL DEFAULT 'M' COMMENT '性别';
```

修改表删除列的命名 例如将学生表的 `stu_sex` 修改为 `stu_gender`
```SQL
ALTER TABLE `tb_student` CHANGE COLUMN `stu_sex` `stu_gender` boolean DEFAULT 1 COMMENT '性别';
```

修改表删除约束条件 例如删除学生表的 col_id列的外键约束
```SQL
ALTER TABLE `tb_student` DROP FOREIGN KEY 'fk_student_col_id`;
```

修改表添加约束条件 例如给学生表的 col_id 列加上外键约束
```SQL
ALTER TABLE `tb_student` ADD FOREIGN KEY (`col_id`)  REFERENCES `tb_college` (`col_id`);
```