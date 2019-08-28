from neuralnet import *

n = Network(100, 100, 100)
randomiseWeights(-1,1,n)
n.setInputs([1,1,1])
n.evaluate()
