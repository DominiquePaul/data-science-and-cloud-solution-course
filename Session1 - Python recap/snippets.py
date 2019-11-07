num = 3
if num % 2 == 0:
    print("Your integer is even")
else:
    print("Your integer is odd")


# task 11
for char in '-.,;\n"\'':
    text = text.replace(char,'')
print(text)

# Split converts string to list.
# Each item in list is split on spaces
text.split(' ')[0:20]

# Making new list with no empty words in it
cleaned_list = []

for word in text.split(' '):
    word_length = len(word)
    if word_length > 0:
        cleaned_list.append(word)

cleaned_list[0:20]

# task 11:
# Making empty lists to append even and odd numbers to.
even_numbers = []
odd_numbers = []

for number in range(1,51):
    if number % 2 == 0:
        even_numbers.append(number)
    else: 
        odd_numbers.append(number)

print("Even Numbers: ", even_numbers)

print("Odd Numbers: ", odd_numbers)

# task 12
# Note, there are better ways to code this which I will go over in later videos
a,b = 1,1
for i in range(10):
    print("Fib(a): ", a, "b is: ", b)
    a,b = b,a+b
