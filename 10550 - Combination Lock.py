""" last accepted : 2021.10.05 00:48 by Ananda Phan"""

eachDeg = 360/40
while True:
    combination = list(map(int,input().split()))
    if(sum(combination)==0):
        break
    
    degree = 1080                                           #3x full turn
    degree += (combination[0]-combination[1])%40 * eachDeg  #clockwise
    degree += (combination[2]-combination[1])%40 * eachDeg  #counter-clockwise
    degree += (combination[2]-combination[3])%40 * eachDeg  #clockwise
    
    print(int(degree))
