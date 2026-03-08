# Ask user for name
name = input ("Whats your name: ").strip().title()

# Split users name into first name and last name
first, last = name.split(" ")

# Say hello to user
print (f"Hello, {first}")