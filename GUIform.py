import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("GUI")

name_label = ttk.Label(win, text='enter your name')
name_label.grid(row=0, column=0)

email_label = ttk.Label(win, text="enter you email")
email_label.grid(row=1 , column=0)

age_label = ttk.Label(win, text="enter your age")
age_label.grid(row=2, column=0)

gender_label = ttk.Label(win, text='select your gender')
gender_label.grid(row=3, column=0)

# entry
name = tk.StringVar()
name_entry = ttk.Entry(win, width=20, textvariable=name)
name_entry.grid(row=0, column=1)
name_entry.focus()

email = tk.StringVar()
email_entry = ttk.Entry(win, width=20, textvariable=email)
email_entry.grid(row=1, column=1)

age= tk.StringVar()
age_entry = ttk.Entry(win, width=20, textvariable=age)
age_entry.grid(row=2, column=1)

gender= tk.StringVar()
gender_combobox = ttk.Combobox(win, textvariable=gender, state="readonly")
gender_combobox['value'] = ('male', 'female', 'others')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

# radio button
profession = tk.StringVar()

radiobtn1 = ttk.Radiobutton(win, text="student", value="student" , variable=profession)
radiobtn1.grid(row=4,column=0)


radiobtn2 = ttk.Radiobutton(win, text="teacher", value="teacher" , variable=profession)
radiobtn2.grid(row=4,column=1)

# check button
check = tk.IntVar()
check_button = ttk.Checkbutton(win, text='please check for newaletter', variable=check)
check_button.grid(row=5, columnspan=3)

# button 
def myfunction():
    print(f"name is {name.get()} email is {email.get()} and age is {age.get()} profession is {profession.get()} and gender is {gender.get()}")
    
    if check.get() == 0:
        subscribe = "NO"
    else:
        
        subscribe = "YES"
    print(f"user subscribe : {subscribe}")    
submit_btn = ttk.Button(win, text="submit", command=myfunction)
submit_btn.grid(row=6, column=0)



win.mainloop()
