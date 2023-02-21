import random
# this should create a list with all values for as single deck of cards
# the param should be the number of decks returned in the final return of the function
def makeDeck(numDecks):
  # finalCards will be the list with every card value based on how many decks is asked for.  This value will be in order and NOT shuffled
  finalCards = []
  # we make the decks and return them
  # by using a for loop, we can make the function do the deck creation logic as many times as decks requested
  for i in range(numDecks):
    # here we do 1 round per suit (since there 4 suits, we do 0, 1, 2, 3 as 4 is exculded in range)
    for j in range(4):
      # default suit will be spades
      suit = 'Spades'
      if j == 1:
        suit = 'Clubs'
      elif j == 2:
        suit = 'Hearts'
      elif j == 3:
        suit = 'Diamonds'
      # here we set the range to 13 so that we can get every card in the suit
      for k in range(13):
        # then we need to make sure we account for the following: 0: king, 1: ace, 11: jack, 12: queen3
        value = k
        name = str(k)
        if k == 0:
          value = 10
          name = 'King'
        elif k == 1:
          value = 11
          name = 'Ace'
        elif k == 11:
          value = 10
          name = 'Jack'
        elif k == 12:
          value = 10
          name = 'Queen'
        card = {
          'value' : value,
          'name' : name,
          'suit': suit,
        }
        finalCards.append(card)
        
        # once we create the card (we can use a dictionary for this to make it easily accesible and store data)
        # next we can use a method to add the newly created card to the finalCards list (each card will be a dictionary)


  return finalCards





def shuffleCards(cards):
  # first we declare an empty list to hold all the cards, but in a new order
  shuffledCards = []
  # this will take in a list (all of the cards) and return the exact same cards in a randomized order
  # we set a while loop to continue shuffling until the original list of cards is created
  while len(cards) > 0:
    # every iteration of the loop we generate a random number that will be the index of the random card we choose from the original list
    # this has to be held in a variable so we ensure that we only remove the exact card (index) that we added to our new shuffled deck
    idx = random.randint(0, len(cards) -1)
    # next we append the card into our shuffled list (this is a random card from the sorted list), append places it in the next available index position
    shuffledCards.append(cards[idx])
    # we remove the card we just placed in the shuffled list from the original list here
    cards.pop(idx)
    # we re run the loop with a smaller list (we just removed a card from it), and continue this untill we have a random list  
  return shuffledCards


newDeck = makeDeck(3)
shufDeck = shuffleCards(newDeck)
print(shufDeck)