import tkinter


def button_click():
    new_text = int(text.get())
    kilometer = str(round(new_text*1.6, 1))
    km_value.config(text=kilometer)


window = tkinter.Tk()
window.title("My first GUI program.")
window.config(padx=20, pady=20)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

km_value = tkinter.Label(text="0")
km_value.grid(row=1, column=1)

km = tkinter.Label(text="Km")
km.grid(row=1, column=2)

button = tkinter.Button(text="calculate", command=button_click)
button.grid(row=2, column=1)

text = tkinter.Entry(width=10)
text.grid(row=0, column=1)


window.mainloop()
