friend = ['Karstark', 'Tully']
enemy = ['Lannister', 'Frey']
def who_is_this_house_to_starks(name):
    friend = ['Karstark', 'Tully']
    enemy = ['Lannister', 'Frey']
    if name in friend:
        return 'friend'
    elif name in enemy:
        return 'enemy'
    else:
        return 'neutral'