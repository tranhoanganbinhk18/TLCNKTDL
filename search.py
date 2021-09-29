from tkinter import *
from PIL import ImageTk
from tkinter import messageboxsearch
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Search")
        self.root.geometry("749x416+100+50")
        self.root.resizable(False, False)
        #Background Image
        self.bg=ImageTk.PhotoImage(file="Image/BackgroundLogin.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)
        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, width= 749, height=416)
        #username
        lbl_user = Label(Frame_login, text="Nội dung tiềm kiếm ", font=("font",10,"bold"), fg="grey", bg="white").place(x= 15,y=20)
        self.username= Entry(Frame_login, font=("font",10,"bold"), bg="#E7E6E6")
        self.username.place(x= 20,y= 45, width= 550, height= 25)
        #button
        submit = Button(Frame_login, cursor="hand2" ,text="Search",bd=0, font=("font",10), bg="#6162FF", fg="white").place(x=  580,y= 45, width= 100, height= 25)
                 
root = Tk()
obj = Login(root)
root.mainloop()