# Redis 安装

1. 下载软件包

   找到redis官网，下载最新软件包[Redis官网下载](https://redis.io/download)

   ![image-20211101145703590](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101145703590.png)

2. 安装redis 根据官方文档[重新开始快速 - 重新 (redis.io)](https://redis.io/topics/quickstart)

   1. 将下载的Redis安装包拖入虚拟机中

      ![image-20211101150530540](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101150530540.png)

   2. 解压安装redis

      ```bash
      [root@localhost ~]# tar -zxvf redis-6.2.6.tar.gz 
      ```

      ![image-20211101150952168](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101150952168.png)

      ```bash
      [root@localhost ~]# ls
      anaconda-ks.cfg       redis-6.2.6.tar.gz   模板  文档  桌面
      initial-setup-ks.cfg  redis-stable.tar.gz  视频  下载
      redis-6.2.6           公共                 图片  音乐
      [root@localhost ~]# cd redis-6.2.6/
      [root@localhost redis-6.2.6]# make
      ```

      ![image-20211101151428850](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101151428850.png)

   3. 将命令创建软链接

      ```bash
      [root@localhost redis-6.2.6]# sudo cp src/redis-server  /usr/local/bin/
      [root@localhost redis-6.2.6]# sudo cp src/redis-cli  /usr/local/bin/
      ```

   4. 启动redis

      ```bash
      root@localhost redis-6.2.6]# redis-server 
      ```

      ![image-20211101153404851](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101153404851.png)

      > 错误1
      >
      > ```bash
      > 16164:M 01 Nov 2021 15:38:11.205 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
      > 16164:M 01 Nov 2021 15:38:11.205 # Server initialized
      > 16164:M 01 Nov 2021 15:38:11.205 * Loading RDB produced by version 6.2.6
      > 16164:M 01 Nov 2021 15:38:11.205 * RDB age 164 seconds
      > 16164:M 01 Nov 2021 15:38:11.205 * RDB memory usage when created 0.77 Mb
      > 16164:M 01 Nov 2021 15:38:11.205 # Done loading RDB, keys loaded: 0, keys expired: 0.
      > 16164:M 01 Nov 2021 15:38:11.205 * DB loaded from disk: 0.000 seconds
      > 16164:M 01 Nov 2021 15:38:11.205 * Ready to accept connections
      > ```
      >
      > ```bash
      > 16051:M 01 Nov 2021 15:33:31.458#警告：无法强制执行TCP积压设置511，因为/proc/sys/net/core/somaxconn被设置为较低的值128。
      > 
      > 16051:M 01 Nov 2021 15:33:31.458#服务器已初始化
      > 
      > 16051:M 01 Nov 2021 15:33:31.458 35;警告超限#内存设置为0！在内存不足的情况下，后台保存可能会失败。要解决此问题，请将“vm.overmit_memory=1”添加到/etc/sysctl.conf，然后重新启动或运行命令“sysctl vm.overmit_memory=1”，使其生效。
      > 
      > 16051:M 01 Nov 2021 15:33:31.459*准备接受连接
      > 
      > ^C16051:信号处理程序（1635752127）收到SIGINT计划关闭。。。
      > 
      > 16051:M 01 Nov 2021 15:35:27.944 35;用户请求关机。。。
      > 
      > 16051:M 01 Nov 2021 15:35:27.944*退出前保存最终RDB快照。
      > 
      > 16051:M 01 Nov 2021 15:35:27.945*DB保存在磁盘上
      > 
      > 16051:M 01 Nov 2021 15:35:27.945#Redis现在准备退出，再见。。。
      > ```
      >
      > 出现内存设置问题，根据redis报错提示
      >
      > 将参数“vm.overmit_memory=1”添加到/etc/sysctl.conf，然后重新启动或运行命令“sysctl vm.overmit_memory=1”，使其生效。

   5. 将redis后台启动

      ```bash
      [root@localhost redis-6.2.6]# redis-server &
      ```

   6. 测试redis连接

      ```bash
      [root@localhost redis-6.2.6]# redis-cli ping
      PONG
      ```

      ![image-20211101154351825](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101154351825.png)

3. 配置redis的配置文件

   1. 关闭redis

      ```bash
      [root@localhost redis-6.2.6]# redis-cli shutdown
      16278:M 01 Nov 2021 15:49:39.438 # User requested shutdown...
      16278:M 01 Nov 2021 15:49:39.438 * Saving the final RDB snapshot before exiting.
      16278:M 01 Nov 2021 15:49:39.708 * DB saved on disk
      16278:M 01 Nov 2021 15:49:39.708 # Redis is now ready to exit, bye bye...
      [1]+  完成                  redis-server
      ```

      ![image-20211101154949689](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101154949689.png)

   2. 创建存储 Redis 配置文件和数据的目录

      ```bash
      [root@localhost ~]# cd
      [root@localhost ~]# sudo mkdir /etc/redis
      [root@localhost ~]# sudo mkdir /var/redis
      ```

   3. 将在utils目录下的Redis发行版中找到的init脚本复制到/etc/init.d中。我们建议使用运行此Redis实例的端口名来调用它

      ```bash
      [root@localhost ~]# cd redis-6.2.6/
      [root@localhost redis-6.2.6]# sudo cp utils/redis_init_script /etc/init.d/redis_6379
      ```

   4. 编辑初始化脚本

      ```bash
      sudo vim /etc/init.d/redis_6379
      ```

      ![image-20211101155531389](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101155531389.png)

      端口号默认为6379 不用修改

   5. 使用端口号作为名称，将Redis发行版根目录中的模板配置文件复制到/etc/Redis/中

      ```bash
      sudo cp redis.conf /etc/redis/6379.conf
      ```

   6. 在/var/redis内创建一个目录，该目录将用作此redis实例的数据和工作目录

      ```bash
      sudo mkdir /var/redis/6379
      ```

   7. 编辑配置文件,确保执行以下更改:

      - 将daemonize设置为yes（默认情况下设置为no）
      - 将pidfile设置为（根据需要修改端口）/var/run/redis_6379.pid`
      - 相应地更改端口。在我们的示例中，不需要它，因为默认端口已经是6379
      - 设置您的首选日志级别。
      - 将日志文件设置为`/var/log/redis_6379.log`
      - 将dir设置为/var/redis/6379（非常重要的一步！）

      > Edit the configuration file, making sure to perform the following changes:
      > - Set **daemonize** to yes (by default it is set to no).
      > - Set the **pidfile** to (modify the port if needed).`/var/run/redis_6379.pid`
      > - Change the **port** accordingly. In our example it is not needed as the default port is already 6379.
      > - Set your preferred **loglevel**.
      > - Set the **logfile** to `/var/log/redis_6379.log`
      > - Set the **dir** to /var/redis/6379 (very important step!)

      1. 进入配置文件

      ```bash
      [root@localhost redis-6.2.6]# vim /etc/redis/6379.conf
      ```

      8. 修改配置文件

      2. 使用搜索,搜索需要更改的配置项

         ![image-20211101160319846](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101160319846.png)

         ![image-20211101160336306](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101160336306.png)

         ```bash
         257 daemonize yes #257行的此配置项 更改为yes
         ```

      3. 修改pidfile文件位置

         ```bash
         289 pidfile /var/run/redis_6379.pid
         ```

      4. 修改日志级别

         ```bash
         297 loglevel notice
         ```

      5. 修改日志文件位置

         ```bash
         302 logfile "/var/log/redis_6379.log"
         ```

      6. 修改目录位置

         ```bash
         454 dir /var/redis/6379
         ```

      7. 修改默认IP

          ```bash
          75 bind 192.168.117.22
          ```

   8. 使用以下命令将新的Redis init脚本添加到所有默认运行级别(设置开机自启动)

      ```bash
      [root@localhost redis-6.2.6]# systemctl enable redis_6379
      redis_6379.service is not a native service, redirecting to /sbin/chkconfig.
      Executing /sbin/chkconfig redis_6379 on
      ```
      
     9. 启动redis

           ```bash
           [root@localhost redis-6.2.6]# sudo /etc/init.d/redis_6379 start
           Starting Redis server...
           ```

    10. 关闭,开启,连接数据库

      ```bash
      [root@localhost redis-6.2.6]# redis-cli -h 192.168.117.22 shutdown
      
      [root@localhost redis-6.2.6]# sudo /etc/init.d/redis_6379 start
      Starting Redis server...
      
      [root@localhost redis-6.2.6]# redis-cli -h 192.168.117.22 -p 6379
      192.168.117.22:6379> 
      ```

   8. 测试方法

      确保一切按预期进行：

      - 尝试使用redis cli ping您的实例
      - 使用redis cli save执行测试保存，并检查转储文件是否正确存储到/var/redis/6379/（您应该找到一个名为dump.rdb的文件）.
      - 检查您的Redis实例是否正确地登录到日志文件中.
      - 如果这是一台新机器，您可以毫无问题地试用它，请确保在重新启动后，一切仍然正常。