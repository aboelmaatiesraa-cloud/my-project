from tkinter import*
import webbrowser
myframe=Tk()
myframe.title("my project")
myframe.geometry("700x400")

mylabel=Label(myframe,text="programming",font="Tahoma 20 bold")
mylabel.pack(pady=20)

x=Label(myframe,text="Do you like programming?",font="Tahoma 10 bold")
x.pack(padx=10)

mygroup=StringVar()
myoption1=Radiobutton(myframe,text="Yes",variable=mygroup,value="yes")
myoption1.pack()
myoption2=Radiobutton(myframe,text="No",variable=mygroup,value="NO")
myoption2.pack()

p=Label(myframe,text="There are many programming languages including:"
,font="Tahoma 10 bold")
p.pack(padx=10)


mylist=Listbox(myframe)

mylist.pack(padx=30)
mylist.insert(1,"python")
mylist.insert(2,"JavaScript")
mylist.insert(3,"c++")
mylist.insert(4,"c#")

mycheck=Checkbutton(myframe,text="remember me:)")
mycheck.pack()














myframe.mainloop()