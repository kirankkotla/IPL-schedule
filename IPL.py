#Code to create IPL schedule

#Teams are A, B, C, D, E, F, G, H

#Matches are like AB, CD, EF, GH

teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

teams = ['SRH', 'RCB', 'CSK', 'KXIP', 'RR', 'MI', 'DC', 'KKR']

Matches = []

no_teams = len(teams)

print('Number of teams: ' + str(no_teams))

i = 0

for j in range(0,7):
    k = j+1
    while k <= 7:
        temp = teams[j] + 'vs' + teams[k]
        Matches.append(temp)
        k+=1

print("Matches list: ", Matches)
print ('No of matches: ', len(Matches))

#Scheduling matches in order

sch = [Matches[0]]
i=1
j=0
print("first match in schedule: ", sch)

while i < len(Matches):
    match = Matches[i]
    team = match.split('vs')
    #print(team)
    if ((team[0] in sch[j]) or (team[1] in sch[j])) or match in sch:
        i+=1
    else:
        sch.append(match)
        #print(sch)
        j+=1
        i=1
        
print ('Schedule is ', sch)
print('No of matches in schedule: ', len(sch))

print('======')
for i in Matches:
    if i not in sch:
        print(i)


