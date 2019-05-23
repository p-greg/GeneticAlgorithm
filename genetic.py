import queensState as qs
import matplotlib.pyplot as plt
import numpy as np
import random
from numpy.random import choice
import sys
#definition of how the crossover of the two parents is done.

#this crossover takes queens 0-3 from state1 and queens 4-7 from state2
def cross1(state1,state2):
    return qs.State([state1.state[0], state1.state[1], state1.state[2], state1.state[3], state2.state[4], state2.state[5], state2.state[6], state2.state[7]])

#this crossover takes queens 0-4 from state1 and queens 5-7 from state2
def cross2(state1,state2):
    return qs.State([state1.state[0], state1.state[1], state1.state[2], state1.state[3], state1.state[4], state2.state[5], state2.state[6], state2.state[7]])

def mutate(state):
    state.state[random.randint(0,7)]=random.randint(1,8)

def usage():
    print()
    print("Usage: ")
    print("  python3 test.py \x1B[3mnStates nIterations\x1B[23m")
    print()
    print("    -\x1B[3mnStates\x1B[23m is an integer (suggested 100-10000)")
    print("    -\x1B[3mnIterations\x1B[23m is an integer (suggested 100-100000)")
    print()

#create the initial population
parents = []
children = []
normalFitness = []
fitness=[]
genNumber=[]
if len(sys.argv) == 1: #default values
    nStates=100
    nIterations=100
    nMutate=5
elif len(sys.argv) == 4: #user inputted values
    nStates = int(sys.argv[1])
    nIterations = int(sys.argv[2])
    nMutate = int(sys.argv[3])
else:
    print("Wrong number of arguments")
    usage()
    sys.exit()


#step through each state and give
#random values to each index in the array
print("Creating the initial Parents")
for i in range(nStates):
    x = []
    for h in range(8):
        d = random.randint(1,8)
        x.append(d)
    newState = qs.State(x)
    #append the current state to the population with
    #the fitness(hash) and the state array
    parents.append(newState)

#genetic algorithm loop
#each iteration 
for i in range(nIterations):
    print()
    print("Children Generation:  ",i)

    totalFitness = 0
    for n in range(nStates):
        fit = hash(parents[n])
        parents[n].fitness = fit
        totalFitness+=fit

    fitness.append(totalFitness/nStates)
    genNumber.append(i)

    #initialize the normalized fitness array
    print("   Average fitness of Gen",i,": ",fitness[i])
    for x in range(nStates):
        normalFitness.append(parents[x].fitness/totalFitness)

    totalFitness = 0 #reset total fitness

    #loop to print states for testing
    #for x in range(nStates):
        #print("Pop: ",parents[x].state," fitness: ",parents[x].fitness," normalfit: ", normalFitness[x])

    #loop for crossover
    for x in range(nStates):
        parent1 = choice(parents, p=normalFitness)
        parent2 = choice(parents, p=normalFitness)
        child = cross2(parent1,parent2)
        if random.randint(1,nMutate)==1:
            mutate(child)
        children.append(child)
        #print("State1: ", parent1.state, " State2: ",parent2.state, "Cross: ", child.state)

    if not i+1==nIterations:
        parents = children.copy()
    del normalFitness[:]
    del children[:]

print()
print("Final States where fitness > 5:")

for x in range(nStates):
    if parents[x].fitness>5:
        if parents[x].fitness==8:
            print("  **State: ",parents[x].state," | Fitness: ",parents[x].fitness,"**")
        else:
            print("    State: ",parents[x].state," | Fitness: ",parents[x].fitness)

plt.plot(genNumber,fitness)
plt.xlabel('Generation Number')
plt.ylabel('Average Fitness')
plt.title('Fitness over Generations')
plt.show()
