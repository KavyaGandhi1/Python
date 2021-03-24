#take two inputs from user
#1)user name
#2)single character

# output - 2lines
# 1) user's name length
# 2) count the numbers of characters that user inputed (bonus: case insensitive count)

name,character = input("Enter Your name and anyone character inside Your name seperated by comma: ").split(",")

print(f"Length Of Your Name is {len(name)}.\nCharacter count:{name.lower().count(character.lower())}.")