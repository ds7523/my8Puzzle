from informedSearch import *
from pq import *
from search_1 import *
   
class EightPuzzleProblemState(InformedProblemState):
     
    def __init__(self,problemList):
        self.problemList = problemList
        
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
        return str(result)
 
    def moveUp(self):
        copyList = self.problemList[:]
        findZero = copyList.index(0)
        if findZero == 0:
                pass
        elif findZero == 1:
                pass
        elif findZero == 2:
                pass
        elif findZero == 3:
                copyList[0] = self.problemList[3]
                copyList[3] = self.problemList[0]
        elif findZero == 4:
                copyList[1] = self.problemList[4]
                copyList[4] = self.problemList[1]
        elif findZero == 5:
                copyList[2] = self.problemList[5]
                copyList[5] = self.problemList[2]
        elif findZero == 6:
                copyList[3] = self.problemList[6]
                copyList[6] = self.problemList[3]
        elif findZero == 7:
                copyList[4] = self.problemList[7]
                copyList[7] = self.problemList[4]
        else:
                copyList[5] = self.problemList[8]
                copyList[8] = self.problemList[5]
        return EightPuzzleProblemState(copyList)
    def moveDown(self):
        copyList = self.problemList[:]
        findZero = copyList.index(0)
        if findZero == 0:
                copyList[0] = self.problemList[3]
                copyList[3] = self.problemList[0]
        elif findZero == 1:
                copyList[1] = self.problemList[4]
                copyList[4] = self.problemList[1]
        elif findZero == 2:
                copyList[2] = self.problemList[5]
                copyList[5] = self.problemList[2]
        elif findZero == 3:
                copyList[3] = self.problemList[6]
                copyList[6] = self.problemList[3]
        elif findZero == 4:
                copyList[4] = self.problemList[7]
                copyList[7] = self.problemList[4]
        elif findZero == 5:
                copyList[5] = self.problemList[8]
                copyList[8] = self.problemList[5]
        else:
                pass
        return EightPuzzleProblemState(copyList)
    def moveLeft(self):
        copyList = self.problemList[:]
        findZero = copyList.index(0)
        if findZero == 0:
                pass
        elif findZero == 1:
                copyList[1] = self.problemList[0]
                copyList[0] = self.problemList[1]
        elif findZero == 2:
                copyList[1] = self.problemList[2]
                copyList[2] = self.problemList[1]
        elif findZero == 3:
                pass
        elif findZero == 4:
                copyList[3] = self.problemList[4]
                copyList[4] = self.problemList[3]
        elif findZero == 5:
                copyList[4] = self.problemList[5]
                copyList[5] = self.problemList[4]
        elif findZero == 6:
                pass
        elif findZero == 7:
                copyList[6] = self.problemList[7]
                copyList[7] = self.problemList[6]
        else:
                copyList[7] = self.problemList[8]
                copyList[8] = self.problemList[7]
        return EightPuzzleProblemState(copyList)
            

    def moveRight(self):
        copyList = self.problemList[:]
        findZero = copyList.index(0)
        if findZero == 0:
                copyList[0] = self.problemList[1]
                copyList[1] = self.problemList[0]
        elif findZero == 1:
                copyList[1] = self.problemList[2]
                copyList[2] = self.problemList[1]
        elif findZero == 2:
                pass
        elif findZero == 3:
                copyList[3] = self.problemList[4]
                copyList[4] = self.problemList[3]
        elif findZero == 4:
                copyList[4] = self.problemList[5]
                copyList[5] = self.problemList[4]
        elif findZero == 5:
                pass
        elif findZero == 6:
                copyList[6] = self.problemList[7]
                copyList[7] = self.problemList[6]
        elif findZero == 7:
                copyList[7] = self.problemList[8]
                copyList[8] = self.problemList[7]
        else:
                pass
        return EightPuzzleProblemState(copyList)

        """
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
             """
    def illegal(self):
        """
        Tests the state instance for validity.
        Returns true or false.
        """
        return 0
    def applyOperators(self):
        """
        Returns a list of successors to the current state,
        some of which may be illegal.""" 
        return [self.moveUp(),self.moveDown(), self.moveLeft(), self.moveRight()]
        
        #return [self.availableMoves()]
            
    def operatorNames(self):
        """
        Returns a list of operator names in the same order
        as the successors list is generated.
        """
        return ("moveUp","moveDown","moveRight","moveLeft")

        #return ("availableMoves")
    def equals(self, state):
        """
        Tests whether the state instance equals the given
        state.
        """
        if self.problemList == state: return 1
        return 0
    def heuristic(self,goal):
        """
        For use with informed search.  Returns the estimated
        cost of reaching the goal from this state.
        """
        h = 0
        for i in goal.problemList:
            n = i
            if n == 0:
                continue
            h += int(abs(n - 1 - i) / 8) + (abs(n - 1 - i) % 8)
        return h
        
prob = [0,1,2,3,4,5,6,7,8]
goal = [1,2,3,8,0,4,7,6,5]
InformedSearch(EightPuzzleProblemState(prob),EightPuzzleProblemState(goal))

