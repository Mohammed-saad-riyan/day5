import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_symbols = nr_letters + nr_symbols + nr_numbers
# print (nr_symbols)
ch_letter = random.sample(letters, nr_letters)
# print (ch_letter)
ch_number = random.sample(numbers, nr_numbers)
# print (ch_number)
ch_symbols = random.sample(symbols, nr_symbols)
# print (ch_symbols)

# l = ""
# for letter in ch_letter:
#     l += letter
# # print (l)

# n = ""
# for number in ch_number:
#     n += number
# # print (n)

# s = ""
# for symbol in ch_symbols:
#     s += symbol
# # print (s)

# final = random.shuffle
# print (f"randomly generated password is {final}")

final = ch_letter + ch_number + ch_symbols
random.shuffle(final)
# print (final)

d = ""
for f in final:
    d += f
print (d)