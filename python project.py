import tkinter as tk
from tkinter import ttk
from tkinter import *
global index
index=-1
global count
count=0
f1=open("textfile.txt","r")
collectioncars=f1.readlines()
global stypeentry








win =tk.Tk()
win.title=("CAR DATBASE")

#win.resizable(0,0)
topframe=Frame(win)
topframe.pack()
bottomframe=Frame(win)
bottomframe.pack()
bottomostframe=Frame(win).pack()

def done():
    varsomething = stypeentry.get()
    for imp in range(len(collectioncars) - 1):
        if collectioncars[imp][0] == varsomething[0]:
            tempindex = imp

    tempd = collectioncars[tempindex]
    data_1 = tempd.split(' ')
    cmodel.set(data_1[0])
    ccompany.set(data_1[1])
    ccolor.set(data_1[2])
    cprice.set(data_1[3])
    ctype.set(data_1[4])


def src():
    global stypeentry
    win2 = tk.Tk()
    s1 = ttk.Label(win2, text="enter the car you wanna search ").grid(column=0, row=0)
    stype = tk.StringVar()
    stypeentry = ttk.Entry(win2, width=30, textvariable=stype)
    stypeentry.grid(column=1, row=0)
    b15 = ttk.Button(win2, text="DONE", command=lambda: done())
    b15.grid( column=3, row=0)

    win2.mainloop()
def showforward(word):
    global index
    if index<len(collectioncars)-1:
        index=index+1
        tempd = collectioncars[index]
        data_1 = tempd.split(' ')
        cmodel.set(data_1[0])
        ccompany.set(data_1[1])
        ccolor.set(data_1[2])
        cprice.set(data_1[3])
        ctype.set(data_1[4])

def showbackward(word):
    global index
    if index>0:
        index=index-1
        tempd = collectioncars[index]
        data_1 = tempd.split(' ')
        cmodel.set(data_1[0])
        ccompany.set(data_1[1])
        ccolor.set(data_1[2])
        cprice.set(data_1[3])
        ctype.set(data_1[4])

def showextremeleft(word):
    global index
    index=0
    tempd = collectioncars[index]
    data_1 = tempd.split(' ')
    cmodel.set(data_1[0])
    ccompany.set(data_1[1])
    ccolor.set(data_1[2])
    cprice.set(data_1[3])
    ctype.set(data_1[4])

def showextremeright(word):
    global index
    index=len(word)-1
    tempd = collectioncars[index]
    data_1 = tempd.split(' ')
    cmodel.set(data_1[0])
    ccompany.set(data_1[1])
    ccolor.set(data_1[2])
    cprice.set(data_1[3])
    ctype.set(data_1[4])

def addition(word):
    global count
    if count==0:
        cmodel.set("")
        ccompany.set("")
        ccolor.set("")
        cprice.set("")
        ctype.set("")
        count=1
    elif count==1:
        var1=cmodelentry.get()
        var2=ccolorentry.get()
        var3=ccompanyentry.get()
        var4=cpriceentry.get()
        var5=ctypeentry.get()
        cmodel.set("")
        ccompany.set("")
        ccolor.set("")
        cprice.set("")
        ctype.set("")
        str1=var1 + " " + var2 + " " +var3 + " " +var4 + " " +var5
        f1 = open("textfile.txt", "a")
        f1.write('\n'+str1)

def deletion(word):
    global collectioncars
    var1 = cmodelentry.get()
    for i in range(len(collectioncars)-1):
        if collectioncars[i][0]==var1[0]:
            tempindex=i
            break
    finalarray=[]
    cunt=0
    f2 = open("textfile.txt", "w")
    for i in range(len(collectioncars)):
        f2=open("textfile.txt","a")
        if i==tempindex:
            continue
        else:
            tempd = collectioncars[i]
            data_1 = tempd.split(' ')
            str10 = ' '.join(data_1)
            f2.write( str10)
    cmodel.set("")
    ccompany.set("")
    ccolor.set("")
    cprice.set("")
    ctype.set("")
    collectioncars = f1.readlines()
    global index
    print(index)
    index=0


