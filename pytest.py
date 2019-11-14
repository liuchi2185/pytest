import requests
from bs4 import BeautifulSoup

url="http://www.baidu.com/s?wd=刘驰"
r = requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')

for result_table in soup.find_all('h3',class_='t'):
    a_click = result_table.find("a")
    print( "-----标题----\n" + a_click.get_text())
    print("----链接----\n" + str(a_click.get("href")))
