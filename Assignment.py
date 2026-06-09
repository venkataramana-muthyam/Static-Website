# Program 1: Pyramid Pattern

rows = 5

for i in range(1, rows + 1):
    result = ""
    for j in range(i):
        result += "* "
    print(result)

print()

# Program 2: Square Pattern Function

def print_square(size, ch):
    for i in range(size):
        print(ch * size)

print_square(5, "@ ")

print()

# Program 3: Diamond Pattern

rows = 5

for i in range(1, rows + 1):
    result = ""
    for sp in range(rows - i):
        result += " "
    for j in range(i):
        result += "* "
    print(result)

for i in range(rows - 1, 0, -1):
    result = ""
    for sp in range(rows - i):
        result += " "
    for j in range(i):
        result += "* "
    print(result)
