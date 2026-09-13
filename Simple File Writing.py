# Ask the user to enter their name.
# Open a file named name.txt.
# Write the name into the file.
# Close the file.



name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()
print("Name saved successfully.")