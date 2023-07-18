from tkinter import*
from tkinter import ttk
#import pymysql
import time
import datetime
import mysql.connector
from tkinter import messagebox
import uuid
import math
import random
import string



root=Tk()
class bank():
    def __init__(self,root):
        self.root=root
        self.root.title("Bank Managementsystem")
        self.root.geometry("1500x900+0+0")

        title=Label(self.root,text="Bank Management System",bd=9,relief=GROOVE, font=("times now roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

#************All Variables************
        
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.aadhar_var = StringVar()
        self.acc_type_var = StringVar()
        self.pan_var = StringVar()
        self.acc_no_var = StringVar()
        self.acc_bal_var = StringVar()
        #self.search_by=StringVar()
        #self.search_txt=StringVar()

#************MANAGE FRAME************

        MANAGE_FRAME=Frame( self.root ,bd=4,relief=RIDGE,bg="blue")
        MANAGE_FRAME.place(x=20,y=100,width=500,height=650)

        m_title=Label(MANAGE_FRAME,text="Manage Bank",bg="yellow",fg="black",font=("times new roman",38,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20,sticky="w")

        lbl_firstName=Label(MANAGE_FRAME,text="First Name:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_firstName.grid(row=1,column=0,pady=10,padx=20,sticky="W")
        txt_firstName=Entry(MANAGE_FRAME,textvariable=self.firstname_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_firstName.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_LastName=Label(MANAGE_FRAME,text="Last Name:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_LastName.grid(row=2,column=0,pady=10,padx=20,sticky="W")
        txt_LastName=Entry(MANAGE_FRAME,textvariable=self.lastname_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_LastName.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_aadhar=Label(MANAGE_FRAME,text="Aadhar:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_aadhar.grid(row=3,column=0,pady=10,padx=20,sticky="W")
        txt_aadhar=Entry(MANAGE_FRAME,textvariable=self.aadhar_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_aadhar.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_accType=Label(MANAGE_FRAME,text="Account Type:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_accType.grid(row=4,column=0,pady=10,padx=20,sticky="W")
        combo_accType=ttk.Combobox(MANAGE_FRAME,textvariable=self.acc_type_var,font=("times new roman",13,"bold"),state="readonly")
        combo_accType['values']=("Savings","Current")
        combo_accType.grid(row=4,column=1,padx=30,pady=20,sticky="w")

        lbl_pan=Label(MANAGE_FRAME,text="Pan:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_pan.grid(row=5,column=0,pady=10,padx=20,sticky="W")
        txt_pan=Entry(MANAGE_FRAME,textvariable=self.pan_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_pan.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_AccNo=Label(MANAGE_FRAME,text="Account No",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_AccNo.grid(row=6,column=0,pady=10,padx=20,sticky="W")
        txt_AccNo=Entry(MANAGE_FRAME,textvariable=self.acc_no_var,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_AccNo.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_AccBal=Label(MANAGE_FRAME,text="Account Balance:",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_AccBal.grid(row=7,column=0,pady=10,padx=20,sticky="W")
        txt_AccBal=Entry(MANAGE_FRAME,textvariable=self.acc_bal_var,width=20,font=("times in roman",15,"bold"),bd=5,relief=GROOVE)
        txt_AccBal.grid(row=7,column=1,pady=10,padx=20,sticky="w")

#***********************BUTTONS*******************
        btn_frame=Frame(MANAGE_FRAME,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=525,width=500)

        creatAcc=Button(btn_frame,text="Creat Acc",width=10,command=self.creat_acc).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="Clear",width=8,command=self.reset_data).grid(row=0,column=3,padx=10,pady=10)
        withdrawbtn=Button(btn_frame,text="Withdraw",width=10,command=self.withdraw).grid(row=1,column=0,padx=10,pady=10)
        depositbtn=Button(btn_frame,text="Deposit",width=10,command=self.deposit).grid(row=1,column=1,padx=10,pady=10)
        transactionbtn=Button(btn_frame,text="Done Transection",width=15,command=self.done_transactions).grid(row=1,column=2,padx=10,pady=10)
        see_transactionbtn=Button(btn_frame,text="See Transactions",width=15,command=self.see_transactions).grid(row=1,column=3,padx=10,pady=10)
#************DETAILS FRAME************

        DETAILS_FRAME=Frame(self.root ,bd=4,relief=RIDGE,bg="blue")
        DETAILS_FRAME.place(x=550,y=100,width=880,height=650)

        self.com_search_var=StringVar()
        lbl_search=Label(DETAILS_FRAME,text="Search by",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        combo_search=ttk.Combobox(DETAILS_FRAME,font=("times new roman",13,"bold"),textvariable=self.com_search_var,width=10,state="readonly")
        combo_search['values']=("Aadhar","AccType","AccNo")
        combo_search.grid(row=0,column=1,padx=20,pady=10,sticky="w")

        self.search_var=StringVar()
        txt_search=Entry(DETAILS_FRAME,textvariable=self.search_var,font=("times in roman",10,"bold"),width=20,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(DETAILS_FRAME,text="Search",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showAllbtn=Button(DETAILS_FRAME,text="ShowAll",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

#************Table FRAME************

        TABLE_FRAME=Frame(DETAILS_FRAME ,bd=4,relief=RIDGE,bg="crimson")
        TABLE_FRAME.place(x=10,y=70,width=768,height=500)

        scroll_x=Scrollbar(TABLE_FRAME,orient=HORIZONTAL)
        scroll_y=Scrollbar(TABLE_FRAME,orient=VERTICAL)

        self.Bank_table=ttk.Treeview(TABLE_FRAME,column=("First Name","Last Name","Aadhar","Acc Type","Pan","Acc No.","Acc Bal"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config()
        scroll_y.config()

        self.Bank_table.heading("First Name", text="First Name")
        self.Bank_table.heading("Aadhar", text="Aadhar")
        self.Bank_table.heading("Last Name", text="Last Name")
        self.Bank_table.heading("Acc Type", text="Acc Type")
        self.Bank_table.heading("Pan", text="Pan")
        self.Bank_table.heading("Acc No.", text="Acc No.")
        self.Bank_table.heading("Acc Bal", text="Acc Bal")

        self.Bank_table['show'] = 'headings'
        self.Bank_table.column("First Name", width=100)
        self.Bank_table.column("Last Name", width=100)
        self.Bank_table.column("Aadhar", width=100)
        self.Bank_table.column("Acc Type", width=100)
        self.Bank_table.column("Pan", width=100)
        self.Bank_table.column("Acc No.", width=100)
        self.Bank_table.column("Acc Bal", width=100)


        self.Bank_table.pack(fill=BOTH,expand=1)
        self.Bank_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

#*************function declaration**********

    def creat_acc(self):
        if self.aadhar_var.get()=="" or self.acc_no_var.get()=="" or self.firstname_var.get()=="" or self.lastname_var.get()=="" or self.pan_var.get()=="" or self.acc_bal_var.get()=="":
            messagebox.showerror('Error!', 'All Fields are required')
        elif len(self.pan_var.get())!=10:
             messagebox.showerror('Error!','Enter 10 digits in pan')
        elif len(self.aadhar_var.get())!=12:
            messagebox.showerror('Error!','Enter 12 digits in Aadhar')
        elif len(self.acc_no_var.get())!=8:
             messagebox.showerror('Error!','Enter 8 digits in Account No.')
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Anjali@9822", database='bankdata')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into bankdata2 values(%s,%s,%s,%s,%s,%s,%s)", (
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.aadhar_var.get(),
                self.acc_type_var.get(),
                self.pan_var.get(),
                self.acc_no_var.get(),
                self.acc_bal_var.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Account has been created', parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror('Error', f'Due To: {str(err)}', parent=self.root)


#***************Fetch data*************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anjali@9822",database='bankdata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from bankdata2')
        data=my_cursor.fetchall()
        if len(data)!=0:
                self.Bank_table.delete(*self.Bank_table.get_children())
                for i in data:
                     self.Bank_table.insert("",END,values=i)
                conn.commit()
        conn.close()

#***********Get_cursor**********

    def get_cursor(self,event=" "):
        cursor_row=self.Bank_table.focus()
        content=self.Bank_table.item(cursor_row)
        data=content['values']

        self.firstname_var.set(data[0])
        self.lastname_var.set(data[1])
        self.aadhar_var.set(data[2])
        self.acc_type_var.set(data[3])
        self.pan_var.set(data[4])
        self.acc_no_var.set(data[5])
        self.acc_bal_var.set(data[6])
        #self.search_by.set(data[7])
        #self.search_t.set(data[8])

    
#****************update data***********
    def update_data(self):
        if self.aadhar_var.get()=="" or self.acc_no_var.get()=="" or self.firstname_var.get()=="" or self.lastname_var.get()=="" or self.pan_var.get()=="" or self.acc_bal_var.get()=="":
            messagebox.showerror('Error!','All Fields are required')
        elif len(self.pan_var.get())!=10:
             messagebox.showerror('Error!','Enter 10 digits in pan')
        elif len(self.aadhar_var.get())!=12:
            messagebox.showerror('Error!','Enter 12 digits in Aadhar')
        elif len(self.acc_no_var.get())!=8:
             messagebox.showerror('Error!','Enter 8 digits in Account No.')
        
        else:
                try:
                        update=messagebox.askyesno('update','Are you sure to update this data')
                        if update>0:
                                conn=mysql.connector.connect(host="localhost",username="root",password="Anjali@9822",database='bankdata')
                                my_cursor=conn.cursor()
                                #print("Connect")
                                                        
                                my_cursor.execute("UPDATE bankdata2 SET LastName=%s, Aadhar=%s, AccType=%s, Pan=%s, AccBal=%s ,AccNo=%s WHERE FirstName=%s",
                                                                                                                                                        (
                                                                                                                                                        self.lastname_var.get(),
                                                                                                                                                        self.aadhar_var.get(),
                                                                                                                                                        self.acc_type_var.get(),
                                                                                                                                                        self.pan_var.get(),
                                                                                                                                                        self.acc_bal_var.get(),
                                                                                                                                                        self.acc_no_var.get(),
                                                                                                                                                        self.firstname_var.get()
                                                                                                                                                        ))

                        else:
                               if not update:
                                     return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('success','Account successfully updated',parent=self.root)
                except Exception as es:
                     messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    
#*****************DELETE********************

    def delete_data(self):
        if self.aadhar_var.get()=="" or self.acc_no_var.get()=="" or self.firstname_var.get()=="" or self.lastname_var.get()=="" or self.pan_var.get()=="" or self.acc_bal_var.get()=="":
            messagebox.showerror('Error!','All Fields are required')
        else:
                try:
                        Delete=messagebox.askyesno('Delete','Are you sure to delete this account',parent=self.root)
                        if Delete>0:
                                conn=mysql.connector.connect(host="localhost",username="root",password="Anjali@9822",database='bankdata')
                                my_cursor=conn.cursor()
                                sql='delete from bankdata2 where firstname=%s'
                                value=(self.firstname_var.get(),)
                                my_cursor.execute(sql,value)                  
                        else:
                              if not Delete:
                                    return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('success','Account has been deleted',parent=self.root)
                except Exception as es:
                     messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

#***************RESET***********
    def reset_data(self):
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.aadhar_var.set("")
        self.acc_type_var.set("Savings")
        self.pan_var.set("")
        self.acc_no_var.set("")
        self.acc_bal_var.set("")

#*****************SEARCH***************************

    def search_data(self):
        if self.search_var.get()=="" or self.com_search_var.get()=="":
            messagebox.showerror('Error!','All Fields are required')
        else:
                try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Anjali@9822",database='bankdata')
                        my_cursor=conn.cursor()
                        #print("Connect")
                        my_cursor.execute('select * from bankdata2 where ' +str(self.com_search_var.get())+" LIKE '%"+str(self.search_var.get()+"%'"))
                        rows=my_cursor.fetchall()
                        if len(rows)!=0:
                              self.Bank_table.delete(*self.Bank_table.get_children())
                              for i in rows:
                                    self.Bank_table.insert("",END,values=i)
                        conn.commit()
                        conn.close()
                except Exception as es:
                     messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

#***************WITHDRAW******************

    def withdraw(self):
      withdraw_window = Toplevel(root)
      withdraw_window.title("Withdraw")
      withdraw_window.geometry('400x200')
    #   title = Label(withdraw_window, text="Withdraw your money", bd=3, relief=GROOVE, font=("times now roman", 12, "bold"), bg="pink", fg="black")
    #   title.pack(side=TOP, fill=X)

      amount=Label(withdraw_window, text="Amount:", font=("times new roman", 15, "bold"), bg = 'yellow',fg="black")
      amount.grid(row=3, column=0, padx=10, pady=10, sticky='W')
      #self.amount_var=IntVar()

      self.withdraw_amount_var=IntVar()

      amount_txt=Entry(withdraw_window,textvariable=self.withdraw_amount_var,font=("times in roman", 15, "bold"), bd=5, relief=GROOVE)
      amount_txt.grid(row=3, column=3, padx=10, pady=10, sticky='W')

      withdraw_btn1=Button(withdraw_window,text="Withdraw",font=("times new roman",15,"bold"),command=self.withdraw_fun,bg="pink",fg="black").grid(row=6,column=3,padx=10,pady=10)
      #deposit_btn1=Button(withdraw_window,text="",font=("times new roman",15,"bold"),command=self.deposit_fun,bg="pink",fg="black").grid(row=6,column=3,padx=10,pady=10)
      #amount.pack()
      
    def withdraw_fun(self):
        if self.acc_no_var.get() == "" or self.acc_bal_var.get() == "":
          messagebox.showerror("Error!", "Please enter Account No. and Account Balance.")
        else:
           try:
            #withdraw_amount = int(self.amount_var.get())
            withdraw_amount = self.withdraw_amount_var.get()

            conn = mysql.connector.connect(host="localhost", username="root", password="Anjali@9822", database='bankdata')
            my_cursor = conn.cursor()

            # Check if account exists and has sufficient balance
            my_cursor.execute("SELECT * FROM bankdata2 WHERE AccNo = %s", (self.acc_no_var.get(),))
            account = my_cursor.fetchone()
            if account:
                balance = float(account[6])
                if withdraw_amount > balance:
                    messagebox.showerror("Insufficient Balance","Withdrawal amount exceeds account balance.")
                else:
                    new_balance = balance - withdraw_amount
                    # Update account balance in the database
                    my_cursor.execute("UPDATE bankdata2 SET AccBal = %s WHERE AccNo = %s", (new_balance, self.acc_no_var.get()))
                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Amount successfully withdrawn.")
            else:
                messagebox.showerror("Account Not Found", "Account with the specified Account No. does not exist.")

            conn.close()

           except Exception as es:
            messagebox.showerror("Error", f"Error occurred: {str(es)}")
    

    def deposit(self):
      withdraw_window = Toplevel(root)
      withdraw_window.title("Withdraw")
      withdraw_window.geometry('400x200')
    #   title = Label(withdraw_window, text="Withdraw your money", bd=3, relief=GROOVE, font=("times now roman", 12, "bold"), bg="pink", fg="black")
    #   title.pack(side=TOP, fill=X)

      amount=Label(withdraw_window, text="Amount:", font=("times new roman", 15, "bold"), bg = 'yellow',fg="black")
      amount.grid(row=3, column=0, padx=10, pady=10, sticky='W')
      #self.amount_var=IntVar()

      self.deposit_amount_var=IntVar()

      amount_txt=Entry(withdraw_window,textvariable=self.deposit_amount_var,font=("times in roman", 15, "bold"), bd=5, relief=GROOVE)
      amount_txt.grid(row=3, column=3, padx=10, pady=10, sticky='W')

      deposit_btn1=Button(withdraw_window,text="deposit",font=("times new roman",15,"bold"),command=self.deposit_fun,bg="pink",fg="black").grid(row=6,column=3,padx=10,pady=10)

    def deposit_fun(self):
        if self.acc_no_var.get() == "" or self.acc_bal_var.get() == "":
          messagebox.showerror("Error!", "Please enter Account No. and Account Balance.")
        else:
           try:
            #withdraw_amount = int(self.amount_var.get())
            deposit_amount = self.deposit_amount_var.get()

            conn = mysql.connector.connect(host="localhost", username="root", password="Anjali@9822", database='bankdata')
            my_cursor = conn.cursor()

            # Check if account exists and has sufficient balance
            my_cursor.execute("SELECT * FROM bankdata2 WHERE AccNo = %s", (self.acc_no_var.get(),))
            account = my_cursor.fetchone()
            if account:
                balance = float(account[6])
                # if withdraw_amount > balance:
                #     messagebox.showerror("Insufficient Balance","Withdrawal amount exceeds account balance.")
            
                new_balance = balance + deposit_amount
                # Update account balance in the database
                my_cursor.execute("UPDATE bankdata2 SET AccBal = %s WHERE AccNo = %s", (new_balance, self.acc_no_var.get()))
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Amount successfully deposited.")
            else:
                messagebox.showerror("Account Not Found", "Account with the specified Account No. does not exist.")

            conn.close()

           except Exception as es:
            messagebox.showerror("Error", f"Error occurred: {str(es)}")
    
#**************Transaction***********
    # def generate_transaction_id(self):
    #     transaction_id = str(uuid.uuid4())
    #     return transaction_id
    
    def generate_transaction_id(self):
        transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return transaction_id


    def done_transactions(self):

        # Open a new window for displaying transactions
    #     transaction_window = Toplevel()
    #     transaction_window.title("Transactions")
    #     transaction_window.geometry("600x400")

    #     title=Label(transaction_window,text="Transactions",bd=9,relief=GROOVE, font=("times now roman",25,"bold"),bg="green",fg="black")
    #     title.pack(side=TOP,fill=X)
    #     # T_FRAME=Frame(self.root ,bd=4,relief=RIDGE,bg="blue")
    #     # T_FRAME.place(x=500,y=100,width=600,height=300)

    # # Create a treeview to display the transactions
    #     self.transaction_tree = ttk.Treeview(transaction_window, column=("Transaction ID", "Account No.", "Withdrawn Amount", "Deposited Amount","Account Balance"), show="headings")
    #     self.transaction_tree.heading("Transaction ID", text="Transaction ID")
    #     self.transaction_tree.heading("Account No.", text="Account No.")
    #     self.transaction_tree.heading("Withdrawn Amount", text="Withdrawn Amount")
    #     self.transaction_tree.heading("Deposited Amount", text="Deposited Amount")
    #     self.transaction_tree.heading("Account Balance", text="Account Balance")

    #     self.transaction_tree['show'] = 'headings'
    #     self.transaction_tree.column("Transaction ID", width=200)
    #     self.transaction_tree.column("Account No.", width=100)
    #     self.transaction_tree.column("Withdrawn Amount", width=100)
    #     self.transaction_tree.column("Deposited Amount", width=100)
    #     self.transaction_tree.column("Account Balance", width=100)

    # # Add scrollbar to the treeview
    #     scrollbar = ttk.Scrollbar(transaction_window, orient="vertical", command=self.transaction_tree.yview)
    #     scrollbar.pack(side=RIGHT, fill=Y)
    #     self.transaction_tree.configure(yscrollcommand=scrollbar.set)

    #     self.transaction_tree.pack(fill=BOTH, expand=True)

        transaction_id = self.generate_transaction_id()
    # Fetch transactions from the database and insert into the treeview
        if self.acc_no_var.get()=="" :
            messagebox.showerror('Error!','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Anjali@9822", database='bankdata')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into transactions2 values(%s,%s,%s,%s,%s)",(transaction_id,
                                                                                    self.acc_no_var.get(),
                                                                                    self.withdraw_amount_var.get(),
                                                                                    self.deposit_amount_var.get(),
                                                                                    self.acc_bal_var.get(),
                                                                                    ))
        
                conn.commit()
                #self.fetch_Transaction_data()
                conn.close()
                messagebox.showinfo('success','Transaction Done!',parent=self.root)
            except Exception as es:
                     messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


#***************see Trans*************
    def see_transactions(self):

        # Open a new window for displaying transactions
        transaction_window = Toplevel()
        transaction_window.title("Transactions")
        transaction_window.geometry("600x400")

        title=Label(transaction_window,text="Transactions",bd=9,relief=GROOVE, font=("times now roman",25,"bold"),bg="green",fg="black")
        title.pack(side=TOP,fill=X)
        # T_FRAME=Frame(self.root ,bd=4,relief=RIDGE,bg="blue")
        # T_FRAME.place(x=500,y=100,width=600,height=300)

    # Create a treeview to display the transactions
        self.transaction_tree = ttk.Treeview(transaction_window, column=("Transaction ID", "Account No.", "Withdrawn Amount", "Deposited Amount","Account Balance"), show="headings")
        self.transaction_tree.heading("Transaction ID", text="Transaction ID")
        self.transaction_tree.heading("Account No.", text="Account No.")
        self.transaction_tree.heading("Withdrawn Amount", text="Withdrawn Amount")
        self.transaction_tree.heading("Deposited Amount", text="Deposited Amount")
        self.transaction_tree.heading("Account Balance", text="Account Balance")

        self.transaction_tree['show'] = 'headings'
        self.transaction_tree.column("Transaction ID", width=200)
        self.transaction_tree.column("Account No.", width=100)
        self.transaction_tree.column("Withdrawn Amount", width=100)
        self.transaction_tree.column("Deposited Amount", width=100)
        self.transaction_tree.column("Account Balance", width=100)

    # Add scrollbar to the treeview
        scrollbar = ttk.Scrollbar(transaction_window, orient="vertical", command=self.transaction_tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.transaction_tree.configure(yscrollcommand=scrollbar.set)

        self.transaction_tree.pack(fill=BOTH, expand=True)

        #transaction_id = self.generate_transaction_id()

        self.fetch_Transaction_data()
    # Fetch transactions from the database and insert into the treeview
        # if self.acc_no_var.get()=="" :
        #     messagebox.showerror('Error!','All Fields are required')
        # else:
        #     try:
        #         conn = mysql.connector.connect(host="localhost", username="root", password="Anjali@9822", database='bankdata')
        #         my_cursor = conn.cursor()
        #         my_cursor.execute("insert into transaction1 values(%s,%s,%s,%s,%s)",(transaction_id,
        #                                                                             self.acc_no_var.get(),
        #                                                                             self.withdraw_amount_var.get(),
        #                                                                             self.deposit_amount_var.get(),
        #                                                                             self.acc_bal_var.get(),
        #                                                                             ))
        
        #         conn.commit()
        #         self.fetch_Transaction_data()
        #         conn.close()
        #         #messagebox.showinfo('success','Transaction done',parent=self.root)
        #     except Exception as es:
        #              messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


#*************fetch data for transection table************
    def fetch_Transaction_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anjali@9822",database='bankdata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from transactions2')
        data=my_cursor.fetchall()
        if len(data)!=0:
                self.transaction_tree.delete(*self.transaction_tree.get_children())
                for i in data:
                     self.transaction_tree.insert("",END,values=i)
                conn.commit()
        conn.close()


    
class bank():
    pass 
    #root=Tk()
    obj=bank(root)
    root.mainloop()
        