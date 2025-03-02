"""
Estimated time: 25 minutes
Actual time: 40 minutes
"""

text = input("Text: ")

words = text.split()
word_to_count = {}

for word in words:
    word = word.strip('.,!?;:"\'')
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
print(f"Text: {text}")

unique_words = list(word_to_count.keys())
unique_words.sort()
maximum_word_length = max(len(word) for word in unique_words)
