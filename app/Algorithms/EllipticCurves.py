from app.Algorithms.Utils import multiplicative_inverse, power
from app.Algorithms.Constants import ALPHABET

class Point:

  def __init__(self, x, y, curve):
    self.x : int = x
    self.y : int = y
    self.curve = curve
  
  def __add__(self, other):
    I = self.curve.I
    p = self.curve.modulus
    if self == I:
      return Point(other.x, other.y, self.curve)
  
    if other == I:
      return Point(self.x, self.y, self.curve)
  
    if self.x == other.x and self.y != other.y:
      return Point(None, None, self.curve)
  
    if self.x != other.x:
      numerator = (other.y - self.y) % p
      denominator = (other.x - self.x) % p
      m = (numerator * multiplicative_inverse(
        denominator, p
      )) % p
  
      new_x = int(
        power(m,2,p) - self.x - other.x
      ) % p
      new_y = int(m * (self.x - new_x) - self.y) % p
  
      return Point(new_x, new_y, self.curve)
  
    if self == other:
      numerator = (3 * power(self.x,2,p) + self.curve.a) % p
      denominator = (2 * self.y) % p
  
      #m = int(numerator / denominator) % self.curve.modulus
      m = numerator * multiplicative_inverse(
        denominator, p
      ) % p
      new_x = (power(m,2,p) - 2 * self.x) % p
      new_y = (m * (self.x - new_x) - self.y) % p
  
      return Point(new_x, new_y, self.curve)
  
  def __mul__(self, exp : int):
    if exp <= 0:
      return self.curve.I
  
    if exp == 1:
      return Point(self.x, self.y, self.curve)
  
    return self + self * (exp-1)
  
  def __eq__(self, other):
    return (self.x == other.x and self.y == other.y)

  def __neg__(self):
    return Point(
      self.x,
      ((-self.y) % self.curve.modulus),
      self.curve
    )
    
  def __str__(self):
    return f"({self.x}, {self.y})"
  
class EllipticCurve:
  def __init__(self, a : int, b : int, m : int):
    self.a = a
    self.b = b
    self.modulus = m
    self.g = None

    # Calculate all y exponents as a cache
    self.y2Exps = {}
  
    for y in range(self.modulus):
      y2 = power(y,2,self.modulus)
  
      if y2 not in self.y2Exps:
        self.y2Exps[y2] = [ y ]
      else:
        self.y2Exps[y2].append(y)

    # Calculate all possible points
    self.I = Point(None, None, self)
    self.allPoints = []
    self.char2Points = {}
    self.point2Char = {}

    # Iterate over all values of X in F_n
    for x in range(self.modulus):

      # Evaluating x^3 + ax + b
      right_result = (
        power(x,3,self.modulus) + self.a * x + self.b
      ) % self.modulus

      # Seek for values on y in F_n that can get the same result with y^2
      if right_result in self.y2Exps:
        values = self.y2Exps[right_result]

        for y in values:
          self.allPoints.append(Point(x,y,self))
          self.char2Points[(x,y)] = chr(len(self.allPoints) + 31)

    self.allPoints = sorted(self.allPoints, key=lambda item: item.x)
    self.allPoints.insert(0, self.I)

    # Create a dictionary to map points to chars in alphabet
    for i in range(len(ALPHABET)):
      point = self.allPoints[i]
      self.point2Char[(point.x, point.y)] = ALPHABET[i]
      self.char2Points[ALPHABET[i]] = self.allPoints[i]
    
    self.order = len(self.allPoints)
  
  def setGenerator(self, g : Point):
    self.g = g

  def compressPoint(self, point : Point):
    return (point.x, point.y % 2 == 0)

  def decompressPoint(self, compressed):
    x, is_even = compressed
    
    y_2 : int = (
      power(x,3,self.modulus) + self.a * x + self.b
    ) % self.modulus
    
    y : int = self.y2Exps[y_2]

    if is_even and y & 1:
      return Point(x, y, self)

    return Point(x, self.modulus - y, self)

  