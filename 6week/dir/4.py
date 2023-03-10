def file(name):
    with open(name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


print("Number of lines in the file: ", file("test.txt"))
