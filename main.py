import tkinter as tk
from tkinter.ttk import Combobox
import random
import os
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from abc import ABC, abstractmethod


class StudentManagementSystem(ABC):
    @abstractmethod
    def admin_log():
        pass
    @abstractmethod
    def check_login():
        pass

    



root = tk.Tk()
root.geometry('500x500')
root.title('Student Management System')
root.configure(bg="#333333")

bg_color = "#281E7D"
class_list = ['Level-4', 'Level-5', 'Level-6', 'Level-7', 'Level-8', 'Level-9', 'Level-10', 'Level-11', 'Level-12']

current_frame = None  # To keep track of the currently displayed frame



def confirmation_box(message):
    answer = tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        confirm_box.destroy()

    confirm_box = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)
    message_lb = tk.Label(confirm_box, text=message, font=('Times New Roman', 16), bg="white")
    message_lb.pack(pady=20)

    cancel_btn = tk.Button(confirm_box, text='Cancel', font=('Times New Roman', 16), command=lambda: action(False))
    cancel_btn.place(x=50, y=160)

    yes_btn = tk.Button(confirm_box, text='Yes', font=('Times New Roman', 16), command=lambda: action(True))
    yes_btn.place(x=190, y=160, width=80)

    confirm_box.place(x=100, y=120, width=320, height=220)
    root.wait_window(confirm_box)
    return answer.get()

def message_box(message):
    message_box_fm = tk.Frame(root, highlightbackground=bg_color, highlightthickness=3)
    close_btn = tk.Button(message_box_fm, text='X', font=('Times New Roman', 16), command=lambda: message_box_fm.destroy())
    close_btn.place(x=290, y=5)
    message_ = tk.Label(message_box_fm, text=message, fg=bg_color, font=('Times New Roman', 16))
    message_.pack(pady=50)
    message_box_fm.place(x=100, y=120, width=320, height=200)
    

def clear_frame():
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
        current_frame = None

def login_page():
    global current_frame
    clear_frame()

    welcome_page = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = welcome_page

    heading_ = tk.Label(welcome_page, text="Login System Management", fg=bg_color, font=('Brush Script MT', 25))
    heading_.place(x=0, y=0, width=400)

    student_btn = tk.Button(welcome_page, text="Student Login", fg="red", bg=bg_color, font=("Times New Roman", 14), command=std_login)
    student_btn.place(x=120, y=125, width=200)

    admin_btn = tk.Button(welcome_page, text="Admin Login", fg="red", bg=bg_color, font=("Times New Roman", 14), command=adAuth.admin_log)
    admin_btn.place(x=120, y=225, width=200)

    welcome_page.pack(pady=30)
    welcome_page.pack_propagate(False)
    welcome_page.configure(width=400, height=420)

