#genetic algorithm to iterate the generations

from neuralnet import *

def order(networks):
    #sort the networks by fitness
    return sorted(networks, reverse=True, key=lambda x:x.fitness)

def children(parent1, parent2):
    #gives both children of the parents as network objects
    #set the seed. After testing it will become random
    random.seed(2)
    #chromosomes are layers of weights

    inputSize = len(parent1.Matrix[0])
    matrixSize = len(parent1.Matrix[1:-1])
    outputSize = len(parent1.Matrix[-1])

    child1 = Network(inputSize, outputSize, matrixSize)
    child2 = Network(inputSize, outputSize, matrixSize)
    
    #this is the point after which the weights are swapped
    #should not matter which parent this number is generated from
    cross = random.randint(1, len(parent1.weights))

    ###Child1
    w1 = parent1.weights[:cross]
    w1.extend(parent2.weights[cross:])
    child1.setWeights(w1)

    ###Child2
    w2 = parent2.weights[:cross]
    w2.extend(parent1.weights[cross:])
    child2.setWeights(w2)

    return [child1, child2]
    
    
