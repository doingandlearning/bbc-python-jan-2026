# lambda -> anonymous functions 

# ->   =>

def add(a, b):
  print("I'm about to add!")
  return a + b 
 
# throw-away, one-off, bespoke ... functions!
# functions are first class!
add_lambda = lambda a, b: a + b

print(add(1,2))
print(add_lambda(1,2))

place_names = ["Salford", "Glasgow", "Essex", "London", "Belfast"]

def uppercase(word):
  return word.upper()

print(list(map(uppercase, place_names)))
print(list(map(lambda w: w.upper(), place_names)))

people = [
    {"name": "Alice",   "age": 34, "score": 82},
    {"name": "Bob",     "age": 28, "score": 91},
    {"name": "Charlie", "age": 41, "score": 67},
    {"name": "Diana",   "age": 30, "score": 88},
    {"name": "Eve",     "age": 22, "score": 95},
]

# .sort()
def get_age(person):
  return person.get("age")

print(sorted(people, key=get_age)) 
print(sorted(people, key=lambda person: person["name"])) 

def get_score(person):
  return person.get("score")

print(sorted(people, key=get_score))