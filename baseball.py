'''teams = ["Yankees", "Dodgers", "Red Sox", "Cubs"]

scores = {
    "Yankees": [3, 5, 2],
    "Dodgers": [4, 1, 6],
    "Red Sox": [2, 2, 2],
    "Cubs": [5, 3, 1]
}

players = {
    "Yankees": {"Judge": 2, "Stanton": 1},
    "Dodgers": {"Betts": 3, "Freeman": 2},
    "Red Sox": {"Devers": 1, "Turner": 2},
    "Cubs": {"Happ": 2, "Suzuki": 1}
}

total_scores = {}

for team in teams:
    total_scores[team] = 0

for team in scores:
    for i in range(len(scores[team])):
        total_scores[team] += scores[team][i]

for team in players:
    for player in players[team]:
        total_scores[team] = total_scores[team] + players[team][player]

print("Team Scores:")
for team, scores in total_scores:
    print(t, ":", s)

top_team = ""
max_score = 0

for t in total_scores:
    if total_scores[t] > max_score:
        max_score = total_scores[t]
        top_team = t

print("Top Team:", top_team, max_score)

average_scores = {}

for team in scores:
    average_scores[team] = sum(scores[team]) / len(scores)

for team in average_scores:
    if average_scores[team] > 3:
        print(team, "has high average")

extra = ["bonus", "penalty"]

for i in range(3):
    print(extra[i])


Fix all errors
Ensure correct totals, averages, and output
Make the program run without crashing


expected output 
Team Scores:
Yankees : 13
Dodgers : 16
Red Sox : 9
Cubs : 12

Top Team: Dodgers 16

Yankees has high average
Dodgers has high average
Cubs has high average

bonus
penalty'''
teams = ["Yankees", "Dodgers", "Red Sox", "Cubs"]
scores = {
    "Yankees": [3, 5, 2],
    "Dodgers": [4, 1, 6],
    "Red Sox": [2, 2, 2],
    "Cubs": [5, 3, 1],
}
players = {
    "Yankees": {"Judge": 2, "Stanton": 1},
    "Dodgers": {"Betts": 3, "Freeman": 2},
    "Red Sox": {"Devers": 1, "Turner": 2},
    "Cubs": {"Happ": 2, "Suzuki": 1},
}

total_scores = {}
for team in teams:
  total_scores[team] = 0

for team in scores:
  for i in range(len(scores[team])):
    total_scores[team] += scores[team][i]

for team in players:
  for player in players[team]:
    total_scores[team] = total_scores[team] + players[team][player]

print("Team Scores:")
for team, s in total_scores.items():
  print(team, ":", s)

top_team = ""
max_score = 0
for t in total_scores:
  if total_scores[t] > max_score:
    max_score = total_scores[t]
    top_team = t

print("Top Team:", top_team, max_score)

average_scores = {}
for team in scores:
  average_scores[team] = sum(scores[team]) / len(scores[team])

for team in average_scores:
  if average_scores[team] > 3:
    print(team, "has high average")

extra = ["bonus", "penalty"]
for i in range(len(extra)):
  print(extra[i])