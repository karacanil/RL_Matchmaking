from .file_writer import rank_finder
from random import randint
import json

update_path='./Data/randomdata.json'

def insertion(mmr, total_player, dict):
    rank = rank_finder(mmr)
    dict.update({str(total_player+1):[{"mmr": mmr, "rank": rank}]})
    with open(update_path, 'w+') as in_file:
        json.dump(dict,in_file)
        in_file.close()
        return True
    return False

def deletion(id, dict):
    dict.pop(str(id))
    with open(update_path, 'w+') as in_file:
        json.dump(dict,in_file)
        in_file.close()
        return True
    return False

def set_creator(player_number):
    rank_separator = 100
    min_mmr = 900
    max_mmr = 1600
    #player_number = 3

    dataset=[]

    for rank in range(min_mmr, max_mmr, rank_separator):
        for i in range(player_number):
            random_mmr = randint(rank, rank + rank_separator - 1)
            #print(random_mmr)
            dataset.append(random_mmr)
        #print("")

    #print(dataset)

    return dataset