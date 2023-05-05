import pickle
import pandas as pd
import json
import requests
import datetime

api_key = "ST13N47WPA7YZFEHVT5WXEQTTWFRHNPRQI"
url = "https://api.etherscan.io/api"
random_state = 27

def wei_to_eth(wei):
    return int(wei) / 10**18

def get_balance(address):
    """
    Funtion return the Eth balance of an a given address

    >>> get_balance('0x0000000000000000000000000000000000000000')
    0.00897765567

    """
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }

    # Make a GET request with the URL and query parameters
    response = requests.get(url, params=params)

    # Print the response content
    return round(wei_to_eth(response.json()['result']),5)

def get_Erc20_transaction_history(address):

    params = {
        "module": "account",
        "action": "tokentx",
        "address": address,
        "page": 1,
        "offset": 100,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": api_key
    }



    
    response = requests.get(url, params=params).json()
    return response['result']

def calculate_txn_day_ratio(txn_history):
    # Convert timestamps to datetime objects and sort transactions by timestamp
    transactions = sorted(
        [datetime.datetime.fromtimestamp(int(txn['timeStamp'])) for txn in txn_history]
    )
    
    # Calculate the number of days between the earliest and latest transactions
    if len(txn_history) > 0:
        delta_days = (transactions[-1] - transactions[0]).days
    else:
        return 0
    
    # Calculate the transaction-day ratio
    if delta_days == 0:
        txn_day_ratio = len(transactions)
    else:
        txn_day_ratio = len(transactions) / delta_days
        
    return round(txn_day_ratio,3)

def get_wallet_age(history: list[dict]):
    if len(history) > 0:
        creation_time = int(history[0]['timeStamp'])
        creation_date = datetime.datetime.fromtimestamp(creation_time).date()
        current_date = datetime.date.today()
        wallet_age = (current_date - creation_date).days
        return wallet_age
    else:
        return 0

def to_and_from(history:list[dict],address):
    from_count = 0
    to_count = 0
    for transactions in history:
        if transactions['from'] == address:
            from_count +=1
        else:
            to_count += 1
    return from_count, to_count



info = []
def main(address):
    Erc_20_history = get_Erc20_transaction_history(address)
    
    tdr  = calculate_txn_day_ratio(Erc_20_history)
    
    eth_balance = get_balance(address)

    wallet_age = get_wallet_age(Erc_20_history)

    from_count, to_count = to_and_from(Erc_20_history,address)

    row = [eth_balance,tdr,wallet_age,from_count,to_count]

    info.append(row)


address = input('Enter an Eth Address: ')
main(address)

columns = ['balance','TDR','Wallet_Age(Days)','From_Count','To_Count']
address_metrics = pd.DataFrame(info,columns=columns)


classes = {
    1:'2-3 weeks',
    2: '3-4 weeks',
    3: 'Less than a week',
    4:'Over 4 weeks'}

with open('model_weights/rfc.pkl', 'rb') as f:
    rfc = pickle.load(f)

y_pred = rfc.predict(address_metrics)

print(classes[y_pred.tolist()[0]],y_pred)
