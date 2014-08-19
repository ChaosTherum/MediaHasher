import hash, paths
files = {}

dirOrFile = input("Do you wish to scan a (1)File or a (2)Directory: ")

def file(mediaFile):
    hash.idmedia(mediafile)

def dir(directory):
    for i in paths.get_filepaths(directory):
        files[directory] = hash.idmedia(i)

if dirOrFile == 1:
    mediaFile = str(input("Please input the location of your file: "))
    file(mediaFile)
elif dirOrFile == 2:
    directoryInput = str(input("Please input the directory you wish to scan: "))
    print(dir(directoryInput))