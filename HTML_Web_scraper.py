from urllib.request import urlopen
from bs4 import BeautifulSoup
  
htmldata = urlopen('https://www.ey.com/en_uk/careers/students')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')

for item in images:
    print(item['src'])
    print(item['alt'])