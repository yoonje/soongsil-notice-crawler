from bs4 import BeautifulSoup
import requests
import pprint
import re


def viewData(idx):
    url = "?"
    url += "code=XxH00AXY"
    url += "&mode=view"
    url += "&board_num=" + idx
    return url


def parse_page(idx):
    req = requests.get(
        "http://media.ssu.ac.kr/sub.php?code=XxH00AXY&mode=&category=1&searchType=&search=&orderType=&orderBy=&page={}".format(
            idx))
    req.encoding = "utf-8"
    html = req.text
    bs = BeautifulSoup(html, 'html.parser')
    tbody = bs.find("tbody")
    ret = []
    trs = tbody.find_all("tr", {"class": "odd"})
    for tr in trs:
        parsed_item = dict()
        split_tr = tr.text.split("\n")
        parsed_item["title"] = split_tr[-5]
        parsed_item["date"] = split_tr[-3]
        onClick = tr.find('a')['onclick']
        idx = re.findall('[0-9]+', onClick)
        link = viewData(idx[0])
        parsed_item[
            "link"] = "http://media.ssu.ac.kr/sub.php" + link + "&category=1&searchType=&search=&orderType=&orderBy=&page=1"
        ret.append(parsed_item)
    return ret


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))

    return notices
