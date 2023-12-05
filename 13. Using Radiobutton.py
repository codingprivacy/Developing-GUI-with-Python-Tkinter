import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x200")

var = tk.StringVar()
var.set("null")

result = tk.StringVar()

label = tk.Label(root, text="What is the name of this channel?")
label.pack()

radio1 = tk.Radiobutton(root, text="CodingPrivacy", variable=var, value="CodingPrivacy", indicatoron=0)
radio1.pack()

radio2 = tk.Radiobutton(root, text="PrivacyCoding", variable=var, value="PrivacyCoding", indicatoron=0)
radio2.pack()

label = tk.Label(root, textvariable=result)
label.pack()


def radio_logic():
    if var.get() == "CodingPrivacy":
        result.set("This answer is correct")
    else:
        result.set("This answer is not correct")


button = tk.Button(root, text="Submit", command=radio_logic)
button.pack()

root.mainloop()
