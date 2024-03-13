# Write a program that generates 26 text files named A.txt, B.txt, and so on
# up to Z.txt. To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains the name of the file and
# the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98

from random import randint


def generate_file(file_name):
    with open(file_name, 'w') as file:
        random_number = randint(1, 100)
        file.write(str(random_number))


for letter in range(ord('A'), ord('Z') + 1):
    file_name = chr(letter) + '.txt'
    generate_file(file_name)


with open('summary.txt', 'w') as summary_file:
    for letter in range(ord('A'), ord('Z') + 1):
        file_name = chr(letter) + '.txt'
        with open(file_name, 'r') as file:
            number = file.read()
            summary_file.write(f"{file_name}: {number}\n")
