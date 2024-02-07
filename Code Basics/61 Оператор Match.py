def get_number_explanation(count):
    match count:
        case 666:
            return "devil number"
        case 42:
            return "answer for everything"
        case 7:
            return "prime number"
        case _:
            return "just a number"