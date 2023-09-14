import sys
import os
from PIL import Image, ImageOps

file1 = os.path.splitext(sys.argv[1])
file2 = os.path.splitext(sys.argv[2])

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not file1[1] in ['.jpeg', '.jpg', '.png']:
    sys.exit("Invalid output")
elif not os.path.isfile(sys.argv[1]):
        sys.exit("Input does not exist")
elif file1[1] != file2[1]:
    sys.exit("Input and output have different extensions")
else:
    shirt = Image.open("shirt.png")
    input = Image.open(sys.argv[1])
    size = shirt.size
    muppet = ImageOps.fit(input, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])