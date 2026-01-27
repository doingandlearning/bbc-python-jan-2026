locations = ["London", "Salford", "Accrington", "Belfast", "Brighton"]

upper_cased_locations = []

for place in locations:
  if place.startswith("B"):
    upper_cased_locations.append(place.upper())

print(upper_cased_locations)

# code golf -> Pythonic -> Idiomatic Python
upper_cased_locations_2 = [ place.upper() for place in locations if place.startswith("B") ]

print(upper_cased_locations_2)