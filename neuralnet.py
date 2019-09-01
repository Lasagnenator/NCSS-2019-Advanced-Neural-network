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
bots. Parents are rank 1&2 then 3&4 etc

I expect there to be not many neural networks playing as this
concept is hard and usually only done with the help of external
libraries and extensive training.

Week 1 will only allow single card plays but week 2 allows for
2&3 card plays. Because of this I will have multiple instances
running at a time for each rule set. I will copy this file to
a new folder for each rule set.
"""

from Classes import Network

import random

def randomiseWeights(a, b, network):
    """a is low number and b is high number"""
    network.randomiseWeights(lambda: random.uniform(a,b))
