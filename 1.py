import numpy as np


try:
    size = int(input("Введите размер матриц: "))
except ValueError:
    print("Введите число!")
    exit(-1)
if size < 0:
    print("Число должно быть > 0")
    exit(-1)

mat_a = np.random.randint(1, 101, (size, size))
mat_b = np.random.randint(1, 101, (size, size))

compare_sign = input("Введите знак для сравнения матриц: < > или ==: ")
mat_c = None
if compare_sign == "<":
    mat_c = mat_a < mat_b
elif compare_sign == ">":
    mat_c = mat_a > mat_b
elif compare_sign == "==":
    mat_c = mat_a == mat_b
else:
    print("Ошибка! Введено неверное значение")
    exit(-1)

print(mat_c)
