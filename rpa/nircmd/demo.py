import os
import nircmd


def main():
    exefile = '"D:\\documents\\git\\work\\好邻居\\采集台上传测试\\data\\main\\main.exe"'
    open_exe_file(exefile)

def open_exe_file(exefile):
    command = 'start "" {}'.format(exefile)
    os.system(command)
    print('{} file has been opened.'.format(exefile))


if __name__ == "__main__":
    # savePath = os.getcwd()
    # nircmd.save_screenshot_win(savePath)
    main()