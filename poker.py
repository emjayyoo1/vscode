import random

class Card( object ):
  def __init__(self, name, value, suit): 
    self.value = value
    self.suit = suit
    self.name = name
  def __repr__(self):
      return str( self.name) + " of " + self.suit

class StandardDeck(object):
  def __init__(self):
    self.cards = []
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = {"Two":2,
              "Three":3,
              "Four":4,
              "Five":5,
              "Six":6,
              "Seven":7,
              "Eight":8,
              "Nine":9,
              "Ten":10,
              "Jack":11,
              "Queen":12,
              "King":13,
              "Ace":14 }

    for name in values:
      for suit in suits:
        self.cards.append(Card(name, values[name], suit))

deck = StandardDeck()

def shuffle(self, times = 1):
  random.shuffle(self.cards)
  print('Deck shuffled')


def user_name():
  user = input('Enter first name : ')
  return user

def user_chips():
  chips = input('Enter number of chips in stack : ')
  while True:
    if chips.isdigit() == True:
      return chips
    else:
      print('Enter digit.')
      chips = input('Enter number of chips in stack : ')

def give_cards(): 
  card1 = deck.cards.pop()
  return card1

class Player(object):
  def __init__(self, firstname, chips, card1, card2):
    self.firstname = firstname
    self.chips = chips
    self.card1 = card1
    self.card2 = card2
    self.in_hand = True

  #Functions 

  def reveal(self):
    print('Player name :', self.firstname, '\nCard 1 : ', self.card1, '\nCard 2 : ', self.card2, '\nChips remaining : ', self.chips)

  #Check or Raise

  def raise_(self):
    print(self.chips)
    print(self.firstname)
    self.raise_amount = input('enter raise amount, or enter to check : ')
    if self.raise_amount.isdigit()==True:
      while True:
        if int(self.raise_amount) <= self.chips:
          self.chips +=- int(self.raise_amount)
          return int(self.raise_amount)
        else:
          print('Not enough chips.')
          print(self.firstname)
          self.raise_amount = input('enter raise amount, or enter to check : ')
    else:
      return 0

  # Call, Raise, Fold   
   
  def crf(self):
    self.user_decision = input('Type: Call, Raise, or Fold) ')
    if self.user_decision.lower() == 'call':
      self.in_hand = True
      return True
      
    elif self.user_decision.lower() == 'fold':
      self.in_hand = False
      return False

    elif self.user_decision.lower() == 'raise':
      self.in_hand = True
      self.reraise_amount = input('enter raise amount, or enter to check : ')
      if self.reraise_amount.isdigit()==True:
        while True:
          if int(self.reraise_amount) <= self.chips:
            self.chips +=- int(self.reraise_amount)
            return int(self.reraise_amount)
          else:
            print('Not enough chips.')
            self.reraise_amount = input('enter raise amount, or enter to check : ')

    else:
      print(self.firstname, 'checked.')


# Start Game



shuffle(deck)

p1 = Player(user_name(), int(user_chips()), give_cards(), give_cards())
p2 = Player(user_name(), int(user_chips()), give_cards(), give_cards())

pot = 0
flop = []

def start_flop():
  x = deck.cards.pop()
  flop.append(x)
  y = deck.cards.pop()
  flop.append(y)
  z = deck.cards.pop()
  flop.append(z)
  print(flop)

start_flop()


while True:
    if int(p1.raise_()) >=1:
      pot += int(p1.raise_amount)
      print(p1.firstname, 'raised :',p1.raise_amount,'\nPOT : ', pot)

      #P2

      print(p2.firstname, 'Enter : Call, Raise, or Fold')

      p2.crf()

      if p2.user_decision.lower() == 'call':
        print(p2.firstname, 'called')
        pot += int(p1.raise_amount)
        p2.chips += -int(p1.raise_amount)
        break

      elif p2.user_decision.lower() == 'fold':
        print('follld')
        p1.chips += pot
        pot = 0 
        break

      elif p2.user_decision.lower() == 'raise':
        p2.chips += -int(p1.raise_amount)
        pot += int(p1.raise_amount)
      
        if int(p2.raise_()) >=1:
          pot += int(p2.raise_amount)
          print(p2.firstname, 'raised :',p2.raise_amount,'\nPOT : ', pot)
        
        else:
          print('folded')


    else:
      print(p1.firstname, 'checked')
      if int(p2.raise_())>=1:
        pot += int(p2.raise_amount)
        print(p2.firstname,'raised :', p2.raise_amount,'\nPOT : ', pot)

      else:
        print(p2.firstname, 'checked')
        in_raise = 'False'
        break

print('betting over')


print(p1.reveal())
print()
print(p2.reveal())
print()
print('Pot : ', pot)







