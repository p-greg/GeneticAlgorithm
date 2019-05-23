Genetic Algorithm Implementation
Created by Colin Gregory May 2019

Usage:

    python3 genetic.py nStates nIterations nMutate

    Where:
        
        nStates       
            -Integer
            -nStates is the number of states of the population

        nIterations    
            -Integer
            -nInterations is the number of times the algorithm will produce new children

        nMutate         
            -Integer
            -nMutate is the upper bound of the chance to have a child mutate
            

Examples:

    The following command will start with 100 different states, producing new children
    100 times, and each time a child is made it has a 1/5 chance to mutate

        python3 genetic.py 100 100 5

    The following command will start with 5000 different states, producing new children
    200 times, and each time a child is made it has a 1/10 chance to mutate.

        python3 genetic.py 5000 200 10
