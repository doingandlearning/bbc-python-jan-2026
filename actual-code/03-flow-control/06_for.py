# for letter in "Jamie Gilman":  # iterate
#   print(letter)

target = int(input("What number do you want? "))

for value in range(10):
  if value == 3:
    print("I don't think I'll check this one")
    continue  # ignores the rest of the current run, and moves on to the next value
  print(f"Checking {value} to see if it matches {target}")
  if target == value:
    print("Found it!")
    break  # escape the parent loop early!