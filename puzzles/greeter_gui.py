# Concept: Type name into box, click a button, and label in the window greets you by name
import customtkinter

app = customtkinter.CTk()
app.title("Greeter Gui App")
app.geometry("700x400")

def callback():
    typed = entry.get()
    label.configure(text=f"Hello, {typed}!")

entry = customtkinter.CTkEntry(app)
entry.pack(pady=100)

label = customtkinter.CTkLabel(app, text="What's your name?")
label.pack(pady=50)

button = customtkinter.CTkButton(app, text="Press Me", command=callback)
button.pack()

app.mainloop()