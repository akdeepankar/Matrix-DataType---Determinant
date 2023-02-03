class Determinant:

  def __init__(self):
    self.order2()
    self.order3()

  def order2(a11, a12, b21, b22):
    temp1 = a11 * b22
    temp2 = a12 * b21
    temp = temp1 - temp2
    return (temp)

  def order3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    tempa1 = a22 * a33 - a23 * a32
    tempb1 = a21 * a33 - a31 * a23
    tempc1 = a21 * a32 - a31 * a22
    tempa = a11 * tempa1
    tempb = a12 * tempb1
    tempc = a13 * tempc1
    det = tempa - tempb + tempc
    return (det)


class Cramer(Determinant):

  def __init__(self):
    self.lieq2()

  def lieq2(a11, a12, b21, b22, b1, b2):
    det = Determinant.order2(a11, a12, b21, b22)
    print(det)

    if det == 0:
      print("Determinant of A is 0")
    else:
      ax1 = Determinant.order2(b1, a12, b2, b22)
      print(ax1)

      ax2 = Determinant.order2(a11, b1, b21, b2)
      print(ax2)

      x1 = int(ax1 / det)
      x2 = int(ax2 / det)
      print("x1 = ", x1, "\nx2 = ", x2)

  def lieq3(a11, a12, a13, a21, a22, a23, a31, a32, a33, b1, b2, b3):
    det = Determinant.order3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    print(det)

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
      