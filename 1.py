import sys

a = list(map(int, input().split()))
if len(a) != 10:
    print("Неверный размер списка", file=sys.stderr)
    exit(1)
a_fil = []
for elem in a:
    if elem > 8 and elem < 18 and elem % 10 == 0:

        a_fil.append(elem)

if len(a_fil) == 0:
    print(0)
else:
    res = 1
    for elem in a_fil:
        res *= elem
print(res)