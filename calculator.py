from tkinter import *

window = Tk()

frame = Frame(window)

frame.grid()

b0 = Button(frame, text="0", padx=5, pady=5, width=7).grid(row=3, column=0, columnspan=2)

bcomma = Button(frame, text=",", padx=5, pady=5).grid(row=3, column=2)

b1 = Button(frame, text="1", padx=5, pady=5).grid(row=2, column=2)
b2 = Button(frame, text="2", padx=5, pady=5).grid(row=2, column=1)
b3 = Button(frame, text="3", padx=5, pady=5).grid(row=2, column=0)

b4 = Button(frame, text="4", padx=5, pady=5).grid(row=1, column=2)
b5 = Button(frame, text="5", padx=5, pady=5).grid(row=1, column=1)
b6 = Button(frame, text="6", padx=5, pady=5).grid(row=1, column=0)

b7 = Button(frame, text="7", padx=5, pady=5).grid(row=0, column=2)
b8 = Button(frame, text="8", padx=5, pady=5).grid(row=0, column=1)
b9 = Button(frame, text="9", padx=5, pady=5).grid(row=0, column=0)

window.mainloop()