import os
os.mkdir('spam')
os.chdir('spam')
for i in range(10):
    os.mkdir(str(i))
    for j in range(10):
        os.chdir(str(i))
        os.mkdir(str(j))
        os.chdir('..')
