def isPangram(phrase):
    alphabets = 'abcdefghijklmmnopqrstuvwxyz'
    phrase = phrase.lower()
    for char in alphabets:
        if char not in phrase:
            break
    else:
        return True
    return False

if __name__ == "__main__":
    print ("Enter a phrase")
    phrase = input()
    if isPangram(phrase):
        print ("The input phrase is recognized as Pangram")
    else:
        print ("The input phrase is not Pangram")