empty_list = []
print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]

print(len(beatles))
print(beatles[1])
print(beatles[1:])

print("John" in beatles)
print("Kevin" in beatles)

for band_member in beatles:
  print(f"{band_member} was in the beatles")
  print(f"{band_member} is {len(band_member)} letters long.")

# Add things to the list ... 
beatles.append("Ally") # cheap operation ... 
print(beatles)

beatles.insert(0, "Shazia")  # computational expensive operation ... 
print(beatles)

beatles.extend(["Kevin", "Blair", "Shalini", "Petra", "Kevin"])
print(beatles)

# Remove ...
while "Kevin" in beatles:
  beatles.remove("Kevin") 

print(beatles)

# Multiple elements we delete slice/sublist
del beatles[0:2]

print(beatles)

# beatles.sort()
sorted_beatles = sorted(beatles, reverse=True)
print(beatles)
print(sorted_beatles)

beatles.reverse()
reversed(beatles)

# unpacking -> destructuring
cities = ["Glasgow", "Birmingham", "London", "Newcastle"]
city_1 = cities[0]
city_2 = cities[1]
city_3 = cities[2]
city_4 = cities[3]

city_1, city_2, city_3, city_4 = cities
print(city_4)

# rest operator
city_1, city_2, *rest_of_the_cities = cities
print(city_1)
print(rest_of_the_cities)

bands = [
    ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],      # Queen
    ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
    ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"],   # The Rolling Stones
    ["Beyoncé", "Kelly Rowland", "Michelle Williams"],                   # Destiny's Child
    ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # The Beatles
    ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Phil Selway"],  # Radiohead
    ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."],            # U2
    ["Chris Martin", "Guy Berryman", "Jonny Buckland", "Will Champion"], # Coldplay
    ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri"],       # Blondie
    ["Jack White", "Meg White"]                                          # The White Stripes
]
print(bands[1][2])


new_beatles = beatles.copy()

print(beatles)
print(new_beatles)

new_beatles.append("Christine")

print(beatles)
print(new_beatles)


tuple_of_bands = (beatles, ["Ethan", "Emerald"])
print(tuple_of_bands)

tuple_of_bands[0].append("Shalini")
print(tuple_of_bands)