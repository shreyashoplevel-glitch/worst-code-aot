from input import filename
def openfile():
    with open(filename, 'r+') as f:
        content = f.read()
        print(content)

        f.write("new text here")