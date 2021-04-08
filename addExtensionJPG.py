import os

path = "/Folder1/Folder2/Folder3/Target/"
os.chdir(path) #change directory
# print(os.getcwd()) #print current wording directory

# add file extensions to items in the directory that are not folders (i.e. files without extensions)

for file in os.listdir('.'):
    if not os.path.isfile(file): #if item is not a file (e.g. is a folder)
        continue 
        #skip current loop iteration
    head, tail = os.path.splitext(file) 
        #split pathname "/folder/file.txt" --> "/folder/file" + ".txt"
    if not tail: #empty strings considered false. We're making sure it doesn't have a file extension already
       source = os.path.join(path, file) #rejoin after having done split
       dest = os.path.join(path, file + '.jpg')

       if not os.path.exists(dest): # check that a file doesn't already exist with intended file rename
           os.rename(source, dest)