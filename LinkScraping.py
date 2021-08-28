import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
import sys

n = int(sys.argv[1])-1
iterations = int(sys.argv[2])
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
target_list = []

for i in range(iterations):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    target_a = tags[n]
    target_ref = target_a.get('href',None)
    target_list += [target_a.string]
    url = target_ref

print(target_list[-1])
