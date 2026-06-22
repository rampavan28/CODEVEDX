def dictionary_attack(password, wordlist):
    attempts = 0

    for word in wordlist:
        attempts += 1
        if word.strip() == password:
            return True, attempts

    return False, attempts