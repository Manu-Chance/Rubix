from collections import deque
from tkinter import *
import random

# Initial Condition
x =         deque([0,0,0,0]) # 0 ==> Blue
y =         deque([1,1,1,1]) # 1 ==> Red
z =         deque([2,2,2,2]) # 2 ==> White
x_alt =     deque([3,3,3,3]) # 3 ==> Green
y_alt =     deque([4,4,4,4]) # 4 ==> Orange
z_alt =     deque([5,5,5,5]) # 5 ==> Yellow
NOTATION = 'LRUDFBlrudfb'

# Tkinter class
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

def notation_input():
    notation_button.config(bg='purple')
    for x in (notation_entry.get()):
        if x == 'L':
            left()
        elif x == 'R':
            right()
        elif x == 'U':
            up()
        elif x == 'D':
            down()
        elif x == 'F':
            front()
        elif x == 'B':
            back()
        elif x == 'l':
            left_inv()
        elif x =='r':
            right_inv()
        elif x =='u':
            up_inv()
        elif x == 'd':
            down_inv()
        elif x == 'f':
            front_inv()
        elif x == 'b':
            back_inv()
        else:
            notation_button.config(bg='cyan')
            print('Something went wrong') 

def notation_input2(string):
    notation_button.config(bg='purple')
    for x in (string):
        if x == 'L':
            left()
        elif x == 'R':
            right()
        elif x == 'U':
            up()
        elif x == 'D':
            down()
        elif x == 'F':
            front()
        elif x == 'B':
            back()
        elif x == 'l':
            left_inv()
        elif x =='r':
            right_inv()
        elif x =='u':
            up_inv()
        elif x == 'd':
            down_inv()
        elif x == 'f':
            front_inv()
        elif x == 'b':
            back_inv()
        else:
            notation_button.config(bg='cyan')
            print('Something went wrong')
  
def color_picker(color):
    if color == 0:
        return 'blue'
    elif color == 1:
        return 'red'
    elif color == 2:
        return 'white'
    elif color == 3:
        return 'green'
    elif color == 4:
        return 'orange'
    elif color == 5:
        return 'yellow'
    else:
        print('Invalid input')
        return 'purple'

def right():
    buffer = y_alt[1]
    buffer2 = y_alt[2]
    
    y_alt[1] = z[1]
    y_alt[2] = z[2]

    z[1] = y[1]
    z[2] = y[2]
    
    y[1] = z_alt[1]
    y[2] = z_alt[2]

    z_alt[1] = buffer
    z_alt[2] = buffer2

    x.rotate(1)
    update_all_colors()

def right_inv():
    buffer = y_alt[1]
    buffer2 = y_alt[2]

    y_alt[1] = z_alt[1]
    y_alt[2] = z_alt[2]

    z_alt[1] = y[1]
    z_alt[2] = y[2]

    y[1] = z[1]
    y[2] = z[2]

    z[1] = buffer
    z[2] = buffer2

    x.rotate(-1)
    update_all_colors()

def left():
    buffer = y_alt[0]
    buffer2 = y_alt[3]

    y_alt[0] = z_alt[0]
    y_alt[3] = z_alt[3]

    z_alt[0] = y[0]
    z_alt[3] = y[3]

    y[0] = z[0]
    y[3] = z[3]

    z[0] = buffer
    z[3] = buffer2

    x_alt.rotate(1)
    update_all_colors()

def left_inv():
    buffer = y_alt[0]
    buffer2 = y_alt[3]

    y_alt[0] = z[0]
    y_alt[3] = z[3]

    z[0] = y[0]
    z[3] = y[3]

    y[0] = z_alt[0]
    y[3] = z_alt[3]

    z_alt[0] = buffer
    z_alt[3] = buffer2

    x_alt.rotate(-1)
    update_all_colors()

