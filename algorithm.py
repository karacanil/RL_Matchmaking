#Computing the optimal match
# s stands for skill
'''
Each vector represents a team
and each component of it represents
a player of that team
'''
import itertools

def p_norm(vector):
    p = 2 #Euclidean distance
    #Manhattan distance p=1
    n = len(vector)+1
    total_sum = 0
    
    for i in range(1,n):
        total_sum += vector[i-1]**p

    return  total_sum**(1/float(p))

def fairness(team1,team2):
    return abs(p_norm(team1)-p_norm(team2))

def uniformity(users):    
    q=7
    
    #Working out the mean
    mean=sum(users)/len(users)
    
    #For each number:subtract the Mean and square the result
    coeff=[]
    for player in users:
        coeff.append((mean-player)**2)

    #Then work out the mean of those squared differences.
    mean2=sum(coeff)/len(coeff)

    return mean2**(1/float(q))
    
def matcher(players):
    coeff = 0.5
    players.sort()
    team1=[]
    team2=[]
    
    for i in range(3):
        index = -1*i
        team1.append(players[index])
        team2.append(players[i-1])
        
    max_fairness = fairness(team1,team2)
    max_flaw = max_fairness + uniformity(players)
    
    length = len(players) #Has to be 6 since 3v3
    #team1.clear()
    #team2.clear()

    teams = list(itertools.combinations(players,3))
    matches = list(itertools.combinations(teams,2))
    # 2 dimensional grid

    for match in matches:
        team1 = match[0]
        team2 = match[1]
        if team1 == team2:
            continue
        
        fair_check = fairness(team1,team2)
        flaw_check = coeff * fair_check + uniformity(team1 + team2)
        
        if flaw_check <= max_flaw:
            max_flaw = flaw_check
            assined_team1 = team1
            assined_team2 = team2

    best_match=[assined_team1,assined_team2,max_flaw]
    return best_match
    '''
    print("team1: ",fair_team1)
    print("team2: ",fair_team2)
    print("fairness: ",max_fairness)
    '''

#print(uniformity([1100,1100,1100,1100,1100,1125]))




    
