'''
Creating a random dataset in terms of MMR
to test the matchmaking system.
3 random players will be created for each rank
according to the rank distribution in
RankDistribution.txt
'''

import json
#from random import randint

def rank_finder(mmr):
	if 1500<=mmr:
		rank = "Grand Champion"
	elif 1200<=mmr<1500:
		rank = "Champion "
		if 1200<=mmr<1300:
			rank+="1"
		elif 1300<=mmr<1400:
			rank+="2"
		elif 1400<=mmr<1500:
			rank+="3"
	else:
		rank = "Diamond "
		if 900<=mmr<1000:
			rank+="1"
		elif 1000<=mmr<1100:
			rank+="2"
		elif 1100<=mmr<1200:
			rank+="3"

	return rank

def write_file(target_path, dataset):
	#raw data writer
	total_player = len(dataset)
	data={}
	
	for player in range(1,total_player+1):
		player_index = str(player)
		data[player_index] = []
		data[player_index].append({
			'mmr': dataset[player-1],
			'rank': rank_finder(dataset[player-1])
		})

	#'./Data/randomdata.txt'
	# Add a (try-except-finally) part
	with open(target_path, 'w') as outfile:
		json.dump(data,outfile)
		outfile.close()
		#return True

	return dataset, total_player