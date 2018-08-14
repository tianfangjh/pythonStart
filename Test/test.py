# author 姜华
a = [i for i in range(10) if i % 3 > 0]
print(a)

b = [j ** 2 for j in range(10)]
print(b)

for value in [2, 4, 6, 8, 10]:
    print(value + 1, end = ' ')

midpoint = 5
lower = []
upper = []
for i in range(10):
    if i < midpoint:
        lower.append(i)
    else:
        upper.append(i)

print(lower, end = "\n")
print(upper)
x = 1
x = "hello"
print(x)