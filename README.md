# Matrix-Library / DataType
Made Using Object Oriented Programming Concepts such as Classes, Methods, Inheritance and Polymorphism.
After Creating an Object for the Class, The Methods take inputs for Order 2 and 3 Type Matrix and give the result of its Determinant. 
As Well as you can Find The value of x y z using Cramers Rule in a System of Linear Equation of order 2 and 3 in the Form of Ax = B. 
The Adjugate/Adjoint of a Matrix along with its cofactor Matrix as well as the Inverse of a Matrix.

![Matrix](https://user-images.githubusercontent.com/62662701/215990008-2cc7d7d9-b7f7-4089-9ea4-e28583c6bc97.png)

You can use this by Importing the matrix library file.
Then creating an object by calling the Determinant class and its order2 or order3 methods.
The argument will be taken according to order.
and finally you can get the answer by printing the object for that class.

Some Examples:

from matrix import Determinant
from matrix import Cramer
from matrix import Adjugate, Ainverse

mat = Determinant.order3(1,2,3,4,5,6,7,8,9)
mat2 = Determinant.order2(4, -2, -8, 4)
mat22 = Cramer.lieq2(4, -3, 6, 5, 11, 7) #Last 2 Arguments are X #lieq2 is Linear Equation In Matrix Order 2
mat23 = Cramer.lieq3(1,2,3,4,5,6,7,8,9,2,3,4) #Last 3 Arguments are X #lieq3 is Linear Equation In Matrix Order 3
ainv = Ainverse.ainv3(1,2,3,4,5,6,7,8,9) #ainv3 is A inverse of Matrix Order 3
adju = Adjugate.adj3(1,2,3,4,5,6,7,8,9) #adj3 is Adjugate of Matrix Order 3

Thats till Now.
Happy Learning.
