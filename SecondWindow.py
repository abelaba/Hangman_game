
from tkinter import *
from HangmanClass import *
from CanvasFunction import *
from tkinter import messagebox



class secondWindow:
    def __init__(self,window,wordFromEntry):

        self.window = window
        self.wordFromEntry = wordFromEntry
        self.h = HangmanClass(self.wordFromEntry)
        self.h.createUnderScoresList()
        self.tempWord = self.h.getWord()
        self.myfont = ('helvetica',30)
        fail = 'You have ' + str(10 - self.h.getFailureCount()) + ' chances.'

        self.failureCountLabel = Label(self.window, font = self.myfont, text=fail)   # failure count
        self.wordListLabel = Label(self.window, font = self.myfont,text = self.h.getUnderScoresList())  #word list
        self.frameForSecondWindow = Frame(self.window,width = 350,height = 350)     #frame
        self.temporaryCanvas = Canvas(self.frameForSecondWindow,width = 350,height = 350)
        self.letterEntry = Entry(self.window,width=70)
        self.button = Button(self.window,text='Enter',width=70,height=3,command = self.check)
        self.window.bind("<Return>",self.check)    # for using enter key for entering letters

    def check(self,event=None):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        count = 0

        for i in alphabet:
            if i == self.letterEntry.get():
                count += 1

        if count == 0:
            messagebox.showwarning("Error", "You can only enter letters")
        else:
            self.onClick()

    def onClick(self):
        letter = self.letterEntry.get()
        self.h.insertLetter(letter,self.tempWord)
        fail = 'You have ' + str(10 - self.h.getFailureCount()) + ' chances.'
        createCanvas(self.h.getFailureCount(), self.frameForSecondWindow)
        self.failureCountLabel = Label(self.window,text =fail, font = self.myfont ,width = 20)
        self.failureCountLabel.grid(row = 1)
        self.wordListLabel = Label(self.window, text = self.h.getUnderScoresList(),font = self.myfont,width = 20)
        self.wordListLabel.grid(row = 2)
        self.letterEntry.delete(0,3)


        if self.h.getFailureCount() == 10:

            self.letterEntry.grid_forget()
            self.button.grid_forget()
            winLabel = Label (self.window, text = "GAME OVER!",font = self.myfont,width=20)
            wordListLabel = Label(self.window, text = self.tempWord,font = self.myfont,width = 20)
            wordListLabel.grid(row = 2)
            winLabel.grid(row=4,padx = 10, pady=10)
            retryButton = Button(self.window , text = "Retry",  width = 10, height = 2)
            retryButton.grid(row=3,padx = 5, pady = 5)

        elif self.h.getWordLength() == 0:

            self.letterEntry.grid_forget()
            self.button.grid_forget()
            winLabel = Label (self.window, text = "Great Success",font = self.myfont,width=20)
            winLabel.grid(row=1)
            self.frameForSecondWindow.grid_forget()
            retryButton = Button(self.window , text = "Retry" ,width = 10, height = 2)
            retryButton.grid(row=3,padx = 5, pady = 5)


    def activate(self):
        self.failureCountLabel.grid(row = 1,padx=10,pady=10)
        self.wordListLabel.grid(row = 2,padx=10,pady=10)
        self.frameForSecondWindow.grid(row = 3,padx=10,pady=10)
        self.letterEntry.grid(row=4,padx=10,pady=10)
        self.button.grid(row=5,padx=10,pady=10)

        self.temporaryCanvas.grid(row=1,padx=10,pady=10)
