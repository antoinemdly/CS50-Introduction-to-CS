from cs50 import get_string
import re

text = get_string("Text: ")

num_words = len(text.split())

letter_count = 0
for char in text:
    if char.isalpha():
        letter_count += 1

pattern = r'(?<=[.!?]) +'

sentences = re.split(pattern, text)

# Remove empty sentences
sentences = [sentence for sentence in sentences if sentence]
num_sentences = len(sentences)


L = (letter_count * 100) / num_words
S = (num_sentences * 100) / num_words

grade = 0.0588*L - 0.296*S - 15.8

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(grade)}")