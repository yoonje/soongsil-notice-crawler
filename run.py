import parsers

if __name__ == '__main__':
    smartsw = parsers.smartsw.get_notices(parsers.constants.SMART_PAGE_NUM)
    electronic = parsers.electronic.get_notices(parsers.constants.ELECTRONIC_PAGE_NUM)
    sw = parsers.sw.get_notices(parsers.constants.SW_PAGE_NUM)
    cse = parsers.cse.get_notices(parsers.constants.CSE_PAGE_NUM)
    media = parsers.media.get_notices(parsers.constants.MEDIA_PAGE_NUM)

    parsers.utils.save_json('./data', 'smart.json', smartsw)
    parsers.utils.save_json('./data', 'electronic.json', electronic)
    parsers.utils.save_json('./data', 'sw.json', sw)
    parsers.utils.save_json('./data', 'cse.json', cse)
    parsers.utils.save_json('./data', 'media.json', media)
