user1 = {
  "nae": "Alex",
  "tea": "SW Grad",
  "interests": ["Scala", "Python"]
}

user2 = {
  "name": "Shazia",
  "team": "Participation",
  "interests": ["Data science", "Testing"]
}

class WebUser:
  def __init__(self, name, team, interests):  # `this``
    self.name = name
    self.team = team
    self.interests = interests
  
  def __str__(self):  # human readable, appears in logs, useful for debugging
    return f"WebUser with name {self.name} who works in {self.team} and cares about {self.interests}"
  
  def __repr__(self): # Machine readble
    return f"WebUser(name='{self.name}', team='{self.team}', interests={self.interests})"

  def is_interested_in(self, topic):
    return topic in self.interests


# new -> instantiating a new object/instance -> new'ing up -> __init__
user3 = WebUser(name="Lalitha", team="Discoverability", interests=["ML", "Testing"])   

if user3.is_interested_in("ML"):
  print("PyTorch is an important library there.")


# print(user1)

# # print -> what class are you? -> do you have a __str__? -> give me the result__str__
# print(user1)
# print(user3)
# print([user1, user2, user3])
# print(user3.name)
# print(user3.interests)