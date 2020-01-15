from tkinter import *
from tkinter import ttk
root = Tk()
root.title("*gui*")
root.geometry('500x700')


def This_Function():
    if ok.get() == 1:
        subscribe = "YES"
    else:
        subscribe = "NO"

    print(f'''name is {Name_display.get()} \n email is {Email_display.get()}
    and gender is {Gender_combo.get()} and subscribe is {subscribe}''')
    



Label(root,text="ENTRY NAME").grid(row=0,column=0)
Name_display = Entry(root)
Name_display.grid(row=0,column=1)

Label(root,text="ENTER EMAIL").grid(row=1,column=0)
Email_display = Entry(root)
Email_display.grid(row=1,column=1)

Label(root,text="ENTER MOBILE").grid(row=2,column=0)
Mobile_display = Entry(root)
Mobile_display.grid(row=2,column=1)

Label(root,text="ENTER AGE").grid(row=3,column=0)
Age_display = Entry(root)
Age_display.grid(row=3,column=1)

# combobox
Label(root,text="SELECT GENDER").grid(row=4,column=0)
some_value = ['Male','Female','Others']
Gender_combo = ttk.Combobox(root,value=some_value,state="readonly")
Gender_combo.current(0)

# class combobox
Label(root,text="ENTER CLASS").grid(row=5,column=0)
some_value1 = ['CSE','MECH','CIVIL','EC','EX']
Class_combo = ttk.Combobox(root,value=some_value1,state="readonly")
Class_combo.current(0)
Class_combo.grid(row=5,column=1)

Gender_combo.grid(row=4,column=1)

# school combobox
Label(root,text="SCHOOL NAME").grid(row=6,column=0)
some_value2 = ['P.k.Jha','Sant Paul','Gurukul','Sant Karen','S. Niketan']
school_combo = ttk.Combobox(root,value=some_value2,state="readonly")
school_combo.current(0)
school_combo.grid(row=6,column=1)

# radio buttons
Label(root,text="Tick your Profession").grid(row=7,column=0)

selection= StringVar()

student_radio = Radiobutton(root,text="student",value="student",variable=selection)
student_radio.grid(row=8,column=0)

teacher_radio = Radiobutton(root,text="Teacher",value="Teacher",variable=selection)
teacher_radio.grid(row=9,column=0)

doctor_radio = Radiobutton(root,text="Doctor",value="Doctor",variable=selection)
doctor_radio.grid(row=10,column=0)

engineer_radio = Radiobutton(root,text="Enginner",value="Enginner",variable=selection)
engineer_radio.grid(row=11,column=0)

# chek button
ok=IntVar()
chek_button = Checkbutton(root,text="Tick if Intetsted",variable=ok)
chek_button.grid(row=12,column=0)

# submit button
Button(root,text="Submit",command= lambda : This_Function()).grid(row=13,column=0)


root.mainloop()