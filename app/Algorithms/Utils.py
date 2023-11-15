def multiplicative_inverse( number : int, modulus : int):
  return pow( number, -1, modulus )

def power( number: int, exp: int, mod : int):
  return (number ** exp) % mod