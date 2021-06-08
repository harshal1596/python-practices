import sys

# Leap year code
# year = int(sys.argv[1])
year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year is leap year")
        else:
            print("Year is not leap year")
    else:
        print("Year is leap year")
else:
    print("Year is not leap year")

# Fibonacci

number = int(sys.argv[1])
i = 1
add = 0
while add < number:
    print(add)
    j = add
    add = add + i
    i = j


