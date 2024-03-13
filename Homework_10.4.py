# Write a script that reads the data from the previous CSV file and creates a
# new file called high_scores.csv where each row contains the player name and
# their highest score. The final score should be sorted by descending to the 
# highest score.

import csv

players_scores = []
with open("player_scores.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        players_scores.append((row["Player name"], int(row["Score"])))

highest_scores = {}
for player, score in players_scores:
    if player not in highest_scores or score > highest_scores[player]:
        highest_scores[player] = score

sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)

with open("high_scores.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Player name", "Highest score"])
    for player, score in sorted_scores:
        writer.writerow([player, score])
