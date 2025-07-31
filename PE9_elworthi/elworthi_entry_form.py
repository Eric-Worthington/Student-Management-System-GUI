# Eric Worthington, CIS345, PE9

from tkinter import *
from tkinter import ttk
from student_classes import Student, GradStudent

edit_mode = False
edit_index = None

win = Tk()
win.geometry('500x600')
win.title('Student Entry Form')
win.config(bg='light blue')

student_types = {'Student': 'S', 'Graduate Student': 'G'}

def rad_click():
    global thesis_var_entry

    if x.get() == 'G':
        thesis_var_entry.config(state=NORMAL)
    else:
        thesis_var_entry.config(state=DISABLED)

def major_selected():
    global combo_box

def save_student_click():
    global first_name_entry, last_name_entry, major, thesis_var, student_roster, list_box, edit_mode, edit_index
    first_name_value = first_name_entry.get()
    last_name_value = last_name_entry.get()
    major_value = combo_box.get()
    thesis_value = thesis_var_entry.get()

    student_type = x.get()

    if student_type == 'G':
        new_student = GradStudent(thesis_value, first_name_value, last_name_value, major_value)
    else:
        new_student = Student(first_name_value, last_name_value, major_value)

    first_name.set(first_name_value)

    if edit_mode:
        student_roster[edit_index] = new_student
        list_box.delete(edit_index)
        list_box.insert(edit_index, str(new_student))
        edit_mode = False
    else:
        student_roster.append(new_student)
        list_box.insert(END, f"{last_name_value.capitalize()}, {first_name_value.capitalize()}, - {major_value}")

    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    combo_box.set('')
    thesis_var_entry.delete(0, END)

def edit_student(event):
    global edit_mode, edit_index, first_name_entry, last_name_entry, combo_box, thesis_var_entry, student_roster
    edit_mode = True

    edit_index = list_box.curselection()[0]
    edit_student = student_roster[edit_index]

    if isinstance(edit_student, GradStudent):
        stu_type = 'G'
        thesis_var_entry.config(state=NORMAL)
        thesis_var_entry.delete(0, END)
        thesis_var_entry.insert(0, edit_student.thesis)
    else:
        stu_type = 'S'
        thesis_var_entry.config(state=DISABLED)

    first_name_entry.delete(0, END)
    first_name_entry.insert(0, edit_student.fname)
    last_name_entry.delete(0, END)
    last_name_entry.insert(0, edit_student.lname)
    combo_box.set(edit_student.major)


def student_selected(event):
    global list_box, edit_mode, edit_index
    list_box.select_clear(0, END)
    index = list_box.nearest(event.y)
    list_box.select_set(index)
    selected_student = student_roster[index]
    print(selected_student)

    edit_mode = True
    edit_index = index

# Frame Widget
box = Frame(win, bg='light yellow', width=350, height=80, borderwidth=1,relief=SUNKEN)
box.grid(row=0, column=1, columnspan=3, padx=(100, 50))
box.propagate(False)

# inside of Frame Widget
Label(box, text='Student Type', bg='light yellow').pack(anchor=NW)

x = StringVar(box, '0')

for (text, v) in student_types.items():
    rad_btn = Radiobutton(box, bg='light yellow', text=text,
                           variable=x, value=v, anchor=W,
                           command=rad_click)
    rad_btn.pack(side=LEFT, padx=20, ipadx=8)

first_name = StringVar()
last_name = StringVar()
major = StringVar()
#thesis_var = StringVar()

# 4 Label, 3 Entry boxes, 1 Combobox Widget
Label(win, text='First Name:', bg='light blue').grid(row=1, column=1, pady=10, padx=(90, 0), sticky=E)
first_name_entry = Entry(win, bg='white', justify=LEFT, width=31)
first_name_entry.grid(row=1, column=2)

Label(win, text='Last Name: ', bg='light blue').grid(row=2, column=1, pady=10, padx=(90, 0), sticky=E)
last_name_entry = Entry(win, bg='white', justify=LEFT, width=31)
last_name_entry.grid(row=2, column=2)

Label(win, text='Major: ', bg='light blue').grid(row=3, column=1, pady=10, padx=(90, 0), sticky=E)
major = ['CIS', 'ACC','MKT','COM', 'ART']
combo_box = ttk.Combobox(win,values=major, width=28)
combo_box.grid(row=3, column=2, padx=(35,0), sticky=W)
combo_box.current(0)


Label(win, text='Thesis: ', bg='light blue').grid(row=4, column=1, pady=10, padx=(90, 0), sticky=E)
thesis_var_entry = Entry(win, bg='white', justify=LEFT, width=31)
thesis_var_entry.grid(row=4, column=2)

# Save Button Widget
save_button = Button(win, command=save_student_click, text='Save Student')
save_button.grid(row=5, column=2, pady=10, padx=(0,40), sticky=E)

# Double-Click Label Widget
Label(win, text='(Double-Click to Edit a Student)', bg='light blue').grid(row=6, column=1, columnspan=3,
                                                                          padx=(100, 50), sticky=W)

# Listbox Widget
list_box = Listbox(win, width=57, height=15, borderwidth=1)
list_box.grid(row=7, column=1, columnspan=3, padx=(100, 50), sticky=W)
list_box.insert(END)
list_box.bind('<Double-Button-1>', student_selected)
student_roster = []


win.mainloop()