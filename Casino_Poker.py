import random
import re

#get balance
with open('account_balance.txt', 'rb') as file:
    balance = ''.join(re.findall(r'\d+', str(file.readlines())))

with open('bot1_account.txt', 'rb') as file:
    bot1_bal_s = ''.join(re.findall(r'\d+', str(file.readlines())))

bot1_bal = int(bot1_bal_s)

all_in = 0
loose = 0       
pot = 0
total_bet = 0
total_bot_bet = 0

player_best = []
bot_best = []

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

bot_twos = []
bot_threes = []
bot_fours = []
bot_fives = []
bot_sixes = []
bot_sevens = []
bot_eights = []
bot_nines = []
bot_tens = []
bot_jacks = []
bot_queens = []
bot_kings = []
bot_aces = []

spades = []
hearts = []
diamonds = []
clubs = []

bot_spades = []
bot_hearts = []
bot_diamonds = []
bot_clubs = []

num_dict = {2:twos, 3:threes, 4:fours, 5:fives, 6:sixes, 7:sevens, 8:eights, 9:nines, 10:tens, 11:jacks, 12:queens, 13:kings, 14:aces}
bot_num_dict = {2:bot_twos, 3:bot_threes, 4:bot_fours, 5:bot_fives, 6:bot_sixes, 7:bot_sevens, 8:bot_eights, 9:bot_nines, 10:bot_tens, 11:bot_jacks, 12:bot_queens, 
                13:bot_kings, 14:bot_aces}

suit_dict = {1:spades, 2:hearts, 3:diamonds, 4:clubs}
bot_suit_dict = {1:bot_spades, 2:bot_hearts, 3:bot_diamonds, 4:bot_clubs}

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

#Deal Cards
def deal_card(deck):
    return deck.pop() if deck else None

#Assign Card Names
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

#Assign Suit Val
def suit_val(value):
    match value:
        case " of Spades":
            return 1
        case " of Hearts":
            return 2
        case " of Diamonds":
            return 3
        case " of Clubs":
            return 4

#get value for bet off suit
def suit_lens_(suit_lens):
    for i in range(len(suit_lens)):
        if suit_lens[i] == 4:
            return 500
        elif suit_lens[i] == 3 and suit_lens[i+1] == 2:
            return 400 
        elif suit_lens[i] == 3:
            return 300
        elif len(suit_lens) > 1 and suit_lens[i] == 2 and suit_lens[i+1] == 2:
            return 200
        elif suit_lens[i] == 2:
            return 100
        else:
            return 25

#Bot hand val
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

def straight_check(cards):
    player = sorted(cards, reverse=True)

    count = 0
    for i in range(len(player) - 1):
        if player_cards[i] - player_cards[i+1] == 1:
            count += 1

    if count >= 4:
        return True
    else:
        return False

#Bot bet amount
def bet_number(value, account):    
    chance = random.randint(1,100)
    if all_in == 1:
        if chance > 20:
            return "all in"
        else:
            return "fold"
    if 400 <= value <= 550:
        if 80 < chance < 101:
            return "all in"
        else:
            var = random.randint((int(.4*account)),int(.5*account))
            return var
    elif 300 <= value < 400:
        if 85 < chance < 101:
            return "all in"
        elif chance < 3:
            return "fold"
        else:
            var = random.randint((int(.3*account)),(int(.4*account)))
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

#print current best
def best(lens, suitlens, cards, hand):
    flush = False
    cards_sort = sorted(cards, reverse=True)
    player = sorted(suitlens, reverse=True)
    if player[0] == 5:
        flush = True
    if straight_check(cards) and flush == True and cards_sort[0] == 14:
        print('Current Best:')
        print('Royal Flush')
        win_val = 10
        return win_val
    elif straight_check(cards) and flush == True:
        print('Current Best:')
        print('Straight Flush')
        win_val = 9
        return win_val
    for i in range(len(lens)):
        if lens[i] == 4:
            print('Current Best:')
            print('Four of a kind')
            win_val = 8
            return win_val
        elif len(lens) > 2 and lens[i] == 3 and lens[i+1] == 2:
            print('Current Best:')
            print('Full House')
            win_val = 7
            return win_val
        elif flush == True:
            print('Current Best:')
            print('Flush')
            win_val = 6
            return win_val
        elif straight_check(cards):
            print('Current Best:')
            print('Straight')
            win_val = 5
            return win_val
        elif lens[i] == 3:
            print('Current Best:')
            print('Three of a kind')
            win_val = 4
            return win_val
        elif len(lens) > 2 and lens[i] == 2 and lens[i+1] == 2:
            print('Current Best:')
            print('Two Pair')
            win_val = 3
            return win_val
        elif lens[i] == 2:
            print('Current Best:')
            print('One pair')
            win_val = 2
            return win_val
        else:
            if player_names[0] > player_names[1]:
                print('Current Best:')
                print('High card:', card_name(hand[0]))
                win_val = 1
                return win_val
            else:
                print('Current Best:')
                print('High card:', card_name(hand[1]))
                win_val = 1
                return win_val


