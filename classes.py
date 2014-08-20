import hashlib,
__author__ = 'david'

class mediaFile:
    def __init__(self,originDirectory):
        originDirectory = ""
        newDirectory = ""
        series = ""
        se = ""
        ep = 0
        epTitle = ""
        hash = ""

    def idmedia(mediaFile):
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    with open(mediaFile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    hash = hasher.hexdigest()