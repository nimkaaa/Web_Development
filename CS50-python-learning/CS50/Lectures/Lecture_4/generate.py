import random

def main():
   # number = random.randint(1, 10)
   # print(number)

   cards = ["jack", "queen", "king"]
   random.shuffle(cards)

   for card in cards:
      print(card)


main()