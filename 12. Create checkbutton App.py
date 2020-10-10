import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x200")

var1 = tk.IntVar()
var2 = tk.StringVar(value="No Input")
var3 = tk.IntVar()

vars = [var1, var2, var3]
correct_answer = [1, "No Input", 1]

question_label = tk.Label(root, text="What is the name of this YouTube channel?")
question_label.place(x=40, y=20)

check1 = tk.Checkbutton(root, text="Coding Privacy", variable = var1, onvalue=1, offvalue=0)
check1.place(x=40, y=40)


check2 = tk.Checkbutton(root, text="RandomChannel", variable = var2, onvalue="RandomChannel", offvalue="No Input")
check2.place(x=40, y=60)


check3 = tk.Checkbutton(root, text="CodingPrivacy", variable = var3, onvalue=1, offvalue=0)
check3.place(x=40, y=80)


response = tk.Label(root)
response.place(x=40, y=150)


def get_values():
    # approach 1
    # if((check1.var.get()==1) and (check2.var.get()=="No Input") and (check3.var.get()==1)):
    #     response.config(text = "Correct answer !")
    # else:
    #     response.config(text = "Incorrect answer !")

    #approach 2
    flag=0
    for i in range(0, len(correct_answer)):
        if(correct_answer[i] != vars[i].get()):
            flag = 1
    if(flag==0):
        response.config(text="Correct answer !")
    else:
        response.config(text="Incorrect answer !")


submitbtn = tk.Button(root, text="Submit", command=get_values)
submitbtn.place(x=40, y=110)


if __name__ == '__main__':
    root.mainloop()
