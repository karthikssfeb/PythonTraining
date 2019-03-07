def isPalindrome(inputString):
    reversedString = inputString[::-1]
    if inputString==reversedString:
        return True
    else:
        return False

if __name__ == "__main__":
    print ("Is 'radar' a palindrome? \n%s" % isPalindrome('radar'))
