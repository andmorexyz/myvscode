import os#ファイルパスを組みたてる為

import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self,site):
        self.site = site


    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)#BSはすごい
        for tag in sp.find_all("a"):#aはhtmlの<a></a>のリンクを抜き出す為の引数
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                os.path.join("Users")#ファイルパス合ってるかわからん。
                with open("link.txt","w") as f:#link.txtを作成して書き込みたい。合ってるかわからない
                    f.write("\n" + url)


news = "https://news.google.com/"
Scraper(news).scrape()
