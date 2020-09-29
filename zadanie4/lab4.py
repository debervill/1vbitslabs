a = []
m = []

for count in range(10):
    m.append(float(input("Введите m"+str(count)+" ")))

for count in range(9):
    a.append(float(input("Введите m"+str(count)+" ")))

sum_m = 0

for count in range(10):
    sum_m = sum_m + (m[count] + 0.75) ** 2

sum_a = 0

for count in range(9):
    sum_a = sum_a + a[count]

proizv = 1

for count in range(9):
    proizv = proizv * m[count]

s = (sum_m -  sum_a) / proizv

print("S = " + str(s))