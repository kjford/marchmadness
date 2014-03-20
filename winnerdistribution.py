import numpy as np

# pick division brackets:

#bracket=( (((1,16),(8,9)),((5,12),(4,13))) , (((6,11),(3,14)),((7,10),(2,15))) )
bracket=[1,16,8,9,5,12,4,13, 6,11,3,14,7,10,2,15]*4

def predictgame(seeds):
    seed1=seeds[0]
    seed2=seeds[1]
    # returns seed that won
    seedwinner=(np.random.rand()<=seed1/(seed1+seed2*1.0))
    winner = seeds[seedwinner]
    return winner

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

nsims=10000
allwinners=np.zeros(nsims)

for i in range(nsims):
    allwinners[i]=parsegame(bracket)
