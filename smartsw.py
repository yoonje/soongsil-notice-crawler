from bs4 import BeautifulSoup
import constants
import requests
import pprint
import json

def parse_page(idx):
    html = requests.get("http://smartsw.ssu.ac.kr/board/notice/{}".format(idx)).text
    bs = BeautifulSoup(html, 'lxml')
    items = bs.find_all("td")
    page_notice_list = []
    for item in items:
        try:
            parsed_item = dict()
            parsed_item["title"] = item.find('a').get_text()
            parsed_item["link"] = "http://smartsw.ssu.ac.kr" + item.find('a')['href']
        except:
            pass
        page_notice_list.append(parsed_item)

    # erase trash value
    i, count = 0, page_notice_list.count({})
    while i is not count:
        page_notice_list.remove({})
        i += 1
    return page_notice_list


if __name__ == '__main__':
    notice_list = []
    for i in range(1, constants.PAGE_NUM+1):
        notice_list.extend(parse_page(i))

    with open('smart.json', 'w') as fp:
        json.dump(notice_list, fp, ensure_ascii=False)