def std_login():
    global current_frame
    clear_frame()

    def check_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            message_box("Please enter both username and password")
            return

        found = False
        if os.path.exists("passwords.txt"):
            with open("passwords.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role:Student"):
                        stored_username = ""
                        stored_password = ""
                        for j in range(i+1, i+4):
                            if j < len(lines):
                                if lines[j].strip().startswith("Username: "):
                                    stored_username = lines[j].split(":", 1)[1].strip()
                                elif lines[j].strip().startswith("Password: "):
                                    stored_password = lines[j].split(":", 1)[1].strip()
                        if stored_username == username and stored_password == password:
                            found = True
                            break
                    i += 1

        if found:
            student_window()
        else:
            message_box("Invalid username or password")
        
        

    student_login = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = student_login

    heading_std = tk.Label(student_login, text="Student Login", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    username_label = tk.Label(student_login, text="Username", bg=bg_color, fg='white', font=('Times New Roman', 16))
    username_label.place(x=50, y=80)
    username_entry = tk.Entry(student_login)
    username_entry.place(x=160, y=80, width=180)

    password_label = tk.Label(student_login, text="Password", bg=bg_color, fg='white', font=('Times New Roman', 16))
    password_label.place(x=50, y=130)
    password_entry = tk.Entry(student_login, show="*")
    password_entry.place(x=160, y=130, width=180)

    login_btn = tk.Button(student_login, text="Login", command=check_login)
    login_btn.place(x=160, y=190, width=100)

    back_btn = tk.Button(student_login, text="Back", command=login_page)
    back_btn.place(x=160, y=230, width=100)

    student_login.pack(pady=30)
    student_login.pack_propagate(False)
    student_login.configure(width=400, height=420)





##################################################################################################################
###########################____ADMIN__SIDE########################################################################
##################################################################################################################
##################################################################################################################

class adminAuth(StudentManagementSystem):
    def admin_log():
        global current_frame
        clear_frame()

        def check_login():
            username = username_entry.get().strip()
            password = password_entry.get().strip()

            if not username or not password:
                message_box("Please enter both username and password")
                return

            found = False
            if os.path.exists("passwords.txt"):
                with open("passwords.txt", "r") as file:
                    lines = file.readlines()
                    i = 0
                    while i < len(lines):
                        if lines[i].strip().startswith("Role:Admin"):
                            stored_username = ""
                            stored_password = ""
                            for j in range(i+1, i+4):
                                if j < len(lines):
                                    if lines[j].strip().startswith("Username:"):
                                        stored_username = lines[j].split(":", 1)[1].strip()
                                    elif lines[j].strip().startswith("Password:"):
                                        stored_password = lines[j].split(":", 1)[1].strip()
                            if stored_username == username and stored_password == password:
                                found = True
                                break
                        i += 1

            if found:
                admin_window()
            else:
                message_box("Invalid username or password")

        admin_login = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
        current_frame = admin_login

        heading_std = tk.Label(admin_login, text="Admin Login", fg=bg_color, font=('Brush Script MT', 25))
        heading_std.place(x=0, y=0, width=400)

        username_label = tk.Label(admin_login, text="Username", bg=bg_color, fg='white', font=('Times New Roman', 16))
        username_label.place(x=50, y=80)
        username_entry = tk.Entry(admin_login)
        username_entry.place(x=160, y=80, width=180)

        password_label = tk.Label(admin_login, text="Password", bg=bg_color, fg='white', font=('Times New Roman', 16))
        password_label.place(x=50, y=130)
        password_entry = tk.Entry(admin_login, show="*")
        password_entry.place(x=160, y=130, width=180)

        login_btn = tk.Button(admin_login, text="Login", command=check_login)
        login_btn.place(x=160, y=190, width=100)

        back_btn = tk.Button(admin_login, text="Back", command=login_page)
        back_btn.place(x=160, y=230, width=100)

        admin_login.pack(pady=30)
        admin_login.pack_propagate(False)
        admin_login.configure(width=400, height=420)

adAuth=adminAuth

def create_account():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            create_page.destroy()
            student_personal_data()

    def generate_id():
        generated_ID=''
        for r in range(6):
            generated_ID+=str(random.randint(0,9))
        print('id number:',generated_ID)
        student_ID_entry.config(state=tk.NORMAL)
        student_ID_entry.delete(0, tk.END)
        student_ID_entry.insert(tk.END, generated_ID)
        student_ID_entry.config(state='readonly')

    def check_input_validation():
        if student_entry.get()=='':
            message_box(message='Student Name is mandatory')
            return
        elif student_age_entry.get()=='':
            message_box(message='Age must be filled')
            return
        elif not student_age_entry.get().isdigit() :
            message_box(message='Age should be in integer')
            return
        elif student_contact_entry.get()==''or not student_contact_entry.get().isdigit():
            message_box(message='Contact must be filled & integer')
            return
        elif len(student_contact_entry.get())<10:
            message_box(message='Your phone number is invalid')
            return
        elif select_class.get()=='':
            message_box(message='Please select the class')
            return
        
        
        name = student_entry.get()
        gender = gender_var.get()
        age = student_age_entry.get()
        contact = student_contact_entry.get()
        student_class_value = select_class.get()
        student_id = student_ID_entry.get()

            # Prepare a formatted string
        account_data = (
                f"Role: Student\n"
                f"Student ID: {student_id}\n"
                f"Name: {name}\n"
                f"Gender: {gender}\n"
                f"Age: {age}\n"
                f"Contact: {contact}\n"
                f"Class: {student_class_value}\n"
                f"{'-'*40}\n"
            )

            # Save to file (append mode)
        with open("users.txt", "a") as file:
                file.write(account_data)
                message_box("Account created and saved to file!")




    create_page = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = create_page

    heading = tk.Label(create_page, text="Create Account", fg=bg_color, font=('Brush Script MT', 25))
    heading.place(x=0, y=0, width=400)

    student_label = tk.Label(create_page, text="Enter Student Name", font=("Times New Roman", 12), bg=bg_color, fg='white')
    student_label.place(x=5, y=130)
    student_entry = tk.Entry(create_page)
    student_entry.place(x=5, y=160, width=180)

    gender_label = tk.Label(create_page, text="Select gender", font=("Times New Roman", 12), bg=bg_color, fg='white')
    gender_label.place(x=5, y=210)

    gender_var = tk.StringVar()
    gender_M = tk.Radiobutton(create_page, text="MALE", font=("Times New Roman", 12), variable=gender_var, value="Male", bg=bg_color, fg='white', selectcolor=bg_color)
    gender_M.place(x=5, y=240)
    gender_W = tk.Radiobutton(create_page, text="FEMALE", font=("Times New Roman", 12), variable=gender_var, value="Female", bg=bg_color, fg='white', selectcolor=bg_color)
    gender_W.place(x=100, y=240)

    student_age_label = tk.Label(create_page, text="Enter age", font=("Times New Roman", 12), bg=bg_color, fg='white')
    student_age_label.place(x=5, y=275)
    student_age_entry = tk.Entry(create_page)
    student_age_entry.place(x=5, y=305, width=180)

    student_contact_label = tk.Label(create_page, text="Enter contact number", font=("Times New Roman", 12), bg=bg_color, fg='white')
    student_contact_label.place(x=5, y=360)
    student_contact_entry = tk.Entry(create_page)
    student_contact_entry.place(x=5, y=390, width=180)

    student_class_label = tk.Label(create_page, text="Select class", font=("Times New Roman", 12), bg=bg_color, fg='white')
    student_class_label.place(x=5, y=445)
    select_class = Combobox(create_page, state="readonly", values=class_list)
    select_class.place(x=5, y=475, width=180, height=30)

    student_ID_label = tk.Label(create_page, text="Enter Student ID", font=("Times New Roman", 12), bg=bg_color, fg='white')
    student_ID_label.place(x=360, y=125)
    student_ID_entry = tk.Entry(create_page)
    student_ID_entry.place(x=380, y=155, width=80)
    student_ID_entry.config(state='readonly')
    generate_id()


    back_btn = tk.Button(create_page, text="Back", command=redirect_welcome_page)
    back_btn.place(x=290, y=380, width=70)

    submit_btn = tk.Button(create_page, text="Submit", command=check_input_validation)
    submit_btn.place(x=400, y=380, width=70)

    create_page.pack(pady=5)
    create_page.pack_propagate(False)
    create_page.configure(width=480, height=580)


########################_____ADMIN_PERSONAL_DETAILS____#############################################################################
#Admin_Personal_Details
def createadmin_account():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            create_page.destroy()
            Admin_personal_data()


    def check_input_validation():
        if admin_entry.get()=='':
            message_box(message='Student Name is mandatory')
            return
        elif admin_age_entry.get()=='':
            message_box(message='Age must be filled')
            return
        elif not admin_age_entry.get().isdigit() :
            message_box(message='Age should be in integer')
            return
        elif admin_contact_entry.get()==''or not admin_contact_entry.get().isdigit():
            message_box(message='Contact must be filled & integer')
            return
        elif len(admin_contact_entry.get())<10:
            message_box(message='Your phone number is invalid')
            return
                
                # Get form values
        name = admin_entry.get()
        gender = gender_var.get()
        age = admin_age_entry.get()
        contact = admin_contact_entry.get()


            # Prepare a formatted string
        account_data = (
                f"Role: Admin\n"
                f"Name: {name}\n"
                f"Gender: {gender}\n"
                f"Age: {age}\n"
                f"Contact: {contact}\n"
                f"{'-'*40}\n"
            )

            # Save to file (append mode)
        with open("users.txt", "a") as file:
                file.write(account_data)
                message_box("Account created and saved to file!")

    create_page = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = create_page

    heading = tk.Label(create_page, text="Create Account", fg=bg_color, font=('Brush Script MT', 25))
    heading.place(x=0, y=0, width=400)

    admin_label = tk.Label(create_page, text="Enter Admin Name", font=("Times New Roman", 12), bg=bg_color, fg='white')
    admin_label.place(x=5, y=130)
    admin_entry = tk.Entry(create_page)
    admin_entry.place(x=5, y=160, width=180)

    gender_label = tk.Label(create_page, text="Select gender", font=("Times New Roman", 12), bg=bg_color, fg='white')
    gender_label.place(x=5, y=210)

    gender_var = tk.StringVar()
    gender_M = tk.Radiobutton(create_page, text="MALE", font=("Times New Roman", 12), variable=gender_var, value="Male", bg=bg_color, fg='white', selectcolor=bg_color)
    gender_M.place(x=5, y=240)
    gender_W = tk.Radiobutton(create_page, text="FEMALE", font=("Times New Roman", 12), variable=gender_var, value="Female", bg=bg_color, fg='white', selectcolor=bg_color)
    gender_W.place(x=100, y=240)

    admin_age_label = tk.Label(create_page, text="Enter age", font=("Times New Roman", 12), bg=bg_color, fg='white')
    admin_age_label.place(x=5, y=275)
    admin_age_entry = tk.Entry(create_page)
    admin_age_entry.place(x=5, y=305, width=180)

    admin_contact_label = tk.Label(create_page, text="Enter contact number", font=("Times New Roman", 12), bg=bg_color, fg='white')
    admin_contact_label.place(x=5, y=360)
    admin_contact_entry = tk.Entry(create_page)
    admin_contact_entry.place(x=5, y=390, width=180)


    back_btn = tk.Button(create_page, text="Back", command=redirect_welcome_page)
    back_btn.place(x=290, y=380, width=70)

    submit_btn = tk.Button(create_page, text="Submit", command=check_input_validation)
    submit_btn.place(x=400, y=380, width=70)

    create_page.pack(pady=5)
    create_page.pack_propagate(False)
    create_page.configure(width=480, height=580)
###############################################################################################################################
####################################################################################################################


def admin_window():
    global current_frame
    clear_frame()

    admin_role = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = admin_role

    heading_std = tk.Label(admin_role, text="Admin Window", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    new_user_btn = tk.Button(admin_role, text="New Users", font=('Helvetica', 16), fg="red", bg=bg_color, command=new_user)
    new_user_btn.place(x=10, y=80, width=180, height=50)

    student_Personal_btn = tk.Button(admin_role, text="Student Personal\nData", font=('Helvetica', 16), fg="red", bg=bg_color, command=student_personal_data)
    student_Personal_btn.place(x=10, y=180, width=180, height=55)

    Admin_Personal_btn = tk.Button(admin_role, text="Admin Personal\nData", font=('Helvetica', 16), fg="red", bg=bg_color, command=Admin_personal_data)
    Admin_Personal_btn.place(x=10, y=280, width=180, height=55)

    student_Academics_ECA_btn = tk.Button(admin_role, text="Student \n Academics", font=('Helvetica', 16), fg="red", bg=bg_color, command=marks_window)
    student_Academics_ECA_btn.place(x=210, y=80, width=180, height=50)

    student_Insights_btn = tk.Button(admin_role, text="Student \n Insights", font=('Helvetica', 16), fg="red", bg=bg_color, command=student_insights)
    student_Insights_btn.place(x=210, y=180, width=180, height=50)

    student_Insights_btn = tk.Button(admin_role, text="Performance Alert", font=('Helvetica', 16), fg="red", bg=bg_color, command=performance_alerts)
    student_Insights_btn.place(x=210, y=280, width=180, height=50)



    back_btn = tk.Button(admin_role, text="Back", command=login_page, font=('Helvetica',16), fg="red", bg=bg_color)
    back_btn.place(x=120, y=350, width=180, height=50)

    admin_role.pack(pady=30)
    admin_role.pack_propagate(False)
    admin_role.configure(width=400, height=420)

def new_user():
    global current_frame
    clear_frame()

    user_ = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = user_

    heading_std = tk.Label(user_, text="Create New User", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    Add_admin_btn = tk.Button(user_, text="Add Admin", font=('Helvetica', 16), fg="red", bg=bg_color, command=add_new_admin)
    Add_admin_btn.place(x=10, y=80, width=180, height=50)

    Add_student_btn = tk.Button(user_, text="Add Student", font=('Helvetica', 16), fg="red", bg=bg_color, command=add_new_student)
    Add_student_btn.place(x=210, y=80, width=180, height=50)


    back_btn = tk.Button(user_, text="Back", command=admin_window, font=('Helvetica',16), fg="red", bg=bg_color)
    back_btn.place(x=120, y=280, width=180, height=50)

    user_.pack(pady=30)
    user_.pack_propagate(False)
    user_.configure(width=400, height=420)

def add_admin():
    global current_frame
    clear_frame()

    new_admin = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = new_admin

    heading_std = tk.Label(new_admin, text="Admin Login", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    username_label = tk.Label(new_admin, text="Username", bg=bg_color, fg='white', font=('Times New Roman', 16))
    username_label.place(x=50, y=80)
    username_entry = tk.Entry(new_admin)
    username_entry.place(x=160, y=80, width=180)

    password_label = tk.Label(new_admin, text="Password", bg=bg_color, fg='white', font=('Times New Roman', 16))
    password_label.place(x=50, y=130)
    password_entry = tk.Entry(new_admin)
    password_entry.place(x=160, y=130, width=180)

def add_new_admin():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            add_nw_admin.destroy()
            new_user()
    
    def check_input_validation():
        if username_entry.get()=='':
            message_box(message='User Name is mandatory')
        elif password_entry.get()=='':
            message_box(message='Please set a password')

    def submit_form():
        check_input_validation()  # Make sure this is called first

        # Get form values
        username = username_entry.get()
        password = password_entry.get()

        # Prepare a formatted string
        account_data = (
            f"Role:Admin\n"
            f"Username: {username}\n"
            f"Password: {password}\n"
            f"{'-'*40}\n"
        )

        # Save to file (append mode)
        with open("passwords.txt", "a") as file:
            file.write(account_data)

        message_box("Account created and saved to file!")


    add_nw_admin = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = add_nw_admin

    heading_std = tk.Label(add_nw_admin, text="New Admin", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    username_label = tk.Label(add_nw_admin, text="Username", bg=bg_color, fg='white', font=('Times New Roman', 16))
    username_label.place(x=50, y=80)
    username_entry = tk.Entry(add_nw_admin)
    username_entry.place(x=160, y=80, width=180)

    password_label = tk.Label(add_nw_admin, text="Password", bg=bg_color, fg='white', font=('Times New Roman', 16))
    password_label.place(x=50, y=130)
    password_entry = tk.Entry(add_nw_admin)
    password_entry.place(x=160, y=130, width=180)

    submit_btn = tk.Button(add_nw_admin, text="Submit", command=submit_form)
    submit_btn.place(x=160, y=210, width=100)

    back_btn = tk.Button(add_nw_admin, text="Back", command=redirect_welcome_page)
    back_btn.place(x=160, y=290, width=100)

    add_nw_admin.pack(pady=30)
    add_nw_admin.pack_propagate(False)
    add_nw_admin.configure(width=400, height=420)

def add_new_student():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            add_nw_student.destroy()
            new_user()
    
    def check_input_validation():
        if username_entry.get()=='':
            message_box(message='User Name is mandatory')
        elif password_entry.get()=='':
            message_box(message='Please set a password')

    def submit_form():
        check_input_validation()  # Make sure this is called first

        # Get form values
        username = username_entry.get()
        password = password_entry.get()

        # Prepare a formatted string
        account_data = (
            f"Role:Student\n"
            f"Username: {username}\n"
            f"Password: {password}\n"
            f"{'-'*40}\n"
        )

        # Save to file (append mode)
        with open("passwords.txt", "a") as file:
            file.write(account_data)

        message_box("Account created and saved to file!")


    add_nw_student = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = add_nw_student

    heading_std = tk.Label(add_nw_student, text="New Student", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    username_label = tk.Label(add_nw_student, text="Username", bg=bg_color, fg='white', font=('Times New Roman', 16))
    username_label.place(x=50, y=80)
    username_entry = tk.Entry(add_nw_student)
    username_entry.place(x=160, y=80, width=180)

    password_label = tk.Label(add_nw_student, text="Password", bg=bg_color, fg='white', font=('Times New Roman', 16))
    password_label.place(x=50, y=130)
    password_entry = tk.Entry(add_nw_student)
    password_entry.place(x=160, y=130, width=180)

    submit_btn = tk.Button(add_nw_student, text="Submit", command=submit_form)
    submit_btn.place(x=160, y=210, width=100)

    back_btn = tk.Button(add_nw_student, text="Back", command=redirect_welcome_page)
    back_btn.place(x=160, y=290, width=100)

    add_nw_student.pack(pady=30)
    add_nw_student.pack_propagate(False)
    add_nw_student.configure(width=400, height=420)

def student_personal_data():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            std_personal.destroy()
            admin_window()

    std_personal = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = std_personal

    heading_std = tk.Label(std_personal, text="Student Personal Data", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    Add_admin_btn = tk.Button(std_personal, text="Update", font=('Helvetica', 16), fg="red", bg=bg_color, command=create_account)
    Add_admin_btn.place(x=10, y=80, width=180, height=50)

    Add_student_btn = tk.Button(std_personal, text="Modify/Delete", font=('Helvetica', 16), fg="red", bg=bg_color, command=modify_delete_student_details)
    Add_student_btn.place(x=210, y=80, width=180, height=50)

    back_btn = tk.Button(std_personal, text="Back", command=redirect_welcome_page)
    back_btn.place(x=160, y=290, width=100)

    std_personal.pack(pady=30)
    std_personal.pack_propagate(False)
    std_personal.configure(width=400, height=420)

def Admin_personal_data():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            adm_personal.destroy()
            admin_window()

    adm_personal = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = adm_personal

    heading_std = tk.Label(adm_personal, text="Admin Personal Data", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    Add_admin_btn = tk.Button(adm_personal, text="Update", font=('Helvetica', 16), fg="red", bg=bg_color, command=createadmin_account)
    Add_admin_btn.place(x=10, y=80, width=180, height=50)

    Add_student_btn = tk.Button(adm_personal, text="Modify/Delete", font=('Helvetica', 16), fg="red", bg=bg_color, command=modify_delete_admin_details)
    Add_student_btn.place(x=210, y=80, width=180, height=50)

    back_btn = tk.Button(adm_personal, text="Back", command=redirect_welcome_page)
    back_btn.place(x=160, y=290, width=100)

    adm_personal.pack(pady=30)
    adm_personal.pack_propagate(False)
    adm_personal.configure(width=400, height=420)

def marks_window():
    global current_frame
    clear_frame()

    def redirect_welcome_page():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            academics_.destroy()
            admin_window()

    academics_ = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = academics_

    heading_std = tk.Label(academics_, text="Student Academics", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    Add_admin_btn = tk.Button(academics_, text="Update", font=('Helvetica', 16), fg="red", bg=bg_color, command=student_academics)
    Add_admin_btn.place(x=10, y=80, width=180, height=50)

    Add_student_btn = tk.Button(academics_, text="Modify/Delete", font=('Helvetica', 16), fg="red", bg=bg_color, command=modify_delete_grades)
    Add_student_btn.place(x=210, y=80, width=180, height=50)

    update_ECA_btn = tk.Button(academics_, text="Update ECA", font=('Helvetica', 16), fg="red", bg=bg_color, command=update_eca)
    update_ECA_btn.place(x=10, y=150, width=180, height=50)

    modify_ECA_btn = tk.Button(academics_, text="Modify/Delete\n ECA", font=('Helvetica', 16), fg="red", bg=bg_color, command=modify_delete_eca)
    modify_ECA_btn.place(x=210, y=150, width=180, height=50)

    back_btn = tk.Button(academics_, text="Back", command=redirect_welcome_page)
    back_btn.place(x=160, y=290, width=100)

    academics_.pack(pady=30)
    academics_.pack_propagate(False)
    academics_.configure(width=400, height=420)

def student_academics():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        
                        for j in range(i+1, i+5):  
                            if j < len(lines) and lines[j].strip().startswith("Name:"):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students


    def submit_marks():
        selected_student = student_combo.get()
        try:
            marks_it = float(it_entry.get())
            marks_fods = float(fods_entry.get())
            marks_fom = float(fom_entry.get())
            marks_aec = float(aec_entry.get())

            avg_marks = (marks_it + marks_fods + marks_fom + marks_aec) / 4

            grade_data = (
                f"Name: {selected_student}\n"
                f"IT: {marks_it}\n"
                f"FODS: {marks_fods}\n"
                f"FOM: {marks_fom}\n"
                f"AEC: {marks_aec}\n"
                f"Average: {avg_marks}\n"
                f"{'-'*40}\n"
            )

            with open("grades.txt", "a") as f:
                f.write(grade_data)

            message_box(f"Grades saved for {selected_student}!\nAverage: {avg_marks:.2f}")

        except ValueError:
            message_box("Please enter valid numeric marks for all subjects.")

    def redirect_back():
        ans = confirmation_box(message="Do you want to leave this page?")
        if ans:
            student_academic_frame.destroy()
            marks_window()

    student_academic_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = student_academic_frame

    heading = tk.Label(student_academic_frame, text="Student Academics", fg=bg_color, font=('Brush Script MT', 25))
    heading.place(x=0, y=0, width=400)

    # Dropdown for students
    student_label = tk.Label(student_academic_frame, text="Select Student", bg=bg_color, fg='white', font=('Times New Roman', 16))
    student_label.place(x=50, y=50)

    student_combo = Combobox(student_academic_frame, state="readonly", values=get_student_list())
    student_combo.place(x=50, y=80, width=300)
    if student_combo['values']:
        student_combo.current(0)

    # Marks entry
    it_label = tk.Label(student_academic_frame, text="IT Marks:", bg=bg_color, fg='white', font=('Times New Roman', 14))
    it_label.place(x=50, y=130)
    it_entry = tk.Entry(student_academic_frame)
    it_entry.place(x=200, y=130, width=150)

    fods_label = tk.Label(student_academic_frame, text="FODS Marks:", bg=bg_color, fg='white', font=('Times New Roman', 14))
    fods_label.place(x=50, y=170)
    fods_entry = tk.Entry(student_academic_frame)
    fods_entry.place(x=200, y=170, width=150)

    fom_label = tk.Label(student_academic_frame, text="FOM Marks:", bg=bg_color, fg='white', font=('Times New Roman', 14))
    fom_label.place(x=50, y=210)
    fom_entry = tk.Entry(student_academic_frame)
    fom_entry.place(x=200, y=210, width=150)

    aec_label = tk.Label(student_academic_frame, text="AEC Marks:", bg=bg_color, fg='white', font=('Times New Roman', 14))
    aec_label.place(x=50, y=250)
    aec_entry = tk.Entry(student_academic_frame)
    aec_entry.place(x=200, y=250, width=150)

    # Buttons
    submit_btn = tk.Button(student_academic_frame, text="Submit", command=submit_marks)
    submit_btn.place(x=100, y=300, width=100)

    back_btn = tk.Button(student_academic_frame, text="Back", command=redirect_back)
    back_btn.place(x=220, y=300, width=100)

    student_academic_frame.pack(pady=30)
    student_academic_frame.pack_propagate(False)
    student_academic_frame.configure(width=400, height=420)

def modify_delete_grades():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and lines[j].strip().startswith("Name:"):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_grades():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        # Reset entries
        for entry in subject_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("grades.txt"):
            message_box("No grades file found")
            return

        found = False
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    i += 1
                    while i < len(lines) and lines[i].strip() and not lines[i].startswith("-"):
                        for subject in subject_entries:
                            if lines[i].startswith(f"{subject}:"):
                                mark = lines[i].split(":", 1)[1].strip()
                                subject_entries[subject].insert(0, mark)
                        i += 1
                    break
                i += 1
        if not found:
            message_box(f"No grades found of {student_name}")

    def modify_grades():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select student")
            return

        new_marks = {}
        for subject, entry in subject_entries.items():
            mark = entry.get()
            if not mark.isdigit():
                message_box(f"Invalid mark of {subject}")
                return
            new_marks[subject] = int(mark)

        avg = sum(new_marks.values()) / len(new_marks)

        # Update grades.txt
        new_lines = []
        found = False
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip() == f"Name: {student_name}":
                        found = True
                        while i < len(lines) and not lines[i].startswith("-"):
                            i += 1
                        i += 1  
                        new_lines.append(f"Name: {student_name}\n")
                        for subject, mark in new_marks.items():
                            new_lines.append(f"{subject}: {mark}\n")
                        new_lines.append(f"Average: {avg:.2f}\n")
                        new_lines.append("-"*40 + "\n")
                    else:
                        new_lines.append(lines[i])
                        i += 1

        if not found:
            # Add new block if not found
            new_lines.append(f"Name: {student_name}\n")
            for subject, mark in new_marks.items():
                new_lines.append(f"{subject}: {mark}\n")
            new_lines.append(f"Average: {avg:.2f}\n")
            new_lines.append("-"*40 + "\n")

        with open("grades.txt", "w") as file:
            file.writelines(new_lines)

        message_box("Grades updated!")

    def delete_grades():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        if not os.path.exists("grades.txt"):
            message_box("Grades file not found")
            return

        new_lines = []
        found = False
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    while i < len(lines) and not lines[i].startswith("-"):
                        i += 1
                    i += 1 
                else:
                    new_lines.append(lines[i])
                    i += 1

        if found:
            with open("grades.txt", "w") as file:
                file.writelines(new_lines)
            message_box(f"Grades for {student_name} deleted!")
            for entry in subject_entries.values():
                entry.delete(0, tk.END)
        else:
            message_box(f"No grades found for {student_name}")

    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Grades", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(modify_frame, state="readonly", values=get_student_list())
    select_student.pack()

    load_btn = tk.Button(modify_frame, text="Load Grades", command=load_grades)
    load_btn.pack(pady=5)

    subject_entries = {}
    for subject in ["IT", "FODS", "FOM", "AEC"]:
        tk.Label(modify_frame, text=subject, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        subject_entries[subject] = entry

    modify_btn = tk.Button(modify_frame, text="Modify Grades", command=modify_grades)
    modify_btn.pack(pady=5)

    delete_btn = tk.Button(modify_frame, text="Delete Grades", command=delete_grades)
    delete_btn.pack(pady=5)

    back_btn = tk.Button(modify_frame, text="Back", command=student_academics)  # adjust if needed
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)
##################################################################################################
##################################################################################################
##################################################################################################

def modify_delete_student_details():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and (
                                lines[j].strip().startswith("Name:") or lines[j].strip().startswith("Student:")
                            ):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        for entry in detail_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        found = False
        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Student"):
                    block_start = i
                    block_data = {}
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        line = lines[j].strip()
                        if ":" in line:
                            key, value = line.split(":", 1)
                            block_data[key.strip()] = value.strip()
                        j += 1

                    if block_data.get("Name") == student_name or block_data.get("Student") == student_name:
                        found = True
                        for key in detail_entries:
                            if key in block_data:
                                detail_entries[key].insert(0, block_data[key])
                        break
                    i = j
                i += 1

        if not found:
            message_box(f"No details found for {student_name}")

    def modify_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        new_data = {}
        for key, entry in detail_entries.items():
            new_data[key] = entry.get().strip()

        if "Role" not in new_data or new_data["Role"] != "Student":
            new_data["Role"] = "Student"

        new_lines = []
        found = False

        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        block_start = i
                        block_lines = []
                        j = i
                        while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                            block_lines.append(lines[j].strip())
                            j += 1

                        match = False
                        for line in block_lines:
                            if (
                                line == f"Name: {student_name}" or line == f"Student: {student_name}"
                            ):
                                match = True
                                break

                        if match:
                            found = True
                            
                            while i < len(lines) and lines[i].strip() != "-----------------------------------------":
                                i += 1
                            i += 1  

                            
                            new_lines.append("Role: Student\n")
                            for key in detail_entries:
                                new_lines.append(f"{key}: {new_data[key]}\n")
                            new_lines.append("-----------------------------------------\n")
                        else:
                            for line in block_lines:
                                new_lines.append(line + "\n")
                            new_lines.append("-----------------------------------------\n")
                            i = j + 1
                    else:
                        if lines[i].strip() != "-----------------------------------------":
                            new_lines.append(lines[i])
                        i += 1

        if not found:
            new_lines.append("Role: Student\n")
            for key in detail_entries:
                new_lines.append(f"{key}: {new_data[key]}\n")
            new_lines.append("-----------------------------------------\n")

        with open("users.txt", "w") as file:
            file.writelines(new_lines)

        message_box(f"Details updated for {student_name}!")

    def delete_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        new_lines = []
        found = False

        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Student"):
                    block_start = i
                    block_lines = []
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        block_lines.append(lines[j].strip())
                        j += 1

                    match = False
                    for line in block_lines:
                        if (
                            line == f"Name: {student_name}" or line == f"Student: {student_name}"
                        ):
                            match = True
                            break

                    if match:
                        found = True
                        while i < len(lines) and lines[i].strip() != "-----------------------------------------":
                            i += 1
                        i += 1
                    else:
                        for line in block_lines:
                            new_lines.append(line + "\n")
                        new_lines.append("-----------------------------------------\n")
                        i = j + 1
                else:
                    if lines[i].strip() != "-----------------------------------------":
                        new_lines.append(lines[i])
                    i += 1

        if found:
            with open("users.txt", "w") as file:
                file.writelines(new_lines)
            for entry in detail_entries.values():
                entry.delete(0, tk.END)
            message_box(f"Details for {student_name} deleted!")
        else:
            message_box(f"No details found for {student_name}")

    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Student Details", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(modify_frame, state="readonly", values=get_student_list())
    select_student.pack()

    load_btn = tk.Button(modify_frame, text="Load Details", command=load_details)
    load_btn.pack(pady=5)

    detail_entries = {}
    fields = ["Name", "Age", "Email", "Contact"]
    for field in fields:
        tk.Label(modify_frame, text=field, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        detail_entries[field] = entry

    modify_btn = tk.Button(modify_frame, text="Modify Details", command=modify_details)
    modify_btn.pack(pady=5)

    delete_btn = tk.Button(modify_frame, text="Delete Details", command=delete_details)
    delete_btn.pack(pady=5)

    back_btn = tk.Button(modify_frame, text="Back", command=student_academics)  # adjust as needed
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)
    
###############################################################################################
###############################################################################################
def modify_delete_admin_details():
    global current_frame
    clear_frame()

    def get_admin_list():
        admins = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Admin"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and (
                                lines[j].strip().startswith("Name:") or lines[j].strip().startswith("Admin:")
                            ):
                                name = lines[j].split(":", 1)[1].strip()
                                admins.append(name)
                                break
                    i += 1
        return admins

    def load_details():
        admin_name = select_admin.get()
        if not admin_name:
            message_box("Please select an admin")
            return

        for entry in detail_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        found = False
        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Admin"):
                    block_start = i
                    block_data = {}
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        line = lines[j].strip()
                        if ":" in line:
                            key, value = line.split(":", 1)
                            block_data[key.strip()] = value.strip()
                        j += 1

                    if block_data.get("Name") == admin_name or block_data.get("Admin") == admin_name:
                        found = True
                        for key in detail_entries:
                            if key in block_data:
                                detail_entries[key].insert(0, block_data[key])
                        break
                    i = j
                i += 1

        if not found:
            message_box(f"No details found for {admin_name}")

    def modify_details():
        admin_name = select_admin.get()
        if not admin_name:
            message_box("Please select an admin")
            return

        new_data = {}
        for key, entry in detail_entries.items():
            new_data[key] = entry.get().strip()

        if "Role" not in new_data or new_data["Role"] != "Admin":
            new_data["Role"] = "Admin"

        new_lines = []
        found = False

        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Admin"):
                        block_start = i
                        block_lines = []
                        j = i
                        while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                            block_lines.append(lines[j].strip())
                            j += 1

                        match = False
                        for line in block_lines:
                            if (
                                line == f"Name: {admin_name}" or line == f"Admin: {admin_name}"
                            ):
                                match = True
                                break

                        if match:
                            found = True
                            while i < len(lines) and lines[i].strip() != "-----------------------------------------":
                                i += 1
                            i += 1  # skip separator

                            new_lines.append("Role: Admin\n")
                            for key in detail_entries:
                                new_lines.append(f"{key}: {new_data[key]}\n")
                            new_lines.append("-----------------------------------------\n")
                        else:
                            for line in block_lines:
                                new_lines.append(line + "\n")
                            new_lines.append("-----------------------------------------\n")
                            i = j + 1
                    else:
                        if lines[i].strip() != "-----------------------------------------":
                            new_lines.append(lines[i])
                        i += 1

        if not found:
            new_lines.append("Role: Admin\n")
            for key in detail_entries:
                new_lines.append(f"{key}: {new_data[key]}\n")
            new_lines.append("-----------------------------------------\n")

        with open("users.txt", "w") as file:
            file.writelines(new_lines)

        message_box(f"Details updated for {admin_name}!")

    def delete_details():
        admin_name = select_admin.get()
        if not admin_name:
            message_box("Please select an admin")
            return

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        new_lines = []
        found = False

        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Admin"):
                    block_start = i
                    block_lines = []
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        block_lines.append(lines[j].strip())
                        j += 1

                    match = False
                    for line in block_lines:
                        if (
                            line == f"Name: {admin_name}" or line == f"Admin: {admin_name}"
                        ):
                            match = True
                            break

                    if match:
                        found = True
                        while i < len(lines) and lines[i].strip() != "-----------------------------------------":
                            i += 1
                        i += 1  # skip separator
                    else:
                        for line in block_lines:
                            new_lines.append(line + "\n")
                        new_lines.append("-----------------------------------------\n")
                        i = j + 1
                else:
                    if lines[i].strip() != "-----------------------------------------":
                        new_lines.append(lines[i])
                    i += 1

        if found:
            with open("users.txt", "w") as file:
                file.writelines(new_lines)
            for entry in detail_entries.values():
                entry.delete(0, tk.END)
            message_box(f"Details for {admin_name} deleted!")
        else:
            message_box(f"No details found for {admin_name}")

    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Admin Details", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Admin", bg=bg_color, fg='white').pack()
    select_admin = Combobox(modify_frame, state="readonly", values=get_admin_list())
    select_admin.pack()

    load_btn = tk.Button(modify_frame, text="Load Details", command=load_details)
    load_btn.pack(pady=5)

    detail_entries = {}
    fields = ["Name", "Age", "Email", "Contact"]
    for field in fields:
        tk.Label(modify_frame, text=field, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        detail_entries[field] = entry

    modify_btn = tk.Button(modify_frame, text="Modify Details", command=modify_details)
    modify_btn.pack(pady=5)

    delete_btn = tk.Button(modify_frame, text="Delete Details", command=delete_details)
    delete_btn.pack(pady=5)

    back_btn = tk.Button(modify_frame, text="Back", command=admin_window)  # adjust to your navigation
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)

###########################################################################################################
###########################################################################################################

def update_eca():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and lines[j].strip().startswith("Name:"):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def save_eca():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        selected_activities = [activity for activity, var in eca_vars.items() if var.get() == 1]

        if not selected_activities:
            message_box("Please select at least one ECA activity")
            return

        with open("eca.txt", "a") as file:
            file.write(f"Name: {student_name}\n")
            file.write("Activities:\n")
            for activity in selected_activities:
                file.write(f"- {activity}\n")
            file.write("-----------------------------------------\n")

        message_box(f"ECA activities saved for {student_name}!")

        # Clear selections
        for var in eca_vars.values():
            var.set(0)

    # Build frame
    eca_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = eca_frame

    heading = tk.Label(eca_frame, text="Update ECA Activities", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(eca_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(eca_frame, state="readonly", values=get_student_list())
    select_student.pack(pady=5)

    tk.Label(eca_frame, text="Select Activities:", bg=bg_color, fg='white').pack(pady=5)

    eca_activities = ["Sports", "Music", "Debate", "Drama", "Art", "Science Club"]
    eca_vars = {}

    for activity in eca_activities:
        var = tk.IntVar()
        chk = tk.Checkbutton(eca_frame, text=activity, variable=var, bg=bg_color, fg='white',
                             selectcolor=bg_color, activebackground=bg_color)
        chk.pack(anchor='w', padx=20)
        eca_vars[activity] = var

    save_btn = tk.Button(eca_frame, text="Save ECA", command=save_eca)
    save_btn.pack(pady=10)

    back_btn = tk.Button(eca_frame, text="Back", command=student_academics)  # Adjust if needed
    back_btn.pack(pady=10)

    eca_frame.pack(pady=30)
    eca_frame.pack_propagate(False)
    eca_frame.configure(width=400, height=550)
######################################################################################################
######################################################################################################
def modify_delete_eca():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and lines[j].strip().startswith("Name:"):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_eca():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        for var in eca_vars.values():
            var.set(0)

        if not os.path.exists("eca.txt"):
            message_box("No ECA file found")
            return

        found = False
        with open("eca.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    i += 1  # Skip 'Name:'
                    if i < len(lines) and lines[i].strip() == "Activities:":
                        i += 1
                        while i < len(lines) and lines[i].startswith("-"):
                            activity = lines[i].strip()[2:].strip()
                            if activity in eca_vars:
                                eca_vars[activity].set(1)
                            i += 1
                    break
                i += 1
        if not found:
            message_box(f"No ECA activities found for {student_name}")

    def modify_eca():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        selected_activities = [activity for activity, var in eca_vars.items() if var.get() == 1]

        if not selected_activities:
            message_box("Please select at least one ECA activity")
            return

        new_lines = []
        found = False
        if os.path.exists("eca.txt"):
            with open("eca.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip() == f"Name: {student_name}":
                        found = True
                        while i < len(lines) and not lines[i].startswith("-" * 10):
                            i += 1
                        i += 1  # Skip separator
                        new_lines.append(f"Name: {student_name}\n")
                        new_lines.append("Activities:\n")
                        for activity in selected_activities:
                            new_lines.append(f"- {activity}\n")
                        new_lines.append("-" * 40 + "\n")
                    else:
                        new_lines.append(lines[i])
                        i += 1

        if not found:
            new_lines.append(f"Name: {student_name}\n")
            new_lines.append("Activities:\n")
            for activity in selected_activities:
                new_lines.append(f"- {activity}\n")
            new_lines.append("-" * 40 + "\n")

        with open("eca.txt", "w") as file:
            file.writelines(new_lines)

        message_box(f"ECA activities updated for {student_name}!")

    def delete_eca():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        if not os.path.exists("eca.txt"):
            message_box("ECA file not found")
            return

        new_lines = []
        found = False
        with open("eca.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    while i < len(lines) and not lines[i].startswith("-" * 10):
                        i += 1
                    i += 1  # Skip separator
                else:
                    new_lines.append(lines[i])
                    i += 1

        if found:
            with open("eca.txt", "w") as file:
                file.writelines(new_lines)
            message_box(f"ECA activities for {student_name} deleted!")
            for var in eca_vars.values():
                var.set(0)
        else:
            message_box(f"No ECA activities found for {student_name}")

    # Frame
    eca_modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = eca_modify_frame

    heading = tk.Label(eca_modify_frame, text="Modify/Delete ECA Activities", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(eca_modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(eca_modify_frame, state="readonly", values=get_student_list())
    select_student.pack(pady=5)

    load_btn = tk.Button(eca_modify_frame, text="Load Activities", command=load_eca)
    load_btn.pack(pady=5)

    tk.Label(eca_modify_frame, text="ECA Activities:", bg=bg_color, fg='white').pack(pady=5)

    eca_activities = ["Sports", "Music", "Debate", "Drama", "Art", "Science Club"]
    eca_vars = {}

    for activity in eca_activities:
        var = tk.IntVar()
        chk = tk.Checkbutton(eca_modify_frame, text=activity, variable=var, bg=bg_color, fg='white',
                             selectcolor=bg_color, activebackground=bg_color)
        chk.pack(anchor='w', padx=20)
        eca_vars[activity] = var

    modify_btn = tk.Button(eca_modify_frame, text="Modify ECA", command=modify_eca)
    modify_btn.pack(pady=5)

    delete_btn = tk.Button(eca_modify_frame, text="Delete ECA", command=delete_eca)
    delete_btn.pack(pady=5)

    back_btn = tk.Button(eca_modify_frame, text="Back", command=student_academics)  # Adjust if needed
    back_btn.pack(pady=10)

    eca_modify_frame.pack(pady=30)
    eca_modify_frame.pack_propagate(False)
    eca_modify_frame.configure(width=400, height=550)

##########################################################################################################
##########################################################################################################
def student_insights():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip().startswith("Name:"):
                        name = line.split(":", 1)[1].strip()
                        if name not in students:
                            students.append(name)
        return students

    def show_insights():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        subjects = []
        marks = []

        if not os.path.exists("grades.txt"):
            message_box("No grades.txt found!")
            return

        # Load grades
        found = False
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    i += 1
                    while i < len(lines) and lines[i].strip() and not lines[i].startswith("-"):
                        if ":" in lines[i]:
                            key, value = lines[i].split(":", 1)
                            key = key.strip()
                            value = value.strip()
                            if key not in ["Name", "Average"]:
                                subjects.append(key)
                                marks.append(float(value))
                        i += 1
                    break
                i += 1

        if not found:
            message_box(f"No grades found for {student_name}")
            return

        avg_mark = sum(marks) / len(marks) if marks else 0

        # Show bar chart with matplotlib
        fig = plt.Figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(subjects, marks, color='skyblue')
        ax.set_title(f"{student_name}'s Grades")
        ax.set_ylabel('Marks')

        # Clear old chart
        for widget in chart_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Load ECA data
        eca_list = []
        if os.path.exists("eca.txt"):
            with open("eca.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip() == f"Name: {student_name}":
                        i += 1
                        if i < len(lines) and lines[i].strip() == "Activities:":
                            i += 1
                            while i < len(lines) and lines[i].startswith("-"):
                                eca_list.append(lines[i][2:].strip())
                                i += 1
                        break
                    i += 1

        # Correlation display
        eca_count = len(eca_list)
        correlation_text = f"ECA Activities Involved: {', '.join(eca_list) if eca_list else 'None'}\n"
        correlation_text += f"Number of ECAs: {eca_count}\n"
        correlation_text += f"Average Marks: {avg_mark:.2f}\n"

        if eca_count >= 3:
            correlation_text += "Insight: High ECA involvement. Great balance!\n"
        elif eca_count == 0:
            correlation_text += "Insight: No ECA involvement. May focus more on academics.\n"
        else:
            correlation_text += "Insight: Moderate ECA involvement."

        insights_label.config(text=correlation_text)

    # Frame setup
    insights_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = insights_frame

    heading = tk.Label(insights_frame, text="Student Insights", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(insights_frame, text="Select Student:", bg=bg_color, fg='white').pack()
    select_student = Combobox(insights_frame, state="readonly", values=get_student_list())
    select_student.pack(pady=5)

    load_btn = tk.Button(insights_frame, text="Show Insights", command=show_insights)
    load_btn.pack(pady=5)

    chart_frame = tk.Frame(insights_frame, bg=bg_color)
    chart_frame.pack(pady=10)

    insights_label = tk.Label(insights_frame, text="", bg=bg_color, fg='white', justify="left")
    insights_label.pack(pady=5)

    back_btn = tk.Button(insights_frame, text="Back", command=admin_window)  # adjust as needed
    back_btn.pack(pady=10)

    insights_frame.pack(pady=30)
    insights_frame.pack_propagate(False)
    insights_frame.configure(width=500, height=600)
######################################################################################################################
######################################################################################################################
#######################################################################################################################


######################################################################################################################
############################################_____STUDENT__SIDE___________########################################################
######################################################################################################################

def student_window():
    global current_frame
    clear_frame()

    student_role = tk.Frame(root, highlightbackground="red", highlightthickness=3, background=bg_color)
    current_frame = student_role

    heading_std = tk.Label(student_role, text="Student Window", fg=bg_color, font=('Brush Script MT', 25))
    heading_std.place(x=0, y=0, width=400)

    profile_btn = tk.Button(student_role, text="Update Profile", font=('Helvetica', 16), fg="red", bg=bg_color, command=modify_student_details)
    profile_btn.place(x=10, y=80, width=180, height=50)

    view_profile_btn = tk.Button(student_role, text="View Profile", font=('Helvetica', 16), fg="red", bg=bg_color, command=view_student_details)
    view_profile_btn.place(x=10, y=180, width=180, height=55)

    view_ECA_btn = tk.Button(student_role, text="View ECA", font=('Helvetica', 16), fg="red", bg=bg_color, command=student_Eca)
    view_ECA_btn.place(x=10, y=280, width=180, height=55)

    view_Grades_btn = tk.Button(student_role, text="View Grades", font=('Helvetica', 16), fg="red", bg=bg_color, command=view_grades)
    view_Grades_btn.place(x=210, y=80, width=180, height=50)




    back_btn = tk.Button(student_role, text="Back", font=('Helvetica',16), fg="red", bg=bg_color, command=std_login)
    back_btn.place(x=120, y=350, width=180, height=50)

    student_role.pack(pady=30)
    student_role.pack_propagate(False)
    student_role.configure(width=400, height=420)

###############################################################################################################################
###############################################################################################################################

def modify_student_details():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and (
                                lines[j].strip().startswith("Name:") or lines[j].strip().startswith("Student:")
                            ):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        for entry in detail_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        found = False
        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Student"):
                    block_start = i
                    block_data = {}
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        line = lines[j].strip()
                        if ":" in line:
                            key, value = line.split(":", 1)
                            block_data[key.strip()] = value.strip()
                        j += 1

                    if block_data.get("Name") == student_name or block_data.get("Student") == student_name:
                        found = True
                        for key in detail_entries:
                            if key in block_data:
                                detail_entries[key].insert(0, block_data[key])
                        break
                    i = j
                i += 1

        if not found:
            message_box(f"No details found for {student_name}")

    def modify_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        new_data = {}
        for key, entry in detail_entries.items():
            new_data[key] = entry.get().strip()

        if "Role" not in new_data or new_data["Role"] != "Student":
            new_data["Role"] = "Student"

        new_lines = []
        found = False

        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        block_start = i
                        block_lines = []
                        j = i
                        while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                            block_lines.append(lines[j].strip())
                            j += 1

                        match = False
                        for line in block_lines:
                            if (
                                line == f"Name: {student_name}" or line == f"Student: {student_name}"
                            ):
                                match = True
                                break

                        if match:
                            found = True
                            
                            while i < len(lines) and lines[i].strip() != "-----------------------------------------":
                                i += 1
                            i += 1  

                            
                            new_lines.append("Role: Student\n")
                            for key in detail_entries:
                                new_lines.append(f"{key}: {new_data[key]}\n")
                            new_lines.append("-----------------------------------------\n")
                        else:
                            for line in block_lines:
                                new_lines.append(line + "\n")
                            new_lines.append("-----------------------------------------\n")
                            i = j + 1
                    else:
                        if lines[i].strip() != "-----------------------------------------":
                            new_lines.append(lines[i])
                        i += 1

        if not found:
            new_lines.append("Role: Student\n")
            for key in detail_entries:
                new_lines.append(f"{key}: {new_data[key]}\n")
            new_lines.append("-----------------------------------------\n")

        with open("users.txt", "w") as file:
            file.writelines(new_lines)

        message_box(f"Details updated for {student_name}!")



        if found:
            with open("users.txt", "w") as file:
                file.writelines(new_lines)
            for entry in detail_entries.values():
                entry.delete(0, tk.END)
            message_box(f"Details for {student_name} deleted!")
        else:
            message_box(f"No details found for {student_name}")

    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Student Details", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(modify_frame, state="readonly", values=get_student_list())
    select_student.pack()

    load_btn = tk.Button(modify_frame, text="Load Details", command=load_details)
    load_btn.pack(pady=5)

    detail_entries = {}
    fields = ["Name", "Age", "Email", "Contact"]
    for field in fields:
        tk.Label(modify_frame, text=field, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        detail_entries[field] = entry

    modify_btn = tk.Button(modify_frame, text="Modify Details", command=modify_details)
    modify_btn.pack(pady=5)

    back_btn = tk.Button(modify_frame, text="Back", command=student_window)  # adjust as needed
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)

##########################################################################################################################
##########################################################################################################################

def view_student_details():
    global current_frame
    clear_frame()

    

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and (
                                lines[j].strip().startswith("Name:") or lines[j].strip().startswith("Student:")
                            ):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        for entry in detail_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        found = False
        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Student"):
                    block_start = i
                    block_data = {}
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        line = lines[j].strip()
                        if ":" in line:
                            key, value = line.split(":", 1)
                            block_data[key.strip()] = value.strip()
                        j += 1

                    if block_data.get("Name") == student_name or block_data.get("Student") == student_name:
                        found = True
                        for key in detail_entries:
                            if key in block_data:
                                detail_entries[key].insert(0, block_data[key])
                        break
                    i = j
                i += 1

        if not found:
            message_box(f"No details found for {student_name}")

    


    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Student Details", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(modify_frame, state="readonly", values=get_student_list())
    select_student.pack()

    load_btn = tk.Button(modify_frame, text="Load Details", command=load_details)
    load_btn.pack(pady=5)

    detail_entries = {}
    fields = ["Name", "Age", "Email", "Contact"]
    for field in fields:
        tk.Label(modify_frame, text=field, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        detail_entries[field] = entry
    


    back_btn = tk.Button(modify_frame, text="Back", command=student_window)  # adjust as needed
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)
   ################################################################################################################
   ################################################################################################################ 


def view_grades():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and lines[j].strip().startswith("Name:"):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_grades():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        # Reset entries
        for entry in subject_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("grades.txt"):
            message_box("No grades file found")
            return

        found = False
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    i += 1
                    while i < len(lines) and lines[i].strip() and not lines[i].startswith("-"):
                        for subject in subject_entries:
                            if lines[i].startswith(f"{subject}:"):
                                mark = lines[i].split(":", 1)[1].strip()
                                subject_entries[subject].insert(0, mark)
                        i += 1
                    break
                i += 1
        if not found:
            message_box(f"No grades found of {student_name}")

    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Grades", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(modify_frame, state="readonly", values=get_student_list())
    select_student.pack()

    load_btn = tk.Button(modify_frame, text="Load Grades", command=load_grades)
    load_btn.pack(pady=5)

    subject_entries = {}
    for subject in ["IT", "FODS", "FOM", "AEC"]:
        tk.Label(modify_frame, text=subject, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        subject_entries[subject] = entry

    back_btn = tk.Button(modify_frame, text="Back", command=student_window)  # adjust if needed
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)


def student_Eca():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip().startswith("Name:"):
                        name = line.split(":", 1)[1].strip()
                        if name not in students:
                            students.append(name)
        return students

    def show_insights():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        subjects = []
        marks = []

        if not os.path.exists("grades.txt"):
            message_box("No grades.txt found!")
            return

        # Load grades
        found = False
        with open("grades.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == f"Name: {student_name}":
                    found = True
                    i += 1
                    while i < len(lines) and lines[i].strip() and not lines[i].startswith("-"):
                        if ":" in lines[i]:
                            key, value = lines[i].split(":", 1)
                            key = key.strip()
                            value = value.strip()
                            if key not in ["Name", "Average"]:
                                subjects.append(key)
                                marks.append(float(value))
                        i += 1
                    break
                i += 1

        if not found:
            message_box(f"No grades found for {student_name}")
            return

        avg_mark = sum(marks) / len(marks) if marks else 0

        # Show bar chart with matplotlib
        fig = plt.Figure(figsize=(4, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(subjects, marks, color='skyblue')
        ax.set_title(f"{student_name}'s Grades")
        ax.set_ylabel('Marks')

        # Clear old chart
        for widget in chart_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Load ECA data
        eca_list = []
        if os.path.exists("eca.txt"):
            with open("eca.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip() == f"Name: {student_name}":
                        i += 1
                        if i < len(lines) and lines[i].strip() == "Activities:":
                            i += 1
                            while i < len(lines) and lines[i].startswith("-"):
                                eca_list.append(lines[i][2:].strip())
                                i += 1
                        break
                    i += 1

        # Correlation display
        eca_count = len(eca_list)
        correlation_text = f"ECA Activities Involved: {', '.join(eca_list) if eca_list else 'None'}\n"
        correlation_text += f"Number of ECAs: {eca_count}\n"
        correlation_text += f"Average Marks: {avg_mark:.2f}\n"

        if eca_count >= 3:
            correlation_text += "Insight: High ECA involvement. Great balance!\n"
        elif eca_count == 0:
            correlation_text += "Insight: No ECA involvement. May focus more on academics.\n"
        else:
            correlation_text += "Insight: Moderate ECA involvement."

        insights_label.config(text=correlation_text)

    # Frame setup
    insights_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = insights_frame

    heading = tk.Label(insights_frame, text="Student Insights", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(insights_frame, text="Select Student:", bg=bg_color, fg='white').pack()
    select_student = Combobox(insights_frame, state="readonly", values=get_student_list())
    select_student.pack(pady=5)

    load_btn = tk.Button(insights_frame, text="Show Insights", command=show_insights)
    load_btn.pack(pady=5)

    chart_frame = tk.Frame(insights_frame, bg=bg_color)
    chart_frame.pack(pady=10)

    insights_label = tk.Label(insights_frame, text="", bg=bg_color, fg='white', justify="left")
    insights_label.pack(pady=5)

    back_btn = tk.Button(insights_frame, text="Back", command=student_window)  # adjust as needed
    back_btn.pack(pady=5)

    insights_frame.pack(pady=30)
    insights_frame.pack_propagate(False)
    insights_frame.configure(width=500, height=600)



def modify_student_details():
    global current_frame
    clear_frame()

    def get_student_list():
        students = []
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        for j in range(i+1, i+5):
                            if j < len(lines) and (
                                lines[j].strip().startswith("Name:") or lines[j].strip().startswith("Student:")
                            ):
                                name = lines[j].split(":", 1)[1].strip()
                                students.append(name)
                                break
                    i += 1
        return students

    def load_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        for entry in detail_entries.values():
            entry.delete(0, tk.END)

        if not os.path.exists("users.txt"):
            message_box("No users file found")
            return

        found = False
        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip().startswith("Role: Student"):
                    block_start = i
                    block_data = {}
                    j = i
                    while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                        line = lines[j].strip()
                        if ":" in line:
                            key, value = line.split(":", 1)
                            block_data[key.strip()] = value.strip()
                        j += 1

                    if block_data.get("Name") == student_name or block_data.get("Student") == student_name:
                        found = True
                        for key in detail_entries:
                            if key in block_data:
                                detail_entries[key].insert(0, block_data[key])
                        break
                    i = j
                i += 1

        if not found:
            message_box(f"No details found for {student_name}")

    def modify_details():
        student_name = select_student.get()
        if not student_name:
            message_box("Please select a student")
            return

        new_data = {}
        for key, entry in detail_entries.items():
            new_data[key] = entry.get().strip()

        if "Role" not in new_data or new_data["Role"] != "Student":
            new_data["Role"] = "Student"

        new_lines = []
        found = False

        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip().startswith("Role: Student"):
                        block_start = i
                        block_lines = []
                        j = i
                        while j < len(lines) and lines[j].strip() != "-----------------------------------------":
                            block_lines.append(lines[j].strip())
                            j += 1

                        match = False
                        for line in block_lines:
                            if (
                                line == f"Name: {student_name}" or line == f"Student: {student_name}"
                            ):
                                match = True
                                break

                        if match:
                            found = True
                            
                            while i < len(lines) and lines[i].strip() != "-----------------------------------------":
                                i += 1
                            i += 1  

                            
                            new_lines.append("Role: Student\n")
                            for key in detail_entries:
                                new_lines.append(f"{key}: {new_data[key]}\n")
                            new_lines.append("-----------------------------------------\n")
                        else:
                            for line in block_lines:
                                new_lines.append(line + "\n")
                            new_lines.append("-----------------------------------------\n")
                            i = j + 1
                    else:
                        if lines[i].strip() != "-----------------------------------------":
                            new_lines.append(lines[i])
                        i += 1

        if not found:
            new_lines.append("Role: Student\n")
            for key in detail_entries:
                new_lines.append(f"{key}: {new_data[key]}\n")
            new_lines.append("-----------------------------------------\n")

        with open("users.txt", "w") as file:
            file.writelines(new_lines)

        message_box(f"Details updated for {student_name}!")


    # Build frame
    modify_frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = modify_frame

    heading = tk.Label(modify_frame, text="Modify/Delete Student Details", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(modify_frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(modify_frame, state="readonly", values=get_student_list())
    select_student.pack()

    load_btn = tk.Button(modify_frame, text="Load Details", command=load_details)
    load_btn.pack(pady=5)

    detail_entries = {}
    fields = ["Name", "Age", "Email", "Contact"]
    for field in fields:
        tk.Label(modify_frame, text=field, bg=bg_color, fg='white').pack()
        entry = tk.Entry(modify_frame)
        entry.pack()
        detail_entries[field] = entry

    modify_btn = tk.Button(modify_frame, text="Modify Details", command=modify_details)
    modify_btn.pack(pady=5)


    back_btn = tk.Button(modify_frame, text="Back", command=student_window)  # adjust as needed
    back_btn.pack(pady=10)

    modify_frame.pack(pady=30)
    modify_frame.pack_propagate(False)
    modify_frame.configure(width=400, height=550)



def performance_alerts():
    global current_frame
    clear_frame()

    def get_students():
        students = []
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip().startswith("Name:"):
                        students.append(line.split(":", 1)[1].strip())
        return students

    def check_performance():
        student = select_student.get()
        if not student:
            message_box("Please select a student")
            return

        avg = None
        if os.path.exists("grades.txt"):
            with open("grades.txt", "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip() == f"Name: {student}":
                        i += 1
                        while i < len(lines):
                            if lines[i].strip().startswith("Average:"):
                                avg = float(lines[i].split(":", 1)[1].strip())
                                break
                            i += 1
                        break
                    i += 1

        if avg is None:
            message_box(f"No grades found for {student}")
            return

        if avg < 40:
            message = f"{student} is performing below threshold.\nAverage: {avg}\nSuggested Intervention:\n- Arrange extra classes\n- Provide mentoring\n- Parental involvement"
        else:
            message = f"{student} is performing well.\nAverage: {avg}"

        message_box(message)

    frame = tk.Frame(root, highlightbackground="red", highlightthickness=3, bg=bg_color)
    current_frame = frame

    heading = tk.Label(frame, text="Performance Alerts", fg=bg_color, font=('Brush Script MT', 25))
    heading.pack(pady=10)

    tk.Label(frame, text="Select Student", bg=bg_color, fg='white').pack()
    select_student = Combobox(frame, state="readonly", values=get_students())
    select_student.pack(pady=5)

    check_btn = tk.Button(frame, text="Check Performance", command=check_performance)
    check_btn.pack(pady=10)

    back_btn = tk.Button(frame, text="Back", command=admin_window)  # adjust as needed
    back_btn.pack(pady=10)

    frame.pack(pady=30)
    frame.pack_propagate(False)
    frame.configure(width=400, height=400)

if __name__=="__main__":
    login_page()
    root.mainloop()