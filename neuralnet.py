"""
This is the basic neural network framework that will be used for
the NCSS Advanced Challenge 2019.

I need to get this running as soon as possible in order to let it
learn through the genetic algorithm for as long as possible to
make it as strong as possible. My goal is to make the absolute
best bot in the tournament.

To do this I need to implement a pure python neural network as
Grok does not have the support of importing libraries like torch
or tensorflow which would make this a lot easier.

I am confident that when the neural network has had sufficient
training against itself, it should be able to beat even human
players easily.

It will play against itself to train by having 4 individuals in
the population play a match to see the winner, the fitness will
be one point per win of a match. If the bot errors out or takes
too long, the fitness will be zero as I cannot afford to have the
bot be removed from the competition. The final fitness score will
be the win percentage. If loses are zero just double the points.

At the end of a generation the parents are the top 50% and the
the next generation consists of the parents as well as the
children to fill up the last 50% to keep a constant number of
bots.

I expect there to be not many neural networks playing as this
concept is hard and usually only done with the help of external
libraries and extensive training.

Week 1 will only allow single card plays but week 2 allows for
2&3 card plays. Because of this I will have multiple instances
running at a time for each rule set. I will copy this file to
a new folder for each rule set.
"""


#we use pickle to make a 'save-state' of the net so we can come back to it
#this is only going to be used during training
import pickle

#this represents a node in the network
class Node():

    #class properties
    parents = []
    weights = []
    number_conencted = 0
    value = 0
    
    #initialises the class with optional connected parent nodes
    def __init__(self, parents=None, weights=None):
        #basic error checking
        if parents==None or weights==None:
            return self
        if len(parents)!=len(weights):
            raise ValueError("lengths of lists were not equal")
        
        #doesn't matter which one we take the length from
        number_connected = len(parents)

        #and now we just set the node properties to be saved
        self.parents = parents
        self.weights = weights

    #calculates the weighted sum of this node
    def evaluate(self) -> int:
        value = 0
        
        for i in range(number_connected):
            #This is the definition of the weighted sum
            value += parents[i].value * weights[i]

        self.value = value
        return value

    def setValue(self, value:int):
        if not isinstance(value, int):
            raise TypeError("value must be of type int")
        self.value = value

#This will be the class that contains many Node classes
#It can also play the game
class Individual():
    inputNodes = []
    outputNodes = []
    outputNodesWeight = []

    #This is a multidimensional list
    #nodeLayers[0][1] implies first layer and second node in the layer
    #same for nodeLayersWeights
    nodeLayers = []
    nodeLayersWeights = []
    
    #Creates a network with a square shaped hidden layers
    #Every node is connected to every node in the previous layer
    #If it is the starting node, it doens't matter
    #Number of output nodes can be changed so that we can have
    # specific number of outputs
    def __init__(self, numInputs:int, numLayers:int, nodesPerLayer:int,
                 numOutputs:int):
        pass

def saveState(individuals:list):
    with open("./NeuralNet.SaveState", "wb") as f:
        pickle.dump(nodes, f)

def loadState():
    with open("./NeuralNet.SaveState", "rb") as f:
        individuals = pickle.load(f)
    
    #now we return the nodes after leaving the with block
    return individuals
