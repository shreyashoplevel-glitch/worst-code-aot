name = input("What is the name of your new file? ")

print("Type lines to write in the file.")
print("When you are finished, type: /done")

with open(name, "w") as f:
    while True:
        line = input("> ")
        if line.strip() == "/done":
            break
        f.write(line + "\n")

print(f"Created and wrote to file: {name}")
