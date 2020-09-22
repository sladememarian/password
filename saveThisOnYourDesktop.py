import os
file = open("pass.txt", "r+")
Pass = file.readline()
print(Pass)
os.system("git add .")
os.system("git commit -m \"first commit\"")
os.system("git push")
