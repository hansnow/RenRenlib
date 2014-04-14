# -*- coding: utf-8 -*-
import sys
import os
import urllib
import urllib2
import cookielib
import re
import json
import time
import getpass
from bs4 import BeautifulSoup
import chardet
reload(sys)
sys.setdefaultencoding('utf8')
"""
Author：Hansnow
Date：2014-04-14
"""
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'

class RenRen():
    #self的属性 uid requestToken _rtk
    def __init__(self):
        username = raw_input('请输入邮箱：')
        password = getpass.getpass('请输入密码（不会显示任何字符）：')
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        data = urllib.urlencode({'email':username,
            'password':password,
            'icode':'',
            'origURL':'http://www.renren.com/home',
            'domain':'renren.com',
            'key_id':'1',
            'captcha_type':'web_login'})
        req = urllib2.Request(url='http://www.renren.com/PLogin.do',data=data)
        # req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36')
        response = urllib2.urlopen(req)
        self.uid = response.geturl().rpartition('/')[2]
        html_doc = response.read()
        self.requestToken = re.findall("get_check:'(.*?)'",html_doc)[0]
        self._rtk = re.findall("get_check_x:'(\w+)'",html_doc)[0]

    def get_status(self,ownerid):
        #return count and write status into status.txt
        f_status = open('status_.txt'+ownerid,'w')
        status_url = 'http://status.renren.com/GetSomeomeDoingList.do?userId='+ownerid+'&curpage=0'
        status_req = urllib2.Request(url=status_url)
        #status_req.add_header('Cookie',cookie)
        status_req.add_header('User-Agent',UA)
        status_json = urllib2.urlopen(status_req).read()
        status_list = json.loads(status_json)
        count = status_list['count']
        for page in range(0,count/20+1):
            status_url = 'http://status.renren.com/GetSomeomeDoingList.do?userId='+ownerid+'&curpage='+str(page)
            status_req = urllib2.Request(url=status_url)
            #status_req.add_header('Cookie',cookie)
            #status_req.add_header('User-Agent',UA)
            status_json = urllib2.urlopen(status_req).read()
            status_list = json.loads(status_json)
            for item in status_list['likeMap']:
                f_status.write(item+'\n')
                print 'I have saved '+item+' in page'+str(page)
        f_status.close()

    def like(self,status_id,ownerid):
        req = urllib2.Request(url='http://like.renren.com/addlike?gid='+status_id+'&uid='+self.uid+'&owner='+ownerid)
        #req.add_header('Cookie',cookie)
        #req.add_header('User-Agent',UA)
        json_doc = json.loads(urllib2.urlopen(req).read())
        if json_doc['likeCount']>0:
            print '对状态'+status_id+'点赞成功！'
        else:
            print '对状态'+status_id+'点赞失败！'

    def removelike(self,status_id,ownerid):
        req = urllib2.Request(url='http://removelike.renren.com/addlike?gid='+status_id+'&uid='+self.uid+'&owner='+ownerid)
        #req.add_header('Cookie',cookie)
        req.add_header('User-Agent',UA)
        json_doc = json.loads(urllib2.urlopen(req).read())
        if json_doc['likeCount']>0:
            print '对状态'+status_id+'点赞成功！'
        else:
            print '对状态'+status_id+'点赞失败！'
    def addfriend(self,ownerid,why):
        url = 'http://friend.renren.com/ajax_request_friend.do?from=Web_SG_AddFriendRec_addFriend_suggestion&'
        data = urllib.urlencode({'id':ownerid,
            'why':why,
            'codeFlag':'0',
            'code':'',
            'requestToken':requestToken,
            '_rtk':_rtk})
        urllib2.urlopen(url=url,data=data)
    def get_friends():
        f_friends= open('friends_info.json','w')
        html_doc = urllib2.urlopen('http://friend.renren.com/groupsdata').read()
        string = html_doc.partition('"data" : ')[2]
        string = string.rpartition('}')[0]
        f_friends.write(string)
        # for i in string['friends']:
        # print i['fname']
        # print count
        # count+=1
        # print len(s['friends'])
    def get_share(self,ownerid):
        f_share = open('share_'+ownerid+'.txt','w')
        html_doc = urllib2.urlopen('http://share.renren.com/share/timeline/'+ownerid+'?curpage=0&type=0').read()
        soup = BeautifulSoup(html_doc)
        #这里find出来的是Unicode对象，所以一开始的时候总是不能搜索到,总感觉这里怪怪的
        num_span = soup.find(class_='pager-top clearfix').span.text.strip()
        share_num = int(re.findall(u'共(\d+)条',num_span)[0])
        for page in range(0,share_num/20+1):
            soup = BeautifulSoup(urllib2.urlopen('http://share.renren.com/share/timeline/'+ownerid+'?curpage='+str(page)+'&type=0').read())
            share_div = soup.find_all(class_='share-itembox')
            for every_div in share_div:
                f_share.write(every_div['id']+'\n')
                print 'I have saved share \''+every_div['id']+'\' in page'+str(page)
        f_share.close()

    # status_count = 
def main():
    r = RenRen()
    r.get_status('')
    # get_friends()
    # get_share('320072834')
    # reply()
    # get_status('465817176')
    # addfriend()
    # ff = open('status_qiezi.txt','r')
    # status_id_list = ff.readlines()
    # for item in status_id_list:
    #     item = item.strip()
    #     like(item)
    #     time.sleep(240)
    
# def login(username,password):
#     data = urllib.urlencode({'email':username,
#         'password':password,
#         'icode':'',
#         'origURL':'http://www.renren.com/home',
#         'domain':'renren.com',
#         'key_id':'1',
#         'captcha_type':'web_login'})
#     req = urllib2.Request(url='http://www.renren.com/PLogin.do',data=data)
#     # req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36')
#     response =urllib2.urlopen(req)
#     uid = response.geturl().rpartition('/')[2]
#     res = response.read()
#     return uid





# def reply():
    #这个函数有很大的问题，有时间再写
# # share_17128869901
#     html_doc = urllib2.urlopen('http://www.renren.com').read()
#     # print html_doc
#     # requestToken 可能是负数
#     requestToken = re.findall("get_check:'(.*?)'",html_doc)[0]
#     _rtk = re.findall("get_check_x:'(\w+)'",html_doc)[0]
#     #http://www.renren.com/profileLogger/send
#     data1 = urllib.urlencode({
#         'log':'[{"sourceTag":"default","actionTag":"load","targetTag":"timeline_feed_retrieve","needRecordRelation":true,"sendUserId":"483996204","getUserId":"320072834"},{"sourceTag":"default","actionTag":"load","targetTag":"timeline_feed_retrieve","needRecordRelation":true,"sendUserId":"483996204","getUserId":"320072834"},{"actionTag":"reply","sourceTag":"default","targetTag":"feed","sendUserId":"483996204","getUserId":"320072834","needRecordRelation":false}]',
#         'requestToken':requestToken,
#         '_rtk':_rtk
#         })
#     print urllib2.urlopen(url='http://www.renren.com/profileLogger/send',data=data1).read()
#     data2 = urllib.urlencode({
#         'c':'this is a test sent from Python',
#         'owner':'320072834',
#         'rpLayer':'0',
#         'source':'17128869901',
#         't':'5',
#         'requestToken':requestToken,
#         '_rtk':_rtk
#         })
#     urllib2.urlopen(url='http://status.renren.com/feedcommentreply.do?&ff_id=320072834',data=data2)

if __name__ =='__main__':
    main()