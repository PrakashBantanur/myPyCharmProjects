# file = open('my_files.txt')
# content = file.read()
# print(content)
# file.close()

# read mode
with open("/Users/PSB/Desktop/my_files.txt") as file:
    content = file.read()
    print(content)

# # Write mode with new file creation
# with open("new_file.txt", mode = 'w') as file:
#     file.write("What is your fevorite place")
#
# # append with new lines
# with open("my_files.txt", mode='a') as file:
#     file.write("\nMy native is Amingad")

