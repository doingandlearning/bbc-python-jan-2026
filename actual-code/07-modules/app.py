import lib.utils as u  # namespacing!
from lib.utils import Shape, triangle
# import numpy as np
# import pandas as pd
import sys 
# print(sys.path)

from lib.utils import *

import os

print(os.cpu_count())

import requests

response = requests.get("https://api.github.com/users/doingandlearning")
data = response.json()
print(data)


# u.insecure_printer("Hello from app.py!")

# print(u.triangle.type)

# circle = u.Shape("circle")
# print(circle.type)

# parallelogram = Shape("parallelogram")
# print(parallelogram.type)

def main():
  print(f"app.py has a name of {__name__}")


if __name__ == "__main__":
  main()