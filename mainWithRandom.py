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

def make_commit(daysAgo):
    # créer un commit dans le répository en changeant légèrement un fichier

    if whatDay(daysAgo) == "Saturday" or whatDay(daysAgo)=="Sunday":
        os.system(f"echo '{daysAgo}' > file")
        os.system('git add file')
        os.system(f"git commit -m '{daysAgo}' --date relative:{daysAgo}.days.ago") 
    else:
        randomCommitNumber = random.randint(2,4)

        for i in range (randomCommitNumber):
            time.sleep(0.1)
            randomNumber = random.randint(100,4000)
            os.system(f"echo '{daysAgo}+ {randomNumber}' > file")
            os.system('git add file')
            os.system(f"git commit -m '{daysAgo}' --date relative:{daysAgo}.days.ago") 


def make_commits(days):
    for i in range(days):
        make_commit(i)




make_commits(150)

os.system("git push --force origin main")
random_number = random.randint(1, 10)
