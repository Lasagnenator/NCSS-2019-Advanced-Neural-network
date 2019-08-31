from neuralnet import *

#cards are based on numbers
#104 inputs: 52 hand, 52 for play to beat, 1 for is_start_of_round
#52 outputs: cards to play
#10x10 hidden layers
net = Network(52*2+1, 52, 20)

#CHANGE AND FIX WEIGHTS
net.randomiseWeights(lambda:random.uniform(-1,1))

ranks = ["3","4","5","6","7","8","9","0","J","Q","K","A","2"]
suits = ["D","C","H","S"]

def break_card(card):
    card = card.upper()
    return ranks.index(card[0])*4+suits.index(card[1])

def join_card(number):
    return ranks[number//4]+suits[number%4]

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    in_list = [0]*104
    for card in hand:
        in_list[break_card(card)] = 1
    for card in play_to_beat:
        in_list[break_card(card)+52] = 1
    in_list[103] = int(is_start_of_round)
        
    #list has been chosen
    net.setInputs(in_list)
    net.evaluate()
    out = net.getOutputs()
    play = []
    for i, val in enumerate(out,start=0):
        if val==1 and in_list[i]==1:
            play.append(join_card(i))
    if len(play_to_beat)!=0:
        play = play[:len(play_to_beat)]
    return play
