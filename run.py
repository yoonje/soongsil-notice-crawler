#!/home/ubuntu/soongsil-notice-crawler/venv/bin/python3
import parsers

if __name__ == '__main__':
    smartsw = parsers.smartsw.get_notices(parsers.constants.SMART_PAGE_NUM)
    electronic = parsers.electronic.get_notices(parsers.constants.ELECTRONIC_PAGE_NUM)
    sw = parsers.sw.get_notices(parsers.constants.SW_PAGE_NUM)
    cse = parsers.cse.get_notices(parsers.constants.CSE_PAGE_NUM)
    media = parsers.media.get_notices(parsers.constants.MEDIA_PAGE_NUM)
    scatch = parsers.scatch.get_notices(parsers.constants.SCATCH_PAGE_NUM)
    business = parsers.business.get_notices(parsers.constants.BUSINESS_PAGE_NUM)

    parsers.utils.save_json('./data', 'smart.json', smartsw)
    parsers.utils.save_json('./data', 'smart-head.json', smartsw[:7])
    parsers.utils.save_json('./data', 'electronic.json', electronic)
    parsers.utils.save_json('./data', 'electronic-head.json', electronic[:7])
    parsers.utils.save_json('./data', 'sw.json', sw)
    parsers.utils.save_json('./data', 'sw-head.json', sw[:7])
    parsers.utils.save_json('./data', 'cse.json', cse)
    parsers.utils.save_json('./data', 'cse-head.json', cse[:7])
    parsers.utils.save_json('./data', 'media.json', media)
    parsers.utils.save_json('./data', 'media-head.json', media[:7])
    parsers.utils.save_json('./data', 'scatch.json', scatch)
    parsers.utils.save_json('./data', 'scatch-head.json', scatch[:7])
    parsers.utils.save_json('./data', 'business.json', business)
    parsers.utils.save_json('./data', 'business-head.json', business[:7])
