import urllib.request
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout = 1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")