file = open("test.txt", encoding="utf-8")

# .read()
contents = file.read()  # loads the whole as a str
print(contents)
print(type(contents))

# .readlines()
file.seek(0)  # move the cursor to the start
contents = file.readlines()  # returns a list
print(contents)
print(type(contents))

stripped_contents = [line.strip() for line in contents]

stripped_contents = []
for line in contents:
  stripped_contents.append(line.strip())

print(stripped_contents)

# .readline() - iterates over hte file, line by line without opening the whole thing
file.seek(0)
line = file.readline()

while line:
  print(line.strip())
  line = file.readline()


file.close()