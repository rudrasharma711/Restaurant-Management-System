from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
import sqlite3

a = Tk()
wid = a.winfo_screenwidth()
height = a.winfo_screenheight()
a.geometry('%dx%d' %(wid,height))
a.title("ABC Restaurant")
label = Label(a, text = "Welcome To ABC Restaurant", font = ('Metropolis',30,'bold')).place(x = 500, y = 20)
con = sqlite3.connect('restaurant.db')
cur = con.cursor()

class restaurant:
    def __init__(self):
        global menu_items
        global menu_price
        b = Tk()
        b.title("ABC Restaurant")
        wid_1 = b.winfo_screenwidth()
        height_1 = b.winfo_screenheight()
        b.geometry('%dx%d' % (wid_1,height_1))
        b.configure(bg = 'blue')

        MenuBar = Menu(b)
        SubMenu = Menu(MenuBar, tearoff = 0)
        MenuBar.add_command(label = 'Book Now', command = self.book)

        SubMenu1 = Menu(MenuBar, tearoff = 0)
        MenuBar.add_cascade(label = 'Menu', menu = SubMenu1)
        SubMenu1.add_command(label = 'See Menu Here', command = self.menu)

        b.config(menu = MenuBar)

        menu_items = {'1':'Pizza','2':'French Fries','3':'Burger'}
        menu_price = {'1':'100','2':'200','3':'300'}

    def submit(self):
        messagebox.showinfo("Submit","Your Item " + str(item1) + " Has Been Ordered")

    def generate_bill(self):
        h = quantity.get()
        if item1 == menu_items['1']:
            j = menu_price['1']
        elif item1 == menu_items['2']:
            j = menu_price['2']
        elif item1 == menu_items['3']:
            j = menu_price['3']
        k = int(h) * int(j)
        l = k + 5
        if item2 == 'YES':
            xy = l - 4
        else:
            xy = l
        messagebox.showinfo("Generate Bill", "Your Bill (" + str(xy) + " AED) Has Been Made")
        self.feedback()
            
    def book(self):
        c = Tk()
        c.geometry("1920x1080")
        label = Label(c,text = "Book Here", font = ('Metropolis',20,'')).place(x = 10, y = 15)
        label_2 = Label(c, text = 'Table No.', font = ('Metropolis',20,'')).place(x = 50, y = 50)
        label_3 = Label(c,text = 'Item', font = ('Metropolis',20,'')).place(x = 50, y = 100)
        label_4 = Label(c,text = 'Quantity', font = ('Metropolis',20,'')).place(x = 50, y = 150)
        label_5 = Label(c,text = 'Do you have a Corporate or a Government ID with you?', font = ('Metropolis',20,'')).place(x = 50, y = 200)

        
        def get_value(event):
            global item1 
            global item2 
            item1 =  i.get()
            item2 = f.get()


        global table_number, quantity
        table_number = Entry(c)
        quantity = Entry(c)
        table_number.place(x = 200, y = 50)
        quantity.place(x = 200, y = 150)
        item = StringVar()
        item_1 = StringVar()
        i = ttk.Combobox(c, width = 20, textvariable =  item)
        i['value'] =  ('none', menu_items['1'],menu_items['2'],menu_items['3'])
        i.place(x = 200, y = 100)
        i.current(0)
        i.bind("<<ComboboxSelected>>",get_value)
        f = ttk.Combobox(c, width = 20, textvariable =  item_1)
        f['value'] =  ('none', 'YES','NO')
        f.place(x = 800, y = 205)
        f.current(0)
        f.bind("<<ComboboxSelected>>",get_value)
        b1 = Button(c, text = "Submit", font = ('Metropolis',20,''), command = self.submit).place(x = 50, y = 300)
        b2 = Button(c,text = "Generate Bill", font = ('Metropolis',20,''), command = self.generate_bill).place(x = 200, y = 300)
                                                                           

    def menu(self):
        
        d = Tk()
        d.geometry("700x650")

        label_ = Label(d,text = 'Menu', font = ('Metropolis',20,'')).place(x = 10, y = 10)
        label_7 = Label(d,text = 'Item', font = ('Metropolis',20,'')).place(x = 20, y = 90)
        label_8 = Label(d,text = 'Price', font = ('Metropolis',20,'')).place(x = 200, y = 90)
        
        label_1 = Label(d, text = menu_items['1'], font=('Metropolis',20,'')).place(x = 10, y = 120)
        label_2 = Label(d, text = menu_items['2'], font=('Metropolis',20,'')).place(x = 10, y = 180)
        label_3 = Label(d, text = menu_items['3'], font=('Metropolis',20,'')).place(x = 10, y = 240)

        label_4 = Label(d, text = menu_price['1'], font=('Metropolis',20,'')).place(x = 200, y = 120)
        label_5 = Label(d, text = menu_price['2'], font=('Metropolis',20,'')).place(x = 200, y = 180)
        label_6 = Label(d, text = menu_price['3'], font=('Metropolis',20,'')).place(x = 200, y = 240)

    def save_feedback(self):
        vb = name.get()
        vc = email.get()
        vd = DOB.get()
        sql = "INSERT INTO restaurant VALUES(?,?,?,?,?)"
        xyz = (vb,vc,vd,item4,item5)
        try:
            cur.execute(sql,xyz)
            con.commit()
            messagebox.showinfo("Feedback Form","Feedback Saved")
        except:
            con.roleback()
            messagebox.showinfo("Feedback Form", "Feedback not saved")
            
            
    def feedback(self):
        v = Tk()
        v.geometry("1920x1080")

        label = Label(v, text = "Feedback Form", font = ('Metropolis', 20,'')).place(x = 10, y = 5)
        l1 = Label(v, text = "Name", font = ('Metropolis',20,'')).place(x = 20, y = 50)
        l2 = Label(v, text = "Email Id", font = ('Metropolis', 20,'')).place(x = 20, y = 100)
        l3 = Label(v, text = "DOB", font = ('Metropolis',20,'')).place(x = 20, y = 150)
        l4 = Label(v,text = "Service Rating", font = ('Metropolis',20,'')).place(x = 20, y = 200)
        l5 = Label(v,text = "Food Rating", font = ('Metropolis',20,'')).place(x = 20, y = 250)
        global name, email, DOB
    
        name = Entry(v)
        email = Entry(v)
        DOB = Entry(v)
        name.place(x = 150, y = 50)
        email.place(x = 150, y = 100)
        DOB.place(x = 150, y = 150)

        def get_value1(event):
            global item4, item5
            item4 = u.get()
            item5 = xz.get()

        item3 = StringVar()
        item0 = StringVar()
        
        u = ttk.Combobox(v, width = 20, textvariable =  item3)
        u['value'] =  ('0','1','2','3','4','5')
        u.place(x = 300, y = 200)
        u.current(0)
        u.bind("<<ComboboxSelected>>",get_value1)

        xz = ttk.Combobox(v, width = 20, textvariable =  item0)
        xz['value'] =  ('0','1','2','3','4','5')
        xz.place(x = 300, y = 250)
        xz.current(0)
        xz.bind("<<ComboboxSelected>>",get_value1)

        button = Button(v, text = "Submit", font = ('Metropolis',20,''), command = self.save_feedback).place(x = 50, y = 400)
        
def begin():
    a.destroy()
    n = restaurant()

a.after(2000,begin)

