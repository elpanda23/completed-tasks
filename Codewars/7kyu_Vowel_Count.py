def get_count(sentence):
    count = 0
    for i in range(len(sentence)):
        if "a" in sentence[i]:
            count = count + 1
        elif "e" in sentence[i]:
            count = count + 1
        elif "i" in sentence[i]:
            count = count + 1
        elif "o" in sentence[i]:
            count = count + 1
        elif "u" in sentence[i]:
            count = count + 1
    return count