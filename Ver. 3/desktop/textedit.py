import os
from tkinter import *
from tkinter import filedialog

print(os.getcwd())
 
#create a window and declare a variable called root
root = Tk()
root.geometry("1200x660")
root.title("Text Editor For GalaxyOS")

my_menu = Menu(root)
root.config(menu = my_menu)

frame = Frame(root)
frame.pack(pady = 5)

text_scroll_y = Scrollbar(frame)
text_scroll_y.pack(side = RIGHT, fill = Y)

# text_scroll_x = Scrollbar(frame, orient = 'horizontal')
# text_scroll_x.pack(side = BOTTOM, fill = X)

fileText = Text(frame, width = 1200, height = 660, undo = True, yscrollcommand = text_scroll_y.set) # xscrollcommand = text_scroll_x.set
fileText.pack()

text_scroll_y.config(command = fileText.yview)
# text_scroll_x.config(command = fileText.xview)

# File Tab Actions
def newfile():
    root.title("New File - Text Editor For GalaxyOS")
    fileText.delete(1.0, END)

def savetextfile():
    file = filedialog.asksaveasfilename(defaultextension=".*", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    file_title = file
    file_title.replace(os.getcwd(), "")

    # Create file with name
    file_save = open(file_title, 'w')
    file_save.write(fileText.get(1.0, END))
    print(file_title)

def openfile():
    fileText.delete(1.0, END)
    text_open = filedialog.askopenfilename(defaultextension=".*", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    textfiletoOpen = open(text_open, 'r')
    stuffInFile = textfiletoOpen.read()
    fileText.insert(END, stuffInFile)

# Edit Tab Actions
def deleteText():
    fileText.delete("sel.first", "sel.last")

def cutText():
    global selected
    if fileText.selection_get():
        selected = fileText.selection_get()
        fileText.delete("sel.first", "sel.last")

def copyText():
    global selected
    if fileText.selection_get():
        selected = fileText.selection_get()

def pasteText():
    if selected:
        position = fileText.index(INSERT)
        fileText.insert(position, selected)


file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = newfile)
file_menu.add_command(label = "Open", command = openfile)
# file_menu.add_command(label = "Save")
file_menu.add_command(label = "Save As...", command = savetextfile)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

edit_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = cutText, accelerator="Ctrl + X")
edit_menu.add_command(label = "Copy", command = copyText, accelerator="Ctrl + C")
edit_menu.add_command(label = "Paste", command = pasteText, accelerator="Ctrl + V")
edit_menu.add_command(label = "Delete", command = deleteText, accelerator="Del")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo...", command = fileText.edit_undo, accelerator="Ctrl + Z")
edit_menu.add_command(label = "Redo...", command = fileText.edit_redo, accelerator="Ctrl + Y")

root.mainloop()