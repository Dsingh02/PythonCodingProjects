#Password Generator Project
import random
#Creating libraries of letters, numbers and symbols using the list data type
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Asking the using how many of each they want and storing it in the 'nr' things.
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Creating an empty list in the password variable then running the code of choosing random of each library the number of
#times that the user has asked for.
password = []
for i in range(nr_letters):
    password.append(random.choice(letters))
    random.shuffle(password)
for i in range(nr_symbols):
    password.append(random.choice(symbols))
    random.shuffle(password)
for i in range(nr_numbers):
    password.append(random.choice(numbers))
    random.shuffle(password)
final_password = "".join(password)
print(f"Your password is: {final_password}")
