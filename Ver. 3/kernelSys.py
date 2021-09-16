import turtle as t
import os
from tkinter import messagebox
from tkinter import *

def runSys(): 
    # Create a window and declare a variable called window and call the screen()
    window = t.Screen()
    window.title("GalaxyOS - Ver. 2")   
    window.bgcolor("purple")
    window.setup(width = 800, height = 600)
    window.tracer(0)

    # Actions
    def background1(a, b):
        window.bgcolor("darkred")

    def background2(a, b):
        window.bgcolor("darkblue")

    def background3(a, b):
        window.bgcolor("darkcyan")

    def background4(a, b):
        window.bgcolor("green")

    def backgroundDefault(a, b):
        window.bgcolor("purple")

    def removefileordir(a, b):
        FileToDel = t.textinput("Enter File Or Dir Name To Remove", "Name (if it's a file type with the extension):")
        os.remove(FileToDel)

    def mkfl(a, b):
        """
        'old way to make files'

        # taking input
        fileName = t.textinput("Enter File Name", "Name:")
        # taking input
        fileText = t.textinput("Enter Text", "Text:")

        # Create file with name
        file = open(fileName + ".txt", 'w')
        file.write(fileText)
        """
        os.system("textedit.lnk")

    def mkdir(a, b):
        folderName = t.textinput("Enter Folder Name", "Name:")
        os.mkdir(folderName)

    def chdir(a, b):
        changeFolderName = t.textinput("Enter Folder Name To Change", "Name:")
        os.chdir(changeFolderName)

    def getfiles(a, b):
        dir_name = directory
        print(os.listdir(dir_name))
        messagebox.showinfo(title = "Check Files", message = os.listdir(dir_name))
    
    def getdir(a, b):
        chkdir = os.getcwd()
        messagebox.showinfo(title = "Check Directory", message = chkdir)

    t.hideturtle()
    t.penup()
    t.color("white")
    t.setposition(-640, -310)
    t.write("GALAXYOS - VER. 2", font = ("terminal", 21, "normal"))

    taskbar = t.Turtle()
    taskbar.penup()
    taskbar.goto(0, 320)
    taskbar.color("gray")
    taskbar.shapesize(stretch_len = 75, stretch_wid = 3)
    taskbar.shape("square")

    bg1 = t.Turtle()
    bg1.penup()
    bg1.goto(-650, 320)
    bg1.color("red")
    bg1.shapesize(stretch_len = 2, stretch_wid = 2)
    bg1.shape("square")

    bg2 = t.Turtle()
    bg2.penup()
    bg2.goto(-600, 320)
    bg2.color("blue")
    bg2.shapesize(stretch_len = 2, stretch_wid = 2)
    bg2.shape("square")

    bg3 = t.Turtle()
    bg3.penup()
    bg3.goto(-550, 320)
    bg3.color("cyan")
    bg3.shapesize(stretch_len = 2, stretch_wid = 2)
    bg3.shape("square")

    bg4 = t.Turtle()
    bg4.penup()
    bg4.goto(-500, 320)
    bg4.color("green")
    bg4.shapesize(stretch_len = 2, stretch_wid = 2)
    bg4.shape("square")

    bg5 = t.Turtle()
    bg5.penup()
    bg5.goto(-450, 320)
    bg5.color("purple")
    bg5.shapesize(stretch_len = 2, stretch_wid = 2)
    bg5.shape("square")

    # Apps
    obj1 = t.Turtle()
    obj1.penup()
    obj1.goto(-610, 245)
    obj1.color("white")
    obj1.shapesize(stretch_len = 2, stretch_wid = 3)
    obj1.shape("square")

    t.goto(-650, 180)
    text1 = t.write("TEXT EDIT", font = ("terminal", 21, "normal"))

    obj2a = t.Turtle()
    obj2a.penup()
    obj2a.goto(-610, 115)
    obj2a.color("yellow")
    obj2a.shapesize(stretch_len = 3, stretch_wid = 2)
    obj2a.shape("square")

    obj2b = t.Turtle()
    obj2b.penup()
    obj2b.goto(-630, 130)
    obj2b.color("yellow")
    obj2b.shapesize(stretch_len = 1, stretch_wid = 1.5)
    obj2b.shape("square")

    t.goto(-650, 55)
    text2 = t.write("MAKE DIR", font = ("terminal", 21, "normal"))

    obj3 = t.Turtle()
    obj3.penup()
    obj3.goto(-580, 0)
    obj3.color("lightgreen")
    obj3.pencolor("black")
    obj3.shapesize(stretch_len = 6, stretch_wid = 5)
    obj3.shape("classic")

    t.goto(-657, -70)
    text3 = t.write("CHANGE DIR", font = ("terminal", 21, "normal"))

    obj4 = t.Turtle()
    obj4.penup()
    obj4.goto(-610, -115)
    obj4.color("red")
    obj4.shapesize(stretch_len = 2, stretch_wid = 3)
    obj4.shape("square")

    t.goto(-660, -210)
    text4 = t.write("DELETE FILE\n OR FOLDER", font = ("terminal", 21, "normal"))

    obj5 = t.Turtle()
    obj5.penup()
    obj5.goto(-485, 245)
    obj5.color("lightgreen")
    obj5.shapesize(stretch_len = 2, stretch_wid = 3)
    obj5.shape("square")

    t.goto(-535, 180)
    text5 = t.write("CHECK FILES", font = ("terminal", 21, "normal"))

    obj6a = t.Turtle()
    obj6a.penup()
    obj6a.goto(-485, 115)
    obj6a.color("lightgreen")
    obj6a.shapesize(stretch_len = 3, stretch_wid = 2)
    obj6a.shape("square")

    obj6b = t.Turtle()
    obj6b.penup()
    obj6b.goto(-505, 130)
    obj6b.color("lightgreen")
    obj6b.shapesize(stretch_len = 1, stretch_wid = 1.5)
    obj6b.shape("square")

    t.goto(-530, 55)
    text6 = t.write("CHECK DIR", font = ("terminal", 21, "normal"))

    """
    obj7 = t.Turtle()
    obj7.penup()
    obj7.goto(-485, 0)
    obj7.color("white")
    obj7.shapesize(stretch_len = 3, stretch_wid = 3)
    obj7.shape("square")

    t.goto(-527, -70)
    text7 = t.write("", font = ("terminal", 21, "normal"))
    """

    """
    actWindow = t.Turtle()
    WindowXbtnClose = t.Turtle()
    WindowXbtnClose.penup()

    def closeWindow(a, b):
        actWindow.hideturtle()
        WindowXbtnClose.hideturtle()

    WindowXbtnClose.color("red")
    WindowXbtnClose.goto(225, 225)
    WindowXbtnClose.shape("square")
    actWindow.shape("square")
    actWindow.color("gray")
    actWindow.shapesize(stretch_len = 25, stretch_wid = 25)
    WindowXbtnClose.onclick(closeWindow)
    """

    while True:
        window.update()
        directory = os.getcwd()
        # t.write("DIRECTORY: " + directory, font=("terminal", 21, "normal"))
        bg1.onclick(background1)
        bg2.onclick(background2)
        bg3.onclick(background3)
        bg4.onclick(background4)
        bg5.onclick(backgroundDefault)
        obj1.onclick(mkfl)
        obj2a.onclick(mkdir)
        obj3.onclick(chdir)
        obj4.onclick(removefileordir)
        obj5.onclick(getfiles)
        obj6a.onclick(getdir)
