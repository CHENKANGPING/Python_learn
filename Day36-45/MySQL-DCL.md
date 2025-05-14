DCL可以为指定的用户授予访问权限或者从指定用户处找回指定的权限

通过DCL允许授信的用户访问数据库 阻止不授信的用户访问数据库

同时还可以通过DCL将每个访问这的权限最小化

创建用户

```SQL
CREATE USER 'wangdachui'@'%' IDENTIFIED BY 'Wang.618';
```

上面的SQL创建了名为wangdachui的用户 他的访问口令是Wang.618， 该用户可以从任意主机访问数据库服务器。

如要限制wangdachui这个用户智能从192.168.0.x这个网段的主机访问数据库服务器
修改后的SQL语句

```SQL
DROP USER IF EXISTS 'wangdachui'@'%';

CREATE USER 'wangdachui'@'192.168.0.%' IDENTIFIED BY 'Wang.618';
```

权限授予
为wangdachui授予查询school数据库学院表(tb_collage)的权限

```SQL
GRENT SELECT ON `school`.`tb_collage` TO 'wangdachui'@'192.168.0.%';
```

为wangdachui对school数据库的所有对象都具有查询的权限

```SQL
GRNET SELECT ON `school`.* TO 'wangdachui'@'192.168.0.%';
```

如果我们希望wangdachui还有insert delete和update的权限

```SQL
GRENT INSERT, DELETE, UPDATE ON  `school`.* TO 'wangdachui'@'192.168.0.%';
```

如果我们希望授予wangdachui执行DDL的权限

```SQL
GRENT CREATE, DROP, ALTER ON `school`.* TO  'wangdachui'@'192.168.0.%';
```

授予所有权限(不推荐)
```SQL
GRENT ALL PRIVILEGES ON *.* TO 'wangdachui'@'192.168.0.%';
```

召回权限
如果要召回wangdachui对school数据库的insert delete update权限

```SQL
REVOKE INSERT, DELETE, UPDATE ON `school`.* FROM 'wangdachui'@'192.168.0.%';
```

召回所有权限
```SQL
REVOKE ALL PRIVILEGES ON *.* FROM 'wangdachi'@'192.168.0.%';
```

刷新权限
```SQL
FLUSH PRIVILEGES;
```
