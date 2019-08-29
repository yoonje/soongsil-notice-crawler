import parsers

if __name__ == '__main__':
    scatch = parsers.scatch.get_notices(parsers.constants.SCATCH_PAGE_NUM)

    parsers.utils.save_json('./data', 'scatch.json', scatch)
