# -*- coding: encoding -*-
import time,os,sys


dest = svnconfig.Svn_Settings['dest']
svn  = svnconfig.Svn_Settings['svn']
os.chdir(svnconfig.Svn_Settings['svn'])
def checkout():
    svnconfig.Svn_Settings['dest'] = dest + time.strftime('%Y-%m-%d-%H0%M-%S', time.localtime())
    cmd = 'svn export %(url)s %(dest)s --username %(user)s --password %(passwd)s'%svnconfig.Svn_Settings
    print ('execute %s' % cmd)
    return os.system(cmd)

while True:
    ret = checkout()
    if(ret == 0):
        print ('check out success')
    else:
        print('checkout failed')
    time.sleep(svnconfig.Svn_Settings['interval'])

class svn():
    def __init__(self, svnApp):









