def print_reversed_word_by_symbol(word):
    x = len(word)
    for i in range(x - 1, -1, -1):
        character = word[i]
        print(character)