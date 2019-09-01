from bs4 import BeautifulSoup
import requests
from .constants import headers
import pprint


def parse_page(idx):
    html = requests.get("http://biz.ssu.ac.kr/bbs/list.do?&bId=BBS_03_NOTICE&sc_title=&page={}".format(idx),
                        headers=headers).text
    bs = BeautifulSoup(html, 'lxml')
    bList = bs.find("ul", {"id": "bList01"})
    lis = bList.find_all("li")
    ret = []
    for li in lis:
        title = li.find('a')
        ret.append({
            "link": "http://biz.ssu.ac.kr{}".format(title['href']),
            "title": title.text.strip(),
            "date": li.find('span').text.split('/')[0].strip(),
        })

    return ret


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))

    return notices
