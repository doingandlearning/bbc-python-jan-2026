empty_dict = {}
print(empty_dict)
print(type(empty_dict))

user_dict = {
  "name": "Petra",
  "team": "Responsible AI",
  "languages": ["C#", "Python", "Java"]
}

print(user_dict["name"])
print(user_dict.get("name", "Unknown")) # safer way to access data from a dict

print("Petra" in user_dict)
print("name" in user_dict)

print(user_dict.keys())
print(user_dict.values())
print(user_dict.items())

for field in user_dict.items():
  print(f"Key {field[0]} has value {field[1]}.")

# improve with unpacking
for key, value in user_dict.items():
  print(f"Key { key } has value { value }.")