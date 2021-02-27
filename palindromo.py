
def palindrome(word):
    word = word.replace(' ', '').lower()
    #[::] from initial number to final.
    #[::-1] Inversed
    if word[::] == word[::-1]:
        return True
    else:
        return False


def run():
    word = input("Please, Write a word: ")
    ispalindrome = palindrome(word)
    if ispalindrome == True:
        print("You're right!")
    else:
        print("You are wrong.")


if __name__ == '__main__':
    run()
