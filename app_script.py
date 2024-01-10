# Project HouseHosters :)
# imports

import tkinter
# from tkinter import *
# import webbrowser

# predefineed functions
user_name = "sampler nameson"
register_name_entry = "Sample User"
prop1_name = "prop1"
prop2_name = "prop2"
prop3_name = "prop3"
prop4_name = "prop4"

# functions
# opens the homepage
def open_prop1_win():
    prop1 = tkinter.Tk()
    prop1.title("Property Name")
    frame_property = tkinter.Frame(prop1)
    frame_property.grid(row=1, column=0)
    prop1_frame = tkinter.LabelFrame(prop1, text="Links")
    prop1_frame.grid(row=0, column=0, padx=20, pady=20)
    airbnb  = tkinter.Label(prop1_frame, text=(f"Welcome, {register_name_entry}."))
    #welcome_label.grid(row=0, column=0) check this line

def open_home():
    home_page = tkinter.Tk()
    home_page.title("Home Page")

    home_frame = tkinter.LabelFrame(home_page, text="Properties:")
    home_frame.grid(row=1, column=0)

#homelist_frame.grid(row=1, column=0, padx=20, pady=20)
    welcome_label = tkinter.Label(home_frame, text=(f"Welcome, {register_name_entry}."))
    welcome_label.grid(row=0, column=0)

    prop1_button = tkinter.Button(home_frame, text=("Property 1: "+ (prop1_name)), command=open_prop1_win)
    prop1_button.grid(row=4, column=0, padx=20, pady=10)

    prop2_button = tkinter.Button(home_frame, text=("Property 2: "+ (prop2_name)))
    prop2_button.grid(row=5, column=0, padx=20, pady=10)

    prop3_button = tkinter.Button(home_frame, text=("Property 3: "+ (prop3_name)))
    prop3_button.grid(row=6, column=0, padx=20, pady=10)

    prop4_button = tkinter.Button(home_frame, text=("Property 4: "+ (prop4_name)))
    prop4_button.grid(row=7, column=0, padx=20, pady=10)
# add all command = open_prop(number)_win and make functions
    home_page.mainloop()


# checks the credentials of the user (login page)
def check_creds():
    email = email_entry.get()
    password = pass_entry.get()
    correct_email = "example@email.com"
    correct_password = "PassWord123!"
    print("Email : ", email, "Password : ", password)
    if email == correct_email and password == correct_password:
        email_label = tkinter.Label(login_frame, text="Login Successful!", fg="green")
        email_label.grid(row=1, column=0)
        login_frame.grid(row=0, column=0, padx=20, pady=20)
        open_home()
    else:
        result_label.config(text = "Login failed. Invalid credentials.", fg="red")

# shows the password for user to double check
def show_password():
    pass_entry.config(show="")

def open_register_page():
    register_win = tkinter.Tk()
    register_win.title("Registration")

    register_win_frame = tkinter.LabelFrame(register_win, text="Enter your details:")
    register_win_frame.grid(row=0, column=0, padx=20, pady=20)

    register_email_label = tkinter.Label(register_win_frame, text="Email:")
    register_email_label.grid(row=1, column=0)

    register_email_entry = tkinter.Entry(register_win_frame)
    register_email_entry.grid(row=2, column=0)

    register_pass_label = tkinter.Label(register_win_frame, text="Password:")
    register_pass_label.grid(row=3, column=0)

    register_pass_entry = tkinter.Entry(register_win_frame)
    register_pass_entry.config(show="*")
    register_pass_entry.grid(row=4, column=0)

    register_pass_entry2 = tkinter.Entry(register_win_frame)
    register_pass_entry2.grid(row=5, column=0)

    register_name_label = tkinter.Label(register_win_frame, text="Name:")
    register_name_label.grid(row=6, column=0)

    register_name_entry = tkinter.Entry(register_win_frame)
    register_name_entry.grid(row=7, column=0)

    def checkPass():
        password1 = register_pass_entry.get()
        password2 = register_pass_entry2.get()
        email = register_name_entry.get()
        if password1 == password2 and "@" in email :
            passmatch_label = tkinter.Label(register_win_frame, text="Register Successful.", fg="green")
            passmatch_label.grid(row=1, column=0)
        else:
            passnotmatch_label = tkinter.Label(register_win_frame, text="Register unsuccessful. Make sure your email is valid, and both passwords match.", fg="red")
            passnotmatch_label.grid(row=1, column=0)
            enterDetails()

    def enterDetails():
        email = register_email_entry.get()
        password = register_pass_entry.get()
        name = register_name_entry.get()

        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Name: {name}")


    register_button = tkinter.Button(register_win, text="Register", command=checkPass)
    register_button.grid(row=8, column=0, padx=20, pady=10)

    register_win.mainloop()

print("hello")
login_window = tkinter.Tk()
login_window.title("Login Page")
frame = tkinter.Frame(login_window)
frame.pack()
login_frame = tkinter.LabelFrame(frame, text="log in")
login_frame.grid(row=0, column=0, padx=20, pady=20)

app_label = tkinter.Label(login_frame, text="HouseHosters😌")
app_label.grid(row=0, column=0)

email_label = tkinter.Label(login_frame, text="email :")
email_label.grid(row=1, column=0)

pass_label = tkinter.Label(login_frame, text="password :")
pass_label.grid(row=3, column=0)

email_entry = tkinter.Entry(login_frame)
email_entry.grid(row=2, column=0)

pass_entry = tkinter.Entry(login_frame)
pass_entry.config(show="*")
pass_entry.grid(row=4, column=0)

show_pass=tkinter.Button(login_frame, text="show password", command=show_password)
show_pass.grid(row=5, column=0, padx=20, pady=10)

login_button = tkinter.Button(frame, text="log in", command=check_creds)
login_button.grid(row=4, column=0, padx=20, pady=10)

register_button = tkinter.Button(frame, text="new account? register", command = open_register_page)
register_button.grid(row=5, column=0, padx=20, pady=10)

result_label = tkinter.Label( text="", fg="black")
result_label.pack()

login_window.mainloop()




# notes:
# to close previous window, add window.destroy()
# JUst text box to write anything then:
# >>> window = tk.Tk()
# >>> text_box = tk.Text()
# >>> text_box.pack()
# # open hyperlink
# def callback(url):
#     webbrowser.open_new(url)
