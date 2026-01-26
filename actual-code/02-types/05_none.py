first_string = "Hi there how are you i am fine" * 1000
second_string = "Hi there how are you i am fine" * 1000

print(first_string != second_string)
print(first_string is not second_string)

first_string = None
second_string = None

print(first_string is not second_string)

