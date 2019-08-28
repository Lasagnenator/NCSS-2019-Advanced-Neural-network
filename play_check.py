
def is_valid_play(previous_play, play):
    #testing a pass
    if previous_play != [] and play == []:
        return True
    if previous_play == [] and play != []:
        return True
    
    return False
    pass

def len_to_score(length):
    if length<10:
        score = length
    elif 10<=length<=12:
        score = 2*length
    else:
        score = 39

    score = -score
    return score
