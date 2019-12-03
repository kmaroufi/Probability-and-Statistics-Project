from tkinter import *
from tkinter import ttk
from Logic import *
from Util import *
import time
import _thread

class TabTwo:
    def __init__(self, notebook):
        self.tiles_frame = []
        self.board = Board(0, 0)
        self.i = 1
        self.is_job_done = False

        # creating Tab1
        main = ttk.Frame(notebook)
        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=2)

        # left side
        leftside_tab = ttk.Frame(main, borderwidth=0, relief="", width=200, height=400)
        leftside_tab.grid(column=0, row=0)

        # right side
        rightside_tab = ttk.Frame(main, borderwidth=0, relief="", width=400, height=400)
        rightside_tab.grid(column=1, row=0)

        # Creating left side.
        # leftside.rowconfigure(0, weight=1)
        # leftside.rowconfigure(1, weight=1)
        # leftside.rowconfigure(2, weight=1)
        # leftside.rowconfigure(3, weight=1)
        # leftside.rowconfigure(4, weight=1)
        # leftside.rowconfigure(5, weight=1)
        # leftside.rowconfigure(6, weight=1)


        ttk.Frame(leftside_tab, height=100, width=100, relief="").grid(column=0, row=0, sticky=("N", "W", "E", "S"))

        nframe = ttk.Frame(leftside_tab, relief="")
        nframe.grid(column=0, row=1)
        ttk.Label(nframe, text="n: ").grid(column=0, row=0)
        self.n_var = IntVar(value=10)
        n_var = self.n_var
        n = ttk.Entry(nframe, textvariable=n_var, width=6)
        n.grid(column=1, row=0)
        nframe.columnconfigure(0, weight=1)
        nframe.columnconfigure(1, weight=1)

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=2)

        colorframe = ttk.Frame(leftside_tab)
        colorframe.grid(column=0, row=3)
        ttk.Label(colorframe, text="Number of Colors: ").grid(column=0, row=0)
        self.color_var = IntVar(value=5)
        color_var = self.color_var
        color = ttk.Entry(colorframe, textvariable=color_var, width=6)
        color.grid(column=1, row=0)

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=4)

        runsframe = ttk.Frame(leftside_tab)
        runsframe.grid(column=0, row=5)
        ttk.Label(runsframe, text="Number of Runs: ").grid(column=0, row=0)
        self.runs_var = IntVar()
        runs_var = self.runs_var
        runs = ttk.Entry(runsframe, textvariable=runs_var, width=6)
        runs.grid(column=1, row=0)

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=6)

        buttonframe = ttk.Frame(leftside_tab)
        buttonframe.grid(column=0, row=7)

        self.run = False

        self.stun = ttk.Button(buttonframe, text="Run/Stop", command=self.stun_func)
        self.stun.grid(column=1, row=0)

        statusframe = ttk.Frame(leftside_tab)
        statusframe.grid(column=0, row=8)
        self.status_var = StringVar()
        status_var = self.status_var
        status = ttk.Label(statusframe, textvariable=status_var)
        status.grid(column=0, row=0)

        # roundsframe = ttk.Frame(leftside_tab)
        # roundsframe.grid(column=0, row=9)
        # self.rounds_var = StringVar(value="Rounds: 0")
        # rounds_var = self.rounds_var
        # rounds = ttk.Label(roundsframe, textvariable=rounds_var)
        # rounds.grid(column=0, row=0)

        ttk.Frame(rightside_tab, height=50, width=100, relief="").grid(column=0, row=0, sticky=("N", "W", "E", "S"))
        ttk.Label(rightside_tab, text="Seed                                 Rounds").grid(column=0, row=1)


        listbox_var = StringVar()
        listbox_list = []
        l = Listbox(rightside_tab, height=15, width=35, listvariable=listbox_var)
        l.grid(column=0, row=2, sticky=(N, W, E, S))
        self.listbox = l
        s = ttk.Scrollbar(rightside_tab, orient=VERTICAL, command=l.yview)
        s.grid(column=1, row=2, sticky=(N, S))
        l['yscrollcommand'] = s.set
        # rightside_tab.grid_columnconfigure(0, weight=1)
        # rightside_tab.grid_rowconfigure(0, weight=1)
        # for i in range(1, 101):
        #     l.insert('end', 'Line %d of 100' % i)
        avrounds_var = StringVar(value="Average Rounds = ?")
        ttk.Label(rightside_tab, textvariable=avrounds_var).grid(column=0, row=3)
        self.avrounds_var = avrounds_var

        varounds_var = StringVar(value="Variance of Rounds = ?")
        ttk.Label(rightside_tab, textvariable=varounds_var).grid(column=0, row=4)
        self.varounds_var = varounds_var

        self.listbox_var = listbox_var
        self.listbox_list = listbox_list
        self.rounds_list = []

        self.main = main
        self.leftside_tab1 = leftside_tab
        self.rightside_tab1 = rightside_tab

    def stun_func(self):
        if self.run is False:
            self.status_var.set("Status: In Progress")
            self.run = True
            if self.is_job_done:
                self.i = 1
                self.is_job_done = False
            _thread.start_new_thread(self.task2, ())
            # self.stun.after(0, self.task2)
        else:
            self.status_var.set("Status: Stop")
            self.run = False

    def task(self):
        self.listbox_list.clear()
        self.listbox_var.set(self.listbox_list)
        number_of_runs = self.runs_var.get()
        for i in range(number_of_runs):
            print("mission completed.")
            self.board = Board(self.n_var.get(), self.color_var.get())
            self.board.reset_tiles()
            while self.run:
                if not self.board.is_uniformed():
                    self.status_var.set("Status: In Progress")
                    self.board.do_round()

                    self.rounds_var.set("Rounds: " + str(self.board.rounds))
                else:
                    break
            self.listbox_list.append(str(i) + "                                   " + str(self.board.rounds))
            self.listbox_var.set(self.listbox_list)

        self.status_var.set("Status: Done")
        run = False

    def task2(self):
        if self.i == 1:
            self.listbox_list.clear()
            self.listbox_var.set(self.listbox_list)
            self.rounds_list.clear()
            self.avrounds_var.set("Average Rounds = ?")
            self.varounds_var.set("Variance of Rounds = ?")
        self.board = Board(self.n_var.get(), self.color_var.get())
        self.board.reset_tiles()
        self.status_var.set("Status: In Progress")
        while self.run:
            if not self.board.is_uniformed():
                self.board.do_round()
            else:
                break

        if self.run:
            # self.listbox.selection_clear(len(self.listbox_list))
            # self.listbox.selection_set("end")
            self.listbox.see("end")
            self.listbox_list.append("     " + str(self.i) + "                                          " + str(self.board.rounds))
            self.listbox_var.set(self.listbox_list)
            self.rounds_list.append(self.board.rounds)
            if self.i < self.runs_var.get():
                self.i += 1
                _thread.start_new_thread(self.task2, ())
                # self.stun.after(100, self.task2)
            else:
                average =sum(self.rounds_list)/len(self.rounds_list)
                self.avrounds_var.set("Average Rounds = " + str(int(average)))
                variance = 0
                for x in self.rounds_list:
                    variance += (x - average)**2
                variance /= len(self.rounds_list)
                self.varounds_var.set("Variance of Rounds = " + str(int(variance)))
                self.status_var.set("Status: Done")
                self.is_job_done = True
                self.run = False
