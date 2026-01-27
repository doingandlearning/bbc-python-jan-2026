def add(a, b):
  """
  Add some numbers
  
  :param a: First
  :param b: second
  """
  return a + b


print(add(1,2))
print(add(2,4))

def stats(a,b):
  sum = a + b
  diff = a - b
  product = a * b
  quotient = a / b
  return {"sum":sum, "diff":diff, "product":product, "quotient":quotient}
  # return sum, diff, product, quotient  # return a tuple of these values.

print(stats(4,5))




