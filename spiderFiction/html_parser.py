from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    def get_new_data(self, page_url, soup):
        res_data = []
        anodes = soup.find_all('p')
        for anode in anodes:
            res_data.append(anode.get_text())
        
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_data = self.get_new_data(page_url, soup)

        return new_data