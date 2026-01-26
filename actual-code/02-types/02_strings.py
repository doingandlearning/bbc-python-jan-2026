first_name = "Kevin"
last_name = "Cunningham"

# concatenation -> join together
full_name = first_name + " " + last_name
print(full_name)
# print("Hello " + first_name + " how are you today?")

# f-string (format string)
print(f"{ first_name } { last_name } favourite number is { 40 + 2 }")

print("My favourite number is " + str(42))
'He said "Hello"'

"I don't know"

print("First line\nsecond line") 
print('First line\nsecond line')
print('''First line
second line''')


print(len(first_name))
print(first_name.upper())
print(first_name.center(14))
print(first_name.rjust(14))

print(full_name.find("in"))



print(full_name.isdigit())
my_favourite_number = "42 "
print(my_favourite_number.isdigit())



#    0123456789
"Kevin Cunningham"

print(full_name[9])  # single number -> what's there?
print(full_name[1:7])  #  from : up-to (but not including)
print(full_name[:7])
print(full_name[7:])

print(full_name.count("in"))
first_time = full_name.find("in")
print(full_name[first_time + 1:].find("in"))

