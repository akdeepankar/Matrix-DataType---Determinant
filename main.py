from matrix import Determinant
from matrix import Cramer

mat = Determinant.order3(1, 0, 1, -1, 1, 1, 0, -1, 1)
print(mat)

mat2 = Determinant.order2(4, -2, -8, 4)
print(mat2)

mat22 = Cramer.lieq2(4, -3, 6, 5, 11, 7)
print(mat22)

mat23 = Cramer.lieq3(1, 0, 3, 0, 2, 5, 4, 3, 1, 0, 2, 1)
print(mat23)

