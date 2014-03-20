'''
Markov chain bracket picker
Copyright Kevin Ford (2014)

Stochastic chain through brackets where 
probability of team a winning is 1 - ratio over the sum of seeds
i.e. two teams with equal seeds each have 50-50 chance
where as a #5 vs a #12 has 1-5/(5+12) = ~71% chance of winning
'''
import numpy as np

# pick division brackets:

#bracket=( (((1,16),(8,9)),((5,12),(4,13))) , (((6,11),(3,14)),((7,10),(2,15))) )
bracket=[1,16,8,9,5,12,4,13, 6,11,3,14,7,10,2,15]
div=['South','East','West','Midwest']

# base function to determine winner of a game
def predictgame(seeds):
    seed1=seeds[0]
    seed2=seeds[1]
    # returns seed that won
    seedwinner=(np.random.rand()<=seed1/(seed1+seed2*1.0))
    winner = seeds[seedwinner]
    print('Seed %s playing seed %s and %s wins!'%(seed1,seed2,winner))
    return winner

# recursive function to find winner of bracket
def parsegame(br):
    if len(br) == 2:
        return predictgame(br)
    else:
        half=len(br)/2
        y=parsegame(br[:half])
        z=parsegame(br[half:])
        if type(y)==type([]):
            return parsegame(y+z)
        else:
            return parsegame([y,z])


finalfour=[]
for d in div:
    print('Division %s:'%d)
    winner=parsegame(bracket)
    print('Seed %i won Division %s!'%(winner,d))
    finalfour.append(winner)

print('Final 4 time')
#if tied seeds...
if finalfour[0]==finalfour[1]:
    champdiv1=div[np.random.rand()>0.5]
    champ1=finalfour[0]
else:
    champ1=predictgame(finalfour[:2])
    champdiv1=div[finalfour[:2].index(champ1)]
print('Seed %i from the %s won'%(champ1,champdiv1))

if finalfour[2]==finalfour[3]:
    champdiv2=div[2+(np.random.rand()>0.5)]
    champ2=finalfour[2]
else:
    champ2=predictgame(finalfour[2:])
    champdiv2=div[2+finalfour[2:].index(champ2)]
print('Seed %i from the %s won'%(champ2,champdiv2))

print('Final...')

if champ2==champ1:
    finaldiv=[champdiv1,champdiv2][np.random.rand()>0.5]
    final=champ1
else:
    final=predictgame([champ1,champ2])
    finaldiv=[champdiv1,champdiv2][([champ1,champ2].index(final))]

print('Seed %i from the %s won it all!'%(final,finaldiv))
