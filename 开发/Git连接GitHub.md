# 目录

### [安装Git](#安装Git)

### [向GitHub连接上传](#向GitHub连接上传)

### [排错修改](#遇到的错误)

---

#### 安装Git

1. 官网下载安装包[Git - Downloading Package (git-scm.com)](https://git-scm.com/download/win)

2. 安装步骤

   * ![](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101110500849.png)
   * ![](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101110529575.png)

   其余直接下一步

#### 向GitHub连接上传

1. 创建本地仓库

   1. 切换至要作为本地仓库的目录

      ```bash
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~
      $ cd Desktop/github/
      ```

   2. 创建本地仓库

      ```bash
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ git init
      ```

2. 上传文件

   1. 将文件存入暂存区

      ```bash
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ git add annotation.ipynb
      ```

   2. 上传文件

      ```bash
      #设置用户名和邮箱
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ git config --global user.name "mjz"
      
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ git config --global user.email "1355440906@qq.com"
      #上传 后面是标签
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ git commit -m "first"
      ```

3. 创建ssh公钥 连接github

   1. 创建公钥

      ```bash
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ ssh-keygen.exe
      #直接执行这个命令
      Generating public/private rsa key pair.
      Enter file in which to save the key (/c/Users/Luoxue/.ssh/id_rsa):
      /c/Users/Luoxue/.ssh/id_rsa already exists.
      Overwrite (y/n)? y
      #下面直接回车
      Enter passphrase (empty for no passphrase):
      Enter same passphrase again:
      Your identification has been saved in /c/Users/Luoxue/.ssh/id_rsa
      Your public key has been saved in "/c/Users/Luoxue/.ssh/id_rsa.pub" #这里引起来的是文件所在位置
      The key fingerprint is:
      SHA256:QWiRCjaJvAHqLHykiwPSMf3oohe7yNfQMc8mI/Sg11s Luoxue@DESKTOP-7DOR1V6
      The key's randomart image is:
      +---[RSA 3072]----+
      |+. .  .+.        |
      |oo=.  +.         |
      |..=+.o  .        |
      |+oo=.=   .       |
      |+=+.* * S        |
      |=.+= * E         |
      |o.oo= *          |
      |.+oo o           |
      |ooo.             |
      +----[SHA256]-----+
      ```

   2. 打开文件查看公钥

      ```bash
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/Desktop/github (master)
      $ cd /c/Users/Luoxue/.ssh/
      
      Luoxue@DESKTOP-7DOR1V6 MINGW64 ~/.ssh
      $ cat id_rsa.pub # 查看公钥内容
      "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXXY5TXRerxNYsbxtD/8QYmp5KWKLt6bIjproSwMUfzwo/tkzzaYOXcJ9Fz2Rf3Y/Q3PGZE8WNH7RsW6ycOZi3LBDKquGbfBGR0F69BTQO58QJxm72hp7VTmIh1ZXhh00tBx8iK5FTr7oAmSaSOSsaPOtfnIVSQakThAXE+F3T8O2gCC6vUzJRO/9QIgCe1LFfrLqJx5HzwzV1MDoVBDP0wlNOZlJ+DaBnPJkjz946/ZJojsCc0SfMMZD2nr9l+oPx10s1u/62F2laP6Ud8NHB8NT1gfGiZN0Sv+YkR1x9M/JI+vCBgSv3Y93zCOwmjM0/ZKze7wvjr7Rl67jVVzfFPBqrtcQY6Udsi77jpJWDYX/sZyTJhld+Iw3yrn87yCzg4mqp+EjEnvPi6mnM5u+b0OkCIp8C0huCpjXk4LOkTQjoVgFa55FIhQZK++oTV1VNdDIjYq1e6ekpW2yZlkbJRSYzKvvpeDhqVfj5pzOjhmWA1DJLsrVbwGJSpv0rKLE= Luoxue@DESKTOP-7DOR1V6"
      #引起来的是需要复制的
      ```

   3. github添加ssh公钥

      <img src="C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101112040540.png" alt="image-20211101112040540" style="zoom: 67%;" />

      <img src="C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101112106924.png" alt="image-20211101112106924" style="zoom:67%;" />

      ![image-20211101112130385](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101112130385.png)

      ![image-20211101112215263](C:\Users\Luoxue\Desktop\微服务Typory\图片\image-20211101112215263.png)

   4. 连接github

      1. 添加远程仓库

         ```bash
         ssh -T git@github.com #使用ssh连接至github远程仓库
         
         git remote add  origin       git@github.com:luoxue03/11.1.git
         #命令区          #远程仓库别名  #git@远程仓库地址:用户名/仓库名.git
         ```

      2. 同步本地仓库到远程仓库

         ```bash
         git push -u origin master
         #命令        #仓库名 本地仓库名
         ```

      3. 查看github即可

#### 遇到的错误

   遇到错误

   * error: src refspec master does not match any

     > 解决方法:本地仓库没有代码文件，上传为空。在本地仓库上传文件即可
     >
     > [github上传时出现error: src refspec master does not match any解决办法 - 简书 (jianshu.com)](https://www.jianshu.com/p/8d26730386f3)
     
* fatal: not a git repository (or any of the parent directories): .git

  > 解决方法:目录未在本地仓库,无法上传
  >
  > [解决 fatal: Not a git repository (or any of the parent directories): .git 问题_wenb1bai的博客-CSDN博客](https://blog.csdn.net/wenb1bai/article/details/89363588) 
