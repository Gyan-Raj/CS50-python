import random


# choice(seq) => Choose a random element from a non-empty sequence.
coin = random.choice(["head", "tail"])
print(coin)


# randint(a, b) => Return random integer in range [a, b], including both end points.
num = random.randint(1, 10)
print(num)


# shuffle => Shuffle list x in place, and return None.
cards = ["king", "queen", "jack", "ace"]
random.shuffle(cards)
print(cards)
