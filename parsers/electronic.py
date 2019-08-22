from bs4 import BeautifulSoup
import requests


def parse_page(idx):
    html = requests.get("http://infocom.ssu.ac.kr/rb/?c=2/38&p={}".format(idx)).text
    bs = BeautifulSoup(html, 'html.parser')
    page_notice_list = []
    if idx == 1:
        items = bs.find_all("div", {'class': 'list notice'})
        for item in items:
            parse_item = dict()
            parse_item["title"] = item.find("span", {'class': 'subject ntc'}).text
            parse_item["link"] = "http://infocom.ssu.ac.kr{}".format(
                item["onclick"][8:-3])  # you can use regex expression
            page_notice_list.append(parse_item)
        items = bs.find_all("div", {'class': 'list'})
        for item in items:
            parse_item = dict()
            parse_item["title"] = item.find("span", {'class': 'subject'}).get_text()
            parse_item["link"] = "http://infocom.ssu.ac.kr{}".format(item["onclick"][8:-3])
            page_notice_list.append(parse_item)
    else:
        items = bs.find_all("div", {'class': 'list'})
        for item in items:
            parse_item = dict()
            parse_item["title"] = item.find("span", {'class': 'subject'}).get_text()
            parse_item["link"] = "http://infocom.ssu.ac.kr{}".format(item["onclick"][8:-3])
            page_notice_list.append(parse_item)

    return page_notice_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))

    return notices
