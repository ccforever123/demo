# 主界面

import tkinter as tk


class APP:
    def __init__(self, master):
        self.master = master
        self.version = '0.1.0'
        master.geometry('600x400')

        self.homeTeamName = tk.StringVar()
        self.awayTeamName = tk.StringVar()
        self.homeScore = tk.StringVar()
        self.awayScore = tk.StringVar()

        self.text = tk.Text(master, width=200, height=10)

        self.homeScore.set('0')
        self.awayScore.set('0')

        tk.Entry(master, textvariable=self.homeTeamName, width=15).grid(row=0, column=0, columnspan=2, padx=5, pady=5)    # 显示主队队名
        tk.Label(master, textvariable=self.homeScore, width=5).grid(row=0, column=2, padx=5, pady=5)    # 显示主队得分
        tk.Label(master, textvariable=self.awayScore, width=5).grid(row=0, column=3, padx=5, pady=5)    # 显示客队得分
        tk.Entry(master, textvariable=self.awayTeamName, width=15).grid(row=0, column=4, columnspan=2, padx=5, pady=5)    # 显示客队队名
        tk.Button(master, text='开始比赛', width=15).grid(row=0, column=6, padx=5, pady=5)




        tk.Label(master, text='比赛概览', width=25).grid(row=7, column=0, padx=5, pady=5)
        


def gui():
    root = tk.Tk()
    APP(root)
    root.mainloop()


if __name__ == "__main__":
    gui()