import string
from collections import Counter

def process_text(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    return text.split()

def most_frequent_words(file_path, num_words):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = process_text(text)
        word_counts = Counter(words)
        return word_counts.most_common(num_words)
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    num_words = int(input("Enter the number of most frequent words to find: "))

    frequent_words = most_frequent_words(file_path, num_words)
    print(f"The {num_words} most frequent words in the file are:")
    for word, count in frequent_words:
        print(f"{word}: {count} occurrences")
