
from tkinter import *

class HangmanClass:


    def __init__(self,word):
        self.word = word.upper()
        self.failureCount = 0
        self.underScoresList = []



    def getWord(self):
        return self.word

    def getFailureCount(self):

        return self.failureCount

    def getWordLength(self):

        return len(self.word)

    def getUnderScoresList(self):
        return self.underScoresList

    def createUnderScoresList(self):

        for i in range (0, len(self.word)):    # LOOP FOR CREATING A LIST WITH UNDERSCORES
            self.underScoresList.append("_")


    def countLettersAppearance(self,letter):

        numberOfTimesLetterAppears = 0

        for index in range(0,len(self.word)):

            if letter == self.word[index]:

                numberOfTimesLetterAppears += 1 # LOOP FOR COUNTING THE NUMBER OF TIMES THE LETTER GUESSED APPEARS

        return numberOfTimesLetterAppears

    def insertLetter(self,letter,tempWord):
        letter = letter.capitalize()

        letterCount = self.countLettersAppearance(letter)

        if letterCount > 0:

            for i in range(0,letterCount):               # LOOP FOR REMOVING THE LETTER FROM THE WORD

                for index in range(0,len(tempWord)):     # LOOP FOR REPLACING UNDERSCORES WITH THE LETTER GUESSED IN THE LIST

                    if tempWord[index] == letter:

                        self.underScoresList.pop(index)
                        self.underScoresList.insert(index,letter)

                thelettersindex = self.word.index(letter)
                self.word = self.word[ : thelettersindex]+ self.word[ thelettersindex +1: ]

        else:

            self.failureCount += 1
