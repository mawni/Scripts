import os

path = "/Folder1/Folder2/Folder3/Target/"
os.chdir(path) #change directory
# print(os.getcwd()) #print current wording directory

# change file extensions of all files in the 'path' folder but NOT subdirectories/subfolders
def changeExt(targetDir):
    os.chdir(targetDir)
    for file in os.listdir('.'): #iterate through all items within current directory
        if os.path.isfile(file): #if it is a file (NOT folder)
            head, tail = os.path.splitext(file)
            source = head+tail #recombine
            os.rename(source, head+".jpg") #change extension

#changes file extensions in 'path' directory and all subdirectories
def walk_dir(targetDir): 
    topDown = True #modify dirnames in-place. traverse subfolders as well
    for dirpath, dirnames, filenames in os.walk(targetDir, topDown):
        for name in filenames:
            os.rename(targetDir+name, targetDir+name.replace(".png",".jpg"))

changeExt(path)