def up():
    buffer = x_alt[1]
    buffer2 = x_alt[2]

    x_alt[1] = y[0]
    x_alt[2] = y[1]

    y[0] = x[3]
    y[1] = x[0]

    x[3] = y_alt[2]
    x[0] = y_alt[3]

    y_alt[2] = buffer
    y_alt[3] = buffer2

    z.rotate(1)
    update_all_colors()
    
def up_inv():
    buffer = x_alt[1]
    buffer2 = x_alt[2]

    x_alt[1] = y_alt[2]
    x_alt[2] = y_alt[3]

    y_alt[2] = x[3]
    y_alt[3] = x[0]

    x[3] = y[0]
    x[0] = y[1]

    y[0] = buffer
    y[1] = buffer2

    z.rotate(-1)
    update_all_colors()

def down():
    buffer = x_alt[0]
    buffer2 = x_alt[3]

    x_alt[0] = y_alt[1]
    x_alt[3] = y_alt[0]

    y_alt[1] = x[2]
    y_alt[0] = x[1]
    
    x[2] = y[3]
    x[1] =  y[2]

    y[2] = buffer2
    y[3] = buffer
   
    z_alt.rotate(1)
    update_all_colors()

def down_inv():
    buffer = x_alt[0]
    buffer2 = x_alt[3]

    x_alt[0] = y[3]
    x_alt[3] = y[2]

    y[3] = x[2]
    y[2] = x[1]

    x[2] = y_alt[1]
    x[1] = y_alt[0]

    y_alt[1] = buffer
    y_alt[0] = buffer2

    z_alt.rotate(-1)
    update_all_colors()

def front():
    buffer = x[3]
    buffer2 = x[2]

    x[3] = z[3]
    x[2] = z[2]

    z[3] = x_alt[3]
    z[2] = x_alt[2]

    x_alt[3] = z_alt[1]
    x_alt[2] = z_alt[0]

    z_alt[1] = buffer
    z_alt[0] = buffer2

    y.rotate(1)
    update_all_colors()

def front_inv():
    buffer = x[3]
    buffer2 = x[2]

    x[3] = z_alt[1]
    x[2] = z_alt[0]

    z_alt[1] = x_alt[3]
    z_alt[0] = x_alt[2]

    x_alt[3] = z[3]
    x_alt[2] = z[2]

    z[3] = buffer
    z[2] = buffer2

    y.rotate(-1)
    update_all_colors()

def back():
    buffer = x[0]
    buffer2 = x[1]

    x[0] = z_alt[2]
    x[1] = z_alt[3]
    
    z_alt[2] = x_alt[0]
    z_alt[3] = x_alt[1]

    x_alt[0] = z[0]
    x_alt[1] = z[1]

    z[0] = buffer
    z[1] = buffer2

    y_alt.rotate(1)
    update_all_colors()

def back_inv():
    buffer = x[0]
    buffer2 = x[1]

    x[0] = z[0]
    x[1] = z[1]

    z[0] = x_alt[0]
    z[1] = x_alt[1]

    x_alt[0] = z_alt[2]
    x_alt[1] = z_alt[3]

    z_alt[2] = buffer
    z_alt[3] = buffer2

    y_alt.rotate(-1)
    update_all_colors()

def update_all_colors():
    x_button_1.config(bg=color_picker(x[0]))
    x_button_2.config(bg=color_picker(x[1]))
    x_button_3.config(bg=color_picker(x[2]))
    x_button_4.config(bg=color_picker(x[3]))

    y_button_1.config(bg=color_picker(y[0]))
    y_button_2.config(bg=color_picker(y[1]))
    y_button_3.config(bg=color_picker(y[2]))
    y_button_4.config(bg=color_picker(y[3]))

    z_button_1.config(bg=color_picker(z[0]))
    z_button_2.config(bg=color_picker(z[1]))
    z_button_3.config(bg=color_picker(z[2]))
    z_button_4.config(bg=color_picker(z[3]))

    x_alt_button_1.config(bg=color_picker(x_alt[0]))
    x_alt_button_2.config(bg=color_picker(x_alt[1]))
    x_alt_button_3.config(bg=color_picker(x_alt[2]))
    x_alt_button_4.config(bg=color_picker(x_alt[3]))

    y_alt_button_1.config(bg=color_picker(y_alt[0]))
    y_alt_button_2.config(bg=color_picker(y_alt[1]))
    y_alt_button_3.config(bg=color_picker(y_alt[2]))
    y_alt_button_4.config(bg=color_picker(y_alt[3]))

    z_alt_button_1.config(bg=color_picker(z_alt[0]))
    z_alt_button_2.config(bg=color_picker(z_alt[1]))
    z_alt_button_3.config(bg=color_picker(z_alt[2]))
    z_alt_button_4.config(bg=color_picker(z_alt[3]))

