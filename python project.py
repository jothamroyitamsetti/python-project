import random

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

random_number = random.randint(lower_range, upper_range)

print("The number is", random_number)
print("The number is ", "odd" if random_number % 2 else "even")
print("The number is ", "positive" if random_number >= 0 else "negative")
counter = 0
for i in range(1, random_number+1):
    if random_number % i == 0:
        counter += 1

if counter == 2:
    print("The number is prime")
else:
    print("The number is composite")











































