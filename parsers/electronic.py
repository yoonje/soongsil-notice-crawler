from bs4 import BeautifulSoup
import re
import requests


def parse_page(idx):
    html = requests.get("http://infocom.ssu.ac.kr/rb/?c=2/38&p={}".format(idx)).text
    bs = BeautifulSoup(html, 'html.parser')
    page_notice_list = []
    if idx == 1:
        notices = bs.find_all("div", {'class': 'list notice'})
        for notice in notices:
            parse_item = {
                "title": notice.find("span", {'class': 'subject ntc'}).text,
                "link": "http://infocom.ssu.ac.kr{}".format(notice["onclick"][8:-3]),
                "date": notice.find("div", {'class': 'info'}).text.split('|')[1].strip(),
            }
            page_notice_list.append(parse_item)
        informs = bs.find_all("div", {'class': 'list'})
        for inform in informs:
            if 'notice' in inform.attrs['class']:
                continue
            parse_item = {
                "title": inform.find("span", {'class': 'subject'}).get_text(),
                "link": "http://infocom.ssu.ac.kr{}".format(inform["onclick"][8:-3]),
                "date": inform.find("div", {'class': 'info'}).text.split('|')[1].strip(),
            }
            page_notice_list.append(parse_item)
    else:
        informs = bs.find_all("div", {'class': 'list'})
        for inform in informs:
            if 'notice' in inform.attrs['class']:
                continue
            parse_item = {
                "title": inform.find("span", {'class': 'subject'}).get_text(),
                "link": "http://infocom.ssu.ac.kr{}".format(inform["onclick"][8:-3]),
                "date": inform.find("div", {'class': 'info'}).text.split('|')[1].strip(),
            }
            page_notice_list.append(parse_item)

    return page_notice_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))

    return notices

