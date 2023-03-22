from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    entry_Password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    password_list = password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_Password.insert(0,password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website = entry_website.get()
    email = entry_Email.get()
    password = entry_Password.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Alert", message="Please don't leave any fields empty")

    else:
        data_ok = messagebox.askokcancel(title=website,message=f"These are the details Entered:\n Email: {email}\n Password: {password}\n Press 'OK' to save?")

        if data_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0,END)
                entry_Email.delete(0,END)
                entry_Email.insert(0,"alajangilikith@gmail.com")
                entry_Password.delete(0,END)
                entry_website.focus()


    

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)

canvas.grid(column=1,row=0)

#website
website_label =Label(text="Website:" )
website_label.grid(column=0,row=1)
entry_website = Entry(width=36)
entry_website.grid(column=1,row=1,columnspan=2)
entry_website.focus()


#Email
Email_label =Label(text="Email/Username:" )
Email_label.grid(column=0,row=2)
entry_Email = Entry(width=36)
entry_Email.grid(column=1,row=2,columnspan=2)
entry_Email.insert(0,"alajangilikith@gmail.com")

#password and generate

password_label =Label(text="Password:" )
password_label.grid(column=0,row=3)
entry_Password = Entry(width=21)
entry_Password.grid(column=1,row=3)
 
generate_button = Button()
generate_button.config(text="Generate Password",highlightthickness=0,width=15,command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button()
add_button.config(text="Add",width=36,highlightthickness=0,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)








window.mainloop()