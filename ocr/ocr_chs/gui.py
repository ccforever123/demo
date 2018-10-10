import tkinter as tk
import sys, os
from tkinter import messagebox
import ocr_chs
import threading
import inspect
import ctypes
from tkinter.filedialog import askdirectory

class APP:
    def __init__(self, master):

        self.master = master
        self.version = '1.1'
        self.update_info = '=============changelog 1.1=============\n' \
                           '1、添加选择图片文件夹功能' \
                           '2、禁用直接输入目录导致生成txt文件夹异常的bug' \
                           '\n' \
                           '=============changelog 1.0=============\n' \
                           '1、实现基本OCR识别功能'
        master.title('扫描图像OCR工具V{}    By 松鼠男'.format(self.version))
        master.geometry('550x300')

        # set menu bar
        self.menubar = tk.Menu(master)

        file_menu = tk.Menu(self.menubar)
        file_menu.add_command(label='版本信息', command=self.update)
        self.menubar.add_cascade(label='关于', menu=file_menu)

        master['menu'] = self.menubar

        self.show_path(master)
        self.start_button(master)
        self.output_text = tk.StringVar()
        self.output_text.set('')
        self.list = []
        self.l = tk.Text(master, width=72, height=13)
        self.l.grid(row=3, padx=5, pady=5, columnspan=3)

    def update(self):
        messagebox.showinfo('扫描图像OCR工具V{}更新信息'.format(self.version), self.update_info)

    def show_path(self, master):
        tk.Label(text='当前路径：').grid(row=0, column=0, padx=5,pady=5)
        self.pic_path = tk.StringVar()
        self.pic_path.set(os.getcwd())
        current_pic_path = tk.Entry(master, textvariable=self.pic_path, width=50, state='disabled')
        current_pic_path.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(master, text='选择目录', command=self.select_pic_path, width=10, height=1).grid(row=0, column=2, padx=5, pady=5)


        tk.Label(text='输出路径：').grid(row=1, column=0, padx=5, pady=5)
        self.output_path = tk.StringVar()
        self.output_path.set(os.path.join(os.getcwd(), 'txt'))
        current_output_path = tk.Entry(master, textvariable=self.output_path, width=50, state='disabled')
        current_output_path.grid(row=1, column=1, padx=5, pady=5)
        # tk.Button(master, text='选择目录', command=self.select_output_path, width=10, height=1).grid(row=1, column=2, padx=5, pady=5)

    def select_pic_path(self):
        path_ = askdirectory()
        self.pic_path.set(path_)
        self.output_path.set(os.path.join(path_, 'txt'))


    # def select_output_path(self):
    #     path_ = askdirectory()
    #     self.output_path.set(path_)

    def start_button(self, master):
        self.start = tk.Button(master, text='开始', command=self.run, width=10, height=1, state='normal')
        self.start.grid(row=2, column=1, columnspan=2, padx=100, sticky='E')
        self.stop = tk.Button(master, text='停止', command=self.pause, width=10, height=1, state='disabled')
        self.stop.grid(row=2, column=1, columnspan=2, padx=5, sticky='E')

    def run(self):
        self.start['state'] = 'disabled'
        self.stop['state'] = 'normal'
        try:
            if os.path.isdir(self.output_path.get()) == False:
                os.mkdir(self.output_path.get())
            self.t = threading.Thread(target=self.run_ocr, args=())
            self.t.start()
        except Exception as e:
            self.output_text_update(e)

    def run_ocr(self):
        pic_path = self.pic_path.get()
        pic_list = self.get_files(pic_path)
        for pic in pic_list:
            self.output_text_update('-> 正在读取图片：{}\n'.format(pic))
            ocr_chs.get_text(pic_path, pic)
            self.output_text_update('√ 已完成识别：{}\n'.format(pic))
        self.output_text_update('☆ 已完成所有图片识别！ ☆\n')

    def output_text_update(self, txt):
        self.output_text.set(txt)
        self.l.insert(1.0, self.output_text.get())

    def get_files(self, pic_path):
        pic_list = []
        for parent, dirnames, filenames in os.walk(pic_path):
            if parent == os.path.join(os.getcwd(), 'output'):
                break
            for filename in filenames:
                if filename[-3:] in ['bmp', 'jpg', 'BMP', 'JPG']:
                    pic_list.append(filename)
        return pic_list

    def pause(self):
        self.start['state'] = 'normal'
        self.stop['state'] = 'disabled'
        self.stop_thread(self.t)
        self.output_text.set('× OCR已停止！\n')
        self.l.insert(1.0, self.output_text.get())

    def _async_raise(self, tid, exctype):
        # raises the exception, performs cleanup if needed
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)

def gui():
    root = tk.Tk()
    APP(root)
    root.mainloop()

if __name__ == '__main__':
    gui()