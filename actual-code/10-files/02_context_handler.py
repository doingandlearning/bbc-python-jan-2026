# file = open("test.txt")
# print(file.read())
# file.close()

with open("test.txt") as file:
  print(file.read())
