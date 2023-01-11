from random import shuffle, choice
i=0
win=0
false=0
while i<100000:
    doors = [0,0,1]
    shuffle(doors)
    doors
    users = choice(doors)
    if users == 0:
        win+=1
    else:
        false+=1
    i+=1
print(f'100000 times of simulation: {win/(win+false)} times win(change) {false/(win+false)} times win(stay)')
