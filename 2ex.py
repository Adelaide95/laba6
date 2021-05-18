a = list(map(float, input("Введите список:").split()))
C = float(input("С="))
m = 0
n = 0
count = 0
for elem in a:
    if elem > C:
        count += 1
print("Количество чисел больших С:",
      count)
max_elem = 0


for i, item in enumerate(a):
    elem_abs = abs(item)
    if elem_abs > max_elem:
        max_elem, max_elem_ind = elem_abs, i

if max_elem_ind == len(a) - 1:
    print(0)
else:
    s = 1
    for i in enumerate(a, 0):
        if m < i[1]:
            m = i[1]
            n = i[0]
    c = a[n:]
    g = a[n * 1:]
    s *= g
    print("Произведение чисел после максимального по модулю числа", s)

a_pos = []
a_neg = []

for elem in a:
    if elem >= 0:
        a_pos.append(elem)
    else:
        a_neg.append(elem)

print("Список сначала с отрицательными, а потом позитивными числами:", a_neg + a_pos)