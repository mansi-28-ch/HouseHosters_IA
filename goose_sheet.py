# Project HouseHosters :)
# imports
import tkinter
import webbrowser
from functools import partial

# predefineed variables
user_name = "sampler nameson"
register_name_entry = "Sample User"
prop1_name = "prop1"
prop2_name = "prop2"
prop3_name = "prop3"
prop4_name = "prop4"
new = 1
url = "https://www.google.com"
# functions
def openLink(entry_widget1):
    url = entry_widget1.get()
    webbrowser.open(url, new=new)

def resetPropName(entry_widget, label_widget):
    prop_name = entry_widget.get()
    label_widget.config(text=f"P1: {prop_name}")

def check_creds():
    email = email_entry.get()
    password = pass_entry.get()
    correct_email = "e.com"
    correct_password = "pass"
    print("Email : ", email, "Password : ", password)
    if email == correct_email and password == correct_password:
        email_label = tkinter.Label(loginFrame, text="Login Successful!", fg="green")
        email_label.grid(row=1, column=0)
        loginFrame.grid(row=0, column=0, padx=20, pady=20)
        open_home()
    else:
        result_label.config(text = "Login failed. Invalid credentials.", fg="red")
# shows the password for user to double check
def show_password():
    pass_entry.config(show="")


    def checkPass():
        password1 = register_pass_entry.get()
        password2 = register_pass_entry2.get()
        email = register_name_entry.get()

        if password1 == password2 and "@" in email:
            passmatch_label = tkinter.Label(register_win_frame, text="Register Successful.", fg="green")
            passmatch_label.grid(row=1, column=0)
        else:
            passnotmatch_label = tkinter.Label(register_win_frame,
                                               text="Register unsuccessful. Make sure your email is valid, and both passwords match.",
                                               fg="red")
            passnotmatch_label.grid(row=1, column=0)
            # Placeholder code - you can add additional logic here
            print("Registration failed. Passwords do not match or invalid email.")
            enterDetails()

    # this function returns the details put into the registration page into the program
    def enterDetails():
        email = register_email_entry.get()
        password = register_pass_entry.get()
        name = register_name_entry.get()

        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Name: {name}")


def recheck_info():
    register_button = tkinter.Button(registerWindow(), text="Register", command=checkPass)
    register_button.grid(row=8, column=0, padx=20, pady=10)

    registerWindow.mainloop()

# opens the homepage
def open_prop1_win():
    prop1 = tkinter.Tk()
    prop1.title("Property Name")

    prop1_frame = tkinter.LabelFrame(prop1, text=f"P1: {prop1_name}.")
    prop1_frame.grid(row=0, column=0, padx=20, pady=20)

    propNameLabel = tkinter.Label(prop1_frame, text="Property Name:")
    propNameLabel.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    propNameEntry = tkinter.Entry(prop1_frame)
    propNameEntry.grid(row=2, column=0, columnspan=2)

    prop1_name_label = tkinter.Label(prop1_frame, text=f"P1: {prop1_name}")
    prop1_name_label.grid(row=3, column=0, columnspan=2)

    link1Label = tkinter.Label(prop1_frame, text="Airbnb link:")
    link1Label.grid(row=4, column=0)

    link1Entry = tkinter.Entry(prop1_frame)
    link1Entry.grid(row=5, column=0)

    link1 = tkinter.Button(prop1_frame, text="property link", command=lambda: openLink(link1Entry))
    link1.grid(row=6, column=0)

    link2Label = tkinter.Label(prop1_frame, text="Booking.com link:")
    link2Label.grid(row=4, column=1)

    link2Entry = tkinter.Entry(prop1_frame)
    link2Entry.grid(row=5, column=1)

    link2 = tkinter.Button(prop1_frame, text="property link", command=lambda: openLink(link2Entry))
    link2.grid(row=6, column=1)

    refreshButton = tkinter.Button(prop1_frame, text="save details", command=lambda: resetPropName(propNameEntry, prop1_frame))
    refreshButton.grid(row=7, column=0, columnspan=2, padx=20, pady=2)

    from calcPage import openCalcWin

    calcPageButton = tkinter.Button(prop1_frame, text="price calculator", command=partial(openCalcWin))
    calcPageButton.grid(row=8, column=1)

    prop1.mainloop()


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

    prop2_button = tkinter.Button(home_frame, text=("Property 2: "+ (prop2_name)), command=open_prop1_win)
    prop2_button.grid(row=5, column=0, padx=20, pady=10)

    prop3_button = tkinter.Button(home_frame, text=("Property 3: "+ (prop3_name)), command=open_prop1_win)
    prop3_button.grid(row=6, column=0, padx=20, pady=10)

    prop4_button = tkinter.Button(home_frame, text=("Property 4: "+ (prop4_name)), command=open_prop1_win)
    prop4_button.grid(row=7, column=0, padx=20, pady=10)
