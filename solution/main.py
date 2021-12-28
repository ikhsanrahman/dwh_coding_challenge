import json
import os
import pandas as pd
import glob
from data import *

if __name__ == '__main__':
    set max column to be viewed
    pd.set_option('display.max_columns', None)

    print(PATH_FILE)

    path_accounts = f"{PATH_FILE}/accounts/*"
    path_cards = f"{PATH_FILE}/cards/*"
    path_savings_accounts = f"{PATH_FILE}/savings_accounts/*"

    json_pattern_accounts = os.path.join(path_accounts)
    json_pattern_cards = os.path.join(path_cards)
    json_pattern_savings_accounts = os.path.join(path_savings_accounts)

    file_list_accounts = glob.glob(json_pattern_accounts)
    file_list_cards = glob.glob(json_pattern_cards)
    file_list_savings_accounts = glob.glob(json_pattern_savings_accounts)

    dfs_accounts = []
    dfs_cards = []
    dfs_savings_accounts = []

    # # READ ACCOUNTS #
    for file in file_list_accounts:
        with open(file) as f:
            json_data = pd.json_normalize(json.loads(f.read()))
        dfs_accounts.append(json_data)

    # # READ CARDS #
    for file in file_list_cards:
        with open(file) as f:
            json_data = pd.json_normalize(json.loads(f.read()))
        dfs_cards.append(json_data)

    # # READ SAVING ACCOUNTS #
    for file in file_list_savings_accounts:
        with open(file) as f:
            json_data = pd.json_normalize(json.loads(f.read()))
        dfs_savings_accounts.append(json_data)

    df_accounts = pd.concat(dfs_accounts, sort=False).sort_values(by=['ts'])
    df_cards = pd.concat(dfs_cards, sort=False).sort_values(by=['ts'])
    df_saving_accounts = pd.concat(dfs_savings_accounts, sort=False).sort_values(by=['ts'])

    print(">> -------------------- TASK no 1 --------------------")
    print(">> Dataframe for accounts")
    print(df_accounts.to_markdown() + "\n")
    print(">> Dataframe for cards")
    print(df_cards.to_markdown() + "\n")
    print(">> Dataframe for savings_accounts")
    print(df_saving_accounts.to_markdown() + "\n")

    print("\n")

    # df_accounts[['data.account_id', 'data.name', 'data.address', 'data.phone_number', 'data.email']] \
    #     = df_accounts[['data.account_id', 'data.name', 'data.address', 'data.phone_number', 'data.email']]\
    #     .fillna(method='ffill')
    # df_cards[['data.card_id', 'data.card_number', 'data.credit_used', 'data.monthly_limit', 'data.status']] \
    #     = df_cards[['data.card_id', 'data.card_number', 'data.credit_used', 'data.monthly_limit', 'data.status']]\
    #     .fillna(method='ffill')
    # df_saving_accounts[['data.savings_account_id', 'data.balance', 'data.interest_rate_percent', 'data.status']] \
    #     = df_saving_accounts[['data.savings_account_id', 'data.balance', 'data.interest_rate_percent', 'data.status']]\
    #     .fillna(method='ffill')

    df_accounts = df_accounts.fillna(method='ffill')
    df_cards = df_cards.fillna(method='ffill')
    df_saving_accounts = df_saving_accounts.fillna(method='ffill')

    df_result0 = pd.merge(df_accounts, df_cards, how="outer", on='ts').sort_values(by=['ts'])
    df_result1 = pd.merge(df_accounts, df_saving_accounts, how="outer", on='ts').sort_values(by=['ts'])

    # df_result = pd.merge(df_result0, df_result1, how="outer",
    #                      on=['ts', 'id_x', 'data.account_id', 'data.name', 'data.address', 'data.phone_number',
    #                     'data.email', 'set.phone_number', 'set.savings_account_id', 'set.address', 'set.email',
    #                     'set.card_id']).sort_values(by=['ts'])
    df_result = pd.merge(df_result0, df_result1, how="outer",
                         on=['ts']).sort_values(by=['ts'])

    print("\n")

    df_result.fillna(method='ffill', inplace=True)
    print("--------------- TASK no 2 ---------------")
    print(df_result.to_markdown() + "\n")

    df_result = df_result[['ts','set.balance', 'set.credit_used']].dropna(subset = ['set.balance', 'set.credit_used'], axis = 0, how = 'all')
    df_result.fillna(0, inplace=True)
    df_result["datetime"] = df_result["ts"]/1000
    df_result["datetime"] = pd.to_datetime(df_result["datetime"], unit="s")

    print("\n\n")
    print("--------------- TASK no 3 ---------------")
    print(df_result)
