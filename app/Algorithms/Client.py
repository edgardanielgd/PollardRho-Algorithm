from app.Algorithms.EllipticCurves import EllipticCurve, Point
import random

class AlgorithmClient:
  def __init__(self, curve : EllipticCurve, key : int, generateKey = True):
    self.curve = curve
    self.privKey = key

    # Calculate client's public key
    self.pubKey = None
    if generateKey:
      self.pubKey = curve.g * key

  def getPubKey(self) -> Point:
    return self.pubKey

  def encrypt(
    self, otherPubKey : Point, plainText : list[Point]
  ):
    b = random.randint(0, self.curve.order - 1)
    c1 = self.curve.g * b

    bA = otherPubKey * b

    output : list = []

    for m in plainText:
      output.append( m + bA )
    
    return (c1, output)

  def decrypt(
    self, c1 : Point, cipherText : list[Point]
  ):
    plainText : list = []
    c1a = -(c1 * self.privKey)
    
    for c2 in cipherText:
      plainText.append( c2 + c1a )

    return plainText