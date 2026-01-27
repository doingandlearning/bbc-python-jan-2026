# input -> function -> output
# def <name_of_the_function> (argument list)
def print_message(message, seperator="=", seperator_length=10):
  """
  A function to print messages.

  :message: The message to print
  """
  print(seperator * seperator_length)
  print(message)
  print(seperator * seperator_length)

value = print_message("Hello from Glasgow", "=", 20)
print_message("Hello from Belfast", "*", 15)
print_message(seperator_length=15, message="Hello from London" )



