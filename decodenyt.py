import requests
from bs4 import BeautifulSoup
r_html = ""


def writenythtml():
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text
    with open('files/nyt.html', 'a') as write_html:
        write_html.writelines(str(r_html))


def readhtml():
    global r_html
    with open('files/nyt.html') as read_html:
        r_html = read_html.read()


def souplesse():
    global r_html
    soup = BeautifulSoup(r_html, features="html.parser")
    title = soup.find('h2')
    print(title)


readwrite = input('w: write only\n'
                  'r: read & souplesse\n')


if readwrite == 'w':
    writenythtml()
elif readwrite == 'r':
    readhtml()
    souplesse()
