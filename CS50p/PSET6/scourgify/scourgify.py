import sys
import os
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not os.path.isfile(sys.argv[1]):
    sys.exit(f"Could not read {sys.argv[1]}")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    after = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)


        for row in reader:
            name = row['name']
            last, first = name.split(", ")
            house = row['house']
            after.append({'first': first, 'last': last, 'house': house})

    with open(sys.argv[2], 'w') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(after)
