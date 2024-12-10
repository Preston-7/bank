import tkinter as tk

window = tk.Tk()


# label = tk.Label(
#     text="Enter your name below.",
#     foreground='white',
#     background='black',
#     width = 50,
#     height = 8
# )

# entry = tk.Entry(fg='black', bg='white', width=50)

# name = entry.get()

# label.pack()
# entry.pack()

text_box = tk.Text()
text_box.pack()

window.mainloop()