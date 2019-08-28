import random
import play_check

_deck = "5C 6D 6C 7D 7C 8C 8S 9C 0C QC QH KC 2H".split(" ")
_deck.extend("3C 4D 4C 5H 9D 9S 0H JD JS KH KS AD 2D".split(" "))
_deck.extend("3D 3S 4H 5D 5S 8H 0D 0S JC QS AH 2C 2S".split(" "))
_deck.extend("3H 4S 6H 6S 7H 7S 8D 9H JH QD KD AC AS".split(" "))

#print("p1 hand", p1_hand)
#print("p2 hand", p2_hand)
#print("p3 hand", p3_hand)
#print("p4 hand", p4_hand)

def start_game(p0_play, p1_play, p2_play, p3_play):
    #args are play functions for each player
    #hand, func, score

    for round_number in range(10): #10 rounds
        print("round", round_number)
        deck = _deck
        random.shuffle(deck)

        current_player = 0

        p0_hand = deck[0:13]
        p1_hand = deck[13:26]
        p2_hand = deck[26:39]
        p3_hand = deck[39:52]

        players = [[p0_hand, p0_play, 0],
                   [p1_hand, p1_play, 0],
                   [p2_hand, p2_play, 0],
                   [p3_hand, p3_play, 0]]

        print("Dealt cards.")

        if "3D" in p0_hand:
            current_player = 0
        elif "3D" in p1_hand:
            current_player = 1
        elif "3D" in p2_hand:
            current_player = 2
        elif "3D" in p3_hand:
            current_player = 3
            
        previous_play = []
        trick_count = 0
        
        round_history = []
        hand_sizes = [13,13,13,13]
        scores = [0,0,0,0]
        
        while players[0][0] and players[1][0] and players[2][0] and players[3][0]:
            #update params
            print("trick", trick_count)
            #play a trick
            play = players[current_player][1](players[0][0],
                                              round_number==0,
                                              previous_play,
                                              round_history,
                                              current_player,
                                              hand_sizes,
                                              scores,
                                              round_number)
            print("player", current_player, "played", play)
            if not play_check.is_valid_play(previous_play, play):
                players[current_player][2] -= 10
                current_player += 1
                if current_player==4:
                    current_player = 0
                continue
            previous_play = play
            round_history.append((currentplayer, play))
            #remove the cards from their hand
            [players[current_player].remove(card) for card in play]
            current_player += 1
            if current_player==4:
                current_player = 0
            trick_count += 1
            if trick_count==100: #round ends after 100 tricks
                #theoretically could go forever with passes
                break

            
            
        #round ended, calculate scores
        total_cards = len(players[0][0])+len(players[1][0])+len(players[2][0])+len(players[3][0])
        for i, player in enumerate(players):
            players[i][2] += play_check.len_to_score(len(player[0]))
            hand_sizes[i] = len(player[0])
            if len(player[0])==0: #winner of the round gets all points
                players[i][2] += total_cards

        scores = [plaers[0][2], players[1][2], players[2][2], players[3][2]]
        round_history = []

    key = lambda x:players[[0,1,2,3].index(x)][2]
    ranks = sorted([0,1,2,3], key=key, reverse=True)
    return ranks
        
            
