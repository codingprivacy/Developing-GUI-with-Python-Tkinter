import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("CodingPrivacy")
root.geometry("300x150")

#1st approach
# photo = tk.PhotoImage(file = "Assets/Image.png")

#2nd approach
photo2 = Image.open("Assets/Image.png")
resized_image = photo2.resize((300,150), Image.ANTIALIAS)
converted_image= ImageTk.PhotoImage(resized_image)

label = tk.Label(root, image= converted_image, width = 300, height = 150,
                 bg = "black", fg = "yellow")
label.pack()

root.mainloop()