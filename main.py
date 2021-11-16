import tkinter

ui = tkinter.Tk()
#Logic
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def btnenter():
    global operator
    sum=str(eval(operator))
    text_input.set(sum)
    operator=sum .btnClick
ui.configure(background='azure4')
#Display
operator = ""
text_input = tkinter.StringVar()
txtdisplay = tkinter.Entry(ui,font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg="azure4", justify='right').grid(columnspan=4)
#Tombol row 1
btnclear=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="red", font=('arial', 20,'bold'), text='C', bg="azure3", command=btnClear) .grid(row=1, column=0)
btnpangkat=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='^', bg="azure3", command=lambda:btnClick("**")) .grid(row=1, column=1)
btnbagi=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text=':', bg="azure3", command=lambda:btnClick("/")) .grid(row=1, column=2)
btnkali=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='X', bg="azure3", command=lambda:btnClick("*")) .grid(row=1, column=3)
#Tombol row 2
btn7=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='7', bg="azure3", command=lambda:btnClick(7)) .grid(row=2, column=0)
btn2=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='2', bg="azure3", command=lambda:btnClick(2)) .grid(row=2, column=1)
btn2=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='9', bg="azure3", command=lambda:btnClick(9)) .grid(row=2, column=2)
btnkurang=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='-', bg="azure3", command=lambda:btnClick("-")) .grid(row=2, column=3)
#Tombol row 3
btn4=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='4', bg="azure3", command=lambda:btnClick(4)) .grid(row=3, column=0)
btn5=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='5', bg="azure3", command=lambda:btnClick(5)) .grid(row=3, column=1)
btn6=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='6', bg="azure3", command=lambda:btnClick(6)) .grid(row=3, column=2)
btntambah=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='+', bg="azure3", command=lambda:btnClick("+")) .grid(row=3, column=3)
#Tombol row 4
btnc1=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='1', bg="azure3", command=lambda:btnClick(1)) .grid(row=4, column=0)
btn2=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='2', bg="azure3", command=lambda:btnClick(2)) .grid(row=4, column=1)
btn3=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='3', bg="azure3", command=lambda:btnClick(3)) .grid(row=4, column=2)
btnenter=tkinter.Button(ui,padx=16,pady=64,bd=9, fg="black", font=('arial', 20,'bold'), text='=', bg="azure3", command=btnenter) .grid(row=4, column=3, rowspan=2)
#Tombol row 5
btn0=tkinter.Button(ui,padx=64,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text='0', bg="azure3", command=lambda:btnClick(0)) .grid(row=5, column=0, columnspan=2)
btncoma=tkinter.Button(ui,padx=16,pady=16,bd=9, fg="black", font=('arial', 20,'bold'), text=',', bg="azure3", command=lambda:btnClick(".")) .grid(row=5, column=2)

ui.mainloop()