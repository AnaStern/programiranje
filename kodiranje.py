from tkinter import *

class Test():
    def __init__(self, master):

        menu = Menu(master)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="Meni", menu=file_menu)

        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_separator()
        file_menu.add_command(label="Izhod", command=master.destroy)

        self.vnosnistavek = StringVar(master, value="")
        self.vrnjenstavek = StringVar(master, value="")
        self.seznam = []

        polje_a = Entry(master, textvariable=self.vnosnistavek)
        polje_a.grid(row=0, column=0, columnspan= 10)

        gumb_kodiraj = Button(master, text= "Zakodiraj", command=self.kodiraj) 
        gumb_kodiraj.grid(row=0, column=11, columnspan= 3)

        polje_b = Entry(master, textvariable= self.vrnjenstavek)
        polje_b.grid(row=0, column=14, columnspan= 10)

        self.list= Listbox(master)
        self.list.grid(row=2, column=0, columnspan=24, sticky=E+W+N+S)

    def kodiraj(self):
        self.niz1= "abcčdefghijklmnoprsštuvzž"
        self.niz2= "*÷?%$*¤€&*@;!+#*<={/$*?+&"
        self.niz3= "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"
        self.beseda= ""
        self.mesto= 0
        for znak in self.vnosnistavek.get():
            if znak in self.niz1 :
                self.mesto= self.niz1.index(znak)
                self.beseda += self.niz2[self.mesto]
            elif znak in self.niz3 :
                self.mesto= self.niz3.index(znak)
                self.beseda += self.niz2[self.mesto]
            else:
                self.beseda += znak
        self.vrnjenstavek.set(self.beseda)
        self.list.insert(0,str(self.vrnjenstavek.get())+ "   pomeni:  " + str(self.vnosnistavek.get()))
        self.seznam += [str(self.vrnjenstavek.get())+ "   pomeni:  " + str(self.vnosnistavek.get())]
            
    

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "": 
            return
        with open(ime, "wt", encoding="utf8") as f:
            for elt in self.seznam:
                f.write(elt + "\n")

    def odpri(self):
        ime = filedialog.askopenfilename()
        if ime == "": 
            return
        with open(ime, encoding="utf8") as f:
            for vrstica in f:
                self.list.insert(0, vrstica)
                







root = Tk()

aplikacija = Test(root)
root.mainloop()
