import os
print('Exist:', os.access('b.txt', os.F_OK))
print('Readable:', os.access('b.txt', os.R_OK))
print('Writable:', os.access('b.txt', os.W_OK))
print('Executable:', os.access('b.txt', os.X_OK))