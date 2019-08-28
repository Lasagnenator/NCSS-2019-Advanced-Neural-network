from neuralnet import *

#cards are based on numbers
#18 inputs <1-13: hand, 14-18: play_to_beat>
#6 outputs <1: how many card to play, 2-6: cards_to_play>
#10x10 hidden layers
net = Network(18, 6, 10)
net.randomiseWeights(lambda:random.uniform(-1,1))

ranks = ["3","4","5","6","7","8","9","0","J","Q","K","A","2"]
suits = ["D","C","H","S"]

def break_card(card):
    card = card.upper()
    return ranks.index(card[0])*4+suits.index(card[1])

def join_card(number):
    return ranks[number//4]+suits[number%4]

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
    new_hand = [break_card(card) for card in hand]
    #now in number format
    net.setInputs(new_hand)
    net.evaluate()
    out = net.getOutputs()
    num_to_play = int(out[0])
    if num_to_play == 0: #as in a pass
        return []
    out = out[1:]
    out = [join_card(card) for card in out]
    
    #else return the best chance play
    return sorted(out)[:num_to_play]
