# Concept: Button that when clicked increments a number shown on a label

import customtkinter

count = 0

app = customtkinter.CTk()
app.title("Click Counter")
app.geometry("700x400")

def on_click():
    global count
    count = count + 1
    label.configure(text=count)

button = customtkinter.CTkButton(app, text="Add 1", command=on_click)
button.pack(pady=100)

label = customtkinter.CTkLabel(app, text=0)
label.pack(pady=50)

app.mainloop()