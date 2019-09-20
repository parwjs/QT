# Redis



![主流应用架构](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568820638616.png)



穿透查询：Redis缓存里面没有内容的时候会进入数据库进行查询。

---



缓存中间件一Memcache和Redis的区别

Memcache：代码层次类似Hash

+ 支持简单数据类型

+ 不支持数据持久化存储

+ 不支持主从

+ 不支持分片



Redis

+ 数据类型丰富

+ 支持数据磁盘持久化存储

+ 支持主从

+ 支持分片



----



为什么Redis能这么快

+ 完全基于内存，绝大部分请求是纯粹的内存操作，执行效率高
+ 数据结构简单，对数据操作也简单
+ 采用单线程，单线程也能处理高并发请求，想多核也可启动多实例
+ 使用多路I/O复用模型，非阻塞IO



多路I/O复用模型

FD：File Descriptor，文件描述符

一个打开的文件通过唯一的描述符进行引用，该描述符是打开文件的元数据到文件本身的映射

+ 传统的阻塞I/O模型

  

  ![传统的阻塞IVO模型](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568821276257.png)



+ 多路I/O复用模型

  + Select系统调用

  ![多路I/O复用模型](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568821389315.png)	





Redis采用的I/O多路复用函数：epoll/kqueue/evport/select？

+ 因地制宜
+ 优先选择时间复杂度为O(1)的I/0多路复用函数作为底层实现
+ 以时间复杂度为O(n)的select作为保底
+ 基于react设计模式监听I/O事件基于react设计模式监听I/O事件



---------



## Redis的数据类型

String：最基本的数据类型，二进制安全(最大能存储512M)

+ set name "redis"
+ get name
+ set count 1
+ get count
+ incr count  //增加1

Hash：String元素组成的字典，适合用于存储对象

+ hmset lilei name "lilei" age 26 title "Senior"
+ hget lilei age
+ hset lilei title "Pricipal"

List：列表，按照String元素插入顺序排序

+ lpush mylist aaa
+ lpush mylist bbb
+ lpush mylist ccc
+ lrange mylist 0 10 //取出数据，取出10条，先进后出



Set：String元素组成的无序集合，通过哈希表实现，不允许重复

+ sadd myset 111
+ sadd myset 222
+ sadd myset abc
+ smembers myset //打印出所有元素



Sorted Set：通过分数来为集合中的成员进行从小到大的排序

+ zadd myzset 3 abc
+ zadd myzset 1 abd
+ zadd myzset 3 acb
+  zrangebyscore myzset 0 10  //按照分数的大小排序输出



用于计数的HyperLogLog，用于支持存储地理位置信息的Geo





-------



底层数据类型基础

1.简单动态字符串
2.链表
3.字典
4.跳跃表
5.整数集合
6.压缩列表
7.对象



----------

## 海量数据

从海量Key里查询出某一固定前缀的Key

**留意细节**

+ 摸清数据规模，即问清楚边界
+ 



使用keys对线上的业务的影响

KEYS pattern：查找所有符合给定模式pattern的key

keys k1*  返回以k1开头的所有key

+ KEYS指令一次性返回所有匹配的key
+ 键的数量过大会使服务卡顿





SCAN cursor [MATCH pattern] [COUNT count]

scan 0 match k1* count 10  返回以k1开头的key，大体上返回10条，首先返回游标

scan 5242880 match k1* count 10 基于游标继续查询返回

+ 基于游标的迭代器，需要基于上一次的游标延续之前的迭代过程

+ 以0作为游标开始一次新的迭代，直到命令返回游标0完成一次遍历

+ 不保证每次执行都返回某个给定数量的元素，支持模糊查询
+ 一次返回的数量不可控，只能是大概率符合count参数



注：scan查询返回的值中可能出现重复值，可以在Java程序中设置HashSet，每次查询出来的key，存入HashSet进行去重。



---

## Redis分布式锁

分布式锁需要解决的问题

+ 互斥性
+ 安全性
+ 死锁
+ 容错



如何通过Redis实现分布式锁

SETNX key value：如果key不存在，则创建并赋值

setnx locknx test

+ 时间复杂度：O(1)
+ 返回值：设置成功，返回1；设置失败，返回0



如何解决SETNX长期有效的问题

EXPIRE key seconds

+ 设置key的生存时间，当key过期时（生存时间为0），会被自动删除

  expiire locknx 2

+ 缺点：原子性得不到满足



SET key value [EX seconds ] [PX milliseconds] [NX | XX]

set locktarget 12345 ex 10 nx

set locktarget 888 ex 10 xx

+ EX second：设置键的过期时间为second秒
+ PX millisecond：设置键的过期时间为millisecond 毫秒
+ NX：只在键不存在时，才对键进行设置操作
+ XX：只在键已经存在时，才对键进行设置操作SET操作成功完成时，返回OK，否则返回nil



大量的key同时过期的注意事项

集中过期，由于清除大量的key很耗时，会出现短暂的卡顿现象

+ 解放方案：在设置key的过期时间的时候，给每个key加上随机值



