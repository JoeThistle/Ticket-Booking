from tkinter import *
#Program Title: Ticket Booking System
#Author: Joe Thistlethwaite
#Date: 7/5/24
#Purpose: To allow a user to book tickets for an event
#Version: 2.0

pricing = {"Child":5,"Adult":15,"Student/Senior":10}
class Ticket:
    def __init__(self,type):
        self.type = type
        self.lbl_text = (f"{self.type}: ${pricing[self.type]}")
        self.amt = IntVar()
    def lbl_print(self):
        labels = Label(window,text=self.lbl_text)
        labels.grid(row=list(pricing.keys()).index(self.type),column=0,sticky="WE",ipady=8,ipadx=15)
    def ent_print(self):
        entries = Entry(window,textvariable=self.amt)
        entries.grid(row=list(pricing.keys()).index(self.type),column=1,sticky="WE",ipady=8,ipadx=15)


window = Tk()
window.title("Ticket Booking")

for i in range(len(pricing)):
    Ticket(list(pricing.keys())[i]).lbl_print()
    Ticket(list(pricing.keys())[i]).ent_print()

total_btn = Button(window,text="Total Cost:")
total_btn.grid(row=3,column=0,sticky="WE",ipady=8,ipadx=15)


window.mainloop()