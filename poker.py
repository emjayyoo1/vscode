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
        self.flush_hand = []
        self.made_hand = []
        self.made_hand_three = []
        self.made_hand_four = []
        self.pair = 0
        self.two_pair = False
        self.three_of_kind = False
        self.four_of_kind = False
        self.straight = False
        self.full_house = False
        self.full_house_test = []
        self.is_flush = False
        self.is_straight_flush = False
        self.straight_list = []
        self.score = 0

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

    # ========================= Hand ranking all ============================

    def hand_ranking(self):

        self.seven_cards = self.card1 + game.flop
        # Pair, three, four of a kind

        self.test2 = []
        for x in self.seven_cards:
            self.test2.append(x.value)

        c = Counter(getattr(x, 'value') for x in self.seven_cards)
        for x in c:

            if c[x] == 4:
                self.made_hand_four.append(x)
                self.four_of_kind = True

            if c[x] == 3:
                self.made_hand_three.append(x)
                self.three_of_kind = True
                self.full_house_test.append(x)
                self.full_house_test.append(x)
                self.full_house_test.append(x)

            if self.pair == 0:
                if c[x] == 2:
                    self.made_hand.append(x)
                    self.made_hand.append(x)
                    self.pair += 1
                    self.full_house_test.append(x)
                    self.full_house_test.append(x)

            else:
                if c[x] == 2:
                    self.made_hand.append(x)
                    self.made_hand.append(x)
                    self.two_pair = True
                    self.pair += 1

        # Straight

        d = sorted(self.seven_cards, key=attrgetter('value'), reverse=True)
        count_straight = 0

        for x in d:

          # [6,7,8,9,J,A ]

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

        # Flush

        e = Counter(getattr(x, 'suit') for x in self.seven_cards)

        if (e['Clubs'] or e['Hearts'] or e['Diamonds'] or e['Spade']) >= 5:
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
                suit_return = 'Clubs'
            if hearts >= 5:
                suit_return = 'Hearts'
            if diamonds >= 5:
                suit_return = 'Diamonds'
            if spades >= 5:
                suit_return = 'Spades'

            for x in self.seven_cards:
                if x.suit == suit_return:
                    self.flush_hand.append(x)

        if self.four_of_kind == True:
            print(self.firstname, 'Four of a kind : ', self.made_hand_four)

        if count_straight >= 5:
            print(self.firstname, 'has straight :', self.straight_list)
            self.straight = True

        elif (self.three_of_kind and self.pair) == True:
            print(self.firstname, 'full house : ', self.made_hand_three,
                  "'s over ", self.made_hand, "'s")
            self.full_house = True

        elif self.three_of_kind == True:
            print(self.firstname, 'Three of a kind : ', self.made_hand_three)

        elif self.pair >= 2:
            print(self.firstname, 'Two pairs of : ',
                  sorted(self.made_hand[0:4], reverse=True))

        elif self.pair == 1:
            print(self.firstname, 'Pairs of : ', self.made_hand)

        # Scoring

        # Straight Flush - Error - counts straight flush from 7 not 5

        # if (self.straight and self.flush) == True:
        #     self.score += 80000 + self.straight_list[-1].value

        # Full House

        elif self.full_house == True:
            self.test2.remove(self.made_hand_three[0])
            self.test2.remove(self.made_hand_three[0])
            self.test2.remove(self.made_hand_three[0])
            self.made_hand_sorted = sorted(self.made_hand, reverse=True)
            self.test2.remove(self.made_hand_sorted[0])
            self.test2.remove(self.made_hand_sorted[0])
            test2sorted = (sorted(self.test2, reverse=True))
            self.score += 70000 + \
                (self.made_hand_three[0]*500) + \
                (self.made_hand_sorted[0])

       # Four of a kind

        elif self.four_of_kind == True:
            self.test2.remove(self.made_hand_four[0])
            self.test2.remove(self.made_hand_four[0])
            self.test2.remove(self.made_hand_four[0])
            self.test2.remove(self.made_hand_four[0])
            test2sorted = (sorted(self.test2, reverse=True))
            self.score += 60000 + \
                (self.made_hand_four[0] * 500) + test2sorted[0]

        # Flush

        elif self.flush == True:
            self.flush_hand_sorted = sorted(
                self.flush_hand, key=attrgetter('value'), reverse=True)
            print(self.flush_hand_sorted)
            self.score += 50000 + (self.flush_hand_sorted[0].value*500) + \
                (self.flush_hand_sorted[1].value*20) + self.flush_hand_sorted[2].value + \
                ((self.flush_hand_sorted[3].value/20)) + (self.flush_hand_sorted[3].value /
                                                          500) + (self.flush_hand_sorted[4].value/10000)

       # Straight - Need to include wheel

        elif self.straight == True:
            self.score += 40000 + self.straight_list[-1].value
            # TERMINOLOGY WORKS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

       # Three of a kind

        elif self.three_of_kind == True:
            self.test2.remove(self.made_hand_three[0])
            self.test2.remove(self.made_hand_three[0])
            self.test2.remove(self.made_hand_three[0])
            self.test2sorted = (sorted(self.test2, reverse=True))
            self.score += 30000 + \
                (self.made_hand_three[0] * 500) + \
                (self.test2sorted[0]*20) + self.test2sorted[1]

        # Two Pair

        elif self.two_pair == True:
            self.made_hand_sorted = sorted(self.made_hand, reverse=True)
            self.test2.remove(self.made_hand_sorted[0])
            self.test2.remove(self.made_hand_sorted[0])
            self.test2.remove(self.made_hand_sorted[2])
            self.test2.remove(self.made_hand_sorted[2])
            self.test2sorted = (sorted(self.test2, reverse=True))
            self.score += 20000 + \
                (self.made_hand_sorted[0]*500) + \
                (self.made_hand_sorted[3]*20) + self.test2sorted[0]

        # 1 Pair

        elif self.pair == 1:
            self.made_hand_sorted = sorted(self.made_hand, reverse=True)
            self.test2.remove(self.made_hand_sorted[0])
            self.test2.remove(self.made_hand_sorted[0])
            self.test2sorted = (sorted(self.test2, reverse=True))
            self.score += 10000 + \
                (self.made_hand_sorted[0]*500) + \
                (self.test2sorted[0]*20) + self.test2sorted[1] + \
                ((self.test2sorted[2]/20))

        # High Card

        else:
            self.test2sorted = (sorted(self.test2, reverse=True))
            self.score += (self.test2sorted[0]*500) + \
                (self.test2sorted[1]*20) + self.test2sorted[2] + \
                ((self.test2sorted[3]/20)) + (self.test2sorted[3] /
                                              500) + (self.test2sorted[4]/10000)

    # ========================= ===================== ============================

    # Check or Raise

    # Raising system - redo

    # def raise_(self):
    #     print(self.chips)
    #     print(self.firstname)
    #     self.raise_amount = input('enter raise amount, or enter to check : ')
    #     if self.raise_amount.isdigit() == True:
    #         while True:
    #             if int(self.raise_amount) <= self.chips:
    #                 self.chips += - int(self.raise_amount)
    #                 return int(self.raise_amount)
    #             else:
    #                 print('Not enough chips.')
    #                 print(self.firstname)
    #                 self.raise_amount = input(
    #                     'enter raise amount, or enter to check : ')

    # Give cardsd

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

    # Deal Flop

    def start_flop(self):
        x = deck.cards.pop()
        self.flop.append(x)
        y = deck.cards.pop()
        self.flop.append(y)
        z = deck.cards.pop()
        self.flop.append(z)
        print('Flop : ', self.flop[0], '//',
              self.flop[1], '//', self.flop[2], '//', '\n')

    # Deal Turn

    def start_turn(self):
        x = deck.cards.pop()
        self.flop.append(x)
        print('Turn : ', self.flop[3], '\n')

    # Deal River

    def start_river(self):
        x = deck.cards.pop()
        self.flop.append(x)
        print('River : ', self.flop[4], '\n')


# Game details and player information - Fixed at present

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
# deck.reset()
# p1.give__cards()
# p1.reveal()
# p1.clear_hand()
# game.start_flop()
# game.start_turn()
# game.start_river()
# p1.hand_ranking


deck.reset()

p1.give__cards()
p2.give__cards()

p1.reveal()
p2.reveal()

game.start_flop()
game.start_turn()
game.start_river()


print('--------------------------Showdown-------------------------\n')
p1.hand_ranking()
print()
p2.hand_ranking()

print('\n-------------------------------------------------------------\n')
print(p1.firstname, 'Ranking Score : ', p1.score)
print(p2.firstname, 'Ranking Score : ', p2.score)


if p1.score > p2.score:
    print(p1.firstname, 'wins')
elif p2.score > p1.score:
    print(p2.firstname, 'wins')
else:
    print('Draw')


sys.exit()


# Test code /////////////////////////////////////////////////////////////////////////


p1 = Player(user_name(), int(user_chips()), [], [])
p2 = Player(user_name(), int(user_chips()), [], [])
