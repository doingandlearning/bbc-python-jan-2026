empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

#            -5       -4        -3       -2        -1
#             0        1         2        3         4
names = ("Ashleigh", "Ally", "Shalini", "Blair", "Blair")
print(names)
print(type(names))

print(names.count("Blair"))

target_name = "Christine"

if target_name not in names:
  print(f"{target_name} not in tuple.")
else:
  print(f"The first {target_name} is at index {names.index(target_name)}")

print(f"This tuple has {len(names)} elements.")

print(names[2])
print(names[1:3])
print(names[:4])
print(names[2:])
print(names[1:-2])

for name in names:
  print(f"{name} works at the bbc")


more_names = (names, ("Shazia", "Stuart", "Petra", "Alex"), ("Huzaib", "Lalitha"), ("Jamie", "Christine"))

# Petra
print("Petra")
print(more_names)
print(more_names[1][2])

names = set(names)
names = tuple(names)
print(names)


