import sys

def word_count(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py 'sentence'")
    else:
        sentence = sys.argv[1]
        count = word_count(sentence)
        print(f"Number of words in the sentence: {count}")
