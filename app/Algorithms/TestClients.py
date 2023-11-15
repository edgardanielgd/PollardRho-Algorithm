from app.Algorithms.EllipticCurves import Point, EllipticCurve
from app.Algorithms.Client import Client

curve = EllipticCurve(416,569,659)
g = Point(23,213,curve)
curve.setGenerator(g)

clientA = Client(
  curve, 10
)

plain = [
  Point(381, 307, curve)
]

clientB = Client(
  curve, 25
)

cipher = clientB.encrypt(
  clientA.getPubKey(),
  plain
)

plainAgain = clientA.decrypt(
  cipher[0], cipher[1]
)

print(
  clientA.getPubKey(),
  cipher[0], cipher[1][0], plainAgain[0]
)