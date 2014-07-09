#!/usr/bin/python
#coding:utf-8

from fabric.api import *
from conf.config_auth_tomcat import *

get_app_packge = "wget -N -P /data/setup/  http://192.168.35.57/app/tomcat7_dev.tar.gz"
tomcatinstall = "cd /data/setup/; tar zxvf tomcat7_dev.tar.gz; sh install_tomcat.sh"

@roles('app')
def getapp():
	run(get_app_packge)
	run(tomcatinstall)

def dotask():
	execute(getapp)






