import random
import re

#var for loosing 
var = 0

#get balance
try:
    with open('account_balance.txt', 'rb') as file:
        content = file.read()  # Read the entire file content as bytes
        balance = ''.join(re.findall(r'\d+', content.decode('utf-8')))
    print(f"Current Balance: {balance}")
except FileNotFoundError:
    print("GO TO THE CASINO")
    quit()

print()
print("I love BlackJack")
print()

#set aces list
ace = 'ace'
aces = []

#rename cards
def card_name(value):
    if value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    elif value == 1:
        aces.append(ace)
        return "Ace"
    else:
        return value

#balance change function
def balance_change(bal_change):
    n_balance = (bal_change + (int(balance) - bet_amount))
    temp = ('Balance =', n_balance)
    write = str(temp).replace("'",'').replace(',','').replace('(','').replace(')','')
    with open('account_balance.txt', 'w') as file:
        file.write(write)

#Get bet amount
while True:
    try:
        print('current balance is: ',balance)
        bet_amount = int(input("bet amount?: "))
        if bet_amount <= int(balance):
            break
        else:
            print('Not enough balance')
    except ValueError:
        print("Please enter a number")


#set cards 1 and 2
Card1 = random.randint(1, 13)
Card2 = random.randint(1, 13)

Card1_name = card_name(Card1)
Card2_name = card_name(Card2)

Card1_value = 10 if Card1 > 10 else Card1
Card1_value = 11 if Card1 == 1 else Card1_value
Card2_value = 10 if Card2 > 10 else Card2
Card2_value = 11 if Card2 == 1 else Card2_value

player_total = Card1_value + Card2_value

print(f"First Card: {Card1_name}")
print(f"Second Card: {Card2_name}")
print()
print(f"Player Total: {player_total}")
print()


Card3=''

#play BLACKJACK
while player_total < 99:

    hos = input("Hit or Stay?: ")

    if hos.lower() == "hit":
        Card3 = random.randint(1,13)
        Card3_name = card_name(Card3)
        Card3_value = 10 if Card3 > 10 else Card3
        Card3_value = 11 if Card3 == 1 else Card3_value
        player_total += Card3_value

        if player_total > 21 and len(aces) > 0:
            player_total -= 10
            aces.pop(0)
        elif player_total > 21 and len(aces) == 0:
            print()
            print("New Card: ",Card3_name)
            print("New Total: ",player_total)
            print()
            print("You Bust")
            break

        print()
        print("New Card: ",Card3_name)
        print("New Total: ",player_total)
        print()
    else:
        break

dealer = random.randint(17,23)

print()
print("The dealer had: ",dealer)
print()
money = (bet_amount * 2)
if player_total > 21 and dealer > 21:
    print("Push!")
elif player_total > 21 and dealer <= 21:
    print("You Lose :(")
    balance_change(var)
    print("New Balance:",(int(balance) - bet_amount))
elif dealer > 21:
    print("You Win!")
    print('Winnings:', bet_amount * 2)
    balance_change(money)
    print("New Balance:",(int(balance) + bet_amount))
elif player_total == dealer:
    print("Push!")
elif player_total > dealer:
    print('You Win!')
    print('Winnings:', bet_amount * 2)
    balance_change(money)
    print("New Balance:",(int(balance) + bet_amount))
else:
    print("You Lose :(")
    balance_change(var)
    print("New Balance:",(int(balance) - bet_amount))