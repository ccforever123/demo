import tkinter as tk
import watch_preview


class APP:
    def __init__(self, master):
        self.version = '1.0'
        master.title('HUAWEI Watch GT Watchface Previewer V{}'.format(self.version))
        self.update_info = 'Update Info Area'


        master.geometry('1000x500')


        self.img = watch_preview.preview()

        # set menubar
        self.menubar = tk.Menu(master)

        # set file sub-menu
        fileMenu = tk.Menu(self.menubar)
        fileMenu.add_command(label='Close', command=self.close)
        
        # set about sub-menu
        aboutMenu = tk.Menu(self.menubar)
        aboutMenu.add_command(label='About', command=self.about)

        # pack menubar
        master['menu'] = self.menubar


        self.imgPreview = tk.PhotoImage(self.img)
        self.imgLabel = tk.Label(master, image=self.imgPreview)







        self.imgLabel.gird(row=0, column=0, padx=5, pady=5)


    def close(self):
        quit()


    def about(self):
        messagebox.showinfo('About', self.update_info)





def main():
    root = tk.Tk()
    APP(root)

    root.mainloop()


if __name__ == "__main__":
    main()