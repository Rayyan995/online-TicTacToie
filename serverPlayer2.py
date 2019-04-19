# -*- coding: utf-8 -*-
"""
Created on fri Apr 19 10:16:01 2019

@author: Rayyan
"""
# Imports for threading
from _thread import *
import threading
from threading import Thread
# Imports for GUI
from tkinter import*
import tkinter
from tkinter import messagebox
# imports for Socket
from socket import*

# Create a socket
s = socket(AF_INET, SOCK_STREAM)
host = "127.0.0.1"
port = 7000
address = (host, port)
s.bind(address)
print("binding...")
s.listen(5)
print("listening...")

# create a GUI window
wind = tkinter.Tk()
wind.title("server player2")
wind.geometry("300x400")  # size of wind

lb1 = Label(wind, text=" player1 : x ", font="Helvetica")
lb1.grid(row=1, column=0)

lb2 = Label(wind, text=" player2 : o ", font="Helvetica")
lb2.grid(row=2, column=0)

flag = 0
def check():
    global flag
    flag = flag + 1
#extract the text of the nine buttons
    b1 = btn1['text']
    b2 = btn2['text']
    b3 = btn3['text']
    b4 = btn4['text']
    b5 = btn5['text']
    b6 = btn6['text']
    b7 = btn7['text']
    b8 = btn8['text']
    b9 = btn9['text']

# check for the player 1
    if(b1 == b2 and b2 == b3 and b1 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b4 == b5 and b4 == b6 and b4 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b7 == b8 and b8 == b9 and b7 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b1 == b4 and b1 == b7 and b1 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b2 == b5 and b2 == b8 and b2 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b3 == b6 and b9 == b3 and b3 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b1 == b5 and b5 == b9 and b1 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()

    if(b3 == b5 and b7 == b3 and b3 == "x"):
        messagebox.showinfo("winner", "player 1")
        wind.destroy()


# check for the player 2
    if(b1 == b2 and b2 == b3 and b1 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b4 == b5 and b4 == b6 and b4 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b7 == b8 and b8 == b9 and b7 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b1 == b4 and b1 == b7 and b1 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b2 == b5 and b2 == b8 and b2 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b3 == b6 and b9 == b3 and b3 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b1 == b5 and b5 == b9 and b1 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    if(b3 == b5 and b7 == b3 and b3 == "o"):
        messagebox.showinfo("winner", "player 2")
        wind.destroy()

    # if all nine button pressed and no winner
    if(flag == 9):
        messagebox.showinfo("winner", "no winner")
        wind.destroy()
# end of check function

# function that executed when the buttons pressed
def clicked1():
    if(btn1['text'] == " "): # if the button did not pressed yet 
        btn1['text'] = "o"
        message = "1" # then the button one pressed 
        c.send(message.encode("utf-8")) #send the number of the presseed button
    check()

def clicked2():
    if(btn2['text'] == " "):
        btn2['text'] = "o"
        message = "2"
        c.send(message.encode("utf-8"))
    check()

def clicked3():
    if(btn3['text'] == " "):
        btn3['text'] = "o"
        message = "3"
        c.send(message.encode("utf-8"))
    check()

def clicked4():
    if(btn4['text'] == " "):
        btn4['text'] = "o"
        message = "4"
        c.send(message.encode("utf-8"))
    check()

def clicked5():
    if(btn5['text'] == " "):
        btn5['text'] = "o"
        message = "5"
        c.send(message.encode("utf-8"))
    check()

def clicked6():
    if(btn6['text'] == " "):
        btn6['text'] = "o"
        message = "6"
        c.send(message.encode("utf-8"))
    check()

def clicked7():
    if(btn7['text'] == " "):
        btn7['text'] = "o"
        message = "7"
        c.send(message.encode("utf-8"))
    check()

def clicked8():
    if(btn8['text'] == " "):
        btn8['text'] = "o"
        message = "8"
        c.send(message.encode("utf-8"))
    check()

def clicked9():
    if(btn9['text'] == " "):
        btn9['text'] = "o"
        message = "9"
        c.send(message.encode("utf-8"))
    check()
# End of clicked buttons


def rec(c):
    while True:
        btnNumber = c.recv(1024).decode("utf-8")

        if(btnNumber == "1" and btn1['text'] == " "):
            btn1['text'] = "x"
        if(btnNumber == "2" and btn2['text'] == " "):
            btn2['text'] = "x"
        if(btnNumber == "3" and btn3['text'] == " "):
            btn3['text'] = "x"
        if(btnNumber == "4" and btn4['text'] == " "):
            btn4['text'] = "x"
        if(btnNumber == "5" and btn5['text'] == " "):
            btn5['text'] = "x"
        if(btnNumber == "6" and btn6['text'] == " "):
            btn6['text'] = "x"
        if(btnNumber == "7" and btn7['text'] == " "):
            btn7['text'] = "x"
        if(btnNumber == "8" and btn8['text'] == " "):
            btn8['text'] = "x"
        if(btnNumber == "9" and btn9['text'] == " "):
            btn9['text'] = "x"
        check()
        print(btnNumber)


# creating a nine button to play with..
btn1 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked1)
btn1.grid(row=0, column=2)

btn2 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked2)
btn2.grid(row=0, column=3)

btn3 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked3)
btn3.grid(row=0, column=4)

btn4 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked4)
btn4.grid(row=1, column=2)

btn5 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked5)
btn5.grid(row=1, column=3)

btn6 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked6)
btn6.grid(row=1, column=4)

btn7 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked7)
btn7.grid(row=2, column=2)

btn8 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked8)
btn8.grid(row=2, column=3)
btn9 = tkinter.Button(wind, text=" ", bg="blue", fg="white",
                      font="calibri", width=3, height=2, command=clicked9)
btn9.grid(row=2, column=4)

# accept the other player connection
c, add = s.accept()
print("connection acceoted!")
start_new_thread(rec, (c,))

wind.mainloop()
