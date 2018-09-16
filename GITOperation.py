# --*-- coding:UTF-8 --*--
import subprocess,os
import xlwt,openpyxl
'''格式化log输出的集中方式 stackoverflow
    
down vote
accepted
to output to a file:

git log > filename.log
To specify a format, like you want everything on one line

git log --pretty=oneline >filename.log
or you want it a format to be emailed via a program like sendmail

git log --pretty=email |email-sending-script.sh
to generate JSON, YAML or XML it looks like you need to do something like:

git log --pretty=format:"%h%x09%an%x09%ad%x09%s"
'''
if __name__ == '__main__':
    _PATH = r'D:\scripts\WlanRealeaseScripts'
    sonDirs = os.listdir(_PATH)
    cmd = "git log --name-status --date=iso  --pretty=format:\"commit_id=%h; commitor=%cn; commit_date=%cd; contents=%s\" >log.txt"
    for dir in sonDirs:
        if os.path.isdir(dir):
            os.chdir(dir)
            os.system(cmd)
            print(dir)