def Update_Book():
    var1 = cmodelentry.get()
    var2 = ccolorentry.get()
    var3 = ccompanyentry.get()
    var4 = cpriceentry.get()
    var5 = ctypeentry.get()
    for i in range(len(collectioncars)-1):
        if collectioncars[i][0]==var1[0]:
            tempindex=i
            break
    finalarray = []
    cunt = 0
    f2 = open("textfile.txt", "w")
    for i in range(len(collectioncars)):
        f2 = open("textfile.txt", "a")
        if i == tempindex:
            f2.write(var1 + " " + var2 + " " +var3 + " " +var4 + " " +var5)
        else:
            tempd = collectioncars[i]
            data_1 = tempd.split(' ')
            str10 = ' '.join(data_1)
            f2.write(str10)
    collectioncars = f1.readlines()

cmodel=tk.StringVar()
cmodelentry=ttk.Entry(topframe,width=30, textvariable=cmodel)
cmodelentry.grid(column=1,row=0,rowspan=4)

ccompany=tk.StringVar()
ccompanyentry=ttk.Entry(topframe,width=30, textvariable=ccompany)
ccompanyentry.grid(column=1,row=4,rowspan=4)

ccolor=tk.StringVar()
ccolorentry=ttk.Entry(topframe,width=30, textvariable=ccolor)
ccolorentry.grid(column=1,row=8,rowspan=4)

cprice=tk.StringVar()
cpriceentry=ttk.Entry(topframe,width=30, textvariable=cprice)
cpriceentry.grid(column=1,row=12,rowspan=4)

ctype=tk.StringVar()
ctypeentry=ttk.Entry(topframe,width=30, textvariable=ctype)
ctypeentry.grid(column=1,row=16,rowspan=4)




a1=ttk.Label(topframe, text="CAR MODEL: ").grid(column=0, row=0,pady=10,sticky="e",rowspan=4)
a2=ttk.Label(topframe, text="COMPANY: ").grid(column=0, row=4,sticky="e",rowspan=4)
a3=ttk.Label(topframe, text="COLOR: ").grid(column=0, row=8,pady=10,sticky="e",rowspan=4)
a4=ttk.Label(topframe, text="PRICE: ").grid(column=0, row=12,sticky="e",rowspan=4)
a5=ttk.Label(topframe, text="TYPE: ").grid(column=0, row=16,pady=10,sticky="e",rowspan=4)

b1=ttk.Button(bottomframe,text="|<",width=15, command=lambda:showextremeleft(collectioncars))
b1.grid(columnspan=2,column=0, row=5)

b2=ttk.Button(bottomframe,text="<",width=15, command=lambda:showbackward(collectioncars))
b2.grid(columnspan=2,column=2, row=5)

b3=ttk.Button(bottomframe,text=">",width=15, command=lambda:showforward(collectioncars))
b3.grid(columnspan=2,column=4, row=5)

b4=ttk.Button(bottomframe,text=">|",width=15, command=lambda:showextremeright(collectioncars))
b4.grid(columnspan=2,column=6, row=5)

add =ttk.Button(bottomframe,text="ADD",width=15, command=lambda:addition(collectioncars))
add.grid(columnspan=2,column=0, row=6)

delete=ttk.Button(bottomframe,text="DELETE",width=15, command=lambda:deletion(collectioncars))
delete.grid(columnspan=2,column=2, row=6)

update=ttk.Button(bottomframe,width=15,text="UPDATE")
update.grid(columnspan=2,column=4, row=6)

search=ttk.Button(bottomframe,text="SEARCH",width=15, command=lambda:src())
search.grid(columnspan=2,column=6, row=6)


win.mainloop()