from tkinter import *

brush_size=3
brush_color='RED'

win=Tk()
win.title('Paint')


w=Canvas(win,width=800,
        height=600,)

def color_change(new_color):

 global brush_color
 brush_color=new_color





def blue():
  color_change('blue')

def red():
 color_change('red')

def green():
 color_change ('green')

def black ():
 color_change ('black')

def pink ():
 color_change ('pink')

def yellow ():
 color_change ('yellow')


def fife ():
 brish_size_change(5)

def one():
 brish_size_change(1)

def two ():
 brish_size_change(2)

def thee():
  brish_size_change(3)

def four():
  brish_size_change(4)



def paint(event):
 global brush_size
 global brush_color



 x1=event.x-brush_size
 x2=event.x+brush_size

 y1=event.y-brush_size
 y2=event.y+brush_size
 w.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)

def brish_size_change(new_size):
    global brush_size
    brush_size = new_size

# def color_change(new_color):
#  global color
#  color = new_color

w.rowconfigure(5,weight=1)



w.bind('<B1-Motion>',paint)


w.grid(row=2,column=0,
       columnspan=7, padx=5,
       pady=5,sticky=E+W+S+N)

w.columnconfigure(6,weight=1)
w.rowconfigure(3,weight=1)







main_menu = Menu()
filemenu = Menu(main_menu, tearoff=0)
filemenu.add_command(label="Blue.",command =blue())
filemenu.add_command(label="Red.",command =red())
filemenu.add_command(label="Green.",command =green())
filemenu.add_command(label="Black.",command =black())
filemenu.add_command(label="Pink.",command =pink())
filemenu.add_command(label="Yellow.",command = yellow())

helpmenu = Menu(main_menu, tearoff=0)
helpmenu.add_command(label="One.",command =one())
helpmenu.add_command(label="Two.",command =two())
helpmenu.add_command(label="Thee.",command =thee())
helpmenu.add_command(label="Thee.",command =thee())
helpmenu.add_command(label="Four.",command =four())
helpmenu.add_command(label="Fife.",command =fife())


main_menu.add_cascade(label = "Colors" ,menu=filemenu )
main_menu.add_cascade(label = "Size" ,menu=helpmenu )

win.config(menu=main_menu)
win.mainloop()
