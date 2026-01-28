def get_valid_input():
  try:
    number = int(input("Give me a number: "))
    return number
  except ValueError:
    print("That's not a number.")
    return get_valid_input()

print(get_valid_input())