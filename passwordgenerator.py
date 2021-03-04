import random  

def password_generator():
    capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f']
    symbols = ['!', '@', '#', '$', '%', '^', '&']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    characters = capitals + lowercase + symbols + numbers

    password = []


    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)
    
    password = ''.join(password)
    return password


def run():
    password = password_generator()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()