# add all command = open_prop(number)_win and make functions
    home_page.mainloop()

# opens the registration page
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
    register_pass_entry.config(show="*")
    register_pass_entry2.grid(row=5, column=0)

    register_name_label = tkinter.Label(register_win_frame, text="Name:")
    register_name_label.grid(row=6, column=0)

    register_name_entry = tkinter.Entry(register_win_frame)
    register_name_entry.grid(row=7, column=0)
    registerWindow.mainloop()


def registerWindow():
    # this is the starting page for the user to log into
    registerWindow = tkinter.Tk()
    registerWindow.title("Login Page")
    registerFrame = tkinter.Frame(registerWindow)
    registerFrame.pack()
    detailsFrame = tkinter.LabelFrame(registerFrame, text="enter details:")
    detailsFrame.grid(row=0, column=0, padx=20, pady=20)

    app_label = tkinter.Label(detailsFrame, text="Enter details about your property:")
    app_label.grid(row=0, column=0)

    name_label = tkinter.Label(detailsFrame, text="property name:")
    name_label.grid(row=1, column=0)

    address_label = tkinter.Label(detailsFrame, text="address:")
    address_label.grid(row=3, column=0)

    name_entry = tkinter.Entry(detailsFrame)
    name_entry.grid(row=2, column=0)

    address_label = tkinter.Entry(detailsFrame)
    address_label.grid(row=4, column=0)

    refresh_button = tkinter.Button(detailsFrame, text="refresh", command=recheck_info)
    refresh_button.grid(row=5, column=0, padx=20, pady=10)

    register_button = tkinter.Button(detailsFrame, text="new account? register", command=open_register_page)
    register_button.grid(row=7, column=0, padx=20, pady=10)

    registerWindow.mainloop()

# this is the starting page for the user to log into
login_window = tkinter.Tk()
login_window.title("Login Page")
frame = tkinter.Frame(login_window)
frame.pack()
loginFrame = tkinter.LabelFrame(frame, text="log in")
loginFrame.grid(row=0, column=0, padx=20, pady=20)

app_label = tkinter.Label(loginFrame, text="HouseHosters😌")
app_label.grid(row=0, column=0)

email_label = tkinter.Label(loginFrame, text="email :")
email_label.grid(row=1, column=0)

email_entry = tkinter.Entry(loginFrame)
email_entry.grid(row=2, column=0)

pass_label = tkinter.Label(loginFrame, text="password :")
pass_label.grid(row=3, column=0)

pass_entry = tkinter.Entry(loginFrame)
pass_entry.config(show="*")
pass_entry.grid(row=4, column=0)

show_pass=tkinter.Button(loginFrame, text="show password", command=show_password)
show_pass.grid(row=5, column=0, padx=20, pady=2)

login_button = tkinter.Button(loginFrame, text="log in", command=check_creds)
login_button.grid(row=6, column=0, padx=20, pady=2)

register_button = tkinter.Button(loginFrame, text="new account? register", command = open_register_page)
register_button.grid(row=7, column=0, padx=20, pady=2)

result_label = tkinter.Label( text="", fg="black")
result_label.pack()

login_window.mainloop()


# time.sleep(5) is delay
# window.destroy()
