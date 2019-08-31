from bs4 import BeautifulSoup
import requests
from .constants import headers


def parse_page(idx):
    html = requests.get("http://scatch.ssu.ac.kr/공지사항/page/{}/".format(idx), headers=headers).text
    bs = BeautifulSoup(html, 'lxml')
    bbs_list = bs.find('ul', {'class': 'notice-lists'})
    ret_list = []
    lis = bbs_list.find_all("li")
    date = ''
    for li in lis:
        li_class = li['class']
        if 'start' in li_class:
            date_divs = li.find('div', {'class': 'col-lg-2 text-center m-text-left m-mb-10'}).find_all('div')
            date = date_divs[0].text + ' ' + date_divs[1].text
        category = li.find('span', {'class': 'label d-inline-blcok border pl-3 pr-3 mr-2'}).text
        title = li.find('span', {'class': 'd-block d-lg-inline-block m-pt-5'}).text
        link = li.find('a', {'class': 'text-decoration-none d-block'})['href']
        item = {
            'title': title,
            'link': link,
            'category': category,
            'date': date,
        }
        ret_list.append(item)

    return ret_list


def get_notices(max_page=6):
    notices = []
    for i in range(1, max_page):
        notices.extend(parse_page(i))
    return notices
