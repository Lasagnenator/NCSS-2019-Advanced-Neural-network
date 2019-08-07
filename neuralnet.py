#we use pickle to make a 'save-state' of the net so we can come back to it
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

def saveState(nodes:list):
    with open("./NeuralNet.SaveState", "wb") as f:
        pickle.dump(nodes, f)

def loadState(nodes:list):
    #nodes should be a length of zero or this won't work
    if len(nodes)!=0:
        raise ValueError("nodes must be length zero prior to loading")
    
    with open("./NeuralNet.SaveState", "rb") as f:
        temp = pickle.load(f)

    for item in temp:
        nodes.append(item)
