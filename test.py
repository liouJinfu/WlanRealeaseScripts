import getpass
name=input('请输入用户名')
pwd=getpass.getpass('请输入密码')
if name=='xiaoming' and pwd=='123':
    print("欢迎小明")
else:
    print("用户名或密码错误")