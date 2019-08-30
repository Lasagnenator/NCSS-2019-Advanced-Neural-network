class Node():
    weights = []
    value = 0

    def __init__(self):
        self.weights = []
        self.value = 0
    
    def evaluate(self, inputNodes):
        self.value = 0
        for i, input in enumerate(inputNodes):
            self.value += input.value*self.weights[i]
        sign = lambda x: int(x>0)
        self.value = sign(self.value)
        return self.value

    def setValue(self, value):
        self.value = value

    def setWeights(self, weights):
        self.weights = weights

class Network():

    #first index is the layer
    #second index is the node within the layer
    Matrix = []
    weights = []
    fitness = 0
    
    def __init__(self, inputNodes:int,  outputNodes:int, matrixSize:int):
        self.Matrix = []
        self.fitness = 0
        self.weights = []
        #input nodes initilisation
        self.Matrix.append([Node() for i in range(inputNodes)])
        #hidden layers initilisation
        [self.Matrix.append([Node() for i in range(matrixSize)]) for j in range(matrixSize)]
        #output nodes initilisation
        self.Matrix.append([Node() for i in range(outputNodes)])

    def setInputs(self, inputs):
        for i, value in enumerate(inputs):
            self.Matrix[0][i].setValue(value)

    def setWeights(self, weights):
        """
        weights first index is layer
        weights second index is node within layer
            value here is a list of the weights for that node
        """
        #need to set start = 1 to skip the first layer
        for i, layer in enumerate(weights,start=1):
            for j, nodeWeights in enumerate(layer,start=0):
                #print(i,j)
                self.Matrix[i][j].setWeights(nodeWeights)
        self.weights = weights

    #evaluate the network with all weights pre-set
    def evaluate(self):
        #we don't want to check the first layer as it has no parents
        #so we skip it
        preLayer = self.Matrix[0]
        
        for layer in self.Matrix[1:]:
            for node in layer:
                #evaluate each node based on the previous layer's values
                #values are extracted by the node
                node.evaluate(preLayer)
            #set the previous layer to this layer and loop again
            preLayer = layer

    def randomiseWeights(self, rand):
        weightsMatrix = []
        #again first layer doesn't have weights on it so we skip it
        preNodeLength = len(self.Matrix[0])
        for i in range(1, len(self.Matrix)):
            #
            weightsMatrix.append(
                [[rand() for z in range(preNodeLength)] for y in range(len(self.Matrix[i]))]
                )
            preNodeLength = len(self.Matrix[i])

        self.weights = weightsMatrix
        self.setWeights(weightsMatrix)

    def getOutputs(self):
        ret = []
        for node in self.Matrix[-1]:
            ret.append(node.value)
        return ret
