sentence = input("Enter a sentence : ")

words = sentence.split()

max_word = max(words)

max_len = len (max_word)

print(f"\nLongest word is \"{max_word}\" and its length is {max_len}")