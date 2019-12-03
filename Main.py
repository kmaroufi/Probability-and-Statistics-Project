import tkinter
from Tab1 import *
from Tab2 import *
from Tab3 import *
from Tab4 import *
from Util import *

# class myThread (threading.Thread):
#     def __init__(self, threadID, name):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#     def run(self):
#         print("Starting " + self.name)
#         while True:
#             print("ass")
#         print("Exiting " + self.name)
# _thread.start_new_thread(root.mainloop, ())
# gui_thread = myThread(1, "ass")
# gui_thread.start()


root = tkinter.Tk()
root.title("Probability and Statistics Project")

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

notebook = ttk.Notebook(mainframe, height=400, width=600)

tab1 = TabOne(notebook)
tab2 = TabTwo(notebook)
tab3 = TabThree(notebook)
tab4 = TabFour(notebook)

notebook.add(tab1.main, text="n*n matrix")
notebook.pack()

notebook.add(tab2.main, text="Batch n*n matrix")
notebook.pack()

notebook.add(tab3.main, text="Graph n*n matrix")
notebook.pack()

notebook.add(tab4.main, text="Graph")
notebook.pack()

root.resizable(width=False, height=False)
root.mainloop()
