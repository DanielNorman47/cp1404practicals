for i in range(1, 21, 2):
    print(i, end=' ')
print()


for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

for i in range(int(input("Number of stars:"))):
    print("*", end='')
print()

for i in range(0, int(input("Number of stars (increasing):")), 1):
    for j in range(0, i + 1, 1):
        print("*", end='')
    print()
print()