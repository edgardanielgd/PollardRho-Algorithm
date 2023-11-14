import random

from EllipticCurvesBig import EllipticCurve, Point

#### Actual Pollard's Rho algorithm
S1 = set([])
S2 = set([])
S3 = set([])

P = Point(1,1,curve)
Q = Point(2,2,curve)

def iterating_function( Ri : Point, ai : int, bi : int ):
  if item in S1:
    ai1 = ai + 1
    bi1 = bi
    Ri1 = Ri + P
  elif item in S2:
    Ri1 = Ri + Ri
    ai1 = 2 * ai
    bi1 = 2 * bi
  else:
    Ri1 = Ri + Q
    ai1 = ai
    bi1 = bi + 1
  return Ri1, ai1, bi1

def pollard_rho( ):
  aArr = random.randint(0, curve.modulus - 1)
  b0 = random.randint(0, curve.modulus - 1)
  i = 0
  Rarr = { 0 : P * a0 + Q * b0 }

  while Rarr[i] != Rarr[2*i]:
    Ri1[i+1] = iterating_function(Rarr[i], )

  

p1 = Point(2, 2, curve)
p2 = Point(4, 8, curve)
p3 = p1 + p2

print(p3)