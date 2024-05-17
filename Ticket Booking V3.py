from tkinter import *
#Program Title: Ticket Booking System
#Author: Joe Thistlethwaite
#Date: 7/5/24
#Purpose: To allow a user to book tickets for an event
#Version: 3.0
tickets = {}
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
    def calculate(self):
        return ((self.amt.get())**2)**0.5 * pricing[self.type]
def calculate_total():
    global total_tickets
    total_tickets = 0
    for i in pricing:
        total_tickets += tickets[i].amt.get()
    if total_tickets > 100:
        total_lbl = Label(window, text="Too many tickets")
    else:
        total_cost = sum(tickets[i].calculate() for i in pricing)
        total_lbl = Label(window, text=f"${total_cost:.2f}")
    total_lbl.grid(row=len(pricing), column=1, sticky="WE", ipady=8, ipadx=15)
window = Tk()
window.title("Ticket Booking")
for i in pricing:
    tickets[i] = Ticket(i)
    tickets[i].lbl_print()
    tickets[i].ent_print()
calculate_total()
total_btn = Button(window, text="Calculate Total", command=calculate_total)
total_btn.grid(row=len(pricing), column=0, sticky="WE", ipady=8, ipadx=15)
window.mainloop()