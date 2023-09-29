import os

def make_commit(date):
    # créer un commit dans le répository en changeant légèrement un fichier
    os.system(f"echo '{date}' > file")
    os.system('git add file')
    os.system(f"git commit -m '{date}'--amend --no-edit --date {date}")


def make_commits(start_date, end_date):
    # for date in ....
    # make_commit(date)


make_commit("10/10/2023")