def random_scramble():
    global random_scramble
    random_scramble = ''.join(random.choice(NOTATION) for _ in range(50))
    print(random_scramble)
    notation_input2(random_scramble)

def random_scramble_reverse():
    rev_random_scramble = random_scramble[::-1]
    rev_random_scramble = rev_random_scramble.swapcase()
    print(rev_random_scramble)
    notation_input2(rev_random_scramble)


root = Tk()
app = Window(root)
root.wm_title("Rubix Cube 2x2")
root.geometry('1200x900')
root.configure(bg='black')

notation_entry = Entry(root)
notation_entry.place(bordermode=OUTSIDE, height = 100, width = 200, x = 800, y = 500)
notation_button = Button(root, bg='purple', text='NOTATION', command=notation_input)
notation_button.place(bordermode=OUTSIDE, height = 100, width = 200, x = 1000, y= 500)

#y_alt
y_alt_button_1 = Button(root, bg=color_picker(y_alt[0]), state=DISABLED, text='1')
y_alt_button_1.place(bordermode=OUTSIDE, height=100, width=100, x=300)
y_alt_button_2 = Button(root, bg=color_picker(y_alt[1]), state=DISABLED, text='2')
y_alt_button_2.place(bordermode=OUTSIDE, height=100, width=100, x=400)
y_alt_button_3 = Button(root, bg=color_picker(y_alt[2]), state=DISABLED, text='3')
y_alt_button_3.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=100)
y_alt_button_4 = Button(root, bg=color_picker(y_alt[3]), state=DISABLED, text='4')
y_alt_button_4.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=100)

# z    
z_button_1 = Button(root, bg=color_picker(z[0]), state=DISABLED, text='1')
z_button_1.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=200)
z_button_2 = Button(root, bg=color_picker(z[1]), state=DISABLED, text='2')
z_button_2.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=200)
z_button_3 = Button(root, bg=color_picker(z[2]), state=DISABLED, text='3')
z_button_3.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=300)
z_button_4 = Button(root, bg=color_picker(z[3]), state=DISABLED, text='4')
z_button_4.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=300)

# y
y_button_1 = Button(root, bg=color_picker(y[0]), state=DISABLED, text='1')
y_button_1.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=400)
y_button_2 = Button(root, bg=color_picker(y[1]), state=DISABLED, text='2')
y_button_2.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=400)
y_button_3 = Button(root, bg=color_picker(y[2]), state=DISABLED, text='3')
y_button_3.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=500)
y_button_4 = Button(root, bg=color_picker(y[3]), state=DISABLED, text='4')
y_button_4.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=500)

# z_alt
z_alt_button_1 = Button(root, bg=color_picker(z_alt[0]), state=DISABLED, text='1')
z_alt_button_1.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=600)
z_alt_button_2 = Button(root, bg=color_picker(z_alt[1]), state=DISABLED, text='2')
z_alt_button_2.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=600)
z_alt_button_3 = Button(root, bg=color_picker(z_alt[2]), state=DISABLED, text='3')
z_alt_button_3.place(bordermode=OUTSIDE, height=100, width=100, x=400, y=700)
z_alt_button_4 = Button(root, bg=color_picker(z_alt[3]), state=DISABLED, text='4')
z_alt_button_4.place(bordermode=OUTSIDE, height=100, width=100, x=300, y=700)

