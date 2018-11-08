from Tkinter import*
import tkMessageBox
import serial

import time, datetime

import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter


now = time.localtime()
s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)


ard = serial.Serial(1,9600)
#obj = ard.readline()

def hello(c):
    test = "%04d" % (button_click1.counter)
    
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.setFont("Helvetica", 16)
    c.drawString(80, 800, s)
    c.drawString(180, 700, "Turtle Neck Prevent Program(ver.1)")
    c.drawString(80, 650, "Hello, This PDF File is made by Turtle Neck Prevent Program(ver.1)")
    c.drawString(80, 600, "This Turtle Neck Prevent Program(ver.1) is made by Python 2.7")
    c.drawString(80, 550, "This program show message that 'too close to computer'")
    c.drawString(80, 500, "So, I show you how many close your head toward computer")
    c.drawString(80, 450, "I wish be good for your health!")

    c.drawString(80, 400, "<What is the Turtle neck?>")
    c.drawString(80, 350, "Turtle neck syndrome is a condition in which the head is")
    c.drawString(80, 330, "bent forward for a long time, turning into a neck, and a pain ")
    c.drawString(80, 310, "in the back, shoulders, and back.")



    c.drawString(80, 250, "Warning Count : ")
    c.drawString(200, 250, test)

    c.drawString(80, 200, "<Warning Count Information>")

    c.drawString(80, 160, "0~5 : Normal")
    c.drawString(80, 140, "6~10 : Warning")
    c.drawString(80, 120, "11~15 : Danger")
    c.drawString(80, 100, "16~ : Would you meet doctor?")


def foo():
    try:
        foo.counter += 1
    except AttributeError:
        foo.counter = 1

def button_click1():

    try:
        button_click1.counter += 1
    except AttributeError:
        button_click1.counter = 1


    obj = ard.readline()

    while(1):
        if(obj == "1\r\n"):
            tkMessageBox.showinfo('Warning Message!', 'Too close to computer!')
            break
        else:
            obj = ard.readline()
    
    print("Active Success!")
    print(button_click1.counter)

def button_click2():
    c = canvas.Canvas("Turtle Neck Program(ver.1).pdf", pagesize=A4)
    hello(c)
    c.save()
    tkMessageBox.showinfo('PDF Information!', 'Save PDF File!')
    print("Save PDF Success!")
    print(button_click1.counter)


def button_click3():
    tkMessageBox.showinfo('Information!', 'Major : Robotics Name : Choi In Gu Since : 2016/12/10!')
    print("Major : Robotics Name : Choi In Gu Since : 2016/12/10")

def resize(ev=None):
        lHello.config(font='Helvetica -%d bold' %\
            scale.get())

def Msgbox3():
    top.tkMessageBox.showinfo("Message Error!", "Too Close To Computer!")




top = Tk()


top.title("Turtle Neck Prevent Program(Version 1)")
top.geometry("700x200+300+200")


lHello = Label(top, text="<Explain>\n1.Active : Activate Sensor\n2.Save PDF : Save warning count\n3.Information : Print about developer\nIf you have invisible eyes, slide under horizontal scroll")
lHello.configure(foreground='red')
lHello.pack(fill=Y, expand=1)

scale = Scale(top, from_=10, to=40,
                  orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)



b1=Button(top,text="Active", width=15, command=button_click1)
b1.pack(side='left', padx=10, pady=10)

    #disable example
    #b1.configure(state='disabled')

b2=Button(top,text="Save PDF", width=15, command=button_click2)
b2.pack(side='left', padx=10, pady=10)

b3=Button(top,text="Information", width=15, command=button_click3)
b3.pack(side='left', padx=10, pady=10)


    #Quit Button
bQuit = Button(top,text="Quit", command=top.quit)
bQuit.pack(side = 'right', padx=10, pady=10)


top.mainloop()
