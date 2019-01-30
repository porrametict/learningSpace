import random


def playing_card():
    """
    'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
    'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
    'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
    'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'
    """
    rank = list("A23456789") + ["10"] + list("JQK")
    suit = ("\u2660", "\u2665", "\u2666", "\u2663")
    deck = []
    for s in suit:
        for r in rank:
            deck.append(r+s)
    d = [r+s for s in suit for r in rank]
    # print(d)
    # print(deck)
    return d
playing_card()
d = playing_card()
random.shuffle(d)
print(d)