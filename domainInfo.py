#!usr/bin/python
# -*- coding:utf-8 -*-
import re
import requests

domain=raw_input("Please input domain you want to know:")
r = requests.get('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='+domain)
if re.findall(r'<original>210',r.text):
    print 'Domain name is available '
elif re.findall(r'<original>211',r.text):
    print 'Domain name is not available'
elif re.findall(r'<original>212',r.text):
    print 'Domain name is invalid'

r=requests.get('http://whois.chinaz.com/'+domain)
print '注册商'+re.findall(r'注册商(.*)<br/>',r.content)[0].replace("<br/>",'\n')