# x_alt
x_alt_button_1 = Button(root, bg=color_picker(x_alt[0]), state=DISABLED, text='1')
x_alt_button_1.place(bordermode=OUTSIDE, height=100, width=100, x=100, y=200)
x_alt_button_2 = Button(root, bg=color_picker(x_alt[1]), state=DISABLED, text='2')
x_alt_button_2.place(bordermode=OUTSIDE, height=100, width=100, x=200, y=200)
x_alt_button_3 = Button(root, bg=color_picker(x_alt[2]), state=DISABLED, text='3')
x_alt_button_3.place(bordermode=OUTSIDE, height=100, width=100, x=200, y=300)
x_alt_button_4 = Button(root, bg=color_picker(x_alt[3]), state=DISABLED, text='4')
x_alt_button_4.place(bordermode=OUTSIDE, height=100, width=100, x=100, y=300)

# x
x_button_1 = Button(root, bg=color_picker(x[0]), state=DISABLED, text='1')
x_button_1.place(bordermode=OUTSIDE, height=100, width=100, x=500, y=200)
x_button_2 = Button(root, bg=color_picker(x[1]), state=DISABLED, text='2')
x_button_2.place(bordermode=OUTSIDE, height=100, width=100, x=600, y=200)
x_button_3 = Button(root, bg=color_picker(x[2]), state=DISABLED, text='3')
x_button_3.place(bordermode=OUTSIDE, height=100, width=100, x=600, y=300)
x_button_4 = Button(root, bg=color_picker(x[3]), state=DISABLED, text='4')
x_button_4.place(bordermode=OUTSIDE, height=100, width=100, x=500, y=300)

# function buttons
bright = Button(root, bg='red', command=right, text='RIGHT')
bright.place(bordermode=OUTSIDE, height=100, width=50, x=800, y=100)
brightinv = Button(root, bg='purple', command=right_inv, text='RINV')
brightinv.place(bordermode=OUTSIDE, height=100, width=50, x=850, y=100)

bleft = Button(root, bg='purple', command=left, text='LEFT')
bleft.place(bordermode=OUTSIDE, height=100, width=50, x=800, y=200)
bleftinv = Button(root, bg='red', command=left_inv, text='LINV')
bleftinv.place(bordermode=OUTSIDE,height=100, width=50, x=850, y=200)

bup = Button(root, bg='red', command=up, text='UP')
bup.place(bordermode=OUTSIDE, height=100, width=50, x=800, y=300)
bupinv = Button(root, bg='purple', command=up_inv, text='UINV')
bupinv.place(bordermode=OUTSIDE, height=100, width=50, x=850, y=300)

bdown = Button(root, bg='purple', command=down, text='DOWN')
bdown.place(bordermode=OUTSIDE, height=100, width=50, x=900, y=100)
bdowninv = Button(root, bg='red', command=down_inv, text='DINV')
bdowninv.place(bordermode=OUTSIDE, height=100, width=50, x=950, y=100)

bfront = Button(root, bg='red', command=front, text='FRONT')
bfront.place(bordermode=OUTSIDE, height=100, width=50, x=900, y=200)
bfrontinv = Button(root, bg='purple', command=front_inv, text='FINV')
bfrontinv.place(bordermode=OUTSIDE, height=100, width=50, x=950, y=200)

bback = Button(root, bg='purple', command=back, text='BACK')
bback.place(bordermode=OUTSIDE, height=100, width=50, x=900, y=300)
bbackinv = Button(root, bg='red', command=back_inv, text='BINV')
bbackinv.place(bordermode=OUTSIDE, height=100, width=50, x=950, y=300)

rb = Button(root, bg='lime', command=random_scramble, text='RNG')
rb.place(bordermode=OUTSIDE, height=100, width=50, x=1050, y=100)

reverse_rb = Button(root, bg='lime', command=random_scramble_reverse, text='revRNG')
reverse_rb.place(bordermode=OUTSIDE, height=100, width=50, x=1050, y=200)

root.mainloop()
