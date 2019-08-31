import random
import play_check
import sys

_deck = "5C 6D 6C 7D 7C 8C 8S 9C 0C QC QH KC 2H".split(" ")
_deck.extend("3C 4D 4C 5H 9D 9S 0H JD JS KH KS AD 2D".split(" "))
_deck.extend("3D 3S 4H 5D 5S 8H 0D 0S JC QS AH 2C 2S".split(" "))
_deck.extend("3H 4S 6H 6S 7H 7S 8D 9H JH QD KD AC AS".split(" "))

def start_game(p0_play, p1_play, p2_play, p3_play):
    #args are play functions for each player

    old_stdout = sys.stdout
    sys.stdout = open("out.txt", "w")

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

        players = [[p0_hand, p0_play, 0],
                   [p1_hand, p1_play, 0],
                   [p2_hand, p2_play, 0],
                   [p3_hand, p3_play, 0]]

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
            
        previous_play = []
        trick_count = 0
        
        round_history = [[]]
        hand_sizes = [13,13,13,13]
        scores = [0,0,0,0]
        
        while players[0][0] and players[1][0] and players[2][0] and players[3][0]:
            player_correct = [True,True,True,True]
            player_passes = [0,0,0,0]
            print("Trick", trick_count)
            #play a trick
            play = players[current_player][1](players[current_player][0],
                                              round_number==0,
                                              previous_play,
                                              round_history,
                                              current_player,
                                              hand_sizes,
                                              scores,
                                              round_number)
            print("Player", current_player, "played", play)
            validity = play_check.is_valid_play(previous_play, play)
            print("Validity:", validity)
            if not validity:
                players[current_player][2] -= 50
                player_correct[current_player] = False
                print(player_correct)
            else:
                previous_play = play
                round_history[-1].append((current_player, play))
                #remove the cards from their hand
                print("Player",current_player,"hand:",players[current_player][0])
                [players[current_player][0].remove(card) for card in play]
            current_player += 1
            if current_player==4:
                current_player = 0
            trick_count += 1
            if trick_count==100: #round ends after 100 tricks
                #theoretically could go forever with passes
                break
            if player_correct.count(False)==4: #all four players made a mistake
                print("All players made a mistake in this trick")
                break

            
            
        #round ended, calculate scores
        total_cards = len(players[0][0])+len(players[1][0])+len(players[2][0])+len(players[3][0])
        for i, player in enumerate(players):
            players[i][2] += play_check.len_to_score(len(player[0]))
            hand_sizes[i] = len(player[0])
            if len(player[0])==0: #winner of the round gets all points
                players[i][2] += total_cards

        scores = [players[0][2], players[1][2], players[2][2], players[3][2]]
        round_history = []

    key = lambda x:players[[0,1,2,3].index(x)][2]
    ranks = sorted([0,1,2,3], key=key, reverse=True)
    print("**************")
    print(ranks)
    sys.stdout.flush()
    sys.stdout.close()
    sys.stdout = old_stdout
    return ranks

if __name__=="__main__":
    import program as p1
    import program as p2
    import program as p3
    import program as p4
    start_game(p1.play, p2.play, p3.play, p4.play)
