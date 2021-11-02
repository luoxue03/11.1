# coding=utf-8
# @Time: 2021/11/1下午 5:24
# @Author: 马俊哲
# @Email:majunzhe04@163.com

# redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
# 可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池

import redis

pool = redis.ConnectionPool(host="192.168.117.22", port=6379, decode_responses=True)
# host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型
r = redis.Redis(connection_pool=pool)
r.set("gender", "male")
# key是"gender" value是"male" 将键值对存入redis缓存
print(r.get('gender'))
# gender 取出键male对应的值
