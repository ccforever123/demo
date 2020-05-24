import adb

adb.system_ctrl('shell uiautomator dump /sdcard/app.uix')
adb.system_ctrl('pull /sdcard/app.uix D:\\android_dev\\app.uix')
adb.system_ctrl('shell rm /sdcard/app.uix')
adb.system_ctrl('shell screencap -p /sdcard/app.png')
adb.system_ctrl('pull /sdcard/app.png D:\\android_dev\\app.png')
adb.system_ctrl('shell rm /sdcard/app.png')