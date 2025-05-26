## Linux 常用命令

1.ls : 列出当前目录中的文件和子目录。

2.pwd : 显示当前工作目录的路径。

3.cd : 切换工作目录。

```Shell
cd /path/to/directory
```


4.mkdir : 创建新目录。

```Shell
mkdir directory_name
```

5.rmdir : 删除空目录。

```Shell
rmdir directory_name
```

6.rm : 删除文件或目录。

```Shell
rm file_name
```

7.cp : 复制文件或目录。

```Shell
cp source_file destination
cp -r source_directory destination
```

8.mv : 移动或重命名文件或目录。

```Shell
mv old_name new_name
```

9.touch : 创建空文件或更新文件的时间戳。

```Shell
touch file_name
```

10.cat : 连接和显示文件内容。

```Shell
cat file_name
```

11.more/less : 逐页显示文本文件内容。

```Shell
more file_name
less file_name
```
12.head/tail : 显示文件的前几行或后几行。

```Shell
head -n 10 file_name
tail -n 20 file_name
```

13.grep : 在文件中搜索指定文本。

```Shell
grep search_term file_name
```

14.ps : 显示当前运行的进程。

```Shell
ps aux
```

15.kill : 终止进程。

```Shell
kill process_id
```

16.ifconfig/ip:查看和配置网络接口信息。

```Shell
ifconfig
ip addr show
```

17.ping : 测试与主机的连通性。

```Shell
ping host_name_or_ip
```

18.wget/curl : 从网络下载文件。

```Shell
wget URL
culr -0 URL
```

19.chmod : 修改文件或目录的权限。

```Shell
chmod permissions file_name
```

20.chown : 修改文件或目录的所有者。

```Shell
chown owner:group file_name
```
 
21.tar : 用于压缩和解压文件和目录。

```Shell
tar -czvf archive.tar.gz directory_name 
tar -xzvf archive.tar.gz 
```

22.df/du : 显示磁盘使用情况。

```Shell
df -h
du -h directory_name
```
23.mount/umount : 挂载和卸载文件系统。

```Shell
mount /dev/sdX1 /mnt 
umount /mnt
```

24.psql/mysql : 用于与PostgreSQL或MySQL数据库交互的命令行工具。

```Shell
psql -U  username -d database_name
mysql -u username -p
```

25.top/htop : 显示系统资源的实时使用情况和进程信息。

```Shell
top
htop
```

26.ssh : 远程登陆到其他计算机。

```Shell
ssh username@remote_host
```

27.scp : 安全地将文件从本地复制到远程主机，或从远程主机复制到本地。

```Shell
scp local_file remote_user@remote_host:/remote/directory
```

28.find : 在文件系统中查找文件和目录。

```Shell
find /path/to/search -name "file_pattern"
```

29.grep : 在文本中搜索匹配的行，并可以使用正则表达式进行高级搜索。

```Shell
grep -r "pattern" /path/to/search
```

30.sed : 流编辑器，用于文本处理和替换。

```Shell
sed 's/old_text/new_text/' file_name
```

31.awk : 用于文本处理和数据提取的文本处理工具。

```Shell
awk '{print $1}' file_name
```

32.ssh-keygen : 生成SSH密钥对，用于身份验证远程服务器。

```Shell
ssh-keygen -t rsa
```

33.date : 显示或设置系统日期和时间。

```Shell
date
```

34.echo : 将文本输出到标准输出。

```Shell
echo "Hello, World!"
```

35.ln : 创建硬连接或符号连接。

```Shell
ln source_file link_name
ln -s source_file link_name
```

36.uname : 显示系统信息。

```Shell
uname -a
```

37.shoutdown/reboot : 关闭或重新启动系统。

```Shell
shoutdown -h now
reboot
```

38.who/w : 显示当前登陆的用户信息。

```Shell
who
w
```

39.curl : 用于与网络资源进行交互，支持各种协议。

```Shell
curl -X GET http://example.com
```

40.zip/unzip : 用于解压ZIP文件。

```Shell
zip archive.zip file1 file2
unzip archive.zip
```

41.useradd/userdel : 用于添加和删除用户账户。

```Shell
useradd new_user
userdel username
```

42.passwd : 更改用户密码。

```Shell
passwd username
```

43.cron : 定时任务管理器，用于自动执行计划任务。

```Shell
crontab -e
```

44.uptime : 显示系统的运行时间和负载情况。

```Shell
uptime
```

45.hostname : 显示设置计算机的主机名。

```Shell
hostname
```

46.iptables/ufw : 用于配置防火墙规则。

```Shell
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
ufw unable
```

47.netstat/ss : 显示网络连接信息。
 netstat -tuln
ss -tuln
```

48.history : 查看命令历史记录。

```Shell
history
```

49.free : 显示系统内存使用情况。

```Shell
free
```

50.lsblk/fdisk : 查看磁盘分区信息和管理磁盘。

```Shell
lsblk
fdisk /dev/sdX
```

51.nc : 用于网络连接测试和数据传输。

```Shell
nc -vz host_name_or_ip port
```

52.stat : 显示文件或目录的详细信息。

```Shell
stat file_or_directory
```

53.nmcli : 用于管理网络连接的命令行工具

```Shell
nmcli connection show
```
54.tailf : 实时追踪文件的末尾，类似于tail-f

```Shell
tailf file_name
```

55.scp : 安全的将文件从本地复制到远程主机，或从远程主机复制到本地。

```Shell
scp local_file remote_user@remote_host:/remote/directory
scp remote_user@remote_host:/remote/file local_directory
```

56.rsync : 用于在本地和远程系统之间同步文件和目录。

```Shell
rsync -avz source_directory/ remote_user@remote_host:/remote/directory
```

57.dd : 用于复制和转换文件。

```Shell
dd if=input_file of=output_file bs=block_size
```

58.sudo 以超级用户权限运行命令。

```Shell
sudo command_to_run_as_superuser
```

















