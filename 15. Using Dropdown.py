import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

dropdown_var = tk.StringVar()
dropdown_var.set('No Option Selected')

months = ['January', 'February', 'March']
dropdown = tk.OptionMenu(root, dropdown_var, *months)
dropdown.pack()

def get_value(*args):
    for i in args:
        print(i)
    print(dropdown_var.get())

button = tk.Button(root, text='Get Value', command=get_value)
button.pack()


dropdown_var.trace('w', get_value)
root.mainloop()