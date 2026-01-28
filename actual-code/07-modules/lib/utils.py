class Shape:
  def __init__(self, type):
    self.type = type

  
triangle = Shape("triangle")

def insecure_printer(message):
  print("I'm about to print")
  print(message)
  print("Did I do okay? (insecurely)")

# insecure_printer("Hello from utils.py!")
if __name__ == "__main__":
  print(f"utils.py has a name of {__name__}")