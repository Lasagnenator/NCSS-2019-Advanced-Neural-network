#genetic algorithm to iterate the generations

from neuralnet import *

mutation_rate = 0.001

def order(networks):
    #sort the networks by fitness
    return sorted(networks, reverse=True, key=lambda x:x.fitness)

def children(parent1, parent2):
    #gives both children of the parents as network objects
    #chromosomes are layers of weights

    inputSize = len(parent1.Matrix[0])
    matrixSize = len(parent1.Matrix[1:-1])
    outputSize = len(parent1.Matrix[-1])

    child1 = Network(inputSize, outputSize, matrixSize)
    child2 = Network(inputSize, outputSize, matrixSize)
    
    #this is the point after which the weights are swapped
    #should not matter which parent this number is generated from
    cross = random.randint(1, len(parent1.weights))

    mutations = 0
    ###Child1
    w1 = parent1.weights[:cross]
    w1.extend(parent2.weights[cross:])
    #mutations
    for i,layer in enumerate(w1):
        for j,node in enumerate(layer):
            for k,weight in enumerate(node):
                if random.choices([True, False], [mutation_rate, 100-mutation_rate], k=1)[0]:
                    w1[i][j][k] = random.uniform(-1,1)
                    mutations += 1
                    #print("Mutation happened")
                
    child1.setWeights(w1)

    ###Child2
    w2 = parent2.weights[:cross]
    w2.extend(parent1.weights[cross:])
    #mutations
    for i,layer in enumerate(w2):
        for j,node in enumerate(layer):
            for k,weight in enumerate(node):
                if random.choices([True, False], [mutation_rate, 100-mutation_rate], k=1)[0]:
                    w2[i][j][k] = random.uniform(-1,1)
                    mutations += 1
                    #print("Mutation happened")
    
    child2.setWeights(w2)
    #print(mutations, "mutations happened")
    return [child1, child2]
    
    
