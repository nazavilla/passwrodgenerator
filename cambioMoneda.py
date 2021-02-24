def conversor( country , dolarValue):
    pesos = input("Enter amount in" + country + "you would like to convert?: ")
    pesos = float(pesos)
    dollars = pesos / dolarValue
    dollars = str(round(dollars, 2))
    dollars = str(dollars)
    print("You own " + dollars + " Dollars")

menu = """
Welcome to my money conversor 💲
1- Chilean Pesos to U.S Dollars
2- Colombian Pesos to U.S Dollars
3- Mexican Pesos to U.S Dollars

Choose an option:  """

option = int(input(menu))

if option == 1:
    conversor("Chilenos", 704.70)
elif option == 2:
    conversor("Colombianos", 3592.88)
elif option == 3:
    conversor("Mexicanos", 20.6)
else:
    print(" Please, Choose a valid option!") 

