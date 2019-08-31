import random
import play_check
import sys

_deck = "5C 6D 6C 7D 7C 8C 8S 9C 0C QC QH KC 2H".split(" ")
_deck.extend("3C 4D 4C 5H 9D 9S 0H JD JS KH KS AD 2D".split(" "))
_deck.extend("3D 3S 4H 5D 5S 8H 0D 0S JC QS AH 2C 2S".split(" "))
_deck.extend("3H 4S 6H 6S 7H 7S 8D 9H JH QD KD AC AS".split(" "))

#print("p1 hand", p1_hand)
#print("p2 hand", p2_hand)
#print("p3 hand", p3_hand)
#print("p4 hand", p4_hand)

def start_game(p0_play, p1_play, p2_play, p3_play):

    old_stdout = sys.stdout
    sys.stdout = open("out.txt", "w")

    round_history = []

    for round_number in range(10): #10 rounds
        print("--------------------")
        print("Round", round_number)
        deck = _deck
        random.shuffle(deck)

        current_player = 0

        p0_hand = deck[0:13]
        p1_hand = deck[13:26]
        p2_hand = deck[26:39]
        p3_hand = deck[39:52]

        #hand, func, score, passed
        players = [[p0_hand, p0_play, 0, False],
                   [p1_hand, p1_play, 0, False],
                   [p2_hand, p2_play, 0, False],
                   [p3_hand, p3_play, 0, False]]

        print("Dealt cards.")
        print("Player 0:",p0_hand)
        print("Player 1:",p1_hand)
        print("Player 2:",p2_hand)
        print("Player 3:",p3_hand)

        if "3D" in p0_hand:
            current_player = 0
            print("Player 0 had 3D")
        elif "3D" in p1_hand:
            current_player = 1
            print("Player 1 had 3D")
        elif "3D" in p2_hand:
            current_player = 2
            print("Player 2 had 3D")
        elif "3D" in p3_hand:
            current_player = 3
            print("Player 3 had 3D")

        round_end = False
        #start the round now
        while not round_end:
            for trick_num in range(13):
                print("Starting trick", trick_num)

                current_player, round_end = do_trick(players, current_player, round_number)
                if round_end:
                    break
            update_scores(players)

    print([players[[0,1,2,3].index(x)][2] for x in range(4)])
    key = lambda x:players[[0,1,2,3].index(x)][2]
    ranks = sorted([0,1,2,3], key=key, reverse=True)
    print("**************")
    print(ranks)
    sys.stdout.close()
    sys.stdout = old_stdout

def do_trick(players, current_player, round_number):
    previous_play = []
    failures = [0,0,0,0]
    passes = [0,0,0,0]
    round_end = False
    #using i because it is just for repetition
    for i in range(52): #maximum plays in a trick
        play = players[current_player][1](players[current_player][0],
                                          round_number==0,
                                          previous_play,
                                          None,
                                          current_player,
                                          [len(players[0][0]), len(players[1][0]), len(players[2][0]), len(players[3][0])],
                                          [players[0][2], players[1][2], players[2][2], players[3][2]],
                                          round_number)
        validity = play_check.is_valid_play(previous_play, play)
        print("Player",current_player,"played",play)
        print("Valid:",validity)
        if not validity:
            players[current_player][2] -= 50
            failures[current_player] = 1
        else:
            if play==[]:#pass
                passes[current_player] = 1
        if passes.count(1)==3:
            round_end = True
            break
        if all(failures):
            print("All players failed to play a valid play. Ending round.")
            round_end = True
            break
        current_player += 1
        if current_player>3:
            current_player = 0
        
    return current_player, round_end

def update_scores(players):
    total_cards = 0
    hands = [0,0,0,0]
    for i,player in enumerate(players):
        players[i][2] += play_check.len_to_score(len(players[i][0]))
        hands[i] = len(players[i][0])
        total_cards += len(players[i][0])
    winner = hands.index(min(hands))
    players[winner][2] = total_cards
    

if __name__=="__main__":
    import program as p1
    import program as p2
    import program as p3
    import program as p4
    start_game(p1.play, p2.play, p3.play, p4.play)