def win_check(player_val, bot_val):
    if player_val > bot_val:
        print('You Win!')
        print('Pot:',pot)
        balance_change(pot)
    elif player_val < bot_val:
        print('You Loose :(')
        balance_change(loose)
    else:
        if player_best[0] > bot_best[0]:
            print('You Win!')
            print('Pot:',pot)
            balance_change(pot)
        elif player_best[0] < bot_best[0]:
            print('You Loose :(')
            balance_change(loose)
        elif player_best[0] == bot_best[0] and player_best[1] > bot_best[1]:
            print('You Win!')
            print('Pot:',pot)
            balance_change(pot)
        elif player_best[0] == bot_best[0] and player_best[1] < bot_best[1]:
            print('You Loose :(')
            balance_change(loose)
        else:
            sort1 = sorted(player_names, reverse=True)
            sort2 = sorted(bot_names, reverse=True)
            if sort1[0] > sort2[0]:
                print('You Win!')
                print('Pot:',pot)
                balance_change(pot)
            elif sort1[0] < sort2[0]:
                print('You Loose :(')
                balance_change(loose)
            else:
                print('Tie')
                balance_change(pot/2)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PLAYER Player

player_cards = []
player_suits = []
player_names = []
#DEAL PLAYER CARDS
for i in range(2):
    playercards = deal_card(deck)
    player_names.append(playercards[0])
    player_suits.append(playercards[1])
    player_cards.append(playercards[0])

card_1 = str(card_name(player_names[0])) + str(player_suits[0])
card_2 = str(card_name(player_names[1])) + str(player_suits[1])

for n in player_names:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
player_best = []
for i in num_dict:
    length = len(num_dict[i])
    if length == 2:
        player_best.append(i)
    lens.append(length)
lens = [i for i in lens if i != 0]
player_best.sort(reverse=True)
lens.sort(reverse=True)

#suit vals
suit_value = []
for i in range(len(player_suits)):
    var1 = player_suits[i]
    var2 = suit_val(var1)
    suit_value.append(var2)

for n in suit_value:
    if n in suit_dict:
        suit_dict[n].append(n)

suit_lens = []
for i in suit_dict:
    length = len(suit_dict[i])
    suit_lens.append(length)
suit_lens = [i for i in suit_lens if i != 0]
suit_lens.sort(reverse=True)

print('Card 1:',card_1)
print('Card 2:',card_2)
print()

best(lens, suit_lens, player_cards, player_names)

#get bet amount
while True:
    if all_in == 1:
        break
    else:
        print('current balance is: ',balance)
        bet_amount_1 = input("bet amount?: ")
        if bet_amount_1.lower() == 'fold':
            balance_change(loose)
            quit()
        elif bet_amount_1.lower() == 'all in':
            total_bet = int(balance)
            all_in = 1
            break
        elif int(bet_amount_1) <= int(balance):
            total_bet = bet_amount_1
            break
        elif int(bet_amount_1) >= int(balance):
            print('Not enough balance')
        else:
            print('Try Something Real')
            


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#PLAYER Bot

bot_cards = []
bot_actual = []
bot_names = []
bot_suits = []
for i in range(2):
    botcards = deal_card(deck)
    bot_actual.append(botcards)
    bot_names.append(botcards[0])
    bot_suits.append(botcards[1])
    bot_cards.append(botcards[0])

