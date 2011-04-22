import string
import random

class WordSearch:
    def __init__(self):
        self.matrix = []
        self.locks = []
        
    def generateRandom(self, size):
        rows = size
        cols = size
        for row in range(rows):
            array = []
            lockArray =[]
            for col in range(cols):
                lockArray.append(False)
                array.append(
                    string.uppercase[random.randint(0,len(string.uppercase)-1)])
            self.locks.append(lockArray)
            self.matrix.append(array) 
        return
        
    def getOutputStr (self):
        outputStr = ''
        for row in self.matrix:
            for col in row:
                outputStr += col
            outputStr += '\n'
        return outputStr  
     
    #private method         
    def addWord(self, rowIndexes, colIndexes, word): 
        #check if locations are locked and different
        for i in range(len(rowIndexes)):
            if self.locks[rowIndexes[i]][colIndexes[i]]:
                if (self.matrix[rowIndexes[i]][colIndexes[i]] != word[i]):
                    return False
        #set locations and locks
        for i in range(len(rowIndexes)):
            self.locks[rowIndexes[i]][colIndexes[i]] = True
            self.matrix[rowIndexes[i]][colIndexes[i]] = word[i]         
        return True
        
    def addWordHorizontal(self, word):
        #test if the word is too long to add
        if len(word) > len(self.matrix[0]):
            return False
            
        wordWasAdded = False
        while (wordWasAdded == False):
            #pick random row
            startRow = random.randint(0,len(self.matrix) - 1)
            #pick random location within row as the starting col
            startCol = random.randint(0,len(self.matrix[0])- len(word))
            colIndexes = range(startCol, startCol + len(word)) 
            rowIndexes = [startRow] * len(word)
            wordWasAdded = self.addWord(rowIndexes, colIndexes, word)
        return True              
            
    def addWordVertical(self, word):
        #test if the word is too long to add
        if len(word) > len(self.matrix):
            return False
            
        wordWasAdded = False
        while (wordWasAdded == False):
            #pick random col
            startCol = random.randint(0,len(self.matrix[0]) - 1)
            #pick random location within col as the starting row
            startRow = random.randint(0,len(self.matrix)- len(word))
            rowIndexes = range(startRow, startRow + len(word)) 
            colIndexes = [startCol] * len(word)
            wordWasAdded = self.addWord(rowIndexes, colIndexes, word)
        return True       
           
