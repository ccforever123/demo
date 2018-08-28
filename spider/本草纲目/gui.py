import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext
import lookup


class APP:
    def __init__(self, master):
        self.version = 0.1


        frame_operator = tk.Frame(master)

        master.title('本草纲目 Demo {}'.format(self.version))
        master.geometry('500x500')

        self.menubar(master)
        self.frame_input_label(master)
        self.frame_content_label(master)


    def menubar(self, master):
        self.menubar = tk.Menu(master)
        file_menu = tk.Menu(self.menubar)
        file_menu.add_command(label='关闭', command=self.close)
        self.menubar.add_cascade(label='文件', menu=file_menu)
        file_about = tk.Menu(master)
        file_about.add_checkbutton(label='版本信息', command=self.version)
        self.menubar.add_cascade(label='关于', menu=file_about)
        master.config(menu=self.menubar)

    def frame_input_label(self, master):
        input_label = tk.Label(master, text='关键词：')
        self.input_var = tk.StringVar()
        input_keyword = tk.Entry(master, width=20, textvariable=self.input_var)
        search_button = tk.Button(master, text='搜索', command=self.search_button, width=10, height=1)
        clear_button = tk.Button(master, text='清空', command=self.clear_button, width=10, height=1)
        input_label.grid(row=0, column=0, padx=10, pady=5)
        input_keyword.grid(row=0, column=1, padx=10, pady=5)
        search_button.grid(row=0, column=2, padx=10, pady=5)
        clear_button.grid(row=0, column=3, padx=10, pady=5)

    def frame_content_label(self, master):
        master.update()
        self.scrolW = master.winfo_width()
        self.scrolH = master.winfo_height()
        self.keyword_text = tk.StringVar()
        self.keyword_text.set('')
        self.content_text_0 = tk.StringVar()
        self.content_text_0.set('')
        self.content_text_1 = tk.StringVar()
        self.content_text_1.set('')
        self.content_text_2 = tk.StringVar()
        self.content_text_2.set('点击搜索查看结果...')
        self.content_text_3 = tk.StringVar()
        self.content_text_3.set('')
        self.content_text_4 = tk.StringVar()
        self.content_text_4.set('')
        keyword_text = tk.Label(master, textvariable=self.keyword_text)
        content_sub_title = tk.Label(master, background='#f0f0f0', text='标题')
        content_text_0 = tk.Label(master, background='#f0f0f0', textvariable=self.content_text_0, wraplength=600)
        content_shiming = tk.Label(master, background='#f0f0f0', text='释名')
        content_text_1 = tk.Label(master, background='#f0f0f0', textvariable=self.content_text_1, wraplength=600)
        content_qiwei = tk.Label(master, background='#f0f0f0', text='气味')
        content_text_2 = tk.Label(master, background='#f0f0f0', textvariable=self.content_text_2, wraplength=600)
        content_zhuzhi = tk.Label(master, background='#f0f0f0', text='主治')
        content_text_3 = tk.Label(master, background='#f0f0f0', textvariable=self.content_text_3, wraplength=600)
        content_fufang = tk.Label(master, background='#f0f0f0', text='附方')
        content_text_4 = tk.Label(master, background='#f0f0f0', textvariable=self.content_text_4, wraplength=600)

        keyword_text.grid(row=1, column=0, padx=10, pady=5)
        content_sub_title.grid(row=2, column=0, padx=10, pady=5)
        content_text_0.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky=tk.W)
        content_shiming.grid(row=3, column=0, padx=10, pady=5)
        content_text_1.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky=tk.W)
        content_qiwei.grid(row=4, column=0, padx=10, pady=5)
        content_text_2.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky=tk.W)
        content_zhuzhi.grid(row=5, column=0, padx=10, pady=5)
        content_text_3.grid(row=5, column=1, columnspan=3, padx=10, pady=5, sticky=tk.W)
        content_fufang.grid(row=6, column=0, padx=10, pady=5)
        content_text_4.grid(row=6, column=1, columnspan=3, padx=10, pady=5, sticky=tk.W)

        self.current_page = 0
        self.total_page = 0
        nav_left = tk.Button(master, text='上一条', width=10, height=1, command=self.page_left)
        self.page_info = tk.StringVar()
        self.page_info.set('0 / 0')
        page = tk.Label(master, textvariable=self.page_info)
        nav_right = tk.Button(master, text='下一条', width=10, height=1, command=self.page_right)
        nav_left.grid(row=7, column=0, padx=10, pady=5)
        page.grid(row=7, column=1, padx=10, pady=5)
        nav_right.grid(row=7, column=2, padx=10, pady=5)

    def page_left(self):
        self.current_page -= 1
        return self.current_page

    def page_right(self):
        self.current_page -= 1
        return self.current_page


    def clear_button(self):
        self.input_var.set('')


    def search_button(self):
        keyword = self.input_var.get()
        if keyword == '':
            return None
        result = lookup.search(keyword)
        text = ''
        self.total_page = len(result)
        self.current_page = 1
        self.page_info.set('{} / {}'.format(self.current_page, self.total_page))
        if self.total_page == 0:
            self.keyword_text.set(keyword)
            self.content_text_1.set('找不到指定数据')
        else:
            self.content_text_0.set(result[self.current_page - 1][0])
            self.content_text_1.set(result[self.current_page - 1][1][0][1])
            self.content_text_2.set(result[self.current_page - 1][1][1][1])
            self.content_text_3.set(result[self.current_page - 1][1][2][1])
            self.content_text_4.set(result[self.current_page - 1][1][3][1])



    def close(self):
        quit()


    def version(self):
        tk.messagebox.showinfo('Version', '当前版本为{}'.format(self.version))


def main():
    root = tk.Tk()
    APP(root)

    root.mainloop()


if __name__ == '__main__':
    main()