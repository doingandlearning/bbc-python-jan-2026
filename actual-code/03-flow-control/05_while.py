user_input = input("Enter your password: ")
password = "password123"
attempts_tried = 1

while user_input != password and attempts_tried < 3:
  print("Unauthorized. Please try again.")
  attempts_tried += 1
  user_input = input("Enter your password: ")

if attempts_tried < 3:
  print("Here are your secret documents.")