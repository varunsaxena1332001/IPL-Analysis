import pandas as pd

matches = pd.read_csv("IPL Matches 2008-2020.csv")
deliveries = pd.read_csv("IPL Ball-by-Ball 2008-2020.csv")

team_names = matches.team1.unique()
print(team_names)

team_names_abv = ["RCB", "KXIP", "DD", "MI", "KKR", "RR", "DeCh", "CSK", "KTK", "PWI", "SH", "GL", "RPS", "RPS", "DC"]
matches.replace(team_names, team_names_abv, inplace=True)

print(matches)
