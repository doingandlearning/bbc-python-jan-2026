# httpx
import requests

# URL  -> METHOD (GET/POST/PUT/PATCH/DELETE) -> parameters


response = requests.get("https://swapi.dev/api/people")
response.raise_for_status() 
data = response.json()

import json
with open("starwars.json", mode="w") as file:
  file.write(json.dumps(data, indent=1))
