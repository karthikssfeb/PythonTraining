import string
def findPalindrome(phrase):
    testPhrase = phrase.replace(' ','')
    testPhrase = testPhrase.upper()
    palindromeTestString = ""
    for char in testPhrase:
        if char not in string.punctuation:
            palindromeTestString +=char
    reversedString = palindromeTestString[::-1]
    if reversedString == palindromeTestString:
        return True
    else:
        return False

if __name__ == "__main__":
    print ("Enter a phrase")
    phrase = input()
    if findPalindrome(phrase):
        print ("The input phrase is recognized as Palindrome")
    else:
        print ("The input phrase is not Palindrome")