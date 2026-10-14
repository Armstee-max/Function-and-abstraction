with open("text.txt", "w") as file:
    file.write("Welcome To python")


with open("text.txt", "a") as file:
    file.write("\nAdding text")


with open("text.txt", "r") as file:
    content = file.read()
    print(content)