如何使用Redis做异步队列

使用List作为队列，RPUSH生产消息，LPOP消费消息

+ 缺点：没有等待队列里有值就直接消费
+ 弥补：可以通过在应用层引入Sleep机制去调用LPOP重试



BLPOP key[key..J timeout：阻塞直到队列有消息或者超时

blpop mylist 30  等待mylist生产数据，只等待30秒，没有数据就会阻塞

+ 缺点：只能供一个消费者消费



pub/sub：主题订阅者模式

+ 发送者（pub）发送消息，订阅者（sub）接收消息
+ 订阅者可以订阅任意数量的频道

![pub/sub](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568950519221.png)





1. 监听频道：subscribe myTopic
2. 发布频道信息：publish myTopic "Hello"



**注：消息的发布是无状态的，无法保证可达**



---



## Redis如何做持久化



RDB（快照）持久化：保存某个时间点的全量数据快照

+ SAVE：阻塞Redis的服务器进程，直到RDB文件被创建完毕(Redis一般是一个进程，所以一般不会使用save方法)

save

+ **BGSAVE:Fork出一个子进程来创建RDB文件，不阻塞服务器进程**

bgsave

会生成dump.rdb文件，可以设置程序进行控制生成dumpxxxxx.rdb文件





自动化触发RDB持久化的方式

+ 根据redis.conf配置里的SAVEmn定时触发（用的是BGSAVE）
+ 主从复制时，主节点自动触发
+ 执行Debug Reload
+ 执行Shutdown且没有开启AOF持久化



![BGSAVE原理](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568951777167.png)





Copy-on-Write

如果有多个调用者同时要求相同资源（如内存或磁盘上的数据存储），他们会共同获取相同的指针指向相同的资源，直到某个调用者试图修改资源的内容时，系统才会真正复制一份专用副本给该调用者，而其他调用者所见到的最初的资源仍然保持不变





缺点：

+ 内存数据的全量同步，数据量大会由于I/O而严重影响性能
+ 可能会因为Redis挂掉而丢失从当前至最近一次快照期间的数据





AOF（Append-Only-File）持久化：保存写状态

+ 记录下除了查询以外的所有变更数据库状态的指令
+ 以append的形式追加保存到AOF文件中（增量）



日志重写解决AOF文件大小不断增大的问题，原理如下：

+ 调用fork（），创建一个子进程
+ 子进程把新的AOF写到一个临时文件里，不依赖原来的AOF文件
+ 主进程持续将新的变动同时写到内存和原来的AOF里
+ 主进程获取子进程重写AOF的完成信号，往新AOF同步增量变动
+ 使用新的AOF文件替换掉旧的AOF文件



RDB和AOF文件共存情况下的恢复流程

![RDB与AOF共存](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568989971572.png)

RDB和AOF的缺点

+ RDB优点：全量数据快照，文件小，恢复快
+ RDB缺点：无法保存最近一次快照之后的数据
+ AOF优点：可读性高，适合保存增量数据，数据不易丢失
+ AOF缺点：文件体积大，恢复时间长



RDB-AOF混合持久化方式

+ BGSAVE做镜像全量持久化，AOF做增量持久化



---------



## Pipeline

+ Pipeline与Linux的管道类似
+ Redis基于请求/响应模型，单个请求处理需要一一应答
+ Pipeline批量执行指令，节省多次I0往返的时间
+ 有顺序依赖的指令建议分批发送



## Redis的同步机制

主从同步原理

+ Salve发送sync命令到Master
+  Master启动一个后台进程，将Redis中的数据快照保存到文件中
+ Master将保存数据快照期间接收到的写命令缓存起来
+ Master完成写文件操作后，将该文件发送给Salve
+ 使用新的AOF文件替换掉旧的AOF文件
+ Master将这期间收集的增量写命令发送给Salve端



增量同步过程

+ Master接收到用户的操作指令，判断是否需要传播到Slave
+ 将操作记录追加到AOF文件
+ 将操作传播到其他Slave：1、对齐主从库；2、往响应缓存写入指令
+ 将缓存中的数据发送给Slave



## Redis Sentinel

解决主从同步Master宕机后的主从切换问题：

+ 监控：检查主从服务器是否运行正常
+ 提醒：通过API向管理员或者其他应用程序发送故障通知
+ 自动故障迁移：主从切换



## 流言协议Gossip

在杂乱无章中寻求一致

+ 每个节点都随机地与对方通信，最终所有节点的状态达成一致
+ 种子节点定期随机向其他节点发送节点列表以及需要传播的消息
+ 不保证信息一定会传递给所有节点，但是最终会趋于一致





------



## Redis的集群原理

+ 分片：按照某种规则去划分数据，分散存储在多个节点上
+ 常规的按照哈希划分无法实现节点的动态增减

一致性哈希算法：对2^32取模，将哈希值空间组织成虚拟的圆环

将数据key使用相同的函数Hash计算出哈希值

![1568991243654](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1568991243654.png)



Hash环的数据倾斜问题

+ 引入虚拟节点解决数据倾斜的问题

