from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login system")
        self.root.geometry("749x416+100+50")
        self.root.resizable(False, False)
        #Background Image
        self.bg=ImageTk.PhotoImage(file="Image/BackgroundLogin.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=175, y=75, width= 400, height=250)
        #title & subtitle
        title= Label(Frame_login, text="Login Here", font=("font",24,"bold"), fg="#6162FF", bg="white").place(x= 45,y=15)
        subtitle= Label(Frame_login, text="Member Login Area", font=("font",10,"bold"), fg="#1d1d1d", bg="white").place(x= 45,y=55)
        #username
        lbl_user = Label(Frame_login, text="Username", font=("font",10,"bold"), fg="grey", bg="white").place(x= 45,y=75)
        self.username= Entry(Frame_login, font=("font",10,"bold"), bg="#E7E6E6")
        self.username.place(x= 45,y=96, width= 190, height= 22)
        #pass
        lbl_password= Label(Frame_login, text="Password", font=("font",10,"bold"), fg="grey", bg="white").place(x= 45,y=119)
        self.password= Entry(Frame_login, font=("font",10,"bold"), bg="#E7E6E6")
        self.password.place(x= 45,y=140, width= 190, height= 22)
        #button
        forget = Button(Frame_login, text="Forgot password ?",bd=0, cursor="hand2",font=("font",6), fg="#6162FF", bg="white").place(x= 45,y=170)
        submit = Button(Frame_login, command=self.check_function, cursor="hand2" ,text="Login",bd=0, font=("font",10), bg="#6162FF", fg="white").place(x= 45,y=200, width=160, height= 30)
    def check_function(self):
            if self.username.get()=="" or self.password.get()=="":
                 messagebox.showerror("Error","ALL fields are required", parent=self.root)
            elif self.username.get()!="anbi" or self.password.get()!="123456":
                messagebox.showerror("Error","Invalid fields are required", parent=self.root)
            else:
                messagebox.showinfo("Wellcome", f"Welcome {self.username.get()}")
               
root = Tk()
obj = Login(root)
root.mainloop()