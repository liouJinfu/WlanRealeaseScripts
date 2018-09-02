# --*-- coding:utf-8 --*--
import getpass, subprocess, os
from WlanRealeaseScripts.Excel import Excel_Test
def Get_Uer_LogInfo():
    name = input('请输入用户名：')
    passwd = getpass.getpass('请输入密码：')
    return (name, passwd)
_PATH = r'D:\\MyTestSvn\\'
# if __name__ == '__main__':
#     L = ['conf', 'db',  'Desktop.ini',  'format',  'hooks',  'locks',  'log',  'README.txt',  'svn.ico']
#     for x in L:
#         cu_path = os.path.join(_PATH, x)
#         cmd = r'svn commit %s -m %s'%(cu_path,"\"[commit log]xxxxaaaaaxxxx\"")
#         pro = subprocess.Popen(cmd,
#                                shell=True)
#         try:
#             outs, errs = pro.communicate(timeout=2)
#             print(outs, errs)
#         except TimeoutError:
#             print('out of time')
if __name__ == '__main__':
    Excel_Test()