#NUM LENS
for n in bot_names:
    if n in bot_num_dict:
        bot_num_dict[n].append(n)

bot_lens = []
bot_best = []
for i in bot_num_dict:
    length = len(bot_num_dict[i])
    if length == 2:
        bot_best.append(i)
    bot_lens.append(length)
bot_lens = [i for i in bot_lens if i != 0]
bot_best.sort(reverse=True)
bot_lens.sort(reverse=True)


#SUIT LENS
bot_suit_value = []
for i in range(len(bot_suits)):
    var1 = bot_suits[i]
    var2 = suit_val(var1)
    bot_suit_value.append(var2)

for n in bot_suit_value:
    if n in bot_suit_dict:
        bot_suit_dict[n].append(n)

bot_suit_lens = []
for i in bot_suit_dict:
    length = len(bot_suit_dict[i])
    bot_suit_lens.append(length)
bot_suit_lens = [i for i in bot_suit_lens if i != 0]
bot_suit_lens.sort(reverse=True)

hand_int = hand_value(lens)
suit_value = suit_lens_(bot_suit_lens)
total_value = hand_int + suit_value
bot_bet = bet_number(hand_int, bot1_bal)

#print('bot Cards:',bot_actual)
#print(bot_num_dict)
#print(bot_suit_dict)
#print('bot Bet:',bot_bet)
#print()

if bot_bet == "fold":
    print('Bot Folds')
    print('You Win:',pot)
    balance_change(pot)
    quit()
elif bot_bet == "all in":
    total_bot_bet = bot1_bal
else:
    total_bot_bet += bot_bet

pot = total_bet + total_bot_bet
print('Pot:',pot)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#FLOP Player

flop_suits = []
flop_names = []
#DEAL FLOP
for i in range(3):
    flopcards = deal_card(deck)
    flop_names.append(flopcards[0])
    flop_suits.append(flopcards[1])
    player_cards.append(flopcards[0])
    bot_cards.append(flopcards[0])

flop_1 = str(card_name(flop_names[0])) + str(flop_suits[0])
flop_2 = str(card_name(flop_names[1])) + str(flop_suits[1])
flop_3 = str(card_name(flop_names[2])) + str(flop_suits[2])

for n in flop_names:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
player_best = []
for i in num_dict:
    length = len(num_dict[i])
    if length == 2:
        player_best.append(i)
    lens.append(length)
lens = [i for i in lens if i != 0]
player_best.sort(reverse=True)
lens.sort(reverse=True)

#suit vals
suit_value = []
for i in range(len(player_suits)):
    var1 = player_suits[i]
    var2 = suit_val(var1)
    suit_value.append(var2)

for n in suit_value:
    if n in suit_dict:
        suit_dict[n].append(n)

suit_lens = []
for i in suit_dict:
    length = len(suit_dict[i])
    suit_lens.append(length)
suit_lens = [i for i in suit_lens if i != 0]
suit_lens.sort(reverse=True)

print('Card 1:',card_1)
print('Card 2:',card_2)
print()
print('Flop:')
print()
print(flop_1)
print(flop_2)
print(flop_3)
print()
best(lens, suit_lens, player_cards, player_names)

#get bet amount
while True:
    if all_in == 1:
        break
    else:
        print('current balance is: ',balance)
        bet_amount_2 = input("bet amount?: ")
        if bet_amount_2.lower() == 'fold':
            balance_change(loose)
            quit()
        elif bet_amount_2.lower() == 'all in':
            total_bet = int(balance)
            all_in = 1
            break
        elif int(bet_amount_2) <= int(balance):
            total_bet = bet_amount_1 + bet_amount_2
            break
        elif int(bet_amount_2) >= int(balance):
            print('Not enough balance')
        else:
            print('Try Something Real')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#FLOP Bot

#NUM LENS
for n in flop_names:
    if n in bot_num_dict:
        bot_num_dict[n].append(n)

bot_lens = []
bot_best = []
for i in bot_num_dict:
    length = len(bot_num_dict[i])
    if length == 2:
        bot_best.append(i)
    bot_lens.append(length)
bot_lens = [i for i in bot_lens if i != 0]
bot_best.sort(reverse=True)
bot_lens.sort(reverse=True)

