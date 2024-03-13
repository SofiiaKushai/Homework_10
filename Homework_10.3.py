# Write a program that will simulate user scores in a game.
# Create a list with 5 players’ names after that simulate 100 rounds for each
# player. As a result of the game create a list with the player's name and
# score (0-1000 range). And save it to a CSV file.

from random import randint
import csv

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
players_scores = []

for player in players:
    for rounds in range(100):
        score = randint(0, 1000)
        players_scores.append((player, score))

with open("player_scores.csv", "w", newline="") as csvfile:
    fieldnames = ["Player name", "Score"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for player, score in players_scores:
        writer.writerow({"Player name": player, "Score": score})
