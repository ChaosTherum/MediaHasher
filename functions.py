__author__ = 'Administrator'

def createSocket(socketName):
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit();

def connectSocket(host, port):
    s.connect((host, port))