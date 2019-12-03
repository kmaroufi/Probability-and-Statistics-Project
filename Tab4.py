from tkinter import *
from tkinter import ttk
from Logic import *
from Util import *
import _thread
import time
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as Tk
import networkx as nx
from random import random
import Graph_Logic

class TabFour:
    def __init__(self, notebook):
        self.graph = Graph_Logic.Graph(5, 5, 5, 0)
        self.graphic_graph = nx.complete_graph(5)
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


        ttk.Frame(leftside_tab, height=50, width=100, relief="").grid(column=0, row=0, sticky=("N", "W", "E", "S"))

        nframe = ttk.Frame(leftside_tab, relief="")
        nframe.grid(column=0, row=1)
        label1_var = StringVar()
        ttk.Label(nframe, textvariable=label1_var).grid(column=0, row=0)
        self.n_var = IntVar()
        n_var = self.n_var
        def label1(self):
            label1_var.set("n: " + str(n_var.get()))
        n = ttk.Scale(nframe, orient="horizontal", length=100, from_=5.0, to=30.0, variable=n_var, command=label1)
        n.grid(column=1, row=0)
        n.set(5)

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=2)

        colorframe = ttk.Frame(leftside_tab)
        colorframe.grid(column=0, row=3)
        label2_var = StringVar()
        ttk.Label(colorframe, textvariable=label2_var).grid(column=0, row=0)
        self.color_var = IntVar()
        color_var = self.color_var
        def label2(self):
            label2_var.set("Colors: " + str(color_var.get()))
        color = ttk.Scale(colorframe, orient="horizontal", length=100, from_=2, to=15.0, variable=color_var, command=label2)
        color.grid(column=1, row=0)
        color.set(2)

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=4)

        edgesframe = ttk.Frame(leftside_tab)
        edgesframe.grid(column=0, row=5)
        label3_var = StringVar()
        ttk.Label(edgesframe, text="Average num of edges: ", textvariable=label3_var).grid(column=0, row=0)
        self.edges_var = IntVar()
        edges_var = self.edges_var
        def label3(self):
            label3_var.set("Average num of edges: " + str(edges_var.get()))
        edges = ttk.Scale(edgesframe, orient="horizontal", length=100, from_=2, to=15, variable=edges_var, command=label3)
        edges.grid(column=1, row=0)
        edges.set(2)
        self.edges = edges

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=6)

        intervalframe = ttk.Frame(leftside_tab)
        intervalframe.grid(column=0, row=7)
        ttk.Label(intervalframe, text="Interval: ").grid(column=0, row=0)
        self.interval_var = IntVar()
        interval_var = self.interval_var
        interval = ttk.Scale(intervalframe, orient="horizontal", length=100, from_=1, to=1000, variable=interval_var)
        interval.grid(column=1, row=0)
        interval.set(300)

        ttk.Frame(leftside_tab, height=40).grid(column=0, row=8)

        buttonframe = ttk.Frame(leftside_tab)
        buttonframe.grid(column=0, row=9)

        self.reset = ttk.Button(buttonframe, text="Reset", command=self.reset_func)
        self.reset.grid(column=0, row=0)

        self.run = False

        self.stun = ttk.Button(buttonframe, text="Run/Stop", command=self.stun_func)
        self.stun.grid(column=1, row=0)

        statusframe = ttk.Frame(leftside_tab)
        statusframe.grid(column=0, row=10)
        self.status_var = StringVar()
        status_var = self.status_var
        status = ttk.Label(statusframe, textvariable=status_var)
        status.grid(column=0, row=0)

        roundsframe = ttk.Frame(leftside_tab)
        roundsframe.grid(column=0, row=11)
        self.rounds_var = StringVar(value="Rounds: 0")
        rounds_var = self.rounds_var
        rounds = ttk.Label(roundsframe, textvariable=rounds_var)
        rounds.grid(column=0, row=0)

        # plotting Graph
        f = plt.figure(figsize=(3, 3), facecolor='white')
        a = f.add_subplot(111)
        self.a = a
        plt.axis('off')

        # the networkx part
        G = nx.complete_graph(20)
        G.add_node(6, style='filled',fillcolor='black')
        pos = nx.circular_layout(G)

        nx.draw_networkx(G, pos=pos, ax=a)
        self.xlim = a.get_xlim()
        self.ylim = a.get_ylim()
        xlim = self.xlim
        ylim = self.ylim

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=rightside_tab)
        self.canvas = canvas
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas.show()


        self.main = main
        self.leftside_tab1 = leftside_tab
        self.rightside_tab1 = rightside_tab

        self.reset_func()

    def reset_func(self):
        self.status_var.set("Status: Stop")
        self.rounds_var.set("Rounds: 0")

        if self.n_var.get() % 2 == 1 and self.edges_var.get() % 2 == 1:
            self.edges.set(self.edges_var.get()+1)

        print(self.n_var.get(), self.color_var.get(), self.edges_var.get())

        # prepare logic
        self.graph = Graph_Logic.Graph(self.n_var.get(), self.edges_var.get(), self.color_var.get(), 1)

        # prepare graphic
        self.graphic_graph = nx.empty_graph()

        for node in self.graph.vertices:
            self.graphic_graph.add_node(node.number)
        for edge in self.graph.edges:
            self.graphic_graph.add_edge(edge[0], edge[1])

        color_map = []
        for node in self.graph.vertices:
            color_map.append(get_color(node.show_color))

        self.a.cla()
        pos = nx.circular_layout(self.graphic_graph)
        nx.draw_networkx(self.graphic_graph, pos, node_color=color_map, ax=self.a)
        self.a.set_xlim(self.xlim)
        self.a.set_ylim(self.ylim)
        plt.axis('off')
        self.canvas.draw()



    def stun_func(self):
        if self.run is False:
            self.status_var.set("Status: In Progress")
            self.run = True
            _thread.start_new_thread(self.task2, ())
            self.stun.after(50, self.task3)
            # self.stun.after(self.interval_var.get(), self.task)
        else:
            self.status_var.set("Status: Stop")
            self.run = False
            # self.stun.after_cancel(self.id)

    def task(self):
        if self.run:
            if not self.board.is_uniformed():
                self.status_var.set("Status: In Progress")
                self.board.do_round()

                z = 0
                for i in range(self.board.size):
                    for j in range(self.board.size):
                        z += 1
                        style = ttk.Style()
                        style.configure(str(z) + ".TLabel", background=get_color(self.board.tiles[i][j].value))
                        # frame = ttk.Frame(rightside, width=15, height=15, style=str(z)+".TLabel", relief="groov")
                        # frame.grid(column=j, row=i)
                        frame = self.tiles_frame[i][j]
                        frame.config(style=str(z) + ".TLabel")
                self.rounds_var.set("Rounds: " + str(self.board.rounds))
            else:
                self.status_var.set("Status: Done")
                self.run = False
            self.id = self.stun.after(self.interval_var.get(), self.task)

    def task2(self):
        inn = 0
        while self.run:
            if not self.graph.is_uniformed():
                self.graph.do_round()
                self.is_job_done = False
            else:
                self.is_job_done = True
                break
            inn += 1
            if inn == (1010 - self.interval_var.get())//10:
                time.sleep(self.interval_var.get()/1000)
                inn = 0

    def task3(self):
        if self.run:
            if not self.is_job_done:
                self.status_var.set("Status: In Progress")
            else:
                self.status_var.set("Status: Done")
                self.run = False

            # prepare graphic
            self.graphic_graph = nx.empty_graph()

            for node in self.graph.vertices:
                self.graphic_graph.add_node(node.number)
            for edge in self.graph.edges:
                self.graphic_graph.add_edge(edge[0], edge[1])

            color_map = []
            for node in self.graph.vertices:
                color_map.append(get_color(node.show_color))

            self.a.cla()
            pos = nx.circular_layout(self.graphic_graph)
            nx.draw_networkx(self.graphic_graph, pos, node_color=color_map, ax=self.a)
            self.a.set_xlim(self.xlim)
            self.a.set_ylim(self.ylim)
            plt.axis('off')
            self.canvas.draw()

            self.rounds_var.set("Rounds: " + str(self.graph.rounds))
            tmp = 0
            if self.n_var.get() * self.color_var.get() < 40:
                tmp = 100
            elif self.n_var.get() * self.color_var.get() < 60:
                tmp = 250
            elif self.n_var.get() * self.color_var.get() < 80:
                tmp = 350
            elif self.n_var.get() * self.color_var.get() < 100:
                tmp = 450
            else:
                tmp = 550
            self.id = self.stun.after(max(self.interval_var.get(), tmp), self.task3)
