from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_38471.html"
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
count = []
# Retrieve all of the anchor tags
for tag in soup.find_all('span'):
    tag = str(tag)
    tag1 = tag.split('>')[1]
    tag2 = tag1.split('<')
    count.append(int(tag2[0]))
print('Sum: ',sum(count))