#SUIT LENS
bot_suit_value = []
for i in range(len(flop_suits)):
    var1 = flop_suits[i]
    var2 = suit_val(var1)
    bot_suit_value.append(var2)

for n in bot_suit_value:
    if n in bot_suit_dict:
        bot_suit_dict[n].append(n)

bot_suit_lens = []
for i in bot_suit_dict:
    length = len(bot_suit_dict[i])
    bot_suit_lens.append(length)
bot_suit_lens = [i for i in bot_suit_lens if i != 0]
bot_suit_lens.sort(reverse=True)

hand_int = hand_value(lens)
suit_value = suit_lens_(bot_suit_lens)
total_value = hand_int + suit_value
bot_bet = bet_number(hand_int, bot1_bal)

#print('bot Cards:',bot_actual)
#print(bot_num_dict)
#print(bot_suit_dict)
#print('bot Bet:',bot_bet)
#print()

if bot_bet == "fold":
    print('Bot Folds')
    print('You Win:',pot)
    balance_change(pot)
    quit()
elif bot_bet == "all in":
    total_bot_bet = bot1_bal
else:
    total_bot_bet += bot_bet

pot = total_bet + total_bot_bet
print('Pot:',pot)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TURN Player

turn_suit = []
turn_name = []
#DEAL TURN
turncard = deal_card(deck)
turn_name.append(turncard[0])
turn_suit.append(turncard[1])
player_cards.append(turncard[0])
bot_cards.append(turncard[0])

turn = str(card_name(turn_name[0])) + str(turn_suit[0])

for n in turn_name:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
player_best = []
for i in num_dict:
    length = len(num_dict[i])
    if length == 2:
        player_best.append(i)
    lens.append(length)
lens = [i for i in lens if i != 0]
player_best.sort(reverse=True)
lens.sort(reverse=True)

#suit vals
suit_value = []
for i in range(len(player_suits)):
    var1 = player_suits[i]
    var2 = suit_val(var1)
    suit_value.append(var2)

for n in suit_value:
    if n in suit_dict:
        suit_dict[n].append(n)

suit_lens = []
for i in suit_dict:
    length = len(suit_dict[i])
    suit_lens.append(length)
suit_lens = [i for i in suit_lens if i != 0]
suit_lens.sort(reverse=True)

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
best(lens, suit_lens, player_cards, player_names)

#get bet amount
while True:
    if all_in == 1:
        break
    else:
        print('current balance is: ',balance)
        bet_amount_3 = input("bet amount?: ")
        if bet_amount_3.lower() == 'fold':
            balance_change(loose)
            quit()
        elif bet_amount_3.lower() == 'all in':
            total_bet = int(balance)
            all_in = 1
            break
        elif int(bet_amount_3) <= int(balance):
            total_bet = bet_amount_1 + bet_amount_2 + bet_amount_3
            break
        elif int(bet_amount_3) >= int(balance):
            print('Not enough balance')
        else:
            print('Try Something Real')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TURN Bot

#NUM LENS
for n in turn_name:
    if n in bot_num_dict:
        bot_num_dict[n].append(n)

bot_lens = []
bot_best = []
for i in bot_num_dict:
    length = len(bot_num_dict[i])
    if length == 2:
        bot_best.append(i)
    bot_lens.append(length)
bot_lens = [i for i in bot_lens if i != 0]
bot_best.sort(reverse=True)
bot_lens.sort(reverse=True)

#SUIT LENS
bot_suit_value = []
for i in range(len(turn_suit)):
    var1 = turn_suit[i]
    var2 = suit_val(var1)
    bot_suit_value.append(var2)

for n in bot_suit_value:
    if n in bot_suit_dict:
        bot_suit_dict[n].append(n)

bot_suit_lens = []
for i in bot_suit_dict:
    length = len(bot_suit_dict[i])
    bot_suit_lens.append(length)
bot_suit_lens = [i for i in bot_suit_lens if i != 0]
bot_suit_lens.sort(reverse=True)

hand_int = hand_value(lens)
suit_value = suit_lens_(bot_suit_lens)
total_value = hand_int + suit_value
bot_bet = bet_number(hand_int, bot1_bal)

