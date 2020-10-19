#Code to create IPL schedule
import random

teams = ['SRH', 'RCB', 'CSK', 'KXIP', 'RR', 'MI', 'DC', 'KKR']

print('Number of teams: ', len(teams))

#Initialising and creating matches list
Matches = []
for j in range(0,7):
    k = j+1
    while k <= 7:
        temp = teams[j] + 'vs' + teams[k]
        Matches.append(temp)
        k+=1

print("Matches list: ", Matches)
print ('No of matches: ', len(Matches))

#Begining of code for schedule
kotla = 1
while kotla == 1:             #Making sure there is no overlap between 28th and 29th match. Refer line 57
    schedule = []             #Initialising the 56 match schedule
    for joiner in range(0,2):  #For loop for joining 2 lists of 28 matches

        sch = [Matches[0]]    #Initializing a 28 match schedule (half of league)

        t = [1]

        while len(Matches) != len(sch) or max(t)>4:   #Condition that no match is left out and 
                                                      #no team is having more than 4 matches in a quarter of tournament. Refer lines 47 to 54.
            i=1
            j=0
            random.shuffle(Matches)
            sch = [Matches[0]]
            while i < len(Matches):
                match = Matches[i]
                team = match.split('vs')
                #print(team)
                if ((team[0] in sch[j]) or (team[1] in sch[j])) or match in sch:  #Condition that a team did not play the previous match
                    i+=1
                else:
                    sch.append(match)
                    #print(sch)
                    j+=1
                    i=1
            countofx = 0
            t=[]
            for x in teams:
                for y in range(0,14):
                    if x in sch[y]:
                        countofx +=1
                t.append(countofx)
                countofx=0
        schedule = schedule + sch     #Two halfs(sch) are joined here. Each sch contains 28 matches.
    temp = schedule[27].split('vs')
    if temp[0] not in schedule[28] and temp[1] not in schedule[28]:
        kotla = 2

print ('Final Schedule is ', schedule)
print('No of matches in final schedule: ', len(schedule))
print('28th match: ', schedule[27], '\n29th match: ', schedule[28])