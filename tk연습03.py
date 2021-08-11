from tkinter import *
window = Tk()

btnList = [None] *10

for i in range(0,10) :
    btnList[i] = Button(window, text="버튼"+str(i+1))

for btn in btnList :
    btn.pack(side=LEFT)

window.mainloop()