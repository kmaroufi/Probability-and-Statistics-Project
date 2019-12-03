#creating Tab1
main = ttk.Frame(notebook)
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=2)

# left side
leftside_tab1 = ttk.Frame(main, borderwidth=0, relief="", width=200, height=400)
leftside_tab1.grid(column=0, row=0)

# right side
rightside_tab1 = ttk.Frame(main, borderwidth=0, relief="", width=400, height=400)
rightside_tab1.grid(column=1, row=0)



# Creating left side.
# leftside.rowconfigure(0, weight=1)
# leftside.rowconfigure(1, weight=1)
# leftside.rowconfigure(2, weight=1)
# leftside.rowconfigure(3, weight=1)
# leftside.rowconfigure(4, weight=1)
# leftside.rowconfigure(5, weight=1)
# leftside.rowconfigure(6, weight=1)


ttk.Frame(leftside_tab1, height=100, width=100, relief="").grid(column=0, row=0, sticky=("N", "W", "E", "S"))

nframe = ttk.Frame(leftside_tab1, relief="")
nframe.grid(column=0, row=1)
ttk.Label(nframe, text="n: ").grid(column=0, row=0)
n_var = IntVar()
n = ttk.Scale(nframe, orient="horizontal", length=100, from_=5.0, to=20.0, variable=n_var)
n.grid(column=1, row=0)
n.set(5)


ttk.Frame(leftside_tab1, height=40).grid(column=0, row=2)

colorframe = ttk.Frame(leftside_tab1)
colorframe.grid(column=0, row=3)
ttk.Label(colorframe, text="Colors: ").grid(column=0, row=0)
color_var = IntVar()
color = ttk.Scale(colorframe, orient="horizontal", length=100, from_=2, to=15.0, variable=color_var)
color.grid(column=1, row=0)
color.set(2)


ttk.Frame(leftside_tab1, height=40).grid(column=0, row=4)

intervalframe = ttk.Frame(leftside_tab1)
intervalframe.grid(column=0, row=5)
ttk.Label(intervalframe, text="Interval: ").grid(column=0, row=0)
interval_var = IntVar()
interval = ttk.Scale(intervalframe, orient="horizontal", length=100, from_=1, to=1000, variable=interval_var)
interval.grid(column=1, row=0)
interval.set(300)


ttk.Frame(leftside_tab1, height=40).grid(column=0, row=6)

buttonframe = ttk.Frame(leftside_tab1)
buttonframe.grid(column=0, row=7)
def reset_func():
    global tiles_frame
    global board
    global status_var

    status_var.set("Status: Stop")
    rounds_var.set("Rounds: 0")

    print(n_var.get(), color_var.get())

    # prepare logic
    board = Board(n_var.get(), color_var.get())
    board.reset_tiles()

    # prepare graphic
    for x in tiles_frame:
        for y in x:
            if y is not None:
                y.grid_remove()
    tiles_frame = [[None for j in range(n_var.get())] for i in range(n_var.get())]

    z = 0
    for i in range(n_var.get()):
        for j in range(n_var.get()):
            z += 1
            style = ttk.Style()
            style.configure(str(z) + ".TLabel", background=getColor(board.tiles[i][j].value))
            frame = ttk.Frame(rightside_tab1, width=15, height=15, style=str(z) + ".TLabel", relief="groov")
            frame.grid(column=j, row=i)
            tiles_frame[i][j] = frame
reset = ttk.Button(buttonframe, text="Reset", command=reset_func)
reset.grid(column=0, row=0)

run = False
def stun_func():
    global run
    if run is False:
        status_var.set("Status: In Progress")
        run = True
    else:
        status_var.set("Status: Stop")
        run = False
stun = ttk.Button(buttonframe, text="Run/Stop", command=stun_func)
stun.grid(column=1, row=0)

statusframe = ttk.Frame(leftside_tab1)
statusframe.grid(column=0, row=8)
status_var = StringVar()
status = ttk.Label(statusframe, textvariable=status_var)
status.grid(column=0, row=0)

roundsframe = ttk.Frame(leftside_tab1)
roundsframe.grid(column=0, row=9)
rounds_var = StringVar(value="Rounds: 0")
rounds = ttk.Label(roundsframe, textvariable=rounds_var)
rounds.grid(column=0, row=0)