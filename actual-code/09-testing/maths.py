# TDD -> Test Driven Development (red/green/refactor)

def add(a, b):
  # if a and b are not ints or floats raise a type error
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("Both arguments should be numbers.")

  if isinstance(a, bool) or isinstance(b, bool):
    raise TypeError("Both arguments should be numbers.") 
    
  return a + b
  return round(a + b, 8) # one possible fix for adding decimals

"""
- Pattern for writing
- Happy path
- Edge cases => unhappy
- Parameterization
---
- Mocking
- Integration/E2E
"""