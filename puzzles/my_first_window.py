# Concept: creating a GUI window with CustomTkinter - CTk(), title, geometry, mainloop
import customtkinter

app = customtkinter.CTk()
app.title("First Window")
app.geometry("800x650")

app.mainloop()