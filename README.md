RenRenlib使用说明
=========

人人有自己的官方API，而且已经升级到了所谓的2.0版，但是这类API一般都是非常难用的，首先是认证麻烦，需要申请一个应用，而且要填写很多资料。然后呢，官方没有提供Python API。所以小寒用自己的三脚猫功夫写了RenRenlib，用urllib2模拟登录的方法来实现大部分人人API的功能。
##功能概述

* 模拟登录，登录后可以获得Cookie，用于做其他事儿。
* 获取用户的所有状态、所有分享、所有好友
* 通过状态ID对某条状态点赞和取消赞（后期会开发回复）
* 发出好友申请
* 20140414:所有函数已经包含在RenRen这个类中，调用更方便

还有很多功能可以实现，以后慢慢添加。

##TODO

* 获取某个好友信息
* 状态的回复(简单抓了一下包，难度有点大)
* share_id虽然取到了，但是效率很低(html中爬出来的)，不知道有没有json的接口



## 使用方法
示例代码：
`
import RenRenlib
username = raw_input('请输入邮箱：')
password = getpass.getpass('请输入密码（不会显示任何字符）：')
r = RenRenlib.RenRen(username,password)
r.get_status('12345678')
`
###功能解析

* `RenRen.get_status(ownerid)`
该函数回获取所有 *ownerid* 的status_id，并以每行一个的形式保存在程序所在目录的*status_[ownerid].txt*文件中
* `RenRen.like(status_id,ownerid)`
点赞。ownerid为对方ID
* `RenRen.removelike(status_id,uid,ownerid)`
取消赞。用法和上面的相同。（该函数还没经过测试）
* `RenRen.addfriend(id,why)`
添加好友。该函数会向*id*发送好友请求，申请理由为why
* `RenRen.get_mfriends()`
get my friends:获取好友列表。返回一个list，数据格式如下：`data[x]['fid']/['timepos']/['comf']/['compos']/['large_url']/['tiny_url']/['fname']/['info']/['pos']`。其中`fid`为好友id，`fname`为好友姓名，`large_url`为好友大头像，`tiny_url`为好友小头像，其他几项目前意义不明，如果大家发现了可以告诉我哦~
* `RenRen.get_ofriends(ownerid)`
get others friends:获取好友的好友列表。返回一个list，数据格式如下：`data[x]['id']/['netName']/['netNamePrefix']/['head']/['isOnLine']/['name']`。其中`id`为好友id，`netName`为好友的单位/所在城市信息，`netNamePrefix`为`netName`的类型，比如学校、城市等，`head`为小头像url，`isOnline`为是否在线，值为True/False，`name`为好友姓名。
* `RenRen.get_sfriends(ownerid)`
get share friends:获取共同好友列表。返回一个list，数据格式与`get_ofriends(ownerid)`完全相同。
* `RenRen.get_share(ownerid)`
获取分享。该函数和*get_status(ownerid)*结合可以获得owenrid的所有‘新鲜事儿’。share_id以每行一个的形式保存在程序所在目录的*share_[ownerid].txt*文件中

##更新记录
* 2014-04-13:完成大部分基础的功能函数
* 2014-04-14:所有函数包含在一个`RenRen`类中
* 2014-04-16:完成获取好友、共同好友、好友的好友功能


##丑话说在前头
作者很菜，开发出来的东西也很菜，如果发现问题请提交issue或者直接Email：hansnow2012#gmail.com

enjoy~