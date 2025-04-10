MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

for value in MLB_teams.values():
    print(value)
for value in MLB_teams.keys():
    print(value)
for key,value in MLB_teams.items():
    print(key,"->",value)
