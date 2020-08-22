# Modules
import os
import csv

movie = input("What movie are you looking for?")

# Set path for the file
csvpath = os.path.join("resources", "netflix_ratings.csv")

# Set variable to check if we found the movie
found = False

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the movie
    for row in csvreader:
        if row[0] == movie:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            found = True

            break

    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
