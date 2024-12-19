import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap Makinesi- Zeliha")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_106=tk.Button(root)
        GButton_106["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_106["font"] = ft
        GButton_106["fg"] = "#000000"
        GButton_106["justify"] = "center"
        GButton_106["text"] = "-"
        GButton_106.place(x=130,y=240,width=30,height=25)
        GButton_106["command"] = self.GButton_106_command

        GButton_626=tk.Button(root)
        GButton_626["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_626["font"] = ft
        GButton_626["fg"] = "#000000"
        GButton_626["justify"] = "center"
        GButton_626["text"] = "+"
        GButton_626.place(x=30,y=240,width=30,height=25)
        GButton_626["command"] = self.GButton_626_command

        GLineEdit_417=tk.Entry(root)
        GLineEdit_417["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_417["font"] = ft
        GLineEdit_417["fg"] = "#333333"
        GLineEdit_417["justify"] = "center"
        GLineEdit_417["text"] = "Entry1"
        GLineEdit_417.place(x=30,y=60,width=70,height=25)

        GLineEdit_908=tk.Entry(root)
        GLineEdit_908["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_908["font"] = ft
        GLineEdit_908["fg"] = "#333333"
        GLineEdit_908["justify"] = "center"
        GLineEdit_908["text"] = "Entry2"
        GLineEdit_908.place(x=120,y=60,width=70,height=25)

        GButton_732=tk.Button(root)
        GButton_732["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_732["font"] = ft
        GButton_732["fg"] = "#000000"
        GButton_732["justify"] = "center"
        GButton_732["text"] = "*"
        GButton_732.place(x=220,y=240,width=30,height=25)
        GButton_732["command"] = self.GButton_732_command

        GLineEdit_761=tk.Entry(root)
        GLineEdit_761["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_761["font"] = ft
        GLineEdit_761["fg"] = "#333333"
        GLineEdit_761["justify"] = "center"
        GLineEdit_761["text"] = "Entry3"
        GLineEdit_761.place(x=210,y=60,width=70,height=25)

        GLabel_857=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_857["font"] = ft
        GLabel_857["fg"] = "#333333"
        GLabel_857["justify"] = "center"
        GLabel_857["text"] = "rakam 1"
        GLabel_857.place(x=30,y=20,width=70,height=25)

        GLabel_200=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_200["font"] = ft
        GLabel_200["fg"] = "#333333"
        GLabel_200["justify"] = "center"
        GLabel_200["text"] = "rakam 2"
        GLabel_200.place(x=110,y=20,width=70,height=25)

        GLabel_657=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_657["font"] = ft
        GLabel_657["fg"] = "#333333"
        GLabel_657["justify"] = "center"
        GLabel_657["text"] = "sonuc"
        GLabel_657.place(x=200,y=20,width=70,height=25)

        GButton_490=tk.Button(root)
        GButton_490["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_490["font"] = ft
        GButton_490["fg"] = "#000000"
        GButton_490["justify"] = "center"
        GButton_490["text"] = "/"
        GButton_490.place(x=310,y=240,width=30,height=25)
        GButton_490["command"] = self.GButton_490_command

    def GButton_106_command(self):
        print("Buton 2 ye basıldı")


    def GButton_626_command(self):
        print("Buton 1 e basıldı")


    def GButton_732_command(self):
        print("Buton 3 e basıldı")


    def GButton_490_command(self):
        print("Buton 4 e basıldı")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textBoxYazilanlar1=tk.StringVar()
    textBoxYazilanlar2=tk.StringVar()
    textBoxYazilanlar3=tk.StringVar()


    root.mainloop()
