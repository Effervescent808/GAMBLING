import random
import re

#get balance
with open('account_balance.txt', 'rb') as file:
    balance = ''.join(re.findall(r'\d+', str(file.readlines())))

#var for loosing 
var = 0

#balance change function
def balance_change(bal_change):
    n_balance = (bal_change + (int(balance) - total_bet))
    temp = ('Balance =', n_balance)
    write = str(temp).replace("'",'').replace(',','').replace('(','').replace(')','')
    with open('account_balance.txt', 'w') as file:
        file.write(write)

def get_suit(number):
    var = random.randint(1,int(number))
    if var == 1:
        return " of Clubs"
    elif var == 2:
        return " of Spades"
    elif var == 3:
        return " of Hearts"
    elif var == 4:
        return " of Diamonds"
    else:
        return "Error"

#get card names
def card_name(value):
    if value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    elif value == 1:
        return "Ace"
    else:
        return value

#decide cards
card_1 = random.randint(1,13)
card_2 = random.randint(1,13)

#card names
card_1_name = card_name(card_1)
card_2_name = card_name(card_2)

#card suits
card_1_suit = get_suit(4)
card_2_suit = get_suit(4)

card_1_actual = str(card_1_name) + str(card_1_suit)
card_2_actual = str(card_2_name) + str(card_2_suit)

print("First Card:",card_1_actual)
print("Second Card:",card_2_actual)
print()

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

#decide flop
flop_1 = random.randint(1,13)
flop_2 = random.randint(1,13)
flop_3 = random.randint(1,13)

#flop names
flop_1_name = card_name(flop_1)
flop_2_name = card_name(flop_2)
flop_3_name = card_name(flop_3)

#flop suits
flop_1_suit = get_suit(4)
flop_2_suit = get_suit(4)
flop_3_suit = get_suit(4)

#flop actuals
flop_1_actual = str(flop_1_name) + str(flop_1_suit)
flop_2_actual = str(flop_2_name) + str(flop_2_suit)
flop_3_actual = str(flop_3_name) + str(flop_3_suit)

print()
print("Flop:")
print()
print(flop_1_actual)
print(flop_2_actual)
print(flop_3_actual)
print() 
print("Your cards:")
print(card_1_actual)
print(card_2_actual)
print()

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

turn_1 = random.randint(1,13)

turn_1_name = card_name(turn_1)

turn_1_suit = get_suit(4)

turn_1_actual = str(turn_1_name) + str(turn_1_suit)

print()
print("Turn:")
print()
print(turn_1_actual)
print()
print(flop_1_actual)
print(flop_2_actual)
print(flop_3_actual)
print() 
print("Your cards:")
print(card_1_actual)
print(card_2_actual)
print()