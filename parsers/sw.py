from bs4 import BeautifulSoup
import requests
import pprint


def get_overlap_list(items):
    overlap_list = []
    for item in items:
        try:
            parse_item = dict()
            parse_item["title"] = item.find("span", {'class': 'notice'}).text
            parse_item["link"] = "https://sw.ssu.ac.kr/{}".format(item.find("a")["href"][3:])
            overlap_list.append(parse_item)
        except:
            continue
    return overlap_list


def remove_overlap_list(overlap_list, page_notice_list):
    for i in overlap_list:
        for j in page_notice_list:
            if i == j:
                page_notice_list.remove(j)

    return page_notice_list


def parse_page(idx):
    if idx == 1:
        html = requests.get("https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_1").text
        bs = BeautifulSoup(html, 'html.parser')
        page_notice_list = []
        items = bs.find_all("td", {'class': 'subject'})
        for item in items:
            parse_item = dict()
            parse_item["title"] = item.find("a").get_text()
            parse_item["link"] = "https://sw.ssu.ac.kr/{}".format(item.find("a")["href"][3:])
            page_notice_list.append(parse_item)
    else:
        html = requests.get("https://sw.ssu.ac.kr/bbs/board.php?bo_table=sub6_1&page={}".format(idx)).text
        bs = BeautifulSoup(html, 'html.parser')
        page_notice_list = []
        items = bs.find_all("td", {'class': 'subject'})
        for item in items:
            parse_item = dict()
            parse_item["title"] = item.find("a").get_text()
            parse_item["link"] = "https://sw.ssu.ac.kr/{}".format(item.find("a")["href"][3:])
            page_notice_list.append(parse_item)
        overlap_list = get_overlap_list(items)
        page_notice_list = remove_overlap_list(overlap_list, page_notice_list)
    return page_notice_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))
    return notices