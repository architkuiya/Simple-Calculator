from tkinter import *
#program to make a calculator
root = Tk()
root.title('Calculator')
icon=PhotoImage(file='icon.png')
root.iconphoto(False,icon)

data = Entry(root,width=45,borderwidth=4)
data.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
def clearing():
    data.delete(0, END)
def input(num):
    current = data.get()
    data.delete(0,END)  
    data.insert(0,str(current)+str(num))
def solution():
        try:
            final = str(data.get())
            clearing()
            data.insert(0,str(eval(final)))
        except:
            clearing()
            data.insert('syntax or zero error, please try again')
Button(root,text='1',command=lambda: input('1'),padx = 40,pady=20).grid(row=1,column=1)
Button(root,text='2',command=lambda: input('2'),padx = 40,pady=20).grid(row=1,column=2)
Button(root,text='3',command=lambda: input('3'),padx = 40,pady=20).grid(row=1,column=3)
Button(root,text='4',command=lambda: input('4'),padx = 40,pady=20).grid(row=2,column=1)
Button(root,text='5',command=lambda: input('5'),padx = 40,pady=20).grid(row=2,column=2)
Button(root,text='6',command=lambda: input('6'),padx = 40,pady=20).grid(row=2,column=3)
Button(root,text='7',command=lambda: input('7'),padx = 40,pady=20).grid(row=3,column=1)
Button(root,text='8',command=lambda: input('8'),padx = 40,pady=20).grid(row=3,column=2)
Button(root,text='9',command=lambda: input('9'),padx = 40,pady=20).grid(row=3,column=3)
Button(root,text='0',command=lambda: input('0'),padx = 40,pady=20).grid(row=4,column=1)
Button(root,text='+',command=lambda: input('+'),padx = 40,pady=20,fg='black',bg='orange').grid(row=1,column=4)
Button(root,text='-',command=lambda: input('-'),padx = 40,pady=20,fg='black',bg='orange').grid(row=2,column=4)
Button(root,text='*',command=lambda: input('*'),padx = 40,pady=20,fg='black',bg='orange').grid(row=3,column=4)
Button(root,text='/',command=lambda: input('/'),padx = 40,pady=20,fg='black',bg='orange').grid(row=4,column=4)
Button(root,text='C',command=clearing,padx=40,pady=20,bg='white',fg='black').grid(row = 4,column=2)
Button(root,text='=',command = solution,padx=40,pady=20).grid(row = 4,column=3)
root.mainloop()
