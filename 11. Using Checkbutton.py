import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x200")

var1 = tk.IntVar(value=1)
var2 = tk.StringVar(value="No Input")
var3 = tk.IntVar(value=1)

question_label = tk.Label(root, text="What is the name of this YouTube channel?")
question_label.place(x=40, y=20)

check1 = tk.Checkbutton(root, text="Coding Privacy", variable = var1, onvalue=0, offvalue=1)
check1.place(x=40, y=40)

check2 = tk.Checkbutton(root, text="RandomChannel", variable = var2, onvalue="RandomChannel", offvalue="No Input")
check2.place(x=40, y=60)

check3 = tk.Checkbutton(root, text="CodingPrivacy", variable = var3, onvalue=0, offvalue=1)
check3.place(x=40, y=80)

response1 = tk.Label(root)
response1.place(x=40, y=140)

response2 = tk.Label(root)
response2.place(x=40, y=160)

response3 = tk.Label(root)
response3.place(x=40, y=180)

def get_values():
    response1.config(text=str(var1.get()))
    response2.config(text=str(var2.get()))
    response3.config(text=str(var3.get()))

submitbtn = tk.Button(root, text="Submit", command=get_values)
submitbtn.place(x=40, y=110)


if __name__ == '__main__':
    root.mainloop()
