from bs4 import BeautifulSoup
import requests


def parse_page(idx):
    html = requests.get("http://smartsw.ssu.ac.kr/board/notice/{}".format(idx)).text
    bs = BeautifulSoup(html, 'html.parser')
    trs = bs.find_all("tr")
    ret = []
    for tr in trs:
        parsed_item = dict()
        # print(item.find('a'))
        tds = tr.findAll('td')
        if tds:
            parsed_item["title"] = tds[0].text.strip()
            parsed_item["link"] = "http://smartsw.ssu.ac.kr{}".format(tds[0].find('a')['href'])
            parsed_item["date"] = tds[2].text
            ret.append(parsed_item)

    return ret


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))

    return notices

