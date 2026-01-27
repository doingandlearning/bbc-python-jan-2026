counter = 10

print(counter)

new_counter = None

def increase_counter():
  global counter
  global new_counter

  new_counter = counter
  print(f"inside function: {counter}")
  counter += 1
  print(f"New counter: {counter}")

increase_counter()
print(counter)

def increase_counter():
  print("Yo!")

increase_counter()

print(sum([1,2,3]))

def sum(numbers):
  return 0

print(sum([1,2,3]))