from tkinter import *

class Library:
    global Books
    global Borrowers
    Books=['Heart of Darkness','Birthday Girl','Pride and Projudice','Black Clover','When They Cry','Tokyo Ghoul','Demon Slayer','Python','SQL','Harry Potter']
    Borrowers={}
    def __init__(self,master):
        self.frame=Frame(master)
        self.b1=Button(self.frame,text="Display Books",fg="black",bg="#71B0F7",width=12,height=2,command=self.display)
        self.b1.grid(row=30,column=30,padx=50,pady=100)
        self.b2=Button(self.frame,text="Add Book",fg="black",bg="#71B0F7",width=12,height=2,command=self.add)
        self.b2.grid(row=30,column=50,padx=100,pady=100)
        self.b3=Button(self.frame,text="Lend Book",fg="black",bg="#71B0F7",width=12,height=2,command=self.lend)
        self.b3.grid(row=32,column=30,padx=50,pady=0)
        self.b4=Button(self.frame,text="Return Book",fg="black",bg="#71B0F7",width=12,height=2,command=self.returnb)
        self.b4.grid(row=32,column=50,padx=100,pady=0)
        self.l1=Label(text="Welcome to the Student Library Application.\nTo proceed click on the desired option,\nand to exit click on the cross button on your top right.", fg="black",bg="#ECECEC")
        self.l1.place(x=70,y=10)
        self.frame.grid()

    def display(self):
        pop=Toplevel(root)
        pop.title("Books")
        pop.geometry("300x300")
        l=Label(pop,text="LIST OF BOOKS:\n"+'\n'.join(Books),fg="black",bg="#ECECEC")
        l.place(x=150,y=100,anchor='center')
        b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=pop.destroy)
        b.place(x=150,y=260,anchor="center")

    def add(self):
        pop=Toplevel(root)
        pop.title("Books")
        pop.geometry("300x300")
        l=Label(pop,text="Enter the Name of the Book",fg="black",bg="#ECECEC")
        l.place(x=150,y=150,anchor='center')
        e=Entry(pop,text="book_name",bg="#71B0F7",bd=5)
        e.place(x=150,y=110,anchor='center')
        b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=lambda:[add1(),pop.destroy()])
        b.place(x=150,y=220,anchor='center')
        def add1():
            name=e.get()
            Books.append(name)
            pop=Toplevel(root)
            pop.title("Books")
            pop.geometry("150x150")
            l=Label(pop,text="Added!",fg="black",bg="#ECECEC")
            l.place(x=75,y=25,anchor='center')
            b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=pop.destroy)
            b.place(x=70,y=95,anchor="center")
            e.delete(0,'end')

    def lend(self):
        pop=Toplevel(root)
        pop.title("Borrow a Book")
        pop.geometry("300x300")
        l1=Label(pop,text="Enter the Name of the Book",fg="black",bg="#ECECEC")
        l1.place(x=150,y=150,anchor='center')
        e1=Entry(pop,text="book_name",bg="#71B0F7",bd=5)
        e1.place(x=150,y=130,anchor='center')
        l2=Label(pop,text="Enter Your Name",fg="black",bg="#ECECEC")
        l2.place(x=150,y=90,anchor='center')
        e2=Entry(pop,text="borrower_name",bg="#71B0F7",bd=5)
        e2.place(x=150,y=70,anchor='center')
        b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=lambda:[add2(),pop.destroy()])
        b.place(x=150,y=220,anchor='center')
        def add2():
            Pname=e2.get()
            Bname=e1.get()
            if(Bname in Books):
                if(Bname not in Borrowers.keys()):
                    Borrowers[Bname]=Pname
                else:
                    pop=Toplevel(root)
                    pop.title("oops")
                    pop.geometry("200x150")
                    l=Label(pop,text="Book is already with\n"+Borrowers[Bname],fg="black",bg="#ECECEC")
                    l.place(x=100,y=25,anchor='center')
                    b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=pop.destroy)
                    b.place(x=100,y=95,anchor="center")
            else:
                pop=Toplevel(root)
                pop.title("oops")
                pop.geometry("300x150")
                l=Label(pop,text="Book is not present in the Library's collection",fg="black",bg="#ECECEC")
                l.place(x=150,y=25,anchor='center')
                b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=pop.destroy)
                b.place(x=150,y=95,anchor="center")
            e1.delete(0,'end')
            e2.delete(0,'end')

    def returnb(self):
        pop=Toplevel(root)
        pop.title("Books")
        pop.geometry("300x300")
        l=Label(pop,text="Enter the name of the book you want to return",fg="black",bg="#ECECEC")
        l.place(x=150,y=150,anchor='center')
        e=Entry(pop,text="book_name",bg="#71B0F7",bd=5)
        e.place(x=150,y=110,anchor='center')
        b=Button(pop,text="Close",fg="black",bg="#71B0F7",width=12,height=2,command=lambda:[remove(),pop.destroy()])
        b.place(x=150,y=220,anchor='center')

        def remove():
            Bname=e.get()
            del Borrowers[Bname]
            e.delete(0,'end')
        
        
root=Tk()
root.title('STUDENT LIBRARY')
root.geometry('450x350')
gui=Library(root)
root.mainloop()
