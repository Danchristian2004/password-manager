from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    pass_entry.delete(0, END)

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)


def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if website == "" or password == "":
        messagebox.showerror("Error", "Preencha todos os campos")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Se tudo estiver correto, clique em OK.\nEmail: {email}\nPassword: {password}"
        )

        if is_ok:
            with open("senhas.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)


web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)


web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="ADD", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()