# opens the file -> empties the file -> writes to it
with open("log.txt", mode="w") as file:
  file.write("Hello!\n")
  file.write("Python is cool!\n")
  file.write("Ministry of funny walks.")

with open("log2.txt", mode="a") as file:
  file.write("This is another line.\n")