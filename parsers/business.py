from bs4 import BeautifulSoup
import requests
from .constants import headers
import pprint


def parse_page(idx):
    html = requests.get("http://biz.ssu.ac.kr/bbs/list.do?&bId=BBS_03_NOTICE&sc_title=&page={}".format(idx),
                        headers=headers).text
    bs = BeautifulSoup(html, 'html.parser')
    bList = bs.find("ul", {"id": "bList01"})
    divs = bList.find_all("div")
    ret = []
    i = 0
    while i < len(divs) - 2:
        parsed_item = dict()
        parsed_item["title"] = divs[i].text.strip()
        parsed_item["link"] = "http://biz.ssu.ac.kr{}".format(divs[i].find('a')['href'])
        parsed_item["date"] = divs[i + 1].find("span").text[0:10]
        ret.append(parsed_item)
        i = i + 3

    return ret


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))

    return notices
