# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.
#
# The itertools library may be helpful. Feel free to 
# define multiple functions if it helps you solve the
# problem. 
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

# CAUTIOUS! With the joker being used as any card, there could be 
# a "five-of-a-kind" card. -- JRZ

import itertools

blackcards = [x + y for x in '23456789TJQKA' for y in 'CS']
redcards   = [x + y for x in '23456789TJQKA' for y in 'HD']

#def best_wild_hand(hand):
#    "Try all values for jokers in all 5-card selections."       
#    # Your code here
#    hand_choices = compute_choices(hand)
#    return max(map(list, hand_choices), key=hand_rank)
#
#def compute_choices(hand):
#    # Replace a lists and return a new one is very tricky. Here I fail.
#    # Be aware of the side effects of ASSIGNMENT! Do not be tempted to use them frequently!
#
#    if not (('?B' in hand) and ('?R' in hand)):
#        return itertools.combinations(hand, 5)
#    elif ('?B' in hand):
#        hand.remove('?B')
#        #new_hands = [ substitute(hand, x) for x in BJoker]
#        new_hands = []
#        for sub in BJoker:
#            new_hands.append([sub if x == '?B' else x for x in hand])
#
#        new_hands = [ itertools.permutations(hand, 5) for hand in new_hands]
#        hand_stream = reduce(new_hands, itertools.chain)
#        return hand_stream
#    elif ('?R' in hand):
#        pass
#    else:
#        pass
#

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    # And this is Prof. Norvig's solution
    # This one line is the key part
    # Notice the use of "*", without which it.product will
    # prodce a totally different result
    # The * is used to remove the outmost brackets as args of a function
    # Notice how this solution cause NO side effect
    hands = set(best_hand(h) for h in itertools.product(*map(replacements, hand)))
    return max(hands, key=hand_rank)

def replacements(card):
    """Return a list of the possible replacements of a card.
    There will be more than 1 only for wild cards"""
    if card == '?B' : return blackcards
    if card == '?R' : return redcards
    else : return [card]

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand." 
    s_hand = itertools.combinations(hand, 5)
    # And this line to avoid duplicate-card problem brought in by the Joker(Don.Flamingo!)
    s_hand = (h for h in s_hand if len(set(h)) == 5)
    return max(s_hand, key = hand_rank)

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
