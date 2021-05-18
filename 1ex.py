import sys

a = list(map(int, input().split()))
if len(a) != 10:
    print("Неверный размер списка", file=sys.stderr)
    exit(1)

for elem in a:
    if (elem > 8 and elem < 18 and elem % 10 == 0):
        res *= elem
    else:
        print(0)
