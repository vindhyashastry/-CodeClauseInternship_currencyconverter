from currency_converter import CurrencyConverter
import tkinter as tk

c=CurrencyConverter()
# print(c.convert(12,"USD","INR"))

window=tk.Tk()
window.geometry("600x360")
window.title("currencyconverter")

def clicked():
    amount=int(entry.get())
    cur1=entry2.get()
    cur2=entry3.get()
    data=c.convert(amount,cur1,cur2)
    label4=tk.Label(window,text=data,font="Times 16 bold").place(x=220,y=300)
label=tk.Label(window,text="currency converter",font="Times 20 bold",fg='green').place(x=120, y=50)

label1=tk.Label(window,text="Enter Amount :",font="Times 16 bold").place(x=80,y=100)
entry=tk.Entry(window)

label2=tk.Label(window,text="Enter Currency :",font="Times 16 bold").place(x=60,y=150)
entry2=tk.Entry(window)

label3=tk.Label(window,text="Enter Desired Currency :",font="Times 16 bold").place(x=15,y=200)
entry3=tk.Entry(window)

button=tk.Button(window,text="click" ,font="Times 16 bold",fg='white',bg='red',command=clicked).place(x=220,y=250)
entry.place(x=230,y=105)
entry2.place(x=230,y=155)
entry3.place(x=250,y=205)

window.mainloop()