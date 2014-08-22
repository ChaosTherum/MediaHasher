import classes, paths
files = {}

dirOrFile = int(input("Do you wish to scan a (1)File or a (2)Directory: "))

if dirOrFile == 1:
    inputFile = str(input("Please input the location of your file: "))
    file = classes.mediaFile()
    file.idmedia(inputFile)

elif dirOrFile == 2:
    directoryInput = str(input("Please input the directory you wish to scan: "))
    print(dir(directoryInput))