import itertools

RANK_ORDER = '34567890JQKA2'
SUIT_ORDER = 'DCHS'

def is_valid_play(previous_play, play):
    if len(play)>5:
        return False
    #testing a pass
    if previous_play != [] and play == []: #pass
        return True
    if previous_play == play == []: #pass
        return True
    if len(play)!=len(previous_play): #must be the same length as the prev
        return False
    
    ###Check if the combo is allowed
    if len(play)==2: #playing a pair
        if play[0][0]!=play[1][0]:
            return False
    elif len(play)==3: #playing a triple
        if not (play[0][0]==play[1][0]==play[2][0]):
            return False
    elif len(play)==4: #playing a four of a kind
        if not (play[0][0]==play[1][0]==play[2][0]==play[3][0]):
            return False
        
    elif len(play)==5: #playing 5 cards
        valid = False
        if is_full_house(play): #full house
            valid = True
        elif is_straight(play): #straight
            valid = True
        elif is_flush(play): #flush
            valid = True
        if not valid:
            return False
    

    ###check different plays
    if previous_play==[] and "3D" in play:
        return True
    if len(previous_play)==len(play)==1: #one card play
        return is_higher(play[0], previous_play[0])
    if len(previous_play)==len(play)==2: #two card play
        return is_higher_pair(play, previous_play)
    if len(previous_play)==len(play)==3: #three card play
        return
    if len(previous_play)==len(play)==4: #four card play
        return
    if len(previous_play)==len(play)==5: #five card play
        return
    return False

def len_to_score(length):
    if length<10:
        score = length
    elif 10<=length<=12:
        score = 2*length
    else:
        score = 39

    score = -score
    return score

#-------------
#card tests

def is_higher(card1, card2):
    c1_r, c1_s = RANK_ORDER.index(card1[0]), SUIT_ORDER.index(card1[1])
    c2_r, c2_s = RANK_ORDER.index(card2[0]), SUIT_ORDER.index(card2[1])
    if c1_r>c2_r:
        return True
    if c1_r<c2_r:
        return False
    if c1_s>c2_s:
        return True
    return False

def is_higher_pair(pair1, pair2):
    c1 = pair1[0]
    c2 = pair1[1]
    if is_higher(c1,c2):
        max1 = c1
    else:
        max1 = c2
    c1 = pair2[0]
    c2 = pair2[1]
    if is_higher(c1,c2):
        max2 = c1
    else:
        max2 = c2
    if is_higher(max1, max2):
        return True
    return False

def is_pair(card1, card2):
    if card1[0]==card2[0]:
        return True
    return False

def is_triple(card1, card2, card3):
    if card1[0]==card2[0] and card3[0]==card1[0]:
        return True
    return False

def all_pairs(hand):
    out = []
    for pair in itertools.combinations(hand, 2):
        if is_pair(*pair):
            out.append(list(pair))
    return out

def all_triples(hand):
    out = []
    for pair in itertools.combinations(hand, 3):
        if is_triple(*pair):
            out.append(list(pair))
    return out

def is_full_house(cards):
    if len(all_triples(cards))==1:
        if len(all_pairs(cards))==4:
            return True
    return False

def is_straight(cards):
    c1_r = RANK_ORDER.index(cards[0][0])
    c2_r = RANK_ORDER.index(cards[1][0])
    c3_r = RANK_ORDER.index(cards[2][0])
    c4_r = RANK_ORDER.index(cards[3][0])
    c5_r = RANK_ORDER.index(cards[4][0])

    if c5_r==c4_r+1==c3_r+2==c2_r+3==c1_r+4:
        return True
    return False

def is_flush(cards):
    c1_s = SUIT_ORDER.index(cards[0][1])
    c2_s = SUIT_ORDER.index(cards[1][1])
    c3_s = SUIT_ORDER.index(cards[2][1])
    c4_s = SUIT_ORDER.index(cards[3][1])
    c5_s = SUIT_ORDER.index(cards[4][1])

    if c1_s==c2_s==c3_s==c3_s==c4_s==c5_s:
        return True
    return False
