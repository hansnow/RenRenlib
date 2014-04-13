# -*- coding: utf-8 -*-
import sys
import base64
import os
import urllib
import urllib2
import cookielib
import re
import json
import time
reload(sys)
sys.setdefaultencoding('utf8')
"""
几个主要的功能函数：
    login(username,password) #登录，并把cookie保存在opener里（cookieJar已经安装为默认的opener）。该语句应该最先执行
    get_status(ownerid) #获取 ownerid 的所有状态id，并保存在同目录下的 status_[ownered].txt 文件中
    like(status_id) #对指定的状态id点赞
    removelike(status_id) #对指定的状态id取消赞
    addfriend(ownerid,why) #向指定的 ownerid 发出好友请求，申请理由为why
"""
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def get_status(ownerid):
    #return count and write status into status.txt
    f = open('status_.txt'+ownerid,'w')
    status_url = 'http://status.renren.com/GetSomeomeDoingList.do?userId='+ownerid+'&curpage=0'
    status_req = urllib2.Request(url=status_url)
    #status_req.add_header('Cookie',cookie)
    status_req.add_header('User-Agent',UA)
    status_json = urllib2.urlopen(status_req).read()
    status_list = json.loads(status_json)
    count = status_list['count']
    for page in range(0,count/20):
        status_url = 'http://status.renren.com/GetSomeomeDoingList.do?userId='+ownerid+'&curpage='+str(page)
        status_req = urllib2.Request(url=status_url)
        #status_req.add_header('Cookie',cookie)
        status_req.add_header('User-Agent',UA)
        status_json = urllib2.urlopen(status_req).read()
        status_list = json.loads(status_json)
        for item in status_list['likeMap']:
            f.write(item+'\n')
            print 'I have saved '+item+' in page'+str(page)
    f.close()

def like(status_id,uid,ownerid):
    req = urllib2.Request(url='http://like.renren.com/addlike?gid='+status_id+'&uid='+uid+'&owner='+ownerid)
    #req.add_header('Cookie',cookie)
    req.add_header('User-Agent',UA)
    json_doc = json.loads(urllib2.urlopen(req).read())
    if json_doc['likeCount']>0:
        print '对状态'+status_id+'点赞成功！'
    else:
        print '对状态'+status_id+'点赞失败！'
    

    # status_count = 
def main():
    login('hansnow2012@gmail.com','woshixhxh4291221')
    # get_status('465817176')
    addfriend()
    # ff = open('status_qiezi.txt','r')
    # status_id_list = ff.readlines()
    # for item in status_id_list:
    #     item = item.strip()
    #     like(item)
    #     time.sleep(240)
    
def login(username,password):
    data = urllib.urlencode({'email':username,
        'password':password,
        'icode':'',
        'origURL':'http://www.renren.com/home',
        'domain':'renren.com',
        'key_id':'1',
        'captcha_type':'web_login'})
    req = urllib2.Request(url='http://www.renren.com/PLogin.do',data=data)
    # req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36')
    response =urllib2.urlopen(req)
    uid = response.geturl().rpartition('/')[2]
    res = response.read()
    return uid
def addfriend(id = '422395300',why = ''):
    html_doc = urllib2.urlopen('http://www.renren.com').read()
    # print html_doc
    # requestToken 可能是负数
    requestToken = re.findall("get_check:'(.*?)'",html_doc)[0]
    _rtk = re.findall("get_check_x:'(\w+)'",html_doc)[0]
    print requestToken
    url = 'http://friend.renren.com/ajax_request_friend.do?from=Web_SG_AddFriendRec_addFriend_suggestion&'
    data = urllib.urlencode({'id':id,
        'why':why,
        'codeFlag':'0',
        'code':'',
        'requestToken':requestToken,
        '_rtk':_rtk})
    urllib2.urlopen(url=url,data=data)


if __name__ =='__main__':
    main()