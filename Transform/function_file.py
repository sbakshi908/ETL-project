


import pandas as pd



# File to Load (Remember to Change These)
matches_to_load = "Resources/matches_250.csv"
players_to_load = "Resources/ranked_players.csv"


def get_players():


    #read in pandas
    read_matches_csv = pd.read_csv(matches_to_load)
    read_players_csv = pd.read_csv(players_to_load)


    read_players_csv


    players_clean_df = read_players_csv.drop(['Link', 'Nickname'], axis=1)
    players_clean_df = players_clean_df.rename(columns={'Unnamed: 0': 'Rank'})
    players_clean_df


    #turn df into dictionary to use when importing to Mongo collection

    player_dict = players_clean_df.to_dict(orient='list')
    player_dict



    matches_clean_df = read_matches_csv.drop('Unnamed: 0', axis=1)
    matches_clean_df = matches_clean_df.fillna("N/A")
    matches_clean_df


    #convert to dictionary to possible use later
    matches_dict = matches_clean_df.to_dict(orient='list')
    matches_dict


    #convert file to pandas and create a fucntion the dictionaries

    return player_dict
