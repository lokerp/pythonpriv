import numpy as np

try:
    size = int(input("Введите размер матриц: "))
except ValueError:
    print("Введите число!")
if size < 0:
    print("Число должно быть > 0")
    exit(-1)

mat_a = np.random.randint(1, 101, (size, size))

print(mat_a)
print("Номер столбца, сумма чисел в котором минимальна:", np.argmin(np.sum(mat_a, axis=0)))