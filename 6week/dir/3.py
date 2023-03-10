import os

print("Test a path exists or not:")
path = r"C:\Users\Айша\Desktop\1week\6week\dir\b.txt"
check = os.path.exists(path)
print(check)
if check:
    print("\nFile name of the path:")
    print(os.path.basename(path))

    print("\nDir name of the path:")
    print(os.path.dirname(path))

