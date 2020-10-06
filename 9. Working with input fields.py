import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x150")

entry = tk.Entry(root, show ="*")
entry.place(x=80, y=40)
entry.insert(0, "This is initial text")

label = tk.Label(root, text="Empty label")
label.place(x=80, y=120)

def get_values():
    v = entry.get()
    btn.config(text=v)

btn = tk.Button(root, text="Process entry widget", command = get_values)
btn.place(x=80, y=80)

root.mainloop()










"""
1. Password in Entry widget
2. Get and set value in Entry widget 
3. Configure function in button
"""