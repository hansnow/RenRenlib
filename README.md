RenRenlib使用说明
=========

人人有自己的官方API，而且已经升级到了所谓的2.0版，但是这类API一般都是非常难用的，首先是认证麻烦，需要申请一个应用，而且要填写很多资料。然后呢，官方没有提供Python API。所以小寒用自己的三脚猫功夫写了RenRenlib，用urllib2模拟登录的方法来实现大部分人人API的功能。
##功能概述

* 模拟登录，登录后可以获得Cookie，用于做其他事儿。
* 获取用户的所有状态、所有好友
* 通过状态ID对某条状态点赞和取消赞（后期会开发回复）
* 发出好友申请

还有很多功能可以实现，以后慢慢添加。

##TODO

* 获取某个好友信息
* 状态的回复
* 刚刚发现，目前只获取了status_id，还有share_id没有获取，而share_id貌似是html里面的
* 获取好友的好友信息


## 使用方法
将RenRenlib.py文件放到你的主程序目录下，然后 import RenRenlib 即可。
###功能解析
* `login(username,password)`
登录，该函数应该在所有函数执行之前执行，以便CookieJar能够获得以后操作所需的Cookie。该函数也返回当前登录用户的uid
* `get_status(ownerid)`
该函数回获取所有 *ownerid* 的status_id，并以每行一个的形式保存在程序所在目录的*status_ownerid.txt*文件中
* `like(status_id,uid,ownerid)`
点赞。uid为登录帐号的id，由login()函数获得。
* `removelike(status_id,uid,ownerid)`
取消赞。用法和上面的相同。（该函数还没经过测试）
* `addfriend(id = '',why = '')`
添加好友。该函数会向*id*发送好友请求，申请理由为why
* `get_friends()`
获取好友列表。将所有好友信息以json格式保存到当前目录下的*friends_info.json*文件下。

##丑话说在前头
作者很菜，开发出来的东西也很菜，如果发现问题请提交Issue或者直接Email：hansnow2012#gmail.com

enjoy~