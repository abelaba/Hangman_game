from tkinter import *
from SecondWindow import *
from tkinter import messagebox

class Mainwindow:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.title('Hangman')
        self.frameForMainWindow = Frame(self.window)
        self.hangmanLabel = Label(self.frameForMainWindow,text='HANGMAN',font=('helvetica',30))
        self.wordEntry = Entry(self.frameForMainWindow,width= 40)
        self.mainWindowButton = Button(self.frameForMainWindow,text ='Enter word',width=15,height=2,command=self.onClick)
        self.window.bind("<Return>",self.onClick)    # for using enter key for entering letters
    def activate(self):
        self.frameForMainWindow.grid(row=1,column=1)
        self.hangmanLabel.grid(row=1,padx=6,pady=6)
        self.wordEntry.grid(row=2,padx=6,pady=6)
        self.mainWindowButton.grid(row=3,padx=6,pady=6)
        self.window.mainloop()
    def check(self,word):
        alphabet ="abcdefghijklmnopqrstuvwxyz"
        word = word.lower()
        count = 0
        for i in alphabet:
            for j in word:
                if i == j:
                    count += 1
        return count
    def onClick(self,event=None):
        self.check(self.wordEntry.get())

        if self.check(self.wordEntry.get()) == len(self.wordEntry.get()):
            self.frameForMainWindow.grid_forget()
            wordFromEntry = self.wordEntry.get()
            secondWindow(self.window, wordFromEntry).activate()

        else:
            messagebox.showwarning("Error", "You must insert only letters")


Mainwindow().activate()
