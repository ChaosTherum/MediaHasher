import hashlib


def idmedia(mediaFile):
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    with open(mediaFile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()