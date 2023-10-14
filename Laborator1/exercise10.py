def count_words(text):
    words = text.split()
    return len(words)

text = "I have Python exam"
count = count_words(text)
print(f"Numarul de cuvinte din text este: {count}")