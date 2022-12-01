
from datetime import datetime
start_time = datetime.now()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")



########### importing libraries 
import socket 
import threading
import tkinter 
import tkinter.scrolledtext
from tkinter import *
from tkinter import ttk
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from random import randint
from time import sleep 


####### defining host and port
HOST = "192.168.56.1"
PORT = 9000

####### email function
def handle_email(client_email,rand):
    def send_mail(fromaddr, frompasswd, toaddr, msg_subject, msg_body):
        try:
            msg = MIMEMultipart()
            print("[+] Message Object Created")
        except:
            print("[-] Error in Creating Message Object")
            return
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = msg_subject
        body = msg_body
        msg.attach(MIMEText(body, 'plain'))
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # s = smtplib.SMTP('mail.iitp.ac.in', 587)
            print("[+] SMTP Session Created")
        except:
            print("[-] Error in creating SMTP session")
            return

        s.starttls()

        try:
            s.login(fromaddr, frompasswd)
            print("[+] Login Successful")
        except:
            print("[-] Login Failed")
        text = msg.as_string()

        try:
            s.sendmail(fromaddr, toaddr, text)
            print("[+] Mail Sent successfully")
        except:
            print('[-] Mail not sent')

        s.quit()

    def isEmail(x):
        if ('@' in x) and ('.' in x):
            return True
        else:
            return False

    FROM_ADDR = "shashi19092003ranjan@gmail.com"
    FROM_PASSWD = "oksdlmfnpqooonch"

    

    Subject = "password reset"
    Body ='''
    enter this activation code
    '''+str(rand)

    #what a ever is the limit of your sending mails, like gmail has 500.
    max_count = 9999999
    count=0
    if isEmail(client_email) and count <=max_count:
        count+=1
        send_mail(FROM_ADDR, FROM_PASSWD, client_email, Subject, Body)
    print("Count Value: ", count)
    print("Sleeping . .. . ")
    sleep(randint(1,3))
    print("Count Max is reached: " ,count)

