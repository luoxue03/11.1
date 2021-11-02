# coding=utf-8
# @Time: 2021/11/1下午 5:33
# @Author: 马俊哲
# @Email:majunzhe04@163.com
import redis

# set(name, value, ex=None, px=None, nx=False, xx=False)
#
# 在Redis中设置值，默认，不存在则创建，存在则修改
# 参数：
# ex，过期时间（秒）
# px，过期时间（毫秒）
# nx，如果设置为True，则只有name不存在时，当前set操作才执行
# xx，如果设置为True，则只有name存在时，当前set操作才执行

# 1.ex,过期时间(秒)这里过期时间是3秒,3秒后,键fiid的值就变成了None
pool = redis.ConnectionPool(host='192.168.117.22', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('food', 'mutton', ex=3)  # key是"food" value是"mutton" 将键值对存入redis缓存
print(r.get("food"))  # mutton 取出键food对应的值

# 2.px,过期时间(毫秒)这里过期时间是3毫秒,3毫秒后,键foo的值就变成None
r = redis.Redis(connection_pool=pool)
r.set('food', 'beef', px=3)
print(r.get("food"))

# 3.nx,如果设置为True,则只有name不存在时,当前的set操作才执行(新建)
r = redis.Redis(connection_pool=pool)
print(r.set('fruit', 'watermelon', nx=True))  # True--不存在
# 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None
print(r.get("fruit"))

# 4.xx,如果设置为True,则只有name存在时,当前的set操作才执行(修改)
print((r.set('fruit', 'new_watermelon', xx=True)))   # True--已经存在
# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None
print(r.get("fruit"))