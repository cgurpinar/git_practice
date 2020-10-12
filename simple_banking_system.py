import sqlite3
from random import randint

conn = sqlite3.connect("card.s3db")
cur = conn.cursor()
tmp_validate_dict = []


def create_account():
    # CARD_NUMBER
    first_six = "400000"
    generate = first_six + str(randint(100000000, 999999999))
    generate += str(find_checksum(generate))

    # PIN
    pin = randint(1000, 9999)

    # add to db (id -> auto_inc, balance -> already default 0)
    cur.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (generate, pin))
    conn.commit()
    return generate, pin


def find_checksum(card_number):                 # FIND LAST DIGIT WITH LUHN'S ALGORITHM
    temp = [int(card_number[i]) * 2 if i % 2 == 0 else int(card_number[i]) for i in range(len(str(card_number)))]
    temp = [int(temp[i]) - 9 if int(temp[i]) > 9 else int(temp[i]) for i in range(len(temp))]

    total = 0
    for number in temp:
        total += number

    if total % 10 == 0:
        checksum = 0
    else:
        num = 10 - total % 10
        checksum = num

    return str(checksum)


def check_luhn_algo(card_number):               # validate card number against Luhn's Algorithm
    cn_last_number = str(card_number)[-1]
    checksum = find_checksum(card_number[:-1])
    return True if str(checksum) == str(cn_last_number) else False


def check_card(card_number):                    # is card exists?
    check = cur.execute(f"SELECT EXISTS(SELECT number FROM card WHERE number = {card_number})")
    for con in check:
        check = con[0]
    return bool(check)


def check_acc(card_number, u_pin):              # is acc exists?
    if check_card(card_number):
        c_pin = cur.execute(f"SELECT pin FROM card WHERE number = {card_number}")
        for c in c_pin:
            c_pin = c[0]
        return True if str(u_pin) == str(c_pin) else False


def del_acc(card_number):
    cur.execute(f'DELETE FROM card WHERE number = {card_number}')
    conn.commit()


def add_income(card_number, income):
    acc_balance = cur.execute(f"SELECT balance FROM card WHERE number = {card_number}" )
    for accb in acc_balance:
        acc_balance = accb[0]
    sql = "UPDATE card SET balance = ? WHERE number = ?"
    cur.execute(sql, ((int(acc_balance) + int(income)), card_number))
    conn.commit()
    return "Income was added!"


def check_balance(card_number, transfer):
    acc_balance = cur.execute(f'SELECT balance FROM card WHERE number = {card_number}')
    for acc in acc_balance:
        acc_balance = acc[0]
    return True if int(acc_balance) >= int(transfer) else False


def m_transfer(card_number, transfer, t_card_number):
    b1, b2 = cur.execute(f'SELECT balance FROM card WHERE (number = {str(card_number)} OR number = {str(t_card_number)})')
    for b in b1:
        balance = b
    for b in b2:
        t_balance = b
    cur.execute(f"UPDATE card SET balance = {int(balance) - int(transfer)} WHERE number = {card_number}")
    cur.execute(f"UPDATE card SET balance = {int(t_balance) + int(transfer)} WHERE number = {t_card_number}")
    conn.commit()
    return "Success!"


def show_balance(card_number):
    balance = cur.execute('SELECT balance FROM card WHERE number = ?', card_number)
    for bal in balance:
        return bal[0]


exit_ = False
log_out = False

while not exit_:
    print("1. Create an account\n2. Log into account\n0. Exit")

    u_choice = input()

    if u_choice == "0":
        print("Bye!")
        exit_ = True
    elif u_choice == "1":
        card_number, pin = create_account()
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card PIN:")
        print(pin)

    elif u_choice == "2":
        print("Enter your card number:")
        u_card_number = str(input())
        print("Enter your PIN:")
        u_pin = int(input())

        if check_luhn_algo(u_card_number) and check_acc(u_card_number, u_pin):
            print("\nYou have successfully logged in!")

            while not log_out:
                print("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                u_choice = input()

                if u_choice == "1":             # Balance
                    print("Balance: {}".format(show_balance(u_card_number)))

                elif u_choice == "2":           # Add Income
                    a_income = int(input("Enter income:"))
                    add_income(u_card_number, a_income)

                elif u_choice == "3":           # Do Transfer
                    print("Transfer")
                    print("Enter card number:")
                    t_card_number = str(input())
                    if check_luhn_algo(t_card_number):
                        if check_card(t_card_number):
                            print("Enter how much money you want to transfer:")
                            t_amount = str(input())

                            if check_balance(u_card_number, t_amount):
                                m_transfer(u_card_number, t_amount, t_card_number)
                            else:
                                print("Not enough money!")
                        else:
                            print("Such a card does not exist.")
                    else:
                        print('Probably you made mistake in card number. Please try again!')

                elif u_choice == "4":           # Close Account
                    del_acc(u_card_number)
                    print("The account has been closed!")
                    log_out = True

                elif u_choice == "5":           # Log out
                    log_out = True
                    print("You have successfully logged out!")

                elif u_choice == "0":           # Exit
                    print("Bye!")
                    log_out = True
                    exit_ = True

        else:
            print("Wrong card number or PIN!")

conn.commit()       # Save database changes
conn.close()        # End the connection
