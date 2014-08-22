import hashlib
__author__ = 'david'

class mediaFile:
    def __init__(self):
        self.originDirectory = ""
        self.newDirectory = ""
        self.series = ""
        self.se = ""
        self.ep = 0
        self.title = ""
        self.hash = ""
        self.year = 0
        self.month = 0
        self.day = 0
        self.format = ""
        self.album = ""
        self.trackNum = 0
        self.artist = ""
        self.publisher = ""
        self.vertiRes = ""
        self.horiRes = ""
        self.genre = ""
        self.mediaType = ""


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