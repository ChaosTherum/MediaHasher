import hashlib
__author__ = 'david'

class mediaFile:
    def __init__(self):
        self.album = ""
        self.artist = ""
        self.day = 0
        self.ep = 0
        self.format = ""
        self.genre = ""
        self.hash = ""
        self.horiRes = ""
        self.mediaType = ""
        self.month = 0
        self.newDirectory = ""
        self.originDirectory = ""
        self.publisher = ""
        self.se = ""
        self.series = ""
        self.title = ""
        self.trackNum = 0
        self.vertiRes = ""
        self.year = 0

#Attribution #2
    def idmedia(self, inputMedia):
        BLOCKSIZE = 65536
        hasher = hashlib.sha256()
        with open(inputMedia, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        self.hash = hasher.hexdigest()

    def checkDatabase(self, hash):