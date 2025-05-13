import random
import time
import re

#get ball spin
ball = random.randint(0,36)

#var for loosing
var = 0

#lists for each number
green = [0]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

#Read balance file
try:
    with open('account_balance.txt', 'rb') as file:
        content = file.read()  # Read the entire file content as bytes
        balance = ''.join(re.findall(r'\d+', content.decode('utf-8')))
    print(f"Current Balance: {balance}")
except FileNotFoundError:
    print("GO TO THE CASINO")
    quit()

#Write to balance file
def balance_change(bal_change):
    n_balance = (bal_change + (int(balance) - bet_amount))
    temp = ('Balance =', n_balance)
    write = str(temp).replace("'",'').replace(',','').replace('(','').replace(')','')
    with open('account_balance.txt', 'w') as file:
        file.write(write)

#find if even
def isEven(number):
    remainder = number % 2
    if remainder > 0:
        return False
    else:
        return True

def spin(a):
    print("Spinning...")
    time.sleep(int(a))
    print(".")
    time.sleep(int(a))
    print(".")
    time.sleep(int(a))
    print(".")
    time.sleep(int(a))

#get bet amount
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

while True:

    bet = input('bet on?: ').lower()

    if bet.isdigit() and 0 < int(bet) < 37:
        bet = int(bet)
        spin(1)
        print('Ball landed on:', ball)
        if bet == ball:
            print('You Win!')
            print('Winnings:', bet_amount * 35)
            money = (bet_amount * 35)
            balance_change(money)
            print("New Balance:",((int(balance) - bet_amount) + money))
            break
        else:
            print('You Loose :(')
            balance_change(var)
            print("New Balance:",(int(balance) - bet_amount))
            break
    else:

        #match case for choosing bets
        match bet:
            #Red Case
            case 'red':
                money = (bet_amount * 2)
                spin(1)
                print('Ball landed on:', ball)
                if ball in red:
                    print('You Win!')
                    print('Winnings: ', bet_amount * 2)
                    balance_change(money)
                    print("New Balance:",((int(balance) - bet_amount) + money))
                    break
                else:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))

                    break
            #Black Case
            case 'black':
                money = (bet_amount * 2)
                spin(1)
                print('Ball landed on:', ball)
                if ball in black:
                    print('You Win!')
                    print('Winnings: ', bet_amount * 2)
                    balance_change(money)
                    print("New Balance:",((int(balance) - bet_amount) + money))
                    break
                else:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))
                    break
            #Even Case
            case 'even':
                money = (bet_amount * 2)
                spin(1)
                print('Ball landed on:', ball)
                if isEven(ball) == True and ball > 0:
                    print('You Win!')
                    print('Winnings:', bet_amount * 2)
                    balance_change(money)
                    print("New Balance:",((int(balance) - bet_amount) + money))
                    break
                elif isEven(ball) == True and ball == 0:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))
                    break
                else:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))
                    break
            #Odd Case
            case 'odd':
                money = (bet_amount * 2)
                spin(1)
                print('Ball landed on:', ball)
                if isEven(ball) == False:
                    print('You Win!')
                    print('Winnings:', bet_amount * 2)
                    balance_change(money)
                    print("New Balance:",((int(balance) - bet_amount) + money))
                    break
                elif isEven(ball) == True and ball == 0:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))
                    break
                else:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))
                    break
            #"0" Case
            case '0':
                money = (bet_amount * 35)
                spin(1)
                print('Ball landed on:', ball)
                if ball == 0:
                    print('You Win!')
                    print('Winnings:', bet_amount * 35)
                    balance_change(money)
                    print("New Balance:",((int(balance) - bet_amount) + money))
                    break
                else:
                    print('You Loose :(')
                    balance_change(var)
                    print("New Balance:",(int(balance) - bet_amount))
                    break
            #"Not an Input" Case
            case _:
                print("unrecognized input")