#from matrix import Determinant
from matrix import Cramer
#from matrix import Adjugate, Ainverse

#mat = Determinant.order3(1,2,3,4,5,6,7,8,9)
#print(mat)

#mat2 = Determinant.order2(1, 2, 2,5)
#print(mat2)

#mat22 = Cramer.lieq2(4, -3, 6, 5, 11, 7)
#print(mat22)

mat23 = Cramer.lieq3(7,2,1,0,3,-1,-3,4,-2,9,4,3)

#adju = Adjugate.adj3(1,2,3,0,2,8,5,6,0)
#print(adju)
#ainv = Ainverse.ainv3(1,2,3,4,5,6,7,8,9)
#adju = Adjugate.adj3(1,2,3,4,5,6,7,8,9)
