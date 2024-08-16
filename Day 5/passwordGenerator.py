import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#solution 1

letter = random.sample(letters, nr_letters)
symbols = random.sample(symbols,  nr_symbols)
numbers = random.sample(numbers, nr_numbers)

password = letter + symbols + numbers
random.shuffle(password)

print(''.join(password))


#solution 2

passwordList = []

for char in range(0, nr_letters):
    passwordList += random.choice(letters)
    print(passwordList)

for char in range(0, nr_symbols):
    passwordList += random.choice(symbols)
    print(passwordList)

for char in range(0, nr_numbers):
    passwordList += random.choice(numbers)

random.shuffle(passwordList)
print(''.join(passwordList))

