from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


try:
    con = mysql.connector.connect(host='localhost', user='root', password="password", database='Information')
    cur = con.cursor()
except mysql.connector.Error as e:
    print(e)

class Student_info:

    def __init__(self, root):

        self.root = root
        self.main_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font="Calibri 20 bold")
        self.main_lbl.grid(row=0,column=4)
        #--------label---------
        self.firstnframe = Label(self.root, text='First Name')
        self.firstnframe.grid(row=0, column=0, padx=15, pady=15)

        self.lnamef = Label(self.root,text='Last Name')
        self.lnamef.grid(row=1, column=0, padx=15, pady=15)

        self.lblAdd = Label(self.root,text="Address")
        self.lblAdd.grid(row=2, column=0, padx=15, pady=15)

        self.lblage = Label(self.root,text='Age')
        self.lblage.grid(row=3, column=0, padx=15, pady=15)

        self.lbldegree = Label(self.root, text='Degree')
        self.lbldegree.grid(row=4, column=0, padx=15, pady=15)

        self.lblcontact = Label(self.root, text='Contact')
        self.lblcontact.grid(row=5, column=0, padx=15, pady=15)

        #---------Entry---------
        self.firsten = Entry(self.root)
        self.firsten.grid(row=0, column=1, padx=15, pady=15)

        self.len = Entry(self.root)
        self.len.grid(row=1, column=1, padx=15, pady=15)

        self.Adden = Entry(self.root)
        self.Adden.grid(row=2, column=1, padx=15, pady=15)

        self.ageen = Entry(self.root)
        self.ageen.grid(row=3, column=1, padx=15, pady=15)

        self.degree = Entry(self.root)
        self.degree.grid(row=4, column=1, padx=15, pady=15)

        self.contact = Entry(self.root)
        self.contact.grid(row=5, column=1, padx=15, pady=15)



        #------------frame---------
        self.rect_frame=Frame(self.root,bd=4,bg='peachpuff4',relief=RIDGE)
        self.rect_frame.place(x=20,y=360,width=500,height=300)

        self.manage_frame = Frame(self.rect_frame, bd=4, bg='bisque4', relief=RIDGE)
        self.manage_frame.place(x=10, y=10, width=460, height=50)

        self.square_frame=Frame(self.rect_frame, bd=4, bg='bisque4', relief=RIDGE)
        self.square_frame.place(x=10, y=80, width=460, height=200)

        self.detail_frame = Frame(self.root, bd=4, relief=RIDGE)
        self.detail_frame.place(x=290, y=50, width=500, height=280)
        # -------scrollbar--------

        self.scroll_x = Scrollbar(self.detail_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.detail_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)




        #table########################33
        self.student_table = ttk.Treeview(self.detail_frame, columns=('fname', 'lname', 'Address', 'Age', 'Contact',
                                                                     'Degree'),xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.student_table.heading('fname', text='Full Name')
        self.student_table.heading('lname', text='Last Name')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Age', text='Age')
        self.student_table.heading('Contact', text='Contact')
        self.student_table.heading('Degree', text='Degree')

        self.student_table.pack(fill=BOTH, expand=True)

        self.student_table['show'] = 'headings'

        self.student_table.column('fname', width=150)
        self.student_table.column('lname', width=150)
        self.student_table.column('Address', width=150)
        self.student_table.column('Age', width=150)
        self.student_table.column('Contact', width=150)
        self.student_table.column('Degree', width=150)
        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        # -----------button--------
        self.addbtn = Button(self.manage_frame, text='Add',command=self.add_info, width=10, height=2)
        self.addbtn.place(x=0, y = 0)

        self.upbtn = Button(self.manage_frame, text='Update',command=self.update, width=10, height=2)
        self.upbtn.place(x=92, y = 0)
        self.deletebtn = Button(self.manage_frame, text='Delete',width=10,command=self.delete, height=2)
        self.deletebtn.place(x=184, y = 0)
        self.clearbtn = Button(self.manage_frame, text='Clear',  width=10,command=self.clear, height=2)
        self.clearbtn.place(x=276, y = 0)

        self.showbtn = Button(self.manage_frame, text='Show All', width=10, command = self.show, height=2)
        self.showbtn.place(x=368, y=0)

        self.lblsearch = Label(self.square_frame, text='Search By', font=('Calibri', 10))
        self.lblsearch.grid(row=0, column=0, pady=5)
        self.lblsort = Label(self.square_frame, text='Sort By', font=('Calibri', 10))
        self.lblsort.grid(row=2, column=0, pady=5)

        self.searchcombo = ttk.Combobox(self.square_frame, font=('Calibri', 10), state='readonly')
        self.searchcombo['values'] = ('fname', 'lname', 'Address', 'Age', 'Degree', 'Contact')
        self.searchcombo.set("fname")
        self.searchcombo.grid(row=0, column=1, pady=10, padx=20)

        self.sortcombo = ttk.Combobox(self.square_frame, font=('Calibri', 10), state='readonly')
        self.sortcombo['values'] = ('fname', 'lname', 'Address', 'Age', 'Degree', 'Contact')
        self.sortcombo.set('fname')
        self.sortcombo.grid(row=2, column=1, pady=10, padx=20)

        self.searchlbl = Label(self.square_frame, text='Search text', font=('Calibri', 10))
        self.searchlbl.grid(row=1, column=0, pady=5)

        self.searchentry = Entry(self.square_frame, width=20)
        self.searchentry.grid(row=1, column=1, pady=10, padx=10)

        self.searchbtn = Button(self.square_frame, text='Search',command=self.search, font=('Calibri', 10), width=8)
        self.searchbtn.grid(row=1, column=3, pady=10, padx=10)

        self.sortbtn = Button(self.square_frame, text='Sort',command=self.sort , font=('Calibri', 10), width=8)
        self.sortbtn.grid(row=2, column=3, pady=10, padx=10)

    def add_info(self):
        fname = self.firsten.get()
        lname = self.len.get()
        Address = self.Adden.get()
        Age = int(self.ageen.get())
        contact = self.contact.get()
        degree = self.degree.get()
        query = 'insert into infos values(%s,%s,%s,%s, %s, %s)'
        values = (fname, lname, Address, Age, contact, degree)
        cur.execute(query,values)
        print('1 row inserted')
        con.commit()
        self.show()
        self.clear()

    def show(self):
        query='select * from infos'
        cur.execute(query)
        rows=cur.fetchall()

        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('',END,values=row)


    def clear(self):
        self.firsten.delete(0,END)
        self.len.delete(0,END)
        self.Adden.delete(0,END)
        self.ageen.delete(0,END)
        self.contact.delete(0,END)
        self.degree.delete(0,END)

    def update(self):

        d1 = self.firsten.get()
        d2 = self.len.get()
        d3 = self.Adden.get()
        d4 = self.ageen.get()
        contact = self.contact.get()
        degree = self.degree.get()

        query='update infos set First_name=%s, Last_name=%s, Address=%s, Contact=%s, Degree=%s where Age=%s'
        values=(d1, d2, d3, contact, degree, d4)
        cur.execute(query,values)
        con.commit()
        self.clear()
        self.show()


    def pointer(self,event):
        point=self.student_table.focus()
        content=self.student_table.item(point)
        row=content['values']
        self.clear()
        self.firsten.insert(0,row[0])
        self.len.insert(0, row[1])
        self.Adden.insert(0, row[2])
        self.ageen.insert(0, row[3])
        self.contact.insert(0, row[4])
        self.degree.insert(0, row[5])

    def delete(self):
        selected_item = self.student_table.selection()
        self.student_table.delete(selected_item)

        age=self.ageen.get()
        query = 'delete from infos where Age=%s'
        values=(age,)
        cur.execute(query,values)
        con.commit()
        self.clear()

    def bubbleSort(self, arr):
        n = len(arr)
        if self.sortcombo.get() == 'fname':
            column = 0
        elif self.sortcombo.get() == 'lname':
            column = 1
        elif self.sortcombo.get() == 'Address':
            column = 2
        elif self.sortcombo.get() == 'Age':
            column = 3
        elif self.sortcombo.get() == 'Degree':
            column = 4
        elif self.sortcombo.get() == 'Contact':
            column = 5
        else:
            return

        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j][column] > arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sort(self):
        query = 'select * from infos'
        cur.execute(query)
        rows = cur.fetchall()

        self.bubbleSort(rows)

        self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)

    def search(self, mylist=None):
        if not mylist:
            query = 'select * from infos'
            cur.execute(query)
            rows = cur.fetchall()
        else:
            rows = mylist
        found = []
        target = self.searchentry.get()
        if self.searchcombo.get() == 'fname':
            column = 0
        elif self.searchcombo.get() == 'lname':
            column = 1
        elif self.searchcombo.get() == 'Address':
            column = 2
        elif self.searchcombo.get() == "Age":
            column = 3
        elif self.sortcombo.get() == 'Degree':
            column = 4
        elif self.sortcombo.get() == 'Contact':
            column = 5
        else:
            return
        for value in rows:
            if target == value[column]:
                found.append(value)

        self.student_table.delete(*self.student_table.get_children())

        for row in found:
            self.student_table.insert('', END, values=row)

        return found


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x850+0+0')
    root.configure(bg='navajowhite4')
    root.title('Student Form')

    gui = Student_info(root)
    root.mainloop()