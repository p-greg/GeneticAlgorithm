import numpy as np

class State:
    state = np.zeros(8)
    fitness=0
    normalizedFitness=0

    def __init__(self, state):
        self.state = state

    #the hash is used to find the fitness
    #the fitness is defined by the number of non attacking queens
    def __hash__(self):
        count = 0
        attackingQueens = [False,False,False,False,False,False,False,False]
        for i in range(0,7):
            x1 = i+1
            y1 = self.state[i]
            for j in range(i+1,8):
                x2 = j+1
                y2 = self.state[j]
                if y1==y2 or abs((x1-x2))==abs((y1-y2)):
                    attackingQueens[i]=True
                    attackingQueens[j]=True
        for attacking in attackingQueens:
            if not attacking:
                count+=1
        self.fitness=count
        return count

def cross(state1, state2):
    return State([state1[0],state1[1],state1[2],state1[3],state2[4],state2[5],state2[6],state2[7]])
