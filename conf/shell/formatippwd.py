#!/usr/bin/python

cs=['192.168.32.25','192.168.32.12','192.168.32.40']
iphost = {}
roledefs={
		'nagios-client':[],
		'nagios-server':[
			"root@192.168.31.96:22",
			],
}
passwords={}
with open('ippwd.txt','r') as f:
	for line in f.readlines():
		for cv in cs:
			k=line.split(" ")[0]
			v=line.split(" ")[1].strip("\n")
			if cv == k:
				nc='root@%s:22' %k
				roledefs['nagios-client'].append(nc)
				passwords[nc]=v
print roledefs,"\n", passwords,

