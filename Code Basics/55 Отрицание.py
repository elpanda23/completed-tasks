def is_palindrome(word):
    word = word.lower()
    x = word[::-1]
    x = x.lower()
    return x == word

def is_not_palindrome(word):
    return not is_palindrome(word)