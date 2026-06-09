rows = 5
for i in range (1,rows+1):
    result=""
    for j in range(i):
        result+="* "
    print(result)

def print_square(size, ch):
    for i in range(size):
        print(ch * size)
print_square(5, "@ ")

rows = 5
for i in range(1,rows+1):
    result="" 
    for sp in range(rows-i):
        result+=" "
    for j in range(i):
            result+="* "
    print(result)
for i in range(rows-1,0,-1):
    result=""
    for sp in range(rows-i):
        result+=" "
    for j in range(i):
        result+="* "
    print(result)