#This is a Personal Project Created by AK DEEPANKAR
#First Year, BS Data Science, IIT Madras (FEB, 2022)

class Determinant:

  def __init__(self):
    self.order2()
    self.order3()

  def order2(a11, a12, a21, a22):
    temp1 = a11 * a22
    temp2 = a12 * a21
    temp = temp1 - temp2
    if temp == 0:     
      print("Determinant is 0")
    else: 
      print(temp)
    
    return (temp)

  def order3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    tempa1 = a22 * a33 - a23 * a32
    tempb1 = a21 * a33 - a31 * a23
    tempc1 = a21 * a32 - a31 * a22
    tempa = a11 * tempa1
    tempb = a12 * tempb1
    tempc = a13 * tempc1
    det = tempa - tempb + tempc
    if det == 0:
      print("Determinant is 0") 
    else:
      print(det)
    
    return (det)


class Cramer(Determinant):

  def __init__(self):
    self.lieq2()

  def lieq2(a11, a12, a21, a22, b1, b2):
    det = Determinant.order2(a11, a12, a21, a22)

    if det == 0:
      print("Determinant of A is 0")
    else:
      ax1 = Determinant.order2(b1, a12, b2, a22)
      print(ax1)

      ax2 = Determinant.order2(a11, b1, a21, b2)
      print(ax2)

      x1 = int(ax1 / det)
      x2 = int(ax2 / det)
      print("x1 = ", x1, "\nx2 = ", x2)

  def lieq3(a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3):
    det = Determinant.order3(a11, a12, a13, a21, a22, a23, a31, a32, a33)

    if det == 0:
      print("Determinant of A is 0")
    else:
      ax1 = Determinant.order3(b1, a12, a13, b2, a22, a23, b3, a32, a33)
      print(ax1)

      ax2 = Determinant.order3(a11, b1, a13, a21, b2, a23, a31, b3, a33)
      print(ax2)

      ax3 = Determinant.order3(a11, a12, b1, a21, a22, b2, a31, a32, b3)
      
      print(ax3)

      x1 = ax1 / det
      x2 = ax2 / det
      x3 = ax3 / det
      print("x1 = ", ax1, "/", det, "=", x1)
      print("x2 = ", ax2, "/", det, "=", x2)
      print("x3 = ", ax3, "/", det, "=", x3)


class Adjugate(Determinant):

  def __init__(self):
    self.adj3()
    

  def adj3(a11, a12, a13, a21, a22, a23, a31, a32, a33):

    det = Determinant.order3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    print("Determinant: ", det)

    m11 = a22 * a33 - a23 * a32
    m12 = a21 * a33 - a23 * a31
    m13 = a21 * a32 - a22 * a31
    m21 = a12 * a33 - a13 * a32
    m22 = a11 * a33 - a13 * a31
    m23 = a11 * a32 - a12 * a31
    m31 = a12 * a23 - a13 * a22
    m32 = a11 * a23 - a13 * a21
    m33 = a11 * a22 - a12 * a21

    #cofactor matrix
    c11 = 1 * m11
    c12 = -1 * m12
    c13 = 1 * m13
    c21 = -1 * m21
    c22 = 1 * m22
    c23 = -1 * m23
    c31 = 1 * m31
    c32 = -1 * m32
    c33 = 1 * m33
    print(c11, c21, c31, c12, c22, c32, c13, c23, c33)
    return(c11, c21, c31, c12, c22, c32, c13, c23, c33)
    print("Cofactor Matrix")
    print(c11, " ", c12, " ", c13)
    print(c21, " ", c22, " ", c23)
    print(c31, " ", c32, " ", c33)

    #AdjugateMatrix = transpose of cofactor

    print("Adjugate Matrix")
    print(c11, " ", c21, " ", c31)
    print(c12, " ", c22, " ", c32)
    print(c13, " ", c23, " ", c33)


class Ainverse(Adjugate):

  def __init__(self):
    self.ainv3()

  def ainv3(a11, a12, a13, a21, a22, a23, a31, a32, a33):

    det = Determinant.order3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    c = Adjugate.adj3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    if det == 0:
      print("Inverse Does Not Exist")
    else:
      result = tuple([i * round(1 / det, 2) for i in c])
      print("A Inverse: ", result)
