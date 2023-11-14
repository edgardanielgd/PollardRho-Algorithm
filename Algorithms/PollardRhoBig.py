from EllipticCurvesBig import EllipticCurve, Point
from Utils import multiplicative_inverse
import math
import random

def pollard_rho(
  curve: EllipticCurve,
  Q: Point,
  max_iter: int = 1000
):
  P : Point = curve.g
  S : list = curve.allPoints
  order : int = curve.order

  # Partition of points in subsets (3 by default)
  S1 : list = []
  S2 : list= []
  S3 : list= []

  for point_id in range(order):
    if point_id % 3 == 0:
      S1.append(S[point_id])
    elif point_id % 3 == 1:
      S2.append(S[point_id])
    else:
      S3.append(S[point_id])

  # Define iter function to use
  def iterating_function( Ri : Point, ai : int, bi : int ):
    if Ri in S1:
      Ri1 = Ri + P
      ai1 = ai + 1
      bi1 = bi
    elif Ri in S2:
      Ri1 = Ri + Ri
      ai1 = 2 * ai
      bi1 = 2 * bi
    else:
      Ri1 = Ri + Q
      ai1 = ai
      bi1 = bi + 1
    return Ri1, ai1, bi1
    
  # Initi a,b and R arrays
  aArr = { 0 : random.randint(0, order - 1) }
  bArr = { 0 : random.randint(0, order - 1) }
  Rarr = { 0 : P * aArr[0] + Q * bArr[0] }
  
  i = 0

  while (i == 0 or Rarr[i] != Rarr[2*i]) and i < max_iter:
    
    Rarr[i+1], aArr[i+1], bArr[i+1] = iterating_function(
      Rarr[i], aArr[i], bArr[i]
    )

    tmpR, tmpA, tmpB = iterating_function(
        Rarr[2*i], aArr[2*i], bArr[2*i]
    )

    Rarr[2*(i+1)], aArr[2*(i+1)], bArr[2*(i+1)] = iterating_function(
      tmpR, tmpA, tmpB
    )
    
    i += 1

    print(
      i, Rarr[i], aArr[i], bArr[i],
      Rarr[2*i], aArr[2*i], bArr[2*i]
    )

  d = math.gcd(
    bArr[2*i] - bArr[i],
    order
  )

  if d == 1:
    return ((
      aArr[2*i] - aArr[i]
    ) * multiplicative_inverse(
      bArr[i] - bArr[2*i],
      order
    )) % order

  return order