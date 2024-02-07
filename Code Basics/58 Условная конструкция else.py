def normalize_url(adres):
    if adres[:8] == 'https://':
        return adres
    elif adres[:7] == 'http://':
        return 'https://' + adres[7:]
    else:
        return 'https://' + adres