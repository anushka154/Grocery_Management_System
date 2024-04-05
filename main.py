from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import sqlite3



class Bill_App:
    def reg(self):
        CustName = self.c_name.get()
        CustMob = self.c_phone.get()
        conn = sqlite3.connect("grodetails.db")
        c=conn.cursor()
        c.execute("INSERT INTO grocerypy VALUES ('"+CustName+"','"+CustMob+"')")
        conn.commit()
        conn.close()

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # VARIABLES
        self.c_name=StringVar() 
        self.c_phon=StringVar() 
        self.bill_no=StringVar() 
        z=random.randint(1000,9999) 
        self.bill_no.set(z) 
        self.c_email=StringVar() 
        self.search_bill=StringVar() 
        #self.product=StringVar() 
        self.subcategory=StringVar() 
        self.prices=IntVar()
        self.qty=IntVar() 
        self.sub_total=StringVar() 
        self.tax_input=StringVar() 
        self.total=StringVar() 

        #Product categories list
        self.Category=["Select Option","Fruits","Vegetables","Dairy","Bread/Bakery","Cereals/Pulses","Snacks","Beverages"]

        #Sub Category
        self.SubCatFruits=["Apples","Mangoes","Bananas","Oranges","Watermelon"]
        self.price_Apples= 100
        self.price_Mangoes= 110
        self.price_banana=40
        self.price_Orange= 50
        self.price_watermelon= 70

        self.SubCatVeggie=["Potato","Tomato","Green chillies","Onion"]
        self.price_potato=40
        self.price_tomato=30
        self.price_green=10
        self.price_onion=50

        self.SubCatDairy=["Milk","Cheese","Egg","Paneer"]
        self.price_Milk= 40
        self.price_cheese = 110
        self.price_egg= 6
        self.price_paneer = 120
        
        self.SubCatBread=["White bread","Whole wheat bread","Multi grain","French bread"]
        self.price_white=40
        self.price_whole=45
        self.price_multi=50
        self.price_french=70
        
        self.SubCatCereals=["Rice","Wheat","Oats","Beans","Dry peas"]
        self.price_rice=45
        self.price_wheat=50
        self.price_oats=50
        self.price_beans=35
        self.price_drypeas=40
        
        self.SubCatSnacks=["Lays","Popcorn","Chocolates","Nachos"]
        self.price_lays=10
        self.price_popcorn=25
        self.price_Chocolates=30
        self.price_nachos=35
        
        self.SubCatBev=["Pepsi","Fruit juice","Cold Coffee"]
        self.price_pepsi=35
        self.price_fruitjuice=30
        self.price_Coldcoffee=40


        #Image 1
        img_1=Image.open("D:\PYTHON PROJECT\image\\b1.webp")
        img_1=img_1.resize((380,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=0,y=0,width=380,height=130)

        #Image 2
        img_2=Image.open("D:\PYTHON PROJECT\image\\b2.PNG")
        img_2=img_2.resize((380,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=380,y=0,width=380,height=130)

        #Image 3
        img_3=Image.open("D:\PYTHON PROJECT\image\\b3.jpg")
        img_3=img_3.resize((380,130),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=760,y=0,width=380,height=130)

        #Image 4
        img_4=Image.open("D:\PYTHON PROJECT\image\\b4.jfif")
        img_4=img_4.resize((380,130),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        lbl_img_4=Label(self.root,image=self.photoimg_4)
        lbl_img_4.place(x=1140,y=0,width=380,height=130)

        lbl_title=Label(self.root,text="Nature's Basket",font=("times new roman",35,"bold","italic"),bg="black",fg="light green")
        lbl_title.place(x=0,y=130,width=1530,height=45)

        #Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)    #1000=1 sec

        lbl = Label(lbl_title,font=('times new roman',16,'bold'),bg='black',fg='light green')
        lbl.place(x=0,y=0,width=120,height=45) 
        time()  

        #Main Frame Below Nature's Basket
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=4)
        
        self.lbl_CustName=Label(Cust_Frame,text="Customer Name",font=("times new roman",12,"bold"),bg="white")
        self.lbl_CustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.entry_CustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.entry_CustName.grid(row=1,column=1,padx=5,pady=4)

        self.lbl_Email=Label(Cust_Frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Email.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.entry_Email=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.entry_Email.grid(row=2,column=1,padx=5,pady=4)

        #Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=660,height=140)

        #Category
        self.lblCategory=Label(Product_Frame,text="Select Categories",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=4)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        #Sub Category
        self.lblSubCategory=Label(Product_Frame,text="Subcategory",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,textvariable=self.subcategory,value=[""],font=("times new roman",12,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=4)
        #self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add) 
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.price)  

        #Product Name
        '''self.lblProduct=Label(Product_Frame,text="Product Name",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblProduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,padx=5,pady=4)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)'''

        #Price
        self.lblPrice=Label(Product_Frame,text="Price",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",12,"bold"),width=24,state="readonly")
        self.ComboPrice.grid(row=0,column=3,padx=5,pady=4)

        #Quantity
        self.lblQty=Label(Product_Frame,text="Qty",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",12,"bold"),width=24)
        self.ComboQty.grid(row=1,column=3,padx=5,pady=4)

        #Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=1020,height=340)

        #Image 1
        img_12=Image.open("D:\PYTHON PROJECT\image\\b5.jpg")
        img_12=img_12.resize((500,340),Image.ANTIALIAS)
        self.photoimg_12=ImageTk.PhotoImage(img_12)

        lbl_img_12=Label(MiddleFrame,image=self.photoimg_12)
        lbl_img_12.place(x=0,y=0,width=500,height=340)

        #Image 2
        img_13=Image.open("D:\PYTHON PROJECT\image\\b6.jpg")
        img_13=img_13.resize((500,340),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=500,y=0,width=500,height=340)

        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1050,y=10,width=460,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("times new roman",12,"bold"),fg="white",bg="red",bd=4)
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=22)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("tmes new roman",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        #Right Frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1050,y=45,width=440,height=400)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=455,width=1520,height=150)

        self.lblSubTotal=Label(Bottom_Frame,text="Sub Total",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",12,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,padx=5,pady=2)

        self.lbl_tax=Label(Bottom_Frame,text="Tax",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,padx=5,pady=2)

        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("times new roman",18,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.EntryAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",12,"bold"),width=24)
        self.EntryAmountTotal.grid(row=2,column=1,padx=5,pady=4)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,height=2,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngeanerate_bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,height=2,cursor="hand2")
        self.Btngeanerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,height=2,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,height=2,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,height=2,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,height=2,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome() 

        self.l=[] 

    #************FUNCTION DECLARATION************** 
    def AddItem(self): 
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m) 
        if self.ComboSubCategory.get()=="": 
            messagebox.showerror("Error","Please select the product") 
        else: 
            self.textarea.insert(END,f"\n {self.ComboSubCategory.get()}\t\t\t{self.qty.get()}\t\t{self.m}") 
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l)))) 
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100))) 
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - self.prices.get()))*Tax)/100))))  

    def gen_bill(self):
      if self.ComboSubCategory.get()=="": 
          messagebox.showerror("Error","Please Add to cart the product") 
      else: 
          text=self.textarea.get(10.0,(10.0+float(len(self.l)))) 
          self.welcome() 
          self.textarea.insert(END,text) 
          self.textarea.insert(END,"\n==============================================") 
          self.textarea.insert(END,f"\n Sub Amount:\t\t{self.sub_total.get()}") 
          self.textarea.insert(END,f"\n Tax Amount:\t\t{self.tax_input.get()}") 
          self.textarea.insert(END,f"\n Total Amount:\t\t{self.total.get()}")
          self.textarea.insert(END,f"\n==============================================")
          
    def save_bill(self):
      op=messagebox.askyesno("Save Bill","Do you want to save the bill") 
      if op>0: 
          self.bill_data=self.textarea.get(1.0,END) 
          f1=open('bills/'+str(self.bill_no.get())+".txt",'w') 
          f1.write(self.bill_data) 
          op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully") 
          f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
    
        self.search_bill.set("")
        #self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


    ##WELCOME PAGE
    def welcome(self): 
        self.textarea.delete(1.0,END) 
        self.textarea.insert(END,"\t\t Welcome to Nature's Basket") 
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}") 
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}") 
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}") 
        self.textarea.insert(END,f"\n Customer Email :{self.c_email.get()}")
        self.textarea.insert(END,"\n==============================================") 
        self.textarea.insert(END,"\n Products \t\t\tQty\t\tPrice") 
        self.textarea.insert(END,"\n==============================================\n") 

    def Categories(self,event=""):
        if self.Combo_Category.get()=="Fruits":
            self.ComboSubCategory.config(value=self.SubCatFruits)
            self.ComboSubCategory.current(0)
        if self.Combo_Category.get()=="Vegetables":
            self.ComboSubCategory.config(value=self.SubCatVeggie)
            self.ComboSubCategory.current(0)
        if self.Combo_Category.get()=="Dairy":
            self.ComboSubCategory.config(value=self.SubCatDairy)
            self.ComboSubCategory.current(0)
        
        if self.Combo_Category.get()=="Bread/Bakery":
            self.ComboSubCategory.config(value=self.SubCatBread)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Cereals/Pulses":
            self.ComboSubCategory.config(value=self.SubCatCereals)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Snacks":
            self.ComboSubCategory.config(value=self.SubCatSnacks)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Beverages":
            self.ComboSubCategory.config(value=self.SubCatBev)
            self.ComboSubCategory.current(0) 

    def price(self,event=""):
         #FRUITS  ["Apples","Mangoes","Bananas","Oranges","Watermelon"] 
        if self.ComboSubCategory.get()=="Apples": 
            self.ComboPrice.config(value=self.price_Apples) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Bananas": 
            self.ComboPrice.config(value=self.price_banana) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Oranges": 
            self.ComboPrice.config(value=self.price_Orange) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Mangoes": 
            self.ComboPrice.config(value=self.price_Mangoes) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Watermelon": 
            self.ComboPrice.config(value=self.price_watermelon) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        #Veggie=["Potato","Tomato","Green chillies","Onion"] 
        if self.ComboSubCategory.get()=="Potato": 
            self.ComboPrice.config(value=self.price_potato) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Tomato": 
            self.ComboPrice.config(value=self.price_tomato) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Onion": 
            self.ComboPrice.config(value=self.price_onion) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Green chillies": 
            self.ComboPrice.config(value=self.price_green) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        #Dairy=["Milk","Cheese","Egg","Paneer"] 
        if self.ComboSubCategory.get()=="Milk": 
            self.ComboPrice.config(value=self.price_Milk) 
            self.ComboPrice.current(0)
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Cheese": 
            self.ComboPrice.config(value=self.price_cheese) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Egg": 
            self.ComboPrice.config(value=self.price_egg) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Paneer": 
            self.ComboPrice.config(value=self.price_paneer) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
         
        #Bread=["White bread","Whole wheat bread","Multi grain","French bread"] 
        if self.ComboSubCategory.get()=="White bread": 
            self.ComboPrice.config(value=self.price_white) 
            self.qty.set(1) 
         
        if self.ComboSubCategory.get()=="Whole Wheat bread": 
            self.ComboPrice.config(value=self.price_whole) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Multi grain": 
            self.ComboPrice.config(value=self.price_multi) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="French bread": 
            self.ComboPrice.config(value=self.price_french) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 

  

        #Cereals=["Rice","Wheat","Oats","Beans","Dry peas"] 
        if self.ComboSubCategory.get()=="Rice": 
            self.ComboPrice.config(value=self.price_rice) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Wheat": 
            self.ComboPrice.config(value=self.price_wheat) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Oats": 
            self.ComboPrice.config(value=self.price_oats) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Beans": 
            self.ComboPrice.config(value=self.price_beans) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Dry peas": 
            self.ComboPrice.config(value=self.price_drypeas) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        #Snacks=["Lays","Popcorn","Chocolates","Nachos"] 
        if self.ComboSubCategory.get()=="Lays": 
            self.ComboPrice.config(value=self.price_lays) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Popcorn": 
            self.ComboPrice.config(value=self.price_popcorn) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Chocolates": 
            self.ComboPrice.config(value=self.price_Chocolates) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Nachos": 
            self.ComboPrice.config(value=self.price_nachos) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        #Bev=["Pepsi","Fruit juice","Cold Coffee"] 
        if self.ComboSubCategory.get()=="Pepsi": 
            self.ComboPrice.config(value=self.price_pepsi) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Fruit juice": 
            self.ComboPrice.config(value=self.price_fruitjuice) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 
  
        if self.ComboSubCategory.get()=="Cold Coffee": 
            self.ComboPrice.config(value=self.price_Coldcoffee) 
            self.ComboPrice.current(0) 
            self.qty.set(1) 






if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()