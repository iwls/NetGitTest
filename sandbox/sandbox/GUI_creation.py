
#Create a first GUi with simple text in it
import tkinter

from tkinter import * # or import a label or impart all like here is one
widget = Label(None, text="This is my first Gui!!") #create a wiget label , in this case a label
widget.pack( )
widget.mainloop( )


#resizing the sidget - keeps the text centered - Configure widget when created
import tkinter
from tkinter import *
Label(text="My first GUI!").pack(expand=YES, fill=BOTH)
mainloop( )

## Configure widgets once they are created
import tkinter
from tkinter import *
root = Tk( )
widget = Label(root)
widget.config(text=’My first GUI!’)
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()

## adding a button
import sys

from tkinter import *
widget = Button(None, text="Click Me", command=sys.exit)
widget.pack( )
widget.mainloop( )

##Adding two buttons providing the user to quit or the show the sum of 2+2
from tkinter import *
def result():
    print("The sum of 2+2 is ",2+2)
win = Frame()
win.pack()
Label(win,  text="Click Add to get the sum or Quit to Exit").pack(side=TOP)
Button(win, text="Add", command=result).pack(side=LEFT)
Button(win, text="Quit",  command=win.quit).pack(side=RIGHT)
win.mainloop()
