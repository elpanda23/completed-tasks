def is_arguments_for_substr_correct(string, index, lenght):
    if (lenght < 0) or (index < 0):
        return False
    elif index > len(string)-1:
        return False
    elif lenght + index > len(string):
        return False
    else:
        return True