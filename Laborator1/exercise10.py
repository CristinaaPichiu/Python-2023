def count_words(text):

    #textul este divizat în cuvinte folosind metoda split()

    words = text.split()
    return len(words)

if __name__ == "__main__":

    text = "I have Python exam"
    count = count_words(text)
    print(f"Numarul de cuvinte din text este: {count}")

