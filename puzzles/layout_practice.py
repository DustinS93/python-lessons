# Concept: creating a GUI window with CustomTkinter - CTk(), title, geometry, mainloop & 
import customtkinter

app = customtkinter.CTk()
app.title("First Window")
app.geometry("800x650")

label = customtkinter.CTkLabel(app, text="Hello!")
label.grid(row=0, column=0)
button = customtkinter.CTkButton(app, text="Push Me")
button.grid(row=1, column=1)
entry = customtkinter.CTkEntry(app)
entry.grid(row=7, column=7)

app.mainloop()



