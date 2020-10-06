import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x150")

v = tk.StringVar()

entry = tk.Entry(root, textvariable = v)
entry.place(x=80, y=40)

label = tk.Label(root, textvariable = v)
label.place(x=80, y=80)

root.mainloop()

