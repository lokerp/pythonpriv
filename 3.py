import numpy as np

f = open("leq.txt", "r")
try:
    size = int(f.readline())
except ValueError:
    print("Неверные данные в файле")
    exit(-1)
try:
   coef = np.loadtxt(f, ndmin=2)
except ValueError:
    print("Неверные данные в файле")
    exit(-1)
f.close()

mat_a = coef[:, :-1]
mat_b = coef[:, -1:]
if (size != mat_a.shape[0] or size != mat_a.shape[1]):
    print("Неверные данные в файле")
    exit(-1)

mat_x = np.linalg.solve(mat_a, mat_b)
print(mat_x)
