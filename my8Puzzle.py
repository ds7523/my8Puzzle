## Name: Dipesh Shrestha (ds7523)
## Date:9/30/15
## CS480: 8Puzzle
## Programming Assignment 01

from informedSearch import *
from search import *

class 8PuzzleProblem(InformedProblemState):
    """
    Inherited from the InformedProblemState class. To solve
    the eight puzzle problem.
    """
    def __init__(self, probArray,operator):
        self.probArray = probArray
        self.operator = operator

    def __str__(self):
       ## Method returns a string representation of the state.
        for row in range(0,3):
            return (str(row), str(row+1), str(row+2),"\n",str(row+3),str(row+4),str(row+5), \
            "\n",str(row+6),str(row+7), str(row+8))
    def equals(self, state):
        
        ## Method to determine whether the state instance
        ## and the given state are equal.
        
        return (self.probArray) == (state.probArray)
    def illegal(self):
            return 0
    def key(self):
        
        ## Method returns a string that can be used as a key
        ## to represent unique states.
        
        return ' '.join(self.probArray)

    ## The five methods below perform the tree traversing
    def move(self, value):
        nList = self.probArray[:]
        position = nList.index(0) ## the empty piece
        val = nList.pop(position + value) 
        nList.insert(position + value, 0)
        nList.pop(position)
        nList.insert(position, val)
        return nList  
    def moveleft(self):
        n = self.move(-1)
        return probArray(n, "move left")
    def moveright(self):
        n = self.move(1)
        return 8PuzzleProblem(n, "move right")
    def moveup(self):
        n = self.move(-3)
        return 8PuzzleProblem(n, "move up")
    def movedown(self):
        n = self.move(+3)
        return 8PuzzleProblem(n, "move down")
    def operatorNames(self):
        return ("move","moveleft","moveright","moveup","movedown")
    def applyOperators(self):
        return (self.moveleft(), self.moveright(),self.moveup(), self.movedown())
            
    def heuristic():
        counter = 0
        for i in range(len(self.probArray)):
            if ((self.probArray[i] != goal.probArray[i]) and self.probArray[i] != 'A'):
                ## Position of current:
                pos = goal.probArray.index(self.probArray[i])
                
            if pos < 3: goalRow = 0
            elif pos < 6: goalRow = 1
            else: goalRow = 2
            
            if i < 3: initRow = 0
            elif i < 6: initRow = 1
            else: startRow = 2
            
            initColumn = i % 3
            goalColumn = pos % 3
            counter += (abs(goalColumn - initColumn) + abs(goalRow - initRowww))
            return counter
        
init = [0,1,2,3,4,5,6,7,8]
goal = [1,2,3,8,0,4,7,6,5]
InformedSearch(8PuzzleProblem(init,"None"),8PuzzleProblem(goal,"None"))                                    
