import tkinter as tk

root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x200")

questions_with_answers = {
    1: {
        'question_title': "What is the name of this channel?",
        'question_options': ['CodingPrivacy', 'PrivacyCoding'],
        'correct_option': 'CodingPrivacy'
    },
    2: {
        'question_title': "What are we learning today?",
        'question_options': ['Radio Button', 'Check Button'],
        'correct_option': 'Radio Button'
    }
}


result = tk.StringVar()

for question_obj in questions_with_answers:
    title = questions_with_answers[question_obj]['question_title']
    options = questions_with_answers[question_obj]['question_options']
    answer = questions_with_answers[question_obj]['correct_option']

    var = tk.StringVar()
    var.set("null")

    label = tk.Label(root, text=title)
    label.pack(padx=50, anchor='w')

    for i in options:
        option = tk.Radiobutton(root, text=i, variable=var, value=i)
        option.pack(padx=50, anchor='w')

    questions_with_answers[question_obj]['submission'] = var

label = tk.Label(root, textvariable=result)
label.pack(padx=50, anchor='w')


def radio_logic():
    flag = 0
    for question_obj in questions_with_answers:
        submission = questions_with_answers[question_obj]['submission']
        if questions_with_answers[question_obj]['correct_option'] != submission.get():
            flag = 1
    if flag == 1:
        result.set("Any one of the answer is incorrect")
    else:
        result.set("Congrats! all the answers are correct")


button = tk.Button(root, text="Submit", command=radio_logic)
button.pack(padx=50, anchor='w')

root.mainloop()
