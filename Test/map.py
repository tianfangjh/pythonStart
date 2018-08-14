numbers = {'one' : 1, 'two' : 2, 'three' : 3}
print(numbers['two'])
numbers['ninety'] = 90
print(numbers)
for i in numbers:
    print(i, numbers[i])

j = 0
while j < 10:
    print('j < 10')
    break

for n in range(20):
    if n % 2 == 0:
        continue
    print(n, end = ' ')

print('\n')

flag = True
n = int(input())

for s in range(2, n - 1):
    if n % s == 0:
        flag = False
        print("no\n")
        break
else:
    print('yes\n')


