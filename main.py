from tkinter import *
import os, sys

mainscreen = Tk()
mainscreen.title("Waddap")
mainscreen.geometry('200x150')

def level_1():
   mainscreen.destroy
   os.system("python level1.py")
   sys.exit()
def level_2():
   mainscreen.destroy
   os.system("python level2.py")
   sys.exit()
def level_3():
   mainscreen.destroy
   os.system("python level3.py")
   sys.exit()

play1 = Button(mainscreen,text='Easy', bd = '5', command = level_1)
play1.pack(side='top')

play2 = Button(mainscreen,text='Medium', bd = '5', command = level_2)
play2.pack(side='top')

play3 = Button(mainscreen,text='Hard', bd = '5', command = level_3)
play3.pack(side='top')

mainscreen.mainloop()
