import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x150")

def func():
    print("Button is clicked!!")

btn = tk.Button(root, text="click here", command = func)
btn.pack(side="top")

root.mainloop()
