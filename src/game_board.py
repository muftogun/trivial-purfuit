from tkinter import *

tk = Tk()
tk.title("Trivial Purfuit")


def button_click(playerName, button):
    if button['text'] == ' ':
        button['text'] = playerName
    elif button['text'] != ' ':
        button['text'] = ' '


p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8, sticky='w')
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8, sticky='w')

label = Label(tk, text="Player 1:", font='Garamond 20 bold', bg='yellow', fg='black', height=1, width=8)
label.grid(row=1, column=0, sticky='e')

label = Label(tk, text="Player 2:", font='Garamond 20 bold', bg='yellow', fg='black', height=1, width=8)
label.grid(row=2, column=0, sticky='e')

sq1 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='red', height=8, width=8,
             command=lambda: button_click(p1.get(), sq1))
sq1.grid(row=3, column=1)

sq2 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='white', height=8, width=8,
             command=lambda: button_click(p2.get(), sq2))
sq2.grid(row=3, column=2)

sq3 = Button(tk, text='Roll Again', font='Helvetica 20 bold', highlightbackground='orange', height=8, width=8)
sq3.grid(row=3, column=3)

sq4 = Button(tk, text='RED HQ', font='Helvetica 20 bold', highlightbackground='red', height=8, width=8)
sq4.grid(row=3, column=4)

sq5 = Button(tk, text='Roll Again', font='Helvetica 20 bold', highlightbackground='orange', height=8, width=8)
sq5.grid(row=3, column=5)

sq6 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='white', height=8, width=8)
sq6.grid(row=3, column=6)

sq7 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='blue', height=8, width=8)
sq7.grid(row=3, column=7)

sq8 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='blue', height=8, width=8)
sq8.grid(row=4, column=1)

sq9 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='green', height=8, width=8)
sq9.grid(row=4, column=4)

sq9 = Button(tk, text=' ', font='Helvetica 20 bold', highlightbackground='purple', height=8, width=8,
             command=lambda: button_click(p2.get(), sq9))
sq9.grid(row=4, column=7)

tk.mainloop()
