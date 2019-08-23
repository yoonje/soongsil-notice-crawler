import parsers

if __name__ == '__main__':
    # smartsw = parsers.smartsw.get_notices(6)
    electronic = parsers.electronic.get_notices(5)

    # parsers.utils.save_json('./data', 'smart.json', smartsw)
    parsers.utils.save_json('./data', 'electronic.json', electronic)
