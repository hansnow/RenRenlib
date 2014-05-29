# -*- coding: utf-8 -*-
from RenRenlib.base import RenRen
import getopt,sys,time,getpass
def main():
    opts,args = getopt.getopt(sys.argv[1:],"vhat:")
    username = ""
    password = ""
    for op,value in opts:
        if op == '-h':
            usage()
            sys.exit()
        elif op == '-v':
            print version
            sys.exit()
        elif op == '-a':
            f_auto = open('test_account.txt')
            account = f_auto.read()
            username = account.partition(':')[0].strip()
            password = account.partition(':')[2].strip()
        elif op == '-t':
            timeout = value
            # sys.exit()
    if username == "" and password == "":
        username = raw_input('请输入邮箱：')
        password = getpass.getpass('请输入密码（不会显示任何字符）：')
    print 'username:'+username
    print 'password:'+password
    r = RenRen(username,password)

    print r.uid
    print r.whoami()
    # r.get_share('465817176')
    # f = open('share_465817176.txt')
    # slist = f.readlines()
    # for i in slist:
    #     print r.like(i.strip(),'465817176')
    # r.get_status('438591664')
    # f = open('status_438591664.txt')
    # status_list = f.readlines()
    # for i in status_list:
    #     print r.like(i.strip(),'465817176')
    #     # time.sleep(1
    # r = RenRen(username,password)
    li = []
    for i in range(1,21):   
        li.append(r.lottery())
    for i in li:
        print r.use_lottery(i)
if __name__ == '__main__':
    main()
