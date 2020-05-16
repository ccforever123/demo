import itchat

def get_msg():
    itchat.send('这是一个测试', toUserName='filehelper')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)                  # hotReload = True, 保持在线，下次运行代码可自动登录
    itchat.run()
    get_msg()