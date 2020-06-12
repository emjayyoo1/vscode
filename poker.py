import random
import sys
from collections import Counter
from operator import attrgetter

# Card and deck of cards


class Card(object):
    def __init__(self, name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name

    def __repr__(self):
        return str(self.name) + " of " + self.suit


class StandardDeck(object):
    def __init__(self):
        self.cards = []

        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = {"Two": 2,
                  "Three": 3,
                  "Four": 4,
                  "Five": 5,
                  "Six": 6,
                  "Seven": 7,
                  "Eight": 8,
                  "Nine": 9,
                  "Ten": 10,
                  "Jack": 11,
                  "Queen": 12,
                  "King": 13,
                  "Ace": 14}

        for name in values:
            for suit in suits:
                self.cards.append(Card(name, values[name], suit))

    # Deck reset & shuffle functions

    def reset(self):
        if p1.card1:
            p1.clear_hand()
        else:
            pass
        if p2.card1:
            p2.clear_hand()
        else:
            pass
        if p3.card1:
            p3.clear_hand()
        else:
            pass
        if p4.card1:
            p4.clear_hand()
        else:
            pass
        if p5.card1:
            p5.clear_hand()
        else:
            pass
        if p6.card1:
            p6.clear_hand()
        else:
            pass
        self.shuffle(deck)
        print('\n------------------------Cards reset--------------------------\n')

    def shuffle(self, times=1):
        random.shuffle(self.cards)
        print('Deck shuffled')

# Player object and functions


class Player(object):
    def __init__(self, firstname, chips, card1):
        self.firstname = firstname
        self.chips = chips
        self.card1 = card1
        self.in_hand = True
        self.flush = False
        self.made_hand = []
        self.made_hand_three = []
        self.made_hand_four = []
        self.pair = 0
        self.two_pair = False
        self.three_of_kind = False
        self.four_of_kind = False
        self.straight = False
        self.full_house = False
        self.straight_list = []

    # Functions

    # Reveal

    def reveal(self):
        print('Player name : \t\t ', self.firstname, '\nChips remaining : \t ', self.chips,
              '\nCard 1 : \t\t ', self.card1[0], '\nCard 2 : \t\t ', self.card1[1],  '\n')

    # Clear hand

    def clear_hand(self):
        deck.cards.append(self.card1.pop())
        deck.cards.append(self.card1.pop())
        print(self.firstname, 'hand cleared\n')

    # Check hand ranking

    # Flush

    def flush_suit_checker(self):
        self.seven_cards = self.card1 + game.flop
        c = Counter(getattr(x, 'suit') for x in self.seven_cards)
        if (c['Clubs'] or c['Hearts'] or c['Diamonds'] or c['Spade']) >= 5:
            print(self.firstname, ': flush')
            self.flush = True

        else:
            pass

        clubs = sum(1 for x in self.seven_cards if x.suit == "Clubs")
        hearts = sum(1 for x in self.seven_cards if x.suit == "Hearts")
        diamonds = sum(1 for x in self.seven_cards if x.suit == "Diamonds")
        spades = sum(1 for x in self.seven_cards if x.suit == "Spades")

        if self.flush == True:
            if clubs >= 5:
                print('Clubs')
            if hearts >= 5:
                print('Hearts')
            if diamonds >= 5:
                print('Diamonds')
            if spades >= 5:
                print('Spades')

    # Hand ranking 4 of a kind - pair

    def hand_ranking(self):
        self.seven_cards = self.card1 + game.flop
        c = Counter(getattr(x, 'value') for x in self.seven_cards)
        for x in c:

            if c[x] == 4:
                self.made_hand_four.append(x)
                self.four_of_kind = True

            if c[x] == 3:
                self.made_hand_three.append(x)
                self.three_of_kind = True

            if self.pair == 0:
                if c[x] == 2:
                    self.made_hand.append(x)
                    self.pair += 1
            else:
                if c[x] == 2:
                    self.made_hand.append(x)
                    self.two_pair = True
                    self.pair += 1

        if self.four_of_kind == True:
            print(self.firstname, 'Four of a kind : ', self.made_hand_four)

        elif (self.three_of_kind and self.pair) == True:
            print(self.firstname, 'full house : ', self.made_hand_three,
                  "'s over ", self.made_hand, "'s")

        elif self.three_of_kind == True:
            print(self.firstname, 'Three of a kind : ', self.made_hand_three)

        elif self.pair >= 2:
            print(self.firstname, 'Two pairs of : ', self.made_hand)

        elif self.pair == 1:
            print(self.firstname, 'Pairs of : ', self.made_hand)

    # Hand ranking for straight

    def hand_ranking_straight(self):
        self.seven_cards = self.card1 + game.flop
        c = sorted(self.seven_cards, key=attrgetter('value'), reverse=True)
        count_straight = 0
        for x in c:

          #[6,7,8,9,J,A ]

            if count_straight == 0:
                self.straight_list.append(x)
                count_straight += 1

            elif count_straight >= 5:
                if x.value - self.straight_list[0].value == -1:
                    pass
                else:
                    pass
            else:
                if x.value - self.straight_list[0].value == -1:
                    self.straight_list.insert(0, x)
                    count_straight += 1
                elif x.value - self.straight_list[0].value == 0:
                    pass
                else:
                    self.straight_list = []
                    self.straight_list.insert(0, x)
                    count_straight = 1

        if count_straight >= 5:
            print(self.firstname, 'has straight :', self.straight_list)
            self.straight = True

    # Check or Raise

    def raise_(self):
        print(self.chips)
        print(self.firstname)
        self.raise_amount = input('enter raise amount, or enter to check : ')
        if self.raise_amount.isdigit() == True:
            while True:
                if int(self.raise_amount) <= self.chips:
                    self.chips += - int(self.raise_amount)
                    return int(self.raise_amount)
                else:
                    print('Not enough chips.')
                    print(self.firstname)
                    self.raise_amount = input(
                        'enter raise amount, or enter to check : ')
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
            self.reraise_amount = input(
                'enter raise amount, or enter to check : ')
            if self.reraise_amount.isdigit() == True:
                while True:
                    if int(self.reraise_amount) <= self.chips:
                        self.chips += - int(self.reraise_amount)
                        return int(self.reraise_amount)
                    else:
                        print('Not enough chips.')
                        self.reraise_amount = input(
                            'enter raise amount, or enter to check : ')

        else:
            print(self.firstname, 'checked.')

    def give__cards(self):
        if self.card1:
            self.clear_hand()
        else:
            pass
        if self.card1:
            self.clear_hand()
        else:
            pass
        self.card1.append(deck.cards.pop())
        self.card1.append(deck.cards.pop())
        print(self.firstname, 'has been dealt cards. \n')


# Give cards functions


# Player inputs, put in afterwards, stored at end

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


class Game(object):
    def __init__(self):
        self.pot = 0
        self.flop = []

    # Community card functions

    def start_flop(self):
        x = deck.cards.pop()
        self.flop.append(x)
        y = deck.cards.pop()
        self.flop.append(y)
        z = deck.cards.pop()
        self.flop.append(z)
        print('Flop : ', self.flop[0], '//',
              self.flop[1], '//', self.flop[2], '//', '\n')

    def start_turn(self):
        x = deck.cards.pop()
        self.flop.append(x)
        print('Turn : ', self.flop[3], '\n')

    def start_river(self):
        x = deck.cards.pop()
        self.flop.append(x)
        print('River : ', self.flop[4], '\n')


# Game details and player information
p1 = Player('Jack', 1000, [],)
p2 = Player('Lolo', 1000, [],)
p3 = Player('', 0, [], )
p4 = Player('', 0, [], )
p5 = Player('', 0, [], )
p6 = Player('', 0, [], )

game = Game()
deck = StandardDeck()

# -------------------------------- Start Game -------------------------------------

# ///////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////

# Key functions
# reset()
# give__cards(self)
# self.reveal()
# self.clear_hand()
# start_flop()
# start_turn()
# start_river()


deck.reset()

p1.give__cards()
p2.give__cards()

p1.reveal()
p2.reveal()

game.start_flop()
game.start_turn()
game.start_river()


p1.flush_suit_checker()
p2.flush_suit_checker()

p1.hand_ranking()
print()
p2.hand_ranking()
print()
p1.hand_ranking_straight()
print()
p2.hand_ranking_straight()


# p1flush = []

# for x in p1.seven_cards:


#     print(p1flush, '\n\n', p2flush)
# else:
#     print('no code')


# clubs = sum(1 for x in seven_cards if x.suit == "Clubs")
# hearts = sum(1 for x in seven_cards if x.suit == "Hearts")
# diamonds = sum(1 for x in seven_cards if x.suit == "Diamonds")
# spades = sum(1 for x in seven_cards if x.suit == "Spades")

# if clubs >= 5:
#     print('flush')
# if hearts >= 5:
#     print('flush')
# if diamonds >= 5:
#     print('flush')
# if spades >= 5:
#     print('flush')
# Test code /////////////////////////////////////////////////////////////////////////

# y = sorted(seven_cards, key=lambda x: x.value, reverse=True)

# flush = print(seven_cards)

# clubs = sum(1 for x in seven_cards if x.suit == "Clubs")
# hearts = sum(1 for x in seven_cards if x.suit == "Hearts")
# diamonds = sum(1 for x in seven_cards if x.suit == "Diamonds")
# spades = sum(1 for x in seven_cards if x.suit == "Spades")

#
#  if clubs >= 5:
#     print('flush')
# if hearts >= 5:
#     print('flush')
# if diamonds >= 5:
#     print('flush')
# if spades >= 5:
#     print('flush')

# seven_cards(self) = self.card1 + game.flop

# flush = False

# c = Counter(getattr(x, 'suit') for x in seven_cards)
# if (c['Clubs'] or c['Hearts'] or c['Diamonds'] or c['Spade']) >= 5:
#     print('flush')
#     flush = True
# else:
#     print('no flush')

# d = Counter(getattr(x, 'value') for x in seven_cards)
# print(d)

sys.exit()


# Test code /////////////////////////////////////////////////////////////////////////

# Think about combining player cards into 1 list.

if (int(p1.card1[0].value) + int(p1.card1[1].value)) >= (int(p2.card1[0].value) + int(p2.card1[1].value)):
    print(p1.firstname, 'wins\n')
elif (int(p1.card1[0].value) + int(p1.card1[1].value)) == (int(p2.card1[0].value) + int(p2.card1[1].value)):
    print('Draw\n')
else:
    print(p2.firstname, 'wins\n')

p1.clear_hand()
p2.clear_hand()


# Test code /////////////////////////////////////////////////////////////////////////


count = 0
for x in deck.cards:
    count += 1
    print(x, count)

sys.exit()

while True:
    if int(p1.raise_()) >= 1:
        pot += int(p1.raise_amount)
        print(p1.firstname, 'raised :', p1.raise_amount, '\nPOT : ', pot)

        # P2

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

            if int(p2.raise_()) >= 1:
                pot += int(p2.raise_amount)
                print(p2.firstname, 'raised :',
                      p2.raise_amount, '\nPOT : ', pot)

            else:
                print('folded')

    else:
        print(p1.firstname, 'checked')
        if int(p2.raise_()) >= 1:
            pot += int(p2.raise_amount)
            print(p2.firstname, 'raised :', p2.raise_amount, '\nPOT : ', pot)

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


p1 = Player(user_name(), int(user_chips()), [], [])
p2 = Player(user_name(), int(user_chips()), [], [])
