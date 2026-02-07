# %% 1.1.1
import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

p = b / a
q = c / a
term1 = -p / 2
term2 = math.sqrt(p**2 / 4 - q)
print(f"x = {term1} +/- {term2}")

# %% 1.1.2

a = 20
b = 6

print(f"a) {hex(a)}, {hex(b)}")

print(f"b) {a/b:.3f}")

print(f"c) {a % b}")

# %% 1.1.3

first_name_str = "First name: "
first_name = input(first_name_str)

last_name_str = "Last name: "
last_name = input(last_name_str)

birth_year_str = "Birth year: "
birth_year = input(birth_year_str)

width = 12
row = "-" * 31
print(row)
print(
    f'| {first_name_str}{" " * (width - len(first_name_str))} | {first_name}{" " * (width - len(first_name))} |'
)
print(row)
print(
    f'| {last_name_str}{" " * (width - len(last_name_str))} | {last_name}{" " * (width - len(last_name))} |'
)
print(row)
print(
    f'| {birth_year_str}{" " * (width - len(birth_year_str))} | {birth_year}{" " * (width - len(birth_year))} |'
)
print(row)

# %% 1.2.1

s = input("Skriv ett antal tal separerade med mellanslag: ")
numbers = [int(chunk) for chunk in s.split(" ")]
mean = 0
for num in numbers:
    mean += num
mean /= len(numbers)

print(f"medelvärde: {mean}")
print(f"minsta tal: {min(numbers)}")
print(f"största tal: {max(numbers)}")

# %% 1.3.1

x = [1, 2]
y = [1, 2]

print(x is y)  # false, the lists are stored in different memory
print(x == y)  # true, the lists are identical in value

# %% 1.4.1

total_age = 0
count = 0
oldest_person = None
oldest_age = 0
print("Stop the program entering no age")
while True:
    name = input("Name: ")
    age = int(input("age: "))
    if age == "":
        break
    if age > oldest_age:
        oldest_age = age
        oldest_person = name
    total_age += age
    count += 1
    print(f"Oldest person: {oldest_person} is {oldest_age}")
    print(f"Average age: {total_age/count}")

# %% 1.5.1

num = 20
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# %% 1.6.1
a = int(input("a: "))
b = int(input("b: "))
N = int(input("N: "))

step = (b - a) / (N - 1)
points = [a + i * step for i in range(N)]
print(points)

# %% 1.7-1

A = eval(input("Enter matrix A: "))
B = eval(input("Enter matrix B: "))


if (len(A) == len(B)) and (len(A[0]) == len(B[0])):
    op = input("S for sum, s for subtract, m for elementwise multiplication: ")
    m = len(A)
    n = len(A[0])
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            print(i, j)
            C[i][j] = A[i][j] + B[i][j]
            match op:
                case "S":
                    C[i][j] = A[i][j] + B[i][j]
                case "s":
                    C[i][j] = A[i][j] - B[i][j]
                case "m":
                    C[i][j] = A[i][j] * B[i][j]
                case _:
                    print("Invalid input")
                    break
    print(C)
else:
    print("Matrix dimensions do not agree")

# %% 1.8.1
import random


numbers = [random.randint(1, 100) for _ in range(100)]
divisible_by = [
    num for num in numbers if (num % 7 == 0) or (num % 11 == 0) or (num % 13 == 0)
]
print(divisible_by)

# %% 1.9.2

l = ["apple", "pear", "banana"]
d = {k: v for k, v in enumerate(l)}
print(d)

# %% 1.10.2

d = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
}
l = list(d.keys())

i = int(input("Index: "))
print(d[l[i]])

# %% 2.1.2
import math


def polar_complex(c: complex):
    arg = math.atan2(c.imag, c.real)
    abs = math.sqrt(c.real**2 + c.imag**2)
    return arg / (2 * math.pi) * 360, abs


c = complex(1, math.sqrt(3))
arg, abs = polar_complex(c)
print(f"{arg=:.2f} degrees, {abs=:.2f}")

# %% 2.2.1

def linspace(a, b, N=100):
    step = (b - a) / (N - 1)
    points = [a + i * step for i in range(N)]
    return points

print(linspace(0.1, 10))

# %% 2.3.2

x = lambda a, b, c: ( -b/(2*a) - math.sqrt((b/(2*a)) ** 2 - c/a), -b/(2*a) + math.sqrt((b/(2*a)) ** 2 - c/a) )
print(x(1,2,0))

# %% 2.4.1
"""
Rock (r), Paper (p), Scissors (s)
p > r
s > p
r > s
"""

_map = {
    "r": 1,
    "p": 2,
    "s": 3,
}
name_map = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}

while True:
    human = _map[input("Choose Rock (r), Paper (p) or Scissors (s): ")]
    computer = random.randint(1, 3)
    print(f"""
    You chose {name_map[human]}.
    The computer chose {name_map[computer]}.
    """)
    if human == computer:
        print("It's a tie!")
    elif (human - computer) in (1,-2):
        print("You won!")
    else:
        print("You lost!")

# %% 2.5.2

def count_word(file_name, target_word):
    with open(file_name, "r") as f:
        text = f.read().replace("\n", " ")

    # Create a list with the words
    alpha_chars = []
    for letter in text:
        if (letter.isalpha() or letter in (" ")):
            alpha_chars.append(letter.lower()) 
    text = "".join(alpha_chars)
    words = text.split(" ")
    
    # Count words
    count = 0
    target_word = target_word.lower()
    for word in words:
        if word == target_word:
            count += 1
    return count

num_occurences = count_word("story.txt", "the")
print(num_occurences)

# %% 
x = 10