# Calculates the approximate grade level needed to comprehend a text
from cs50 import get_string

# Get text input from the user
text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

# Count letters, words and sentences
for i in text:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        words += 1
    elif i == "." or i == "!" or i == "?":
        sentences += 1

# Calculate average of letters and sentences
l = letters / words * 100
s = sentences / words * 100

# Calculate the grade using Coleman-Liau index
calculation = 0.0588 * l - 0.296 * s - 15.8
index = round(calculation)

# Prints the grade needed to comprehend a text
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")