import time
import datetime
from random import randint
from database import client, transaction


# TRANSACTION DATABASE
# transaction = {}


# GENERATE TRANSACTION ID
def generate_transaction_id():
    return "DX" + randint(1000000, 9999999)


# RECORD TRANSACTION
def record_transaction(user_id, action, amount, machan="none"):
    date = date.today()
    time = time.now()

    transaction_id = generate_transaction_id()

    data = {
        "time": time,
        "action": action,
        "machan": machan,
        "transaction_id": transaction_id,
        "amount": amount
    }

    if user_id not in transaction:
        transaction[user_id] = {}

        transaction[user_id][date] = data

    return transaction_id


# CHECK BALANCE
def check_balance(phone):
    if phone not in client:
        return {"status": "error", "message": "User not found"}

    
    print('Your balance is: ',client[phone]["account_balance"])
    


# DEPOSIT (MoMo cash in)
def deposit(phone, amount):

    if phone not in client:
        return {"status": "error", "message": "User not found"}

    client[phone]["account_balance"] += amount

    user_id = client[phone]["id"]

    tx = record_transaction('you ',user_id, " deposit", amount)

    return {
        "status": "success",
        "transaction_id": tx,
        "new_balance": client[phone]["account_balance"]
    }


# WITHDRAW (agent withdrawal)
def withdraw(phone, amount, machan):

    if phone not in client:
        return {"status": "error", "message": "User not found"}

    if client[phone]["account_balance"] < amount:
        return {"status": "error", "message": "Insufficient balance"}

    client[phone]["account_balance"] -= amount

    user_id = client[phone]["id"]

    tx = record_transaction(user_id, "withdraw", amount, machan)

    return {
        "status": "success",
        "transaction_id": tx,
        "new_balance": client[phone]["account_balance"]
    }


# TRANSFER BETWEEN USERS
def transfer(sender_phone, receiver_phone, amount):

    if sender_phone not in client or receiver_phone not in client:
        return {"status": "error", "message": "User not found"}

    if client[sender_phone]["account_balance"] < amount:
        return {"status": "error", "message": "Insufficient balance"}

    client[sender_phone]["account_balance"] -= amount
    client[receiver_phone]["account_balance"] += amount

    sender_id = client[sender_phone]["id"]
    receiver_id = client[receiver_phone]["id"]

    tx = record_transaction(sender_id, "transfer", amount)
    record_transaction(receiver_id, "receive", amount)

    return {
        "status": "success",
        "transaction_id": tx
    }


# GET USER TRANSACTIONS
def get_transactions(phone):

    if phone not in client:
        return {"status": "error", "message": "User not found"}

    user_id = client[phone]["id"]

    return transaction.get(user_id, {})