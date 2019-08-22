from bs4 import BeautifulSoup
import requests
import pprint


def get_overlap_list(items):
    overlap_list = []
    for item in items:
        try:
            parse_item = dict()
            parse_item["title"] = item.find("td", {'class': 'subject'}).text
            parse_item["link"] = "http://cse.ssu.ac.kr/03_sub/01_sub.htm" + item.find("a")["href"]
            if parse_item["title"] != {}:
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
    html = requests.get("http://cse.ssu.ac.kr/03_sub/01_sub.htm?page={}".format(idx)).text
    bs = BeautifulSoup(html, 'html.parser')
    page_notice_list = []
    if idx == 1:
        items = bs.find_all("td")
        for item in items:
            try:
                parse_item = dict()
                parse_item["title"] = item.find("a").text
                parse_item["link"] = "http://cse.ssu.ac.kr/03_sub/01_sub.htm" + item.find("a")["href"]
                if parse_item["title"] != {}:
                    page_notice_list.append(parse_item)
            except:
                continue
    else:
        items = bs.find_all("td")
        for item in items:
            try:
                parse_item = dict()
                parse_item["title"] = item.find("a").text
                parse_item["link"] = "http://cse.ssu.ac.kr/03_sub/01_sub.htm" + item.find("a")["href"]
            except:
                continue
            page_notice_list.append(parse_item)
        overlap_list = get_overlap_list(items)
        page_notice_list = remove_overlap_list(overlap_list, page_notice_list)
    return page_notice_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))
    return notices