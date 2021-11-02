# coding=utf-8
# @Time: 2021/11/1下午 4:32
# @Author: 马俊哲
# @Email:majunzhe04@163.com
# pip install redis #使用pip安装redis模块
import redis  # 导入 redis模块,通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

r = redis.Redis(host="192.168.117.22", port=6379, decode_responses=True, encoding="utf8")
# host是redis主机,需要redis服务端和客户端都启动 redis默认端口是6379
# encoding指定编码，默认是utf8。
# decode_responses，默认为False，如果是True，会以encoding方式解码，然后返回字符串。如果是字符串，就根据encoding编码成bytes
r.set("name", "mjz")
# key是"name" value是"mjz" 将键值对存入redis缓存
print(r["name"])
print(r.get("name")) #取出name对应的值
print(type(r.get("name"))) #查看类型