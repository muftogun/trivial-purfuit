from tkinter import *

tk = Tk()
tk.title("Trivial Purfuit")


sq1 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='red', height=8, width=8)
sq1.grid(row=1, column=1)

sq2 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='white', height=8, width=8)
sq2.grid(row=1, column=2)

sq3 = Button(tk, text='Roll Again', font='Helvetica 20 bold', highlightbackground='orange', height=8, width=8)
sq3.grid(row=1, column=3)

sq4 = Button(tk, text='RED HQ', font='Helvetica 20 bold', highlightbackground='red', height=8, width=8)
sq4.grid(row=1, column=4)

sq5 = Button(tk, text='Roll Again', font='Helvetica 20 bold', highlightbackground='orange', height=8, width=8)
sq5.grid(row=1, column=5)

sq6 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground ='white', height=8, width=8)
sq6.grid(row=1, column=6)

sq7 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground ='blue', height=8, width=8)
sq7.grid(row=1, column=7)

sq8 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground ='blue', height=8, width=8)
sq8.grid(row=2, column=1)

sq9 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground ='green', height=8, width=8)
sq9.grid(row=2, column=7)



tk.mainloop()