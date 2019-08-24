from bs4 import BeautifulSoup
import requests


def parse_page(idx):
    if idx == 1:
        html = requests.get("https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_1").text
        bs = BeautifulSoup(html, 'html.parser')
        res_list = []
        trs = bs.find_all("tr")
        for tr in trs:
            tds = tr.find_all('td')
            if not tds:
                continue
            item = {
                # "num": tds[0].text.strip(),
                "title": tds[1].text.strip(),
                "link": "https://sw.ssu.ac.kr/{}".format(tds[1].find('a')['href'][3:]),
                "date": tds[3].text.strip(),
            }
            res_list.append(item)
        return res_list

    html = requests.get("https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_1&page={}".format(idx)).text
    bs = BeautifulSoup(html, 'html.parser')
    res_list = []
    trs = bs.find_all("tr")
    for tr in trs:
        tds = tr.find_all('td')
        if not tds:
            continue
        if tds[0].text.strip() == '공지':
            continue
        item = {
            # "num": tds[0].text.strip(),
            "title": tds[1].text.strip(),
            "link": "https://sw.ssu.ac.kr/{}".format(tds[1].find('a')['href'][3:]),
            "date": tds[3].text.strip(),
        }
        res_list.append(item)
    return res_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))
    return notices
