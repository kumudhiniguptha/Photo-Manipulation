import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk


root = tk.Tk()
root.geometry("3000x1000")
root.title("Satej Mayank Zaheen Pbl")
root.config(bg="white")

pen_color = "black"
pen_size = 5
file_path = ""
x=0
y=0

def imagess():
    image = Image.open(file_path)
    if image.width<501:
        width, height = int(image.width * 2), int(image.height * 2)
    elif image.width<1001:
        width, height = int(image.width), int(image.height)
    elif image.width<2001:
        width, height = int(image.width / 2), int(image.height / 2)
    elif image.width<3001:
        width, height = int(image.width / 3), int(image.height / 3)
    else:
        width, height = int(image.width / 3), int(image.height / 3)
    return width,height

def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="D:\MIT-WPU\Third Year Semester Two\Dip\PBL\Photos")
    image = Image.open(file_path)
    width, height =imagess()
    image = image.resize((width, height), Image.ANTIALIAS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


def change_size(size):
    global pen_size
    pen_size = size


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')


def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")

def apply_size(size):
    global x
    global y
    image = Image.open(file_path)
    if size =="Fit the Frame":
        x=1200
        y=1000
        image = image.resize((x, y), Image.ANTIALIAS)
    elif size =="Square 1:1":
        x=1000
        y=1000
        image = image.resize((x, y), Image.ANTIALIAS)
    elif size =="Instagram 3:2":
        x=1200
        y=800
        image = image.resize((x, y), Image.ANTIALIAS)
    elif size =="Cinematic 2:1":
        x=1000
        y=500
        image = image.resize((x, y), Image.ANTIALIAS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

def apply_filter(filter):
    image = Image.open(file_path)
    width = x
    height= y
    image = image.resize((width, height), Image.ANTIALIAS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

left_frame = tk.Frame(root, width=800, height=1000, bg="light blue")
left_frame.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=3000, height=1000)
canvas.pack()

image_button = tk.Button(left_frame, text="Add Image",
                         command=add_image, bg="white")
image_button.pack(pady=15)

color_button = tk.Button(
    left_frame, text="Change Pen Color", command=change_color, bg="white")
color_button.pack(pady=5)

pen_size_frame = tk.Frame(left_frame, bg="white")
pen_size_frame.pack(pady=5)

pen_size_1 = tk.Radiobutton(
    pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="white")
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(
    pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 = tk.Radiobutton(
    pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="white")
pen_size_3.pack(side="left")

clear_button = tk.Button(left_frame, text="Clear",
                         command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

Change_size = tk.Label(left_frame, text="Change Size", bg="white")
Change_size.pack()
Change_combobox = ttk.Combobox(left_frame, values=["Fit the Frame", "Square 1:1",
                                             "Instagram 3:2", "Cinematic 2:1"])
Change_combobox.pack()
Change_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_size(Change_combobox.get()))

filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
filter_label.pack()
filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur",
                                             "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()
filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))





canvas.bind("<B1-Motion>", draw)

root.mainloop()