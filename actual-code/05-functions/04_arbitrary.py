def add(a, b, c = 0, d = 0):
  if isinstance(b, tuple):
    numbers = b
    b = 0
    for number in numbers:
      b += number
  return a + b + c + d

def add_list(numbers):
    total = 0
    for number in numbers:
      total += number
    return total

print(add(1,(2, 3)))
print(add(1,(2,3,4)))
print(add(1,2))
print(add(1, 2, 3))
print(add(1,2,3,4))

print(add_list([1,2,3,4]))

def add(*numbers):
    print(numbers)
    total = 0
    for number in numbers:
      total += number
    return total

print(add(1,2))
print(add(1, 2, 3))
print(add(1,2,3,4))

print(1,2,3,4,5,6,7)


print(sum([1,2,3], start=10))