user_channel = input("What channel would you like to watch? ").lower().strip()

if user_channel == "bbc1" or user_channel == "bbc2":
  print("What are you going to watch now the Traitors is over?")
  print("or Time for University Channel")
# elif user_channel == "bbc2":  # elif -> contraction of else if
elif user_channel.startswith("sky") and user_channel.find("news") == -1:
  print("Not around here you won't!")
elif user_channel.startswith("bbc"):
  print("Great broadcaster!")
else:
  print("I don't know that channel.")

match user_channel:
  case "bbc1":
    print("What are you going to watch now the Traitors is over?") 
  case "bbc2":
    print("Time for University Channel")
  case _: # fallback, default
    print("Don't know that one!")
