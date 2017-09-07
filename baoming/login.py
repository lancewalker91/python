#!/usr/bin/env python3
#-*- encoding: utf8 -*-

"""
    登陆
    """
import requests

g_login_url = "http://test.gn100.com/site.main/login"

def login(s, name, passwd):
    r = s.post(g_login_url, data={"uname":name, "password":passwd,"submit":"登录","areaCode":86,"cid":1,"areaId":86})
    r.encoding = "utf8"
    #print(s.cookies.get("test_uid"))	
    return  True, r
'''
    if "基础资料" in r.text and "我的订单" in r.text and "安全设置" in r.text and "退出" in r.text:
        return True, r
    else:
        if "基础资料"  not in r.text:
            print(1)
        if    "我的订单" not in r.text:
            print(2)
        if   "安全设置" not in r.text:
            print(3)
        if  "退出" not in r.text:
            print(4)
'''


if '__main__' == __name__:
    import argparse
    parser = argparse.ArgumentParser(description="login")
    parser.add_argument("user", type=str, help="用户名")
    parser.add_argument("passwd", type=str, help="密码")
    args = parser.parse_args()
    _, r = login(requests, args.user, args.passwd)
    print("response = [{}]".format(r.text))
