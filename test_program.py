RANK_ORDER = '34567890JQKA2'
SUIT_ORDER = 'DCHS'

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

def key(card):
  return SUIT_ORDER.index(card[1]) + RANK_ORDER.index(card[0])*10

def sort_cards(cards):
  return sorted(cards, key=key)

def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
  """
  The parameters to this function are:
  * `hand`: A list of card strings that are the card(s) in your hand.
  * `is_start_of_round`: A Boolean that indicates whether or not the `play` function is being asked to make the first play of a round.
  * `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
  * `round_history`: A list of *trick_history* entries.
    A *trick_history* entry is a list of *trick_play* entries.
    Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
  * `player_no`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
  * `hand_sizes`: A 4-tuple of integers representing the number of cards each player has in their hand, in player number order. 
  * `scores`: A 4-tuple of integers representing the score of each player at the start of this round, in player number order.
  * `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.

  This function should return an empty list (`[]`) to indicate a pass (see "Playing a Round"), or a list of card strings, indicating that you want to play these cards to the table as a valid play.
  """
  if is_start_of_round:
    return ["3D"]
  hand = sort_cards(hand)
  # If we are starting a trick, we cannot pass.
  if len(play_to_beat) == 0:
    return [hand[0]]
  for card in hand:
    if is_higher(card,play_to_beat[0]): #my lowest card is better
      return [card]
  
  # We don't know how to play any other kinds of tricks, so play a pass.
  return []


if __name__ == '__main__':
  # Write your own test cases for your `play` function here.
  # These can be run with the Run button and will not affect the tournament or marking.
  
  # Here's an example test case and testing code to kick you off.
  TESTS = [  # [ expected return value, inputs ]
    [['3D'], [['3D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],
    # Add more tests here.
  ]
  
  # This runs the above test cases.
  for i, test in enumerate(TESTS):
    expected_return_value, inputs = test
    actual_return_value = play(*inputs)
    if actual_return_value == expected_return_value:
      print('PASSED {}/{}.'.format(i + 1, len(TESTS)))
    else:
      print('FAILED {}/{}.'.format(i + 1, len(TESTS)))
      print('    inputs:', repr(inputs))
      print('  expected:', repr(expected_return_value))
      print('    actual:', repr(actual_return_value))
