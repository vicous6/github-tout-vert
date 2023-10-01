#!/usr/bin/env python3
import os
import datetime
import random
import time


def whatDay(jours_a_remonter):
    date_actuelle = datetime.date.today()


    jours_a_remonter = int(jours_a_remonter)


    date_passee = date_actuelle - datetime.timedelta(days=jours_a_remonter)

    nom_jour = date_passee.strftime("%A")

    return nom_jour

def make_commit(daysAgo,min,max,min2,max2):

    if whatDay(daysAgo) == "Saturday" or whatDay(daysAgo)=="Sunday":
        randomCommitNumber = random.randint(int(min),int(max))

        for i in range (randomCommitNumber):
            time.sleep(0.1)
            randomNumber = random.randint(100,4000)
            os.system(f"echo '{daysAgo}+ {randomNumber}' > file")
            os.system('git add file')
            os.system(f"git commit -m '{daysAgo}' --date relative:{daysAgo}.days.ago") 
    else:
        randomCommitNumber = random.randint(int(min2),int(max2))

        for i in range (randomCommitNumber):
            time.sleep(0.1)
            randomNumber = random.randint(100,4000)
            os.system(f"echo '{daysAgo}+ {randomNumber}' > file")
            os.system('git add file')
            os.system(f"git commit -m '{daysAgo}' --date relative:{daysAgo}.days.ago") 


def make_commits(days):
    inp3= input("nombre MIN de commit en semaine? ")
    inp4= input("nombre MAX de commit en semaine? ")
    inp=input("nombre MIN de commit le week end? ")
    inp2= input("nombre MAX de commit le week end")
    for i in range(days):
        make_commit(i,inp,inp2,inp3,inp4)

HowManyDay =input("combien de jour dans le passé souhaiter vous commit?")
make_commits(int(HowManyDay))
os.remove("file")
os.system("git push --force origin main")

