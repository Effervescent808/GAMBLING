import random
import re

#get balance
with open('account_balance.txt', 'rb') as file:
    balance = ''.join(re.findall(r'\d+', str(file.readlines())))

#USE FOR CHECKING FOR DUPLICATES
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

#balance change function
def balance_change(bal_change):
    n_balance = (bal_change + (int(balance) - total_bet))
    temp = ('Balance =', n_balance)
    write = str(temp).replace("'",'').replace(',','').replace('(','').replace(')','')
    with open('account_balance.txt', 'w') as file:
        file.write(write)

def deal_card(deck):
    return deck.pop() if deck else None

def card_name(value):
    if value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    elif value == 14:
        return "Ace"
    else:
        return value

def best(lens):
    for i in range(len(lens)):
        if lens[i] == 4:
            print('Current Best:')
            print('Four of a kind')
            break
        elif lens[i] == 3 and lens[i+1] == 2:
            print('Current Best:')
            print('Full House')
            break
        elif lens[i] == 3:
            print('Current Best:')
            print('Three of a kind')
            break
        elif lens[i] == 2 and lens[i+1] == 2:
            print('Current Best:')
            print('Two Pair')
            break
        elif lens[i] == 2:
            print('Current Best:')
            print('One pair')
            break
        else:
            if player_names[0] > player_names[1]:
                print('Current Best:')
                print('High card:', card_name(player_names[0]))
                break
            else:
                print('Current Best:')
                print('High card:', card_name(player_names[1]))
                break

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PLAYER 

player_suits = []
player_names = []
#DEAL PLAYER CARDS
for i in range(2):
    playercards = deal_card(deck)
    player_names.append(playercards[0])
    player_suits.append(playercards[1])
    all_cards.append(playercards[0])

card_1 = str(card_name(player_names[0])) + str(player_suits[0])
card_2 = str(card_name(player_names[1])) + str(player_suits[1])

for n in player_names:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
for i in num_dict:
    length = len(num_dict[i])
    lens.append(length)
lens = [i for i in lens if i != 0]
lens.sort(reverse=True)

print('Card 1:',card_1)
print('Card 2:',card_2)
print()

best(lens)

#get bet amount
while True:
    try:
        print('current balance is: ',balance)
        bet_amount_1 = int(input("bet amount?: "))
        total_bet = bet_amount_1
        if bet_amount_1 <= int(balance):
            break
        else:
            print('Not enough balance')
    except ValueError:
        print("Please enter a number")

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

flop_1 = str(card_name(flop_names[0])) + str(flop_suits[0])
flop_2 = str(card_name(flop_names[1])) + str(flop_suits[1])
flop_3 = str(card_name(flop_names[2])) + str(flop_suits[2])

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

print('Card 1:',card_1)
print('Card 2:',card_2)
print()
print('Flop:')
print()
print(flop_1)
print(flop_2)
print(flop_3)
print()
best(lens)

while True:
    try:
        print('current balance is: ',(int(balance) - bet_amount_1))
        bet_amount_2 = int(input("bet amount?: "))
        total_bet = bet_amount_1 + bet_amount_2
        if bet_amount_2 <= (int(balance) - bet_amount_1):
            break
        else:
            print('Not enough balance')
    except ValueError:
        print("Please enter a number")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TURN

turn_suit = []
turn_name = []
#DEAL TURN
turncard = deal_card(deck)
turn_name.append(turncard[0])
turn_suit.append(turncard[1])
all_cards.append(turncard[0])

turn = str(card_name(turn_name[0])) + str(turn_suit[0])

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

print('Card 1:',card_1)
print('Card 2:',card_2)
print()
print('Turn:')
print()
print(flop_1)
print(flop_2)
print(flop_3)
print(turn)
print()
best(lens)

while True:
    try:
        print('current balance is: ',(int(balance) - (bet_amount_1 + bet_amount_2)))
        bet_amount_3 = int(input("bet amount?: "))
        total_bet = bet_amount_1 + bet_amount_2 + bet_amount_3
        if bet_amount_3 <= (int(balance) - total_bet):
            break
        else:
            print('Not enough balance')
    except ValueError:
        print("Please enter a number")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#RIVER 

river_suit = []
river_name = []
#DEAL RIVER
rivercard = deal_card(deck)
river_name.append(rivercard[0])
river_suit.append(rivercard[1])
all_cards.append(rivercard[0])

river = str(card_name(river_name[0])) + str(river_suit[0])

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

print('Card 1:',card_1)
print('Card 2:',card_2)
print()
print('River:')
print()
print(flop_1)
print(flop_2)
print(flop_3)
print(turn)
print(river)
print()
best(lens)

while True:
    try:
        print('current balance is: ',(int(balance) - (bet_amount_1 + bet_amount_2 + bet_amount_3)))
        bet_amount_4 = int(input("bet amount?: "))
        total_bet = bet_amount_1 + bet_amount_2 + bet_amount_3 + bet_amount_4
        if bet_amount_4 <= (int(balance) - total_bet):
            break
        else:
            print('Not enough balance')
    except ValueError:
        print("Please enter a number")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PRINTS

print(card_1)
print(card_2)
print()
print(flop_1)
print(flop_2)
print(flop_3)
print(turn)
print(river)

all_cards.sort(reverse=True)
print(all_cards)

print(lens)

best(lens)

