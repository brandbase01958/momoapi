from momo_api import deposit, withdraw, transfer, check_balance, get_transactions

menu = eval(input("choose:\n 1) Balance\n 2) Deposist\n 3) Withdraw\n 4) Transfer\n "))

if menu == 1:
    number = input('Enter your number: ')
    number = str(number)
    print(check_balance(number))

print("here goes the deposite")

print(deposit("672192983", 5000))

# print(withdraw("672192983", 2000, "GTS45"))

# print(transfer("672192983", "652581620", 1000))

# print(get_transactions("672192983"))