class Determinant:

  def __init__(self):
    self.order2()
    self.order3()

  def order2(a11, a12, b21, b22):
    temp1 = a11 * b22
    temp2 = a12 * b21
    temp = temp1 - temp2
    return (temp)

  def order3(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    tempa1 = b2 * c3 - b3 * c2
    tempb1 = a2 * c3 - a3 * c2
    tempc1 = a2 * b3 - a3 * b2
    tempa = a1 * tempa1
    tempb = b1 * tempb1
    tempc = c1 * tempc1
    det = tempa - tempb + tempc
    return (det)
