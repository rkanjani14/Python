from tkinter import *
import parser
root = Tk()
root.title('gui2')

# get a number to press a  button function
i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i += 1

# to delete all input from screen
def clear_all():
    display.delete(0,END)

# to calculation of expression
def calculation():
    a = display.get()
    try:
        b = parser.expr(a).compile()
        result = eval(b)
        clear_all()
        display.insert(i,result)
    except Exception:
        clear_all()
        display.insert(0,"ERROR")


# delete a no in display
def backspace():
    entire_string = display.get()
    if len(entire_string):
        new_string=entire_string[0:-1]
        clear_all()
        display.insert(i,new_string)
    else:
        display.insert(0,"ENTER NO")

def get_operator(operator):
    length = len(operator)
    global i
    display.insert(i,operator)
    i += length





# entry area
display = Entry(root)
display.grid(row=0,columnspan=6)


# numberic button 
Button(root,text="1",command= lambda : get_variable(1)).grid(row=1,column=0)
Button(root,text="2",command= lambda : get_variable(2)).grid(row=1,column=1)
Button(root,text="3",command= lambda : get_variable(3)).grid(row=1,column=2)

Button(root,text="4",command= lambda : get_variable(4)).grid(row=2,column=0)
Button(root,text="5",command= lambda : get_variable(5)).grid(row=2,column=1)
Button(root,text="6",command= lambda : get_variable(6)).grid(row=2,column=2)

Button(root,text="7",command= lambda : get_variable(7)).grid(row=3,column=0)
Button(root,text="8",command= lambda : get_variable(8)).grid(row=3,column=1)
Button(root,text="9",command= lambda : get_variable(9)).grid(row=3,column=2)

# button like AC , zero, equal sign
Button(root,text="AC", command= lambda : clear_all()).grid(row=4,column=0)
Button(root,text="0", command= lambda: get_variable(0)).grid(row=4,column=1)
Button(root,text="=", command= lambda : calculation()).grid(row=4,column=2)


# button for arthematic operation
Button(root,text="+",command= lambda : get_operator("+")).grid(row=1,column=3) 
Button(root,text="-",command= lambda : get_operator("-")).grid(row=2,column=3)
Button(root,text="*",command= lambda : get_operator("*")).grid(row=3,column=3)
Button(root,text="/",command= lambda : get_operator("/")).grid(row=4,column=3)

Button(root,text="pi",command= lambda : get_operator("*3.14")).grid(row=1,column=4)
Button(root,text="%",command= lambda : get_operator("%")).grid(row=2,column=4)
Button(root,text="(",command= lambda : get_operator("(")).grid(row=3,column=4)
Button(root,text="exp",command= lambda : get_operator("**")).grid(row=4,column=4)

Button(root,text="<-",command= lambda : backspace()).grid(row=1,column=5)
Button(root,text="x!").grid(row=2,column=5)
Button(root,text=")",command= lambda : get_operator(")")).grid(row=3,column=5)
Button(root,text="^2",command= lambda : get_operator("**2")).grid(row=4,column=5)

root.mainloop()