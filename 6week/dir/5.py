color = ["colum", "word", "number"]
with open('test.txt', "w") as f:
        for i in color:
                f.write("%s\n" % i)
content = open('test.txt')
print(content.read())
