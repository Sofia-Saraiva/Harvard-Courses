import sys
import os
import csv
from tabulate import tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exit")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers='keys', tablefmt="grid"))
