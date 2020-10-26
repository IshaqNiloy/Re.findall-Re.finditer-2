import re
if __name__ == '__main__':
    string = input()
    substring_list = re.findall('(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})[bcdfghjklmnpqrstvwxyz]', string, flags = re.I)
    if len(substring_list) != 0:
        for substring in substring_list:
            print(substring)
    else:
        print(-1)
