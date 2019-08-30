from DataHandling.file_writer import write_file
from DataHandling.file_reader import read_file
from DataHandling.data_editor import insertion, deletion,set_creator
import algorithm 
import json
import pprint

path='./Data/randomdata.json'

'''
Creates a random dataset and writes it as a JSON file,
also returns the number of the players in the dataset
'''
#total_player = write_file(path)

raw_data, total_player = write_file(path,set_creator(2))

stats = read_file(path)
pprint.pprint(stats)

insertion(1366,total_player,stats) #Insterting a new player
deletion(3,stats) #Deleting a player

pprint.pprint(stats)

'''
for player in range(1,total_player+1):
    print('Player ', player)
    for stat in stats[str(player)]:
        print('MMR: ' , stat['mmr'])
        print('RANK: ' , stat['rank'])
'''

bmatch = algorithm.matcher(raw_data)
print("team1: ",bmatch[0])
print("team2: ",bmatch[1])
print("flaw: ",bmatch[2])
