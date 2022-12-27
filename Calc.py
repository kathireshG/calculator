import tkinter as tk
from tkinter import *
import time
import os


win=tk.Tk()
win.title('Calculator')
win.resizable(0,0)

operator=''
text_input=StringVar()

def Clear():
    global operator
    operator=''
    text_input.set('')

def Equal():
    try:
        global operator
        operator=str(text_input.get())
        operator=operator.replace('x','*')
        text_input.set(str(eval(operator)))
        operator=''
    except Exception as e:
        if type(e)==SyntaxError:
            text_input.set(' !!! Syntax Error !!!   ')
        elif type(e)==ZeroDivisionError:
            text_input.set(' !!! Math Error !!!     ')
        operator=''
def erase():
    global operator
    operator=operator[0:len(operator)-1]
    text_input.set(operator)
    

def buttonClick(value):
    global operator
    operator+=str(value)
    text_input.set(operator)

#icon=PhotoImage(file='C:/Users/kathiresh/Desktop/Capture.PNG')

mainbag=Label(win,bg='Black').place(relheight=1,relwidth=1)
toplabel=Label(win,height=5,bg='Black',width=50).grid(row=0,columnspan=4)
nameLabel=Label(win,height=1,bg='black',fg='white',font=('Audiowide',30,'bold'),width=5,text='KAT').place(x=105,y=15)
mainEntry=Entry(win,bd=30,font=('arial',20,'bold'),justify='right',bg='powder blue',textvariable=text_input).grid(row=1,columnspan=4)

#=========================================================================

button_Cls=Button(win,bd=8,padx=14,pady=8,font=('Times roman',20,'bold'),bg='skyblue',command=Clear,text='C').grid(row=2,column=0)
button_Err=Button(win,bd='8',padx=12,pady=8,font=('Times roman',20,'bold'),bg='skyblue',command=erase,text='<-').grid(row=2,column=1)
button_RightB=Button(win,bd='8',padx=21,pady=8,font=('Times roman',20,'bold'),bg='skyblue',command=lambda:buttonClick('('),text='(').grid(row=2,column=2)
buttonPlus=Button(win,bd='8',padx=20,pady=8,font=('Times roman',20,'bold'),bg='skyblue',command=lambda:buttonClick(')'),text=')').grid(row=2,column=3)

#=========================================================================

button_7=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman',20,'bold'),command=lambda:buttonClick(7),text='7').grid(row=3,column=0,padx=5)
button_8=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(8),text='8').grid(row=3,column=1)
button_9=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(9),text='9').grid(row=3,column=2)
buttonMin=Button(win,bd='8',padx=18,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick('+'),text='+').grid(row=3,column=3)

#=========================================================================
button_4=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(6),text='6').grid(row=4,column=2,padx=5)
button_5=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(5),text='5').grid(row=4,column=1)
button_6=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(4),text='4').grid(row=4,column=0,padx=5)
buttonMul=Button(win,bd='8',padx=21,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick('-'),text='-').grid(row=4,column=3)

#=========================================================================
button_1=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(1),text='1').grid(row=5,column=0,padx=5)
button_2=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(2),text='2').grid(row=5,column=1)
button_3=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(3),text='3').grid(row=5,column=2,padx=5)
buttonDiv=Button(win,bd='8',padx=18,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick('x'),text='x').grid(row=5,column=3)

#=========================================================================
button_Zero=Button(win,bd='8',padx=18,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick(0),text='0').grid(row=6,column=1)
button_Point=Button(win,bd='8',padx=18,pady=8,bg='skyblue',font=('Times roman','20','bold'),command=lambda:buttonClick('.'),text='.').grid(row=6,column=0)
button_Eq=Button(win,bd='8',padx=16,pady=8,bg='skyblue',font=('Times roman','20','bold'),text='=',command=Equal).grid(row=6,column=2)
button_Div=Button(win,bd='8',padx=20,pady=8,bg='skyblue',font=('Times roman','20','bold'),text='/',command=lambda:buttonClick('/')).grid(row=6,column=3)


win.mainloop()
