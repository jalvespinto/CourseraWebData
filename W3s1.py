import socket
import urllib.parse

fhand = 'http://data.pr4e.org/intro-short.txt'
url = urllib.parse.urlparse(fhand)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((url.hostname, 80))
cmd = 'GET /data.pr4e.org/intro-short.txt HTTP/1.1\r\nHost: www.data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()
