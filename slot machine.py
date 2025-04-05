# slot machine
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return[random.choice(symbols) for symbol in range(3)]  # list comprehension to return a random choice in symbol

def print_roll(row):
    print("*************")
    print(" | ".join(row))
    print("*************")


def get_payout(row, bet):
    if  row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        if row[0] == "🍉":
            return bet * 4
        if row[0] == "🍋":
            return bet * 5
        if row[0] == "🔔":
            return bet * 10
        if row[0] == "⭐":
            return bet * 10
    return 0

def main():
    balance = 100

    print("****************************************")
    print("Welcome To Rahh-_- Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("****************************************")

    while balance > 0:
        print(F"current balance: £{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Enter a valid number")
            continue # continue skips the firsts iteration and start from the beginning

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds!!")
            continue

        if bet <= 0 :
            print("Bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("spinning......\n")
        print_roll(row)

        pay_out = get_payout(row, bet)
        if pay_out > 0:
            print(F"You won £{pay_out}")
        else:
            print("Sorry You lost this round!!")

        balance += pay_out

        play_again = input("Do you want to spin again(Y/N): ").upper()
        if play_again != "Y":
            break
    print("*******************************************")
    print(F"Game Over your final balance is £{balance}")
    print("*******************************************")

if __name__ ==  "__main__":
    main()