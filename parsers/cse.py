from bs4 import BeautifulSoup
import requests
from .constants import headers


def parse_page(idx):
    html = requests.get("http://cse.ssu.ac.kr/03_sub/01_sub.htm?page={}".format(idx), headers=headers).text
    bs = BeautifulSoup(html, 'lxml')
    bbs_list = bs.find('div', {'class': 'bbs_list'})
    ret_list = []
    trs = bbs_list.find_all("tr")
    if idx == 1:
        for tr in trs:
            tds = tr.find_all('td')
            if not tds:
                continue
            item = {
                "title": tds[1].text.strip(),
                "link": "http://cse.ssu.ac.kr/03_sub/01_sub.htm{}".format(tds[1].find('a')['href']),
                "date": tds[3].text.strip(),
            }
            ret_list.append(item)
        return ret_list

    for tr in trs:
        tds = tr.find_all('td')
        if not tds:
            continue
        if tds[0].text.strip() == '공지':
            continue
        item = {
            "title": tds[1].text.strip(),
            "link": "http://cse.ssu.ac.kr/03_sub/01_sub.htm{}".format(tds[1].find('a')['href']),
            "date": tds[3].text.strip(),
        }
        ret_list.append(item)
    return ret_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))
    return notices
