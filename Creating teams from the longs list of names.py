#!/usr/bin/env python
# coding: utf-8
#Teams are slected and spaces are removed if there is one in 'lists'
#what is needed to di shorten the code and make a better one 'improve'
#Lets see if there is a posibility of using function
#Looking for some idea to implement

from random import choice
import logging
Players = []
file=open('lists','r')
Players=file.read().splitlines()
Players2=[]
for x in Players:
  players1=x.strip()
  Players2.append(players1)
j=0
teamA=[]
teamB=[]
teamC=[]
teamD=[]
while j<len(Players2):
  playerA=choice(Players2)
  teamA.append(playerA)
  Players2.remove(playerA)
  if len(Players2)!=0:
    playerB=choice(Players2)
    teamB.append(playerB)
    Players2.remove(playerB)
    if len(Players2)!=0:
        playerC=choice(Players2)
        teamC.append(playerC)
        Players2.remove(playerC)
        if len(Players2)!=0:
            playerC=choice(Players2)
            teamD.append(playerC)
            Players2.remove(playerC)
  else:
      break
print("teamA: "+str(teamA))
print("teamB: "+str(teamB))
print("teamC: "+str(teamC))
print("teamD: "+str(teamD))




