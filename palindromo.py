Titulo = """
WELCOME!! THIS PROGRAM IS A PALINDROME CHECKER. BY ADDING A WORD, IT WILL TELL YOU IF IT IS CORRECT OR WRONG!

"""
print(Titulo)

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
        print("You're right! That's a palindrome.")
    else:
        print("Sorry! That's not a palindrome.")


if __name__ == '__main__':
    run()
