def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Напишшіть рік (прміжок між 2016 та 2024): "))

if year < 2016 or year > 2024:
    print("Неправильно вказаний прроміжок. Будь ласка впишіть проміжок 2016 та 2024.")
    exit(1)

if is_leap_year(year):
    print(f"{year} є високосним роком.")
else:
    print(f"{year} не є високосним роком.")

# 1

a = 10
b = 5

# 2

expression1 = (a > b) and (a == 10)
expression2 = (b < a) and (b == 5)

expression3 = (a < b) and (a == 10)
expression4 = (b > a) and (b == 5)

print(expression1)
print(expression2)
print(expression3)
print(expression4)

# 3

expression5 = (a < b) or (a == 10)
expression6 = (b > a) or (b == 5)

expression7 = (a < b) or (a != 10)
expression8 = (b > a) or (b != 5)

print(expression5)
print(expression6)
print(expression7)
print(expression8)

# 4

str1 = "hello"
str2 = "world"

expression9 = (len(str1) > 3) and (str2 == "world")
expression10 = (str1.startswith("h")) and (str2.endswith("d"))

expression11 = (str1 == "hello") and (str2 == "hello")
expression12 = (str1 != "hello") and (str2 == "world")

print(expression9)
print(expression10)
print(expression11)
print(expression12)

# 5

c = (int)(input("Type in a number "))

if c > 0:
    print("The value of the variable is greater than 0")
if c < 0:
    print("The value of the variable is less than 0")

# 6

c = 1

if c > 0:
    print(1)
else:
    print(-1)

# 7

a = 8
b = 12

if a > b:
    c = a - b
elif a < b:
    c = a + b
else:
    c = a

print(c)

#9

n = 20
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1

print()

n = 20
a, b = 0, 1
count = 0

fib_list = []

while count < n:
    fib_list.append(a)
    a, b = b, a + b
    count += 1

for i in range(4, 20):
    print(fib_list[i], end=' ')

print()

number = 0

while number <= 20:
    if number % 2 == 0:
        print(number, end=' ')
    number += 1

print()

number = -1
count = 0

while number >= -21:
    if count % 3 == 0:
        print(number, end=' ')
    number -= 1
    count += 1

print()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sequence = [29, 15, 17, 21, 23, 12, 31, 37, 19, 4, 8, 9, 3, 11, 13, 27, 33, 2, 5, 7]

prime_count = sum(1 for num in sequence if is_prime(num))

print(f"Кількість простих чисел у послідовності: {prime_count}")