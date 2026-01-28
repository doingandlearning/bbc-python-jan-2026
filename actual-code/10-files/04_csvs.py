import csv
import json

with open("movies.csv") as file:
  reader = csv.DictReader(file)
  movies = []
  for line in reader:
    movies.append(line)

with open("movies.json", mode="w") as file:
  file.write(json.dumps(movies, indent=1))

with open("movies.json") as file:
  movies = json.loads(file.read())
  print(type(movies))
  print(type(movies[0]))

# with open("movies.csv", mode="a") as file:
#   # writer = csv.DictWriter(file, ["Title","Year","Director","Genre"])
#   # writer.writerow({
#   #  "Title": "Sinners",
#   #  "Year": "2025",
#   #  "Director": "Ryan Coogler",
#   #  "Genre": "Horror"
#   # })
#   writer = csv.writer(file)
#   writer.writerow(["Sinners", "2025", "Ryan Coogler", "Horror"])