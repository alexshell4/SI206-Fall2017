from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = []
url = input('Enter - ')
links = 0

while links < 7:
    tags = []
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag1 = soup('a')

    for x in range(8):
        for tag in tag1:
            tags.append(tag)

    url = tags[17].get('href',None)
    urls.append(url)
    links += 1

response = re.findall('by_([^ ]*).html',url)
print(response[0])
