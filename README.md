# ETL-project
ETL project due 4/23

Data sources used:
1. https://www.kaggle.com/kaiskermani/high-ranked-tennis-matches-since-2020?select=ranked_players.csv

The first file ranked_players.csv contains information about the players. Legend:

index: the ATP ranking of the player
Name: the name of the player
Nat: the country of the player (nationality)
Pts: The points of the player according to the ATP
Tournaments: The number of the tournaments won by the player
Link: link to the player profile in the website https://www.tennis24.com
Nickname: the name of the player used in the file matches_250.csv

The Second file matches_250.csv contains all the matches played since the beginning of 2020:
index: the index of the match
Date: the date of the match
P1: nickname of the home player
P2: nickname of the away player
Result: 1:home player won, -1:away player won, 0:unresolved
Set1: The score of the first set
Set2: The score of the second set
Set3: The score of the third set (if played)
Set4: The score of the fourth set (if played)
Set5: The score of the fifth set (if played)
Court_Type: The type of the surface of the game (clay, hard …etc)
Tournament: The name of the tournament in which the game is played.


2. wikipedia pages for each major tennis tournament were scrubbed and the table with the most recent champs was pulled 

3. api - https://rapidapi.com/sportcontentapi/api/tennis-live-data/endpoints 
Using the Get Matched by date i can call this API and retrieve all the matched on the chosen day