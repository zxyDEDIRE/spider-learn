import time

from diskcache import Cache
# diskcache即基于磁盘的缓存  代表磁盘和文件支持的缓存

"""
创建缓存:
    set(key, value, expire=None, read=False, tag=None, retry=False)
    key和value分别代表缓存的key与缓存的值；
    expire表示过期时间，单位秒；
    read表示以二进制模式读取内容；
    tag表示与key值相关的文本；
    retry表示连接超时是否重试；
获取缓存:
    get(key, default=None,  expire_time=False, tag=False)
    key表示缓存的键值；
    default表示如果对应的键值没有，则返回这个default设置的默认值；
    Expire_time表示返回缓存的过期时间（从纪元开始的秒数）；
    tag表示返回与key值相关的文本；
更新缓存时间:
    touch(key, expire=None, retry=False)
    key表示缓存的键值；
    expire表示设置的过期时间；
    retry表示是否超时重试；
    值得注意的是如果已经过期的key值是设置不了的。
添加新的缓存:
    类似set方法，当且仅当key值不存在时，才会添加成功
delete/pop缓存删除:
    delete删除返回True或False，而pop删除返回缓存的值
"""

class Demo:
    def text_1(self):
        cache = Cache("C:\\Users\\tob\\Desktop\\test\\python_diskcache")
        cache.set('python', 'python学习', expire=60, read=True, tag="data", retry=True)
        getcache=cache.get('python',default='无',expire_time=True,tag=True)
        print(getcache)
        print(Get_Time(getcache[1]))
        result = cache.touch('python',expire=60)
        print(result)

    def text_2(self):
        cache = Cache("C:\\Users\\tob\\Desktop\\test\\python_diskcache")
        getcache = cache.get('python', default='无', expire_time=True, tag=True)
        cache.set('python',1,expire=60)
        # incr
        cache.incr('python',1)  # val+=1
        print(cache.get('python'))
        # decr
        cache.decr('python',4)  # val-=2
        print(cache.get('python'))

def Get_Time( t):
    Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
    return Time

if __name__ == '__main__':
    # Demo().text_1()
    Demo().text_2()
    # print(Get_Time(1669475268.2791812))
