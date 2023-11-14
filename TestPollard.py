from EllipticCurvesBig import EllipticCurve, Point
from PollardRhoBig import pollard_rho

curve = EllipticCurve(416,569,659)
a = Point(23,213,curve)
curve.setGenerator(a)

b = Point(150,25,curve)

print(
  pollard_rho(
    curve,  b
  )
)