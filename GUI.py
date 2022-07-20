from os import stat
from tkinter import *
import tkinter as tk
import csv
from turtle import bgcolor
import matplotlib.pyplot as plt

# voltage plotting function  (volt_btn)
def voltage():
    with open("EV\sampleFile.csv","r") as volt:
        reader = csv.reader(volt)
        for row in reader:
            plt.plot(row)
            plt.title("Voltage Curve")
            #plt.legend(label = "Voltage",loc = "bottom right")
            plt.show()
            


win1 = Tk()
win1.geometry('400x400')
win1.title("Final GUI")

#volt_frame = Frame(win1).pack()
#curnt_frame = Frame(win1).pack()

label1 = Label(win1,text="Click here for data").pack()

volt_btn = Button(win1,text="V curve",font="Verdana",fg='black',bg="green",height=1,width=10,activebackground="aqua",bd="3",relief="groove",state="normal",cursor="",command=voltage).pack(side="top")

curnt_btn = Button(win1,text="I curve",fg='black',bg="yellow").pack(side="top")



win1.mainloop()