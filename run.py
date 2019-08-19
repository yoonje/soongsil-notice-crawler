import parsers

if __name__ == '__main__':
    smartsw = parsers.smartsw.get_notices(6)

    parsers.utils.save_json('./data', 'smart.json', smartsw)
