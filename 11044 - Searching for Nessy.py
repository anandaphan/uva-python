""" Last Accepted 2021.10.05 10:21:46 by Ananda Phan"""


n=int(input())
for i in range(n):
    num = list(map(int,input().split()))

    
    sonar = (num[0]//3) * (num[1]//3)
    print(int(sonar))

    
    """ to get this formulae, simulate each problem from the simple 4x4,5x5,6x6, 7x7
        and then figure out the possible formula"""
