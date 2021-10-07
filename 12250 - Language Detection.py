""" Last Accepted 2021.10.07 08:21:07 by Ananda Phan"""
line=input()
i=0
while line != "#":
    ans = ""
    if(line == "HELLO") : ans="ENGLISH"
    elif(line == "HOLA") : ans="SPANISH"
    elif(line == "HALLO") : ans="GERMAN"
    elif(line == "BONJOUR") : ans="FRENCH"
    elif(line == "CIAO") : ans="ITALIAN"
    elif(line == "ZDRAVSTVUJTE") : ans="RUSSIAN"
    else: ans="UNKNOWN"
    
    print("Case ",i+1,": ",ans,sep="")
    i+=1
    line = input()

