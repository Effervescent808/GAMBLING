import random
import time
import re

try:
    with open('account_balance.txt', 'rb') as file:
        content = file.read()  # Read the entire file content as bytes
        balance = ''.join(re.findall(r'\d+', content.decode('utf-8')))
    print(f"Current Balance: {balance}")
except FileNotFoundError:
    print("GO TO THE CASINO")
    quit()




def get_slots(slots):
    for i in range(len(slots)):
        slots[i] = random.randint(1,9)

#balance change function
def balance_change(bal_change):
    n_balance = (bal_change + (int(balance) - machine))
    temp = ('Balance =', n_balance)
    write = str(temp).replace("'",'').replace(',','').replace('(','').replace(')','')
    with open('account_balance.txt', 'w') as file:
        file.write(write)

def win(mult):
    money = machine * mult
    balance_change(money)
    print('Winnings:', money)
    print('New Balance:',(money + (int(balance) - machine)))

#play spin animation
def spin(times):
    for i in range(1,times):
        print(".")
        time.sleep(.05)
    for i in range(1,times):
        print(". .")
        time.sleep(.05)
    for i in range(1,times):
        print(". . .")
        time.sleep(.05)

while True:
    try:
        machine = input("Which Slot Machine? (10/50/100/500/1000): ")
        match machine:
            case "10":
                if int(balance) >= 10:
                    machine = 10
                    break
                else:
                    print('Not enough Balance')
                    print()
            case "50":
                if int(balance) >= 50:
                    machine = 50
                    break
                else:
                    print('Not enough Balance')
                    print()
            case "100":
                if int(balance) >= 100:
                    machine = 100
                    break
                else:
                    print('Not enough Balance')
                    print()
            case "500":
                if int(balance) >= 500:
                    machine = 500
                    break
                else:
                    print('Not enough Balance')
                    print()
            case "1000":
                if int(balance) >= 1000:
                    machine = 1000
                    break
                else:
                    print('Not enough Balance')
                    print()
    except ValueError:
        print("Enter a machine type")
        print()

#empty slots
slot_1=''
slot_2=''
slot_3=''
slot_4=''
slot_5=''
slot_6=''
slot_7=''
slot_8=''
slot_9=''

#create lists
row_1 = [slot_1, slot_2, slot_3]
row_2 = [slot_4, slot_5, slot_6]
row_3 = [slot_7, slot_8, slot_9]

#assign lists

get_slots(row_1)
get_slots(row_2)
get_slots(row_3)

s_row_1 = str(row_1).replace('[','').replace(']','').replace(',','')
s_row_2 = str(row_2).replace('[','').replace(']','').replace(',','')
s_row_3 = str(row_3).replace('[','').replace(']','').replace(',','')

#ANIMATION
spin(10)
print("-----")
time.sleep(.2)
print(s_row_1)
time.sleep(.1)
print(s_row_2)
time.sleep(.1)
print(s_row_3)

#ADD MATCH CASES FOR EACH COMBO, basically tick tack toe and side by sides
#don't forget about each row, winners could be in multiple rows

mult = 0

#row 1 if elses
if row_1[0] == row_1[1] == row_1[2]:
    mult += 50
elif row_1[0] == row_1[1]:
    mult += 5
elif row_1[1] == row_1[2]:
    mult += 5

#row 2 if elses
if row_2[0] == row_2[1] == row_2[2]:
    mult += 50
elif row_2[0] == row_2[1]:
    mult += 5
elif row_2[1] == row_2[2]:
    mult += 5

#row 3 if elses
if row_3[0] == row_3[1] == row_3[2]:
    mult += 50
elif row_3[0] == row_3[1]:
    mult += 5
elif row_3[1] == row_3[2]:
    mult += 5

if mult == 0:
    print('Nothing :(')
    win(mult)
elif 0 < mult < 10:
    print('Winner!')
    win(mult)
elif 9 < mult < 20:
    print('Big Win!')
    win(mult)
elif 19 < mult < 50:
    print('Mega Win!')
    win(mult)
elif 49 < mult < 100:
    print('Jackpot!')
    win(mult)
elif 99 < mult < 200:
    print('Mega Jackpot!')
    win(mult)
elif 199 < mult:
    print('Ultra Jackpot')
    win(mult)