import os
path = r"C:\Users\Айша\Desktop\1week\6week\dir\demofile.txt"
check2 = os.path.exists(path)
if check2:
     os.remove("demofile.txt")