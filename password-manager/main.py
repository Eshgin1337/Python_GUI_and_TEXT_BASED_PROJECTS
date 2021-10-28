import tkinter
import random
from tkinter import messagebox
import json


def save():
    if len(website_entry.get()) == 0 and len(password_entry.get()) == 0:
        messagebox.showinfo(title="Empty field", message="Please do not leave the two fields empty!")
    elif len(website_entry.get()) == 0:
        messagebox.showinfo(title="Empty field in website entry", message="Please do not leave website "
                                                                          "entry field empty!")
    elif len(password_entry.get()) == 0:
        messagebox.showinfo(title="Empty field in password entry", message="Please do not leave password "
                                                                           "entry field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the information you want to save:"
                                                                          f"\nEmail: {eu_entry.get()} "
                                                                          f"\nPassword: {password_entry.get()}"
                                                                          f"\nIs it ok to save?")
        new_data = {
            website_entry.get():
                {
                    "email": eu_entry.get(),
                    "password": password_entry.get()
                }
        }

        if is_ok:
            try:
                with open("data.json", "r") as data:
                    output = json.load(data)
                    output.update(new_data)

            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)

            else:
                with open("data.json", "w") as data:
                    json.dump(output, data, indent=4)

            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


def search_website():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data:
            webs = json.load(data)
            messagebox.showinfo(title=f"{website}", message=f"Email: "
                                                            f"{webs[website]['email']}\nPassword: "
                                                            f"{webs[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="None", message=f"There are no details for the website named {website}.")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, tkinter.END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]

    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = []
    password_list.extend(letters_list)
    password_list.extend(symbols_list)
    password_list.extend(numbers_list)
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)


window = tkinter.Tk()
window.title("Password generator")
window.config(padx=50, pady=50, bg="#B6CFC7")

canvas = tkinter.Canvas(width=200, height=200, bg="#B6CFC7", highlightthickness=0)
pass_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.config(bg="#B6CFC7")
website_label.grid(row=1, column=0)

eu_label = tkinter.Label(text="Email/Username:")
eu_label.config(bg="#B6CFC7")
eu_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.config(padx=40, bg="#B6CFC7")
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tkinter.Button(text="Search", width=14, command=search_website)
search_button.config(bg="#E6E2D9", highlightthickness=0)
search_button.grid(row=1, column=2)

eu_entry = tkinter.Entry(width=40)
eu_entry.grid(row=2, column=1, columnspan=2)
eu_entry.insert(0, "eshgin.hasanov.1337@gmail.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

password_generator_button = tkinter.Button(text="Generate Password", command=generate_password, bg="#E6E2D9")
password_generator_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=33, command=save, bg="#E6E2D9")
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
