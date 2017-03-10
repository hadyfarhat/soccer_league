import csv
import random
import math
import os

players = list()
dragons = []
sharks = []
raptors = []
good_players = []
average_players = []

# get players from csv file and put them into a list
def get_players_from_csv_file(csv_file_name):
    with open(csv_file_name, 'r') as csv_file:
        player_info_reader = csv.reader(csv_file, delimiter=',')
        for row in player_info_reader:
            if row[0] == 'Name':
                continue
            else:
                players.append(row)
                
            
# get good players and put them in a list
def get_good_players():
    for player in players:
        if player[2] == 'YES':
            good_players.append(player)


# divide good players into teams
def divide_good_players(good_players):
    if good_players:
        if len(good_players) >= 3:
            for good_player in range(int(math.floor(len(good_players)/3))):
                dragons.append(good_players.pop(good_player))
            for good_player in range(int(math.floor(len(good_players)/2))):
                sharks.append(good_players.pop(good_player))
            for good_player in good_players:
                raptors.append(good_player)
            del good_players[:]
            

# get average players and put them in a list
def get_average_players():
    for player in players:
        if player[2] == 'NO':
            average_players.append(player)


# divide average players into teams
def divide_average_players(average_players):
    if average_players:
        for average_player in range(int(math.floor(len(average_players)/3))):
            dragons.append(average_players.pop(average_player))
        for average_player in range(int(math.floor(len(average_players)/2))):
            sharks.append(average_players.pop(average_player))
        for average_player in average_players:
            raptors.append(average_player)
        del average_players[:]
        

# helper function for write_file(); writes players into the provided file
def write_players(player_list, file):
    for player in player_list:
        file.write("{}\n".format(", ".join(player)))


# write all teams lists in teams.txt file
def write_file():
    if os.path.isfile("teams.txt"):
        os.remove("teams.txt")
    
    with open("teams.txt" , "a") as file:
        # sharks
        file.write("Sharks\n")
        file.write((20*"-") + "\n")
        write_players(sharks, file)
        file.write("\n")
        
        # dragons
        file.write("Dragons\n")
        file.write((20*"-") + "\n")
        write_players(dragons, file)
        file.write("\n")
        
        # raptors
        file.write("Raptors\n")
        file.write((20*"-") + "\n")
        write_players(raptors, file)


# helper function for welcome_letters(); writes a message for each guardian
def write_letter(player, team):
    if os.path.isfile("_".join(player[0].split()) + ".txt"):
        os.remove("_".join(player[0].split()) + ".txt")

    with open("_".join(player[0].split()) + ".txt", "a") as file:
        file.write("""
Dear {guardian_name},

Your son/daughter:
- Name:   {player_name}
- Height:   {player_height}
- Experience    {player_experience}
is in the {team_name} team.
His/Her first practice session is on October 5.

Please reply if you are not ok with this information.

Kind Regards,

Director of Fédération Internationale de Football Association
""".format(
           guardian_name=player[3],
           player_name=player[0],
           player_height=player[1],
           player_experience=player[2],
           team_name=team))


# write a welcome letter for each player
def welcome_letters(sharks,raptors,dragons):
    for player in sharks:
        write_letter(player, "Sharks")
    for player in raptors:
        write_letter(player, "Raptors")
    for player in dragons:
        write_letter(player, "Dragons")
        
    

if __name__ == "__main__":
    get_players_from_csv_file("soccer_players.csv")
    get_good_players()
    divide_good_players(good_players)
    get_average_players()
    divide_average_players(average_players)
    write_file()
    welcome_letters(sharks,raptors,dragons)
