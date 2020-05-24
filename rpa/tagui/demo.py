import rpa as r


def main():
    r.init()
    r.url('https://www.hattrick.org/zh/')
    r.type('ctl00_CPContent_ucLogin_txtUserName', 'ccforever')
    r.type('ctl00_CPContent_ucLogin_txtPassword', 'cc0323')
    r.click('ctl00_CPContent_ucLogin_butLogin')
    r.wait('10')
    r.click('myClubLink')
    # r.wait(5)
    # r.close()




if __name__ == "__main__":
    main()