import sys
import os

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exit")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")
else:
    with open(sys.argv[1], 'r') as file:
        count = 0
        for line in file:
            if not line.lstrip().startswith('#') and not line.isspace():
                count += 1
    print(count)

