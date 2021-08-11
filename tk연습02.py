from tkinter import *
window = Tk()

button1 = Button(window, text="←")
button2 = Button(window, text="↑")
button3 = Button(window, text="→")
button4 = Button(window, text="↓")

button1.pack(side=LEFT)
button2.pack(side=TOP)
button3.pack(side=RIGHT)
button4.pack(side=BOTTOM)

window.mainloop()