def disemvowel(string_):
    x = string_
    for i in string_:
        if i.lower() in "aeiou":
            x = x.replace(i, "")
    return x