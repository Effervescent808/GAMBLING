import random

bot1_bal = 1500
bot2_bal = 1500
bot3_bal = 1500

all_cards = []

twos = []
threes = []
fours = []
fives = []
sixes = []
sevens = []
eights = []
nines = []
tens = []
jacks = []
queens = []
kings = []
aces = []

num_dict = {2:twos, 3:threes, 4:fours, 5:fives, 6:sixes, 7:sevens, 8:eights, 9:nines, 10:tens, 11:jacks, 12:queens, 13:kings, 14:aces}

values = list(range(2,15))
suits = [" of Spades", " of Hearts", " of Diamonds", " of Clubs"]
deck = [(value, suit) for value in values for suit in suits]
random.shuffle(deck)

def deal_card(deck):
    return deck.pop() if deck else None

hand_int = 0
lens= []

def hand_value(lens):
    hand_val = 0
    if bot_names[0] > bot_names[1]:
        hand_val += (2*int(bot_names[0]))
    else:
        hand_val += (2*int(bot_names[1]))

    for i in range(len(lens)):
        if lens[i] == 4:
            return (500 + hand_val)
        elif lens[i] == 3 and lens[i+1] == 2:
            return (400 + hand_val)
        elif lens[i] == 3:
            return (300 + hand_val)
        elif len(lens) > 1 and lens[i] == 2 and lens[i+1] == 2:
            return (200 + hand_val)
        elif lens[i] == 2:
            return (100 + hand_val)
        else:
            return hand_val
    
def bet(value, account):
    chance = random.randint(1,100)
    if 400 <= value <= 550:
        if 80 < chance < 101:
            return "all in"
        else:
            var = random.randint((int(.5*account)),int(account))
            return var
    elif 300 <= value < 400:
        if 85 < chance < 101:
            return "all in"
        elif chance < 3:
            return "fold"
        else:
            var = random.randint((int(.3*account)),(int(.5*account)))
            return var
    elif 200 <= value < 300:
        if 90 < chance < 101:
            return "all in"
        elif chance < 5:
            return "fold"
        else:
            var = random.randint(int((.15*account)),(int(.3*account)))
            return var
    elif 100 <= value < 200:
        if 95 < chance < 101:
            return "all in"
        elif chance < 10:
            return "fold"
        else:
            var = random.randint((int(.05*account)),(int(.15*account)))
            return var
    else:
        if 99 < chance < 101:
            return "all in"
        elif chance < 15:
            return "fold"
        else:
            var = random.randint(1,(int(.1*account)))
            return var


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PLAYER

bot_names = []
bot_suits = []
for i in range(2):
    botcards = deal_card(deck)
    bot_names.append(botcards[0])
    bot_suits.append(botcards[1])
    all_cards.append(botcards[0])

for n in bot_names:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
for i in num_dict:
    length = len(num_dict[i])
    lens.append(length)
lens = [i for i in lens if i != 0]
lens.sort(reverse=True)

hand_int = hand_value(lens)
bot_bet = bet(hand_int, bot1_bal)

#
#Write bet amounts with random fold chance and random go all in change, better hand_val score, better chances of high bet
#add bets to total pot
#



print(bot_names)
print(hand_int)
print(lens)
print()
print(bot_bet)
print()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#FLOP

flop_suits = []
flop_names = []
#DEAL FLOP
for i in range(3):
    flopcards = deal_card(deck)
    flop_names.append(flopcards[0])
    flop_suits.append(flopcards[1])
    all_cards.append(flopcards[0])

for n in flop_names:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
for i in num_dict:
    length = len(num_dict[i])
    lens.append(length)
lens = [i for i in lens if i != 0]
lens.sort(reverse=True)

hand_int = hand_value(lens)
bot_bet = bet(hand_int, bot1_bal)

#
#Write bet amounts with random fold chance and random go all in change, better hand_val score, better chances of high bet
#add bets to total pot
#

print(flop_names)
print(hand_int)
print(lens)
print()
print(bot_bet)
print()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TURN

turn_suit = []
turn_name = []
#DEAL TURN
turncard = deal_card(deck)
turn_name.append(turncard[0])
turn_suit.append(turncard[1])
all_cards.append(turncard[0])

for n in turn_name:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
for i in num_dict:
    length = len(num_dict[i])
    lens.append(length)
lens = [i for i in lens if i != 0]
lens.sort(reverse=True)

hand_int = hand_value(lens)
bot_bet = bet(hand_int, bot1_bal)


#
#Write bet amounts with random fold chance and random go all in change, better hand_val score, better chances of high bet
#add bets to total pot
#

print(turn_name)
print(hand_int)
print(lens)
print()
print(bot_bet)
print()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#RIVER 

river_suit = []
river_name = []
#DEAL RIVER
rivercard = deal_card(deck)
river_name.append(rivercard[0])
river_suit.append(rivercard[1])
all_cards.append(rivercard[0])

for n in river_name:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
for i in num_dict:
    length = len(num_dict[i])
    lens.append(length)
lens = [i for i in lens if i != 0]
lens.sort(reverse=True)

hand_int = hand_value(lens)
bot_bet = bet(hand_int, bot1_bal)


#
#Write bet amounts with random fold chance and random go all in change, better hand_val score, better chances of high bet
#add bets to total pot
#

print(river_name)
print(hand_int)
print(lens)
print()
print(bot_bet)
print()