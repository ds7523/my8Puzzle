from informedSearch import *
from pq import *
from search import *

class Moves:
        moveUp = 'up'
        moveDown = 'down'
        moveRight ='right'
        moveLeft = 'left'

        TotalMoves = [moveUp,moveDown,moveRight,moveLeft]
        
class EightPuzzleProblemState(InformedProblemState):
    global ValidActions 
    def __init__(self,n,problemList):
        self.n = n
        self.L = n * n
        self.problemList = problemList
        if self.problemList.index(0) < 3:
            self.blankCellPos = (0,self.problemList.index(0))
        elif self.problemList.index(0) <4:
            self.blankCellPos = (1,self.problemList.index(0))
        else:
            self.blankCellPos = (2, self.problemList.index(0))
    def __str__(self):
        result =[]
        for i in range(3):
            result.append(self.problemList[i])
            print (self.problemList[i])
        for i in range(3,6):
            result.append(self.problemList[i])
            print (self.problemList[i])
        for i in range(6,9):
            result.append(self.problemList[i])
            print (self.problemList[i])
        return result
    """
    def moveUp(self):
    def moveDown(self):
    def moveLeft(self):
    def moveRight(self):"""
    def availableMoves(self,move):
        (row,col) = self.blankCellPos
        if move == Moves.moveUp:
            if row - 1 < 0:
                return 0
            else:
                return 1
        elif move == Moves.moveDown:
            if row + 1 > self.n-1:
                return 0
            else:
                return 1
        elif move == Moves.moveLeft:
            if col - 1 < 0:
                return 0
            else:
                return 1
        elif move == Moves.moveRight:
            if col + 1 > self.n-1:
                return 0
            else:
                return 1
             
    def illegal(self):
        """
        Tests the state instance for validity.
        Returns true or false.
        """
        return 1
    def applyOperators(self):
        """
        Returns a list of successors to the current state,
        some of which may be illegal.
        return [self.moveUp(),self.moveDown(), self.moveLeft(), self.moveRight()]
        """
        ValidActions = []
        for move in Moves.TotalMoves:
            if(self.availableMoves(move) == 1):
                ValidActions.append(move)
                print (move)
        return ValidActions
            
    def operatorNames(self):
        """
        Returns a list of operator names in the same order
        as the successors list is generated.
        return ("moveUp","moveDown","moveRight","moveLeft")
        """
        return ("availableMoves")
    def equals(self, state):
        """
        Tests whether the state instance equals the given
        state.
        """
        if self.problemList == state: return 1
        return 0
    def heuristic(self, goal):
        """
        For use with informed search.  Returns the estimated
        cost of reaching the goal from this state.
        """
        h = 0
        for i in range(self.L):
            n = tiles[i]
            if n == 0:
                continue
            h += int(abs(n - 1 - i) / self.N) + (abs(n - 1 - i) % self.N)
        return h
        
prob = [0,1,2,3,4,5,6,7,8]
goal = [1,2,3,8,0,4,7,6,5]
InformedSearch(EightPuzzleProblemState(0,prob),EightPuzzleProblemState(0,goal))

