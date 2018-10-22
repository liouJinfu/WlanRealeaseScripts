# --*-- coding:utf-8 --*--
'''我的目标是：在WEB页面，实现语音输入时，根据语音的输出结果进行各种自己的日常操作，目前可以支持查看LIB 的日志记录，
支持发送WLAN的lib'''
import aiml,os
os.chdir('./alice') # 将工作区目录切换到刚才复制的alice文件夹
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')
if __name__ == '__main__':
    alice.respond("hello")
    print(alice.respond("what is your name ?"))