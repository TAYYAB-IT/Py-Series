import requests
from bs4 import BeautifulSoup as bs
x=requests.get("https://pypi.org/project/beautifulsoup4/")
parse=bs(x.content,parser="html.parser")
print(parse.title)