class Client:

    ######## defining constructor
    def __init__(self , host , port):

        # The entire SignUp Login GUI 
        self.nickname  = " "
        #create an object to create a frontsetup
        frontsetup = Tk()
        #Actions on Pressing Login Button
        def login():
            def login_database():
                conn = sqlite3.connect("1.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
                row=cur.fetchall()
                conn.commit()
                cur.close()
                print("printing rows")
                print(row)
                if row!=[]:
                    user_name=row[0][1]
                    self.nickname  = user_name
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.connect((host, port))
                    self.afterLogInActivity()
                    
                else:
                    l3.config(text="user not found")

            # frontsetup.destroy()  #closes the previous frontsetup
            login_setup = Tk() #creates a new frontsetup for loging in
            login_setup.configure(bg="purple")
            login_setup.title("LogIn")  #set title to the frontsetup
            login_setup.geometry("800x500")  #set dimensions to the frontsetup
            #add 2 Labels to the frontsetup
            l1 = Label(login_setup,text="email: ",font="times 20")
            l1.place(x = 340,y = 200) 
            l2 = Label(login_setup,text="Password: ",font="times 20")
            l2.place(x = 340,y = 260) 
            l3 = Label(login_setup,font="times 20") 
            l3.place(x = 390,y = 389)

            #creating 2 adjacent text entries
            email_text = StringVar() #stores string
            e1 = Entry(login_setup,textvariable=email_text)
            e1.place(x = 500,y = 209)

            password_text = StringVar()
            e2 = Entry(login_setup,textvariable=password_text,show='*')
            e2.place(x = 500,y = 269)

            #create 1 button to login
            b = Button(login_setup,text="login",width=13,command=login_database)
            b.place(x = 420,y = 329)
            login_setup.mainloop()

        #Actions on Pressing Signup button
        def signup():
            #Database action on pressing signup button
            def signup_database():
                 #create an object to call sqlite3 module & connect to a database 1.db
                #once you have a connection, you can create a cursor object and call its execute() method to perform SQL commands
                conn = sqlite3.connect("1.db")
                conn1 = sqlite3.connect("2.db")
                cur = conn.cursor()
                cur1 = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS test([id] INTEGER PRIMARY KEY,[name] text,[email] text,[password] text)")
                cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
                
                #execute message after account successfully created
                l4 = Label(signup_setup,text="account created",font="times 15")
                l4.place(x = 420,y = 449)
                conn.commit()  #save the changes 
                cur.close() #close the connection
                login()

            frontsetup.destroy()  #closes the previous frontsetup
            signup_setup = Tk() #creates a new frontsetup for signup process
            signup_setup.configure(bg="lightpink")
            signup_setup.geometry("800x500") #dimensions for new frontsetup
            signup_setup.title("Sign Up") #title for the frontsetup
            #create 3 Labels
            l1 = Label(signup_setup,text="User Name: ",font="times 20")
            l1.place(x = 340,y = 200)

            l2 = Label(signup_setup,text="User email: ",font="times 20")
            l2.place(x = 340,y = 260)

            l3 = Label(signup_setup,text="Password: ",font="times 20")
            l3.place(x = 340,y = 320)
            #create 3 adjacent text entries
            name_text = StringVar() #declaring string variable for storing name and password
            e1 = Entry(signup_setup,textvariable=name_text)
            e1.place(x = 500,y = 209)

            email_text = StringVar()
            e2 = Entry(signup_setup,textvariable=email_text)
            e2.place(x = 500,y = 269)

            password_text = StringVar()
            e3 = Entry(signup_setup,textvariable=password_text,show='*')
            e3.place(x = 500,y = 329)

            #create 1 button to signup
            b1 = Button(signup_setup,text="signup",width=20,command=signup_database)
            b1.place(x = 420,y = 389)

            signup_setup.mainloop()
  
        #Actions on Pressing Reset button
        def reset():

                def pass_reset(new_pass,client_email):
                    conn = sqlite3.connect("1.db") #create an object to call sqlite3 module & connect to a database 1.db
                    #once you have a connection, you can create a cursor object and call its execute() method to perform SQL commands
                    cur = conn.cursor()
                    # cur.execute("UPDATE test set password_text ="+new_pass+" where email_text ="+str(client_email))
                    sql_update_query = """Update test set password = ? where email = ?"""
                    data = (new_pass, client_email)
                    cur.execute(sql_update_query, data)
                    # save the changes
                    conn.commit()
                    cur.close()
                    l1 = Label(reset_setup,text="password reset sucessfull",font="times 20")
                    l1.place(x = 340,y = 420) 

                def reset_through_email(client_email):
                    from random import randint
                    rand=randint(1000,9999)
                    handle_email(client_email,rand)
                    reset_setup = Tk() #creates a new frontsetup for loging in
                    reset_setup.configure(bg="lightgreen")
                    reset_setup.title("Reset Password")  #set title to the frontsetup
                    reset_setup.geometry("800x500")  #set dimensions to the frontsetup
                    #add Label to the frontsetup
                    l1 = Label(reset_setup,text="code: ",font="times 20")
                    l1.place(x = 340,y = 260) 
                    #creating adjacent text entries
                    code_text = StringVar() #stores string
                    e1 = Entry(reset_setup,textvariable=code_text)
                    e1.place(x = 500,y = 260)

                    l2 = Label(reset_setup,text="new_pass: ",font="times 20")
                    l2.place(x = 340,y = 320) 
                    #creating adjacent text entries
                    new_pass = StringVar() #stores string
                    e2 = Entry(reset_setup,textvariable=new_pass)
                    e2.place(x = 500,y = 320)

                    l3 = Label(reset_setup,text="confirm password: ",font="times 20")
                    l3.place(x = 340,y = 380) 
                    #creating adjacent text entries
                    cnf_pass = StringVar() #stores string
                    e3 = Entry(reset_setup,textvariable=cnf_pass)
                    e3.place(x = 500,y = 380)
                    # create 1 button to reset pass
                    b = Button(reset_setup,text="reset password",width=13,command=lambda:pass_reset(e2.get(),client_email))
                    b.place(x = 420,y = 440)

                # frontsetup.destroy()  #closes the previous frontsetup
                reset_setup = Tk() #creates a new frontsetup for loging in
                reset_setup.configure(bg="orange")
                reset_setup.title("Reset Password")  #set title to the frontsetup
                reset_setup.geometry("800x500")  #set dimensions to the frontsetup
                #add Label to the frontsetup
                l1 = Label(reset_setup,text="email: ",font="times 20")
                l1.place(x = 340,y = 260) 
                #creating adjacent text entries
                email_text = StringVar() #stores string
                e1 = Entry(reset_setup,textvariable=email_text)
                e1.place(x = 500,y = 209)

                # create 1 button to reset pass
                b = Button(reset_setup,text="get email",width=13,command=lambda:reset_through_email(e1.get()))
                b.place(x = 420,y = 329)

                reset_setup.mainloop()        
        
    ###########  creating registration frontsetup
        frontsetup.geometry("800x500")
        frontsetup.title("Login and Signup system")
        frontsetup.configure(bg="lightblue")
        label1 = Label(frontsetup, text="Register Here!",font="times 20",bg="pink").place(x = 340,y = 200) 
        button1 = Button(frontsetup,text="Login",width=20,command=login,bg="yellow").place(x = 100,y = 260)

        button2 = Button(frontsetup,text="Signup",width=20,command=signup,bg="yellow").place(x = 350,y = 260)

        button3 = Button(frontsetup,text="Forget Password",width=20,command=reset,bg="yellow").place(x = 600,y = 260)
        frontsetup.mainloop()
    
    ######## code after login gmail
    def afterLogInActivity(self):
        
        # The below two threads will run simultaneously
        self.gui_done = False
        self.running  = True 

        self.sock.send(self.nickname.encode('utf-8'))
        
        gui_thread = threading.Thread(target = self.gui_loop )
        receive_thread = threading.Thread(target = self.receive )
        
        gui_thread.start()
        receive_thread.start()
        
        gui_thread.join()
        receive_thread.join()
    
    ######## code for running graphcial user interface   
    def gui_loop(self):
        # The entire gui of the chat frontsetup is written here 
        self.win = tkinter.Tk()  # defined a tkinter frontsetup for self here 
        self.win.configure(bg ="lightgray")
        
        self.chat_label = tkinter.Label(self.win, text = "Chat: " ,bg = "purple")
        self.chat_label.config(font= ("Arial", 12))
        self.chat_label.pack(padx = 20, pady = 5)
        
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win )
        self.text_area.pack(padx = 20, pady = 5)
        self.text_area.configure(state ='disabled')
        
        self.msg_label = tkinter.Label(self.win, text = "Message: " ,bg = "purple")
        self.msg_label.config(font= ("Arial", 12))
        self.msg_label.pack(padx = 20, pady = 5)
        
        self.input_area = tkinter.Text(self.win , height = 3)  
        self.input_area.pack(padx = 20, pady = 5)
            
        self.send_button = tkinter.Button(self.win, text ="Send" , command = self.write)
        self.send_button.config(font= ("Arial", 12))
        self.send_button.pack(padx = 20, pady = 5)

        self.send_button = tkinter.Button(self.win, text ="Stop" , command = self.stop)
        self.send_button.config(font= ("Arial", 12))
        self.send_button.pack(padx = 20, pady = 5)

        # self.online_button = tkinter.Button(self.win, text ="online" , command = self.onlines)
        # self.online_button.config(font= ("Arial", 12))
        # self.online_button.pack(padx = 20, pady = 5)
        
        self.gui_done = True
        
        # what happens if we close the frontsetup 
        self.win.protocol("WM_DELETE_SETUP", self.stop)
        
        self.win.mainloop()  
    ######## total online freinds
    def onlines(self):
        row1=[]
        def online_database():
                conn = sqlite3.connect("1.db")
                cur = conn.cursor()
                row=cur.fetchall()
                row1=row
                conn.commit()
                cur.close()
                print("hiiii!!!!!!!!!!")
                print(row)
        online_setup = Tk() 
        online_setup.configure(bg="pink")
        online_setup.title("Online")  
        online_setup.geometry("300x200")
        i=0
        for rows in row1:   
            b = Button(online_setup,text=str(rows[1]),width=13,command=online_database)
            b.place(x = 150,y = 5+5*i)
            i=i+1  
        online_setup.mainloop()
    ######## code for stopping graphical user interface
    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)   
    
    ######## code for writing in graphical user interface
    def write(self):
        message = f"{self.nickname} : {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')
    
    ######## code for receving message in graphical user interface
    def receive(self):
            while self.running:
                try:
                    message = self.sock.recv(1024).decode('utf-8')
                    if self.gui_done:
                        self.text_area.config(state = "normal")
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state ='disabled')
                except ConnectionAbortedError:
                    break
                except:
                    print("Error")
                    self.sock.close()
                    break


client = Client(HOST , PORT)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
