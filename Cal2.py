from tkinter import *
import tkinter.font as font

root = Tk()
root.title("CALCULATOR")
root.resizable(0,0)
root.geometry("247x400")
root["bg"] = "#FFFFFF"

myfont = font.Font(size=20)

e = Entry(root, width=15, borderwidth=0)
e["font"] = myfont
e["bg"] = "#FFFFFF"
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def changeview(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))

def hapus1():
    heha = list(e.get())
    if heha == []:
        heha = []
    else :
        heha.pop()
    e.delete(0,END)
    e.insert(0,''.join(heha))


def hapus():
    e.delete(0,END)

def samadengan():
    result = e.get()
    result = result.replace(',', '.')
    result = result.replace(':', '/')
    result = result.replace('x', '*')

    try:
        kon=eval(result)
        kon = round(kon,10)

        if(float(kon).is_integer()):
            kon = int(kon)
        e.delete(0,END)
        e.insert(0,str(kon).replace('.',','))
    except(TypeError, ZeroDivisionError, SyntaxError):
        e.delete(0,END)
        e.insert(0,'eror')
        
        

btn1 = Button(root, text="1", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('1'))
btn2 = Button(root, text="2", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('2'))
btn3 = Button(root, text="3", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('3'))
btn4 = Button(root, text="4", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('4'))
btn5 = Button(root, text="5", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('5'))
btn6 = Button(root, text="6", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('6'))
btn7 = Button(root, text="7", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('7'))
btn8 = Button(root, text="8", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('8'))
btn9 = Button(root, text="9", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('9'))
btn0 = Button(root, text="0", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview('0'))

tam = Button(root, text="+", padx=20, pady=20, bg= 'dodger blue', command=lambda:changeview('+'))
kur = Button(root, text="-", padx=20, pady=20, bg= 'dodger blue', command=lambda:changeview('-'))
kal = Button(root, text="x", padx=20, pady=20, bg= 'dodger blue', command=lambda:changeview('x'))
bag = Button(root, text=":", padx=20, pady=20, bg= 'dodger blue', command=lambda:changeview(':'))
kom = Button(root, text=",", padx=20, pady=20, bg= 'Sky Blue', command=lambda:changeview(','))

hap1 = Button(root, text="<x|", padx=14, pady=20, bg= 'brown1', command=hapus1)
hap = Button(root, text="C", padx=49, pady=20, bg= 'red', command=hapus)
sama = Button(root, text="=", padx=52, pady=20, bg= 'royalblue4', command=samadengan)

btn1.grid(row=4, column=0, pady=2)
btn2.grid(row=4, column=1, pady=2)
btn3.grid(row=4, column=2, pady=2)
btn4.grid(row=3, column=0, pady=2)
btn5.grid(row=3, column=1, pady=2)
btn6.grid(row=3, column=2, pady=2)
btn7.grid(row=2, column=0, pady=2)
btn8.grid(row=2, column=1, pady=2)
btn9.grid(row=2, column=2, pady=2)
btn0.grid(row=5, column=1, pady=2)

tam.grid(row=4, column=3, pady=2)
kur.grid(row=3, column=3, pady=2)
kal.grid(row=2, column=3, pady=2)
bag.grid(row=1, column=3, pady=2)
kom.grid(row=5, column=0, pady=2)

hap1.grid(row=1, column=2, pady=2)
hap.grid(row=1, column=0, pady=2, columnspan=2)
sama.grid(row=5, column=2, pady=2, columnspan=2)

root.mainloop()