#print('bot Cards:',bot_actual)
#print(bot_num_dict)
#print(bot_suit_dict)
#print('bot Bet:',bot_bet)
#print()

if bot_bet == "fold":
    print('Bot Folds')
    print('You Win:',pot)
    balance_change(pot)
    quit()
elif bot_bet == "all in":
    total_bot_bet = bot1_bal
else:
    total_bot_bet += bot_bet

pot = total_bet + total_bot_bet
print('Pot:',pot)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#RIVER Player

river_suit = []
river_name = []
#DEAL RIVER
rivercard = deal_card(deck)
river_name.append(rivercard[0])
river_suit.append(rivercard[1])
player_cards.append(rivercard[0])
bot_cards.append(rivercard[0])

river = str(card_name(river_name[0])) + str(river_suit[0])

for n in river_name:
    if n in num_dict:
        num_dict[n].append(n)

#create length lists to check for pairs and whatnot
lens = []
player_best = []
for i in num_dict:
    length = len(num_dict[i])
    if length == 2:
        player_best.append(i)
    lens.append(length)
lens = [i for i in lens if i != 0]
player_best.sort(reverse=True)
lens.sort(reverse=True)

#suit vals
suit_value = []
for i in range(len(player_suits)):
    var1 = player_suits[i]
    var2 = suit_val(var1)
    suit_value.append(var2)

for n in suit_value:
    if n in suit_dict:
        suit_dict[n].append(n)

suit_lens = []
for i in suit_dict:
    length = len(suit_dict[i])
    suit_lens.append(length)
suit_lens = [i for i in suit_lens if i != 0]
suit_lens.sort(reverse=True)

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
best(lens, suit_lens, player_cards, player_names)

#get bet amount
while True:
    if all_in == 1:
        break
    else:
        print('current balance is: ',balance)
        bet_amount_4 = input("bet amount?: ")
        if bet_amount_4.lower() == 'fold':
            balance_change(loose)
            quit()
        elif bet_amount_4.lower() == 'all in':
            total_bet = int(balance)
            all_in = 1
            break
        elif int(bet_amount_4) <= int(balance):
            total_bet = bet_amount_1 + bet_amount_2 + bet_amount_3 + bet_amount_4
            break
        elif int(bet_amount_4) >= int(balance):
            print('Not enough balance')
        else:
            print('Try Something Real')

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#RIVER Bot

#NUM LENS
for n in river_name:
    if n in bot_num_dict:
        bot_num_dict[n].append(n)

bot_lens = []
bot_best = []
for i in bot_num_dict:
    length = len(bot_num_dict[i])
    if length == 2:
        bot_best.append(i)
    bot_lens.append(length)
bot_lens = [i for i in bot_lens if i != 0]
bot_best.sort(reverse=True)
bot_lens.sort(reverse=True)

#SUIT LENS
bot_suit_value = []
for i in range(len(river_suit)):
    var1 = river_suit[i]
    var2 = suit_val(var1)
    bot_suit_value.append(var2)

for n in bot_suit_value:
    if n in bot_suit_dict:
        bot_suit_dict[n].append(n)

bot_suit_lens = []
for i in bot_suit_dict:
    length = len(bot_suit_dict[i])
    bot_suit_lens.append(length)
bot_suit_lens = [i for i in bot_suit_lens if i != 0]
bot_suit_lens.sort(reverse=True)

hand_int = hand_value(lens)
suit_value = suit_lens_(bot_suit_lens)
total_value = hand_int + suit_value
bot_bet = bet_number(hand_int, bot1_bal)

#print('bot Cards:',bot_actual)
#print(bot_num_dict)
#print(bot_suit_dict)
#print('bot Bet:',bot_bet)
#print()

if bot_bet == "fold":
    print('Bot Folds')
    print('You Win:',pot)
    balance_change(pot)
    quit()
elif bot_bet == "all in":
    total_bot_bet = bot1_bal
else:
    total_bot_bet += bot_bet

pot = total_bet + total_bot_bet
print('Pot:',pot)

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
print()
print(bot_actual)

print('player:')
print()
player_win = best(lens, suit_lens, player_cards, player_names)
print('Bot:')
print()
bot_win = best(bot_lens, bot_suit_lens, bot_cards, bot_names)
print()
win_check(player_win, bot_win)
