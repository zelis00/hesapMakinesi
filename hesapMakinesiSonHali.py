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

        # Butonlar
        GButton_106 = tk.Button(root)
        GButton_106["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_106["font"] = ft
        GButton_106["fg"] = "#000000"
        GButton_106["justify"] = "center"
        GButton_106["text"] = "-"
        GButton_106.place(x=130, y=240, width=30, height=25)
        GButton_106["command"] = self.GButton_106_command

        GButton_626 = tk.Button(root)
        GButton_626["bg"] = "#f0f0f0"
        GButton_626["font"] = ft
        GButton_626["fg"] = "#000000"
        GButton_626["justify"] = "center"
        GButton_626["text"] = "+"
        GButton_626.place(x=30, y=240, width=30, height=25)
        GButton_626["command"] = self.GButton_626_command

        GButton_732 = tk.Button(root)
        GButton_732["bg"] = "#f0f0f0"
        GButton_732["font"] = ft
        GButton_732["fg"] = "#000000"
        GButton_732["justify"] = "center"
        GButton_732["text"] = "*"
        GButton_732.place(x=220, y=240, width=30, height=25)
        GButton_732["command"] = self.GButton_732_command

        GButton_490 = tk.Button(root)
        GButton_490["bg"] = "#f0f0f0"
        GButton_490["font"] = ft
        GButton_490["fg"] = "#000000"
        GButton_490["justify"] = "center"
        GButton_490["text"] = "/"
        GButton_490.place(x=310, y=240, width=30, height=25)
        GButton_490["command"] = self.GButton_490_command

        # Giriş Alanları
        self.GLineEdit_417 = tk.Entry(root)  # Entry1
        self.GLineEdit_417["borderwidth"] = "1px"
        self.GLineEdit_417["font"] = ft
        self.GLineEdit_417["fg"] = "#333333"
        self.GLineEdit_417["justify"] = "center"
        self.GLineEdit_417.place(x=30, y=60, width=70, height=25)

        self.GLineEdit_908 = tk.Entry(root)  # Entry2
        self.GLineEdit_908["borderwidth"] = "1px"
        self.GLineEdit_908["font"] = ft
        self.GLineEdit_908["fg"] = "#333333"
        self.GLineEdit_908["justify"] = "center"
        self.GLineEdit_908.place(x=120, y=60, width=70, height=25)

        self.GLineEdit_761 = tk.Entry(root)  # Sonuç
        self.GLineEdit_761["borderwidth"] = "1px"
        self.GLineEdit_761["font"] = ft
        self.GLineEdit_761["fg"] = "#333333"
        self.GLineEdit_761["justify"] = "center"
        self.GLineEdit_761.place(x=210, y=60, width=70, height=25)

        # Etiketler
        GLabel_857 = tk.Label(root)
        GLabel_857["font"] = ft
        GLabel_857["fg"] = "#333333"
        GLabel_857["justify"] = "center"
        GLabel_857["text"] = "rakam 1"
        GLabel_857.place(x=30, y=20, width=70, height=25)

        GLabel_200 = tk.Label(root)
        GLabel_200["font"] = ft
        GLabel_200["fg"] = "#333333"
        GLabel_200["justify"] = "center"
        GLabel_200["text"] = "rakam 2"
        GLabel_200.place(x=110, y=20, width=70, height=25)

        GLabel_657 = tk.Label(root)
        GLabel_657["font"] = ft
        GLabel_657["fg"] = "#333333"
        GLabel_657["justify"] = "center"
        GLabel_657["text"] = "sonuc"
        GLabel_657.place(x=200, y=20, width=70, height=25)

    def is_valid_number(self, value):
    #     bu parça girilen sayının geçerli olup olmadığını kontrol eder. Ondalık sayılara da izin verir.
        if value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            return True
        return False

    def GButton_106_command(self):
        sayi1 = self.GLineEdit_417.get()
        sayi2 = self.GLineEdit_908.get()

        if self.is_valid_number(sayi1) and self.is_valid_number(sayi2):
            sayi1 = float(sayi1)
            sayi2 = float(sayi2)
            sonuc = sayi1 - sayi2
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, str(sonuc))
        else:
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, "Hata")

    def GButton_626_command(self):
        sayi1 = self.GLineEdit_417.get()
        sayi2 = self.GLineEdit_908.get()

        if self.is_valid_number(sayi1) and self.is_valid_number(sayi2):
            sayi1 = float(sayi1)
            sayi2 = float(sayi2)
            sonuc = sayi1 + sayi2
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, str(sonuc))
        else:
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, "Hata")

    def GButton_732_command(self):
        sayi1 = self.GLineEdit_417.get()
        sayi2 = self.GLineEdit_908.get()

        if self.is_valid_number(sayi1) and self.is_valid_number(sayi2):
            sayi1 = float(sayi1)
            sayi2 = float(sayi2)
            sonuc = sayi1 * sayi2
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, str(sonuc))
        else:
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, "Hata")

    def GButton_490_command(self):
        sayi1 = self.GLineEdit_417.get()
        sayi2 = self.GLineEdit_908.get()

        if self.is_valid_number(sayi1) and self.is_valid_number(sayi2):
            sayi1 = float(sayi1)
            sayi2 = float(sayi2)
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                self.GLineEdit_761.delete(0, tk.END)
                self.GLineEdit_761.insert(0, str(sonuc))
            else:
                self.GLineEdit_761.delete(0, tk.END)
                self.GLineEdit_761.insert(0, "Bölme Hatası")
        else:
            self.GLineEdit_761.delete(0, tk.END)
            self.GLineEdit_761.insert(0, "Hata")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
