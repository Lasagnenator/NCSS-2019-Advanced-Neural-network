from neuralnet import *

n = Network(3, 3, 4)
randomiseWeights(-1,1,n)
n.setInputs([1,2,3])
n.evaluate()
