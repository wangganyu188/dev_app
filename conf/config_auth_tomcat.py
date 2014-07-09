#!/usr/bin/env python
#coding:utf8

from fabric.api import *
import re

nciphost = [
        "192.168.5.102",
        "192.168.5.103",
        ]

env.roledefs = {
'app':[],
}
env.passwords = {}

with open('/root/script/dev_app/conf/ippwd.txt','r') as f:
	for line in f.readlines():
 		for cv in nciphost:
				b = re.match(r'^%s .*' %cv,line,re.M|re.I)
				if b:
								c =  b.group()
								k = c.split()[0]
								v = c.split()[1]
#								print k, "\n", v
								nc='root@%s:22' %k
								env.roledefs['app'].append(nc)
								env.passwords[nc]=v

#print env.passwords,env.roledefs,






