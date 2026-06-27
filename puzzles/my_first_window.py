# Concept: creating a GUI window with CustomTkinter - CTk(), title, geometry, mainloop
import customtkinter

app = customtkinter.CTk()
app.title("First Window")
app.geometry("800x650")

label = customtkinter.CTkLabel(app, text="Hello!")
label.pack()
button = customtkinter.CTkButton(app, text="Push Me")
button.pack()
entry = customtkinter.CTkEntry(app)
entry.pack()

app.mainloop()



