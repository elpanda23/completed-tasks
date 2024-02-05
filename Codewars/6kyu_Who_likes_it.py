def likes(names):
    if len(names) < 1:
        return "no one likes this"
    elif len(names) == 1:
        x = "".join(names)
        return f"{x} likes this"
    elif len(names) == 2:
        x = x = " and ".join(names)
        return f"{x} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) >= 4:
        x = len(names) - 2
        return f"{names[0]}, {names[1]} and {x} others like this"