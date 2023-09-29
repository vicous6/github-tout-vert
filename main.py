#!/usr/bin/env python3
import os

def make_commit(daysAgo):
    # créer un commit dans le répository en changeant légèrement un fichier
    os.system(f"echo '{daysAgo}' > file")
    os.system('git add file')
    os.system(f"git commit -m '{daysAgo}' --date relative:{daysAgo}.days.ago")

def make_commits(days):
    for i in range(days):
        make_commit(i)


make_commits(365)

os.system("git push --force origin main")
