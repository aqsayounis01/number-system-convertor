from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Converter')
root.geometry('1280x780')

num=StringVar()
lblbinary=StringVar()
lbldecimal=StringVar()
lblhexa=StringVar()
lbloctal=StringVar()
svar=StringVar()
svar.set("ready")
rb = StringVar()
rb.set('radio')

def convert():
    if num.get()==0:
        messagebox.showerror('Error','You must enter a number to convert')
        svar.set("error!")
    else:
        import time
        svar.set("processing...")
        sb.update()
        time.sleep(1)
        svar.set("ready now")

        if rb.get()=='bin':
            a=int(num.get(),2)
            b=str(hex(a))
            d=str(oct(a))
            lbldecimal.set(a)
            lblhexa.set(b[2:])
            lbloctal.set(d[2:])

        elif rb.get()=='dec':
            a=int(num.get(),10)
            b=str(hex(a))
            c=str(oct(a))
            d=str(bin(a))
            lblbinary.set(d[2:])
            lblhexa.set(b[2:])
            lbloctal.set(c[2:])

        elif rb.get()=='oct':
            a=int(num.get(),8)
            b=str(hex(a))
            c=str(bin(a))
     
            lblbinary.set(c[2:])
            lblhexa.set(b[2:])
            lbldecimal.set(a)

        elif rb.get()=='hex':
            a=int(num.get(),16)
            c=str(bin(a))
            d=str(oct(a))
            lblbinary.set(c[2:])
            lbldecimal.set(a)
            lbloctal.set(d[2:])


def clear():
    num.set(0)
    lblhexa.set('')
    lbldecimal.set('')
    lblbinary.set('')
    lbloctal.set('')

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):        #yes  - returns True
        root.destroy()

def explain():
    messagebox.showinfo("Explaination","Explaination :- \nTo convert integer to binary, start with the integer in question and divide it by 2 keeping notice of the quotient and the remainder.     \nA binary number can be converted to a decimal number by multiplying the individual digits by powers of 2 raised to the position of the digit in the number.    \nDivide the decimal number by 16. Treat the division as an integer division. Write down the remainder (in hexadecimal). Divide the result again by 16.      \nIn decimal to binary, we divide the number by 2, in decimal to hexadecimal we divide the number by 16. In case of decimal to octal, we divide the number by 8 and write the remainders in the reverse order to get the equivalent octal number.")


Label(root,text='Conversion System', font=('Times New Roman',60,'normal'),fg='#150050',bg='#2192FF',relief=RIDGE).pack(pady=20)

root.config(bg='#2192FF')

n=Label(root,text='Enter Number', font=('Times New Roman',20,'normal'),fg='#150050',bg='#2192FF')
n.place(x=300,y=200)

g=Label(root,text='Given Number', font=('Times New Roman',20,'normal'),fg='#150050',bg='#2192FF')
g.place(x=300,y=270)

bg=Label(root,text='BIN', font=('Times New Roman',18,'normal'),fg='#150050',bg='#2192FF')
bg.place(x=630,y=270)
dg=Label(root,text='DEC', font=('Times New Roman',18,'normal'),fg='#150050',bg='#2192FF')
dg.place(x=715,y=270)
hg=Label(root,text='HEX', font=('Times New Roman',18,'normal'),fg='#150050',bg='#2192FF')
hg.place(x=810,y=270)
og=Label(root,text='OCT', font=('Times New Roman',18,'normal'),fg='#150050',bg='#2192FF')
og.place(x=900,y=270)

b=Label(root,text='Binary', font=('Times New Roman',20,'normal'),fg='#150050',bg='#2192FF')
b.place(x=300,y=340)

d=Label(root,text='Decimal', font=('Times New Roman',20,'normal'),fg='#150050',bg='#2192FF')
d.place(x=300,y=410)

h=Label(root,text='Hexa Decimal', font=('Times New Roman',20,'normal'),fg='#150050',bg='#2192FF')
h.place(x=300,y=480)

o=Label(root,text='Octal', font=('Times New Roman',20,'normal'),fg='#150050',bg='#2192FF')
o.place(x=300,y=550)

sb= Label(root,textvariable=svar,fg='dark blue' ,font='6',relief=SUNKEN,anchor='w')
sb.pack(fill=X,side=BOTTOM)

e1=Entry(root,font='arial 20' , fg = '#150050' , justify = CENTER , relief = GROOVE , textvariable=num)
e1.place(x=650,y=200 )

r1=Radiobutton(root,variable=rb, value='bin',relief=SUNKEN,fg="blue",borderwidth=4)
r1.place(x=675,y=270 )
r1=Radiobutton(root,variable=rb, value='dec',relief=SUNKEN,fg="blue",borderwidth=4)
r1.place(x=765,y=270 )
r1=Radiobutton(root,variable=rb, value='hex',relief=SUNKEN,fg="blue",borderwidth=4)
r1.place(x=860,y=270 )
r1=Radiobutton(root,variable=rb, value='oct',relief=SUNKEN,fg="blue",borderwidth=4)
r1.place(x=950,y=270 )

e2=Entry(root,font='arial 20' , fg = '#150050' , justify = CENTER , relief = GROOVE , textvariable=lblbinary)
e2.place(x=650,y=340 )

e3=Entry(root,font='arial 20' , fg = '#150050' , justify = CENTER , relief = GROOVE  , textvariable=lbldecimal)
e3.place(x=650,y=410 )

e1=Entry(root,font='arial 20' , fg = '#150050' , justify = CENTER , relief = GROOVE  , textvariable=lblhexa)
e1.place(x=650,y=480 )

e4=Entry(root,font='arial 20' , fg = '#150050' , justify = CENTER , relief = GROOVE  , textvariable=lbloctal)
e4.place(x=650,y=550 )

btn1=Button(root,text='Convert' , font='arial 18 bold',fg='#2192FF',bg='#150050',width=8,command=convert )
btn1.place(x=270,y=655)

btn2=Button(root,text='Clear' , font='arial 18 bold',fg='#2192FF',bg='#150050',width=8,command=clear )
btn2.place(x=465,y=655)

btn3=Button(root,text='Explain' , font='arial 18 bold',fg='#2192FF',bg='#150050',width=8,command=explain )
btn3.place(x=655,y=655)

btn3=Button(root,text='Exit' , font='arial 18 bold',fg='#2192FF',bg='#150050',width=8,command=exit )
btn3.place(x=845,y=655)

root.mainloop()
