import random
import datetime
import os

letters = 'abcdefghijklmnopqrstuvwxyz'


def get_file_path(request, filename):
    filename_original = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, filename_original)
    return os.path.join('uploads/', filename)

def generate_pwd():
    letters_lower = list('abcdefghijklmnopqrstuvwxyz')
    letters_upper = list(letters.upper())
    numerics = list('0123456789')
    symbols = list('.,/?%#$*')
    all_chars = letters_lower + letters_upper + numerics + symbols

    output = ''

    for i in range(3):
        output += random.choice(letters_lower)

    for i in range(2):
        output += random.choice(letters_upper)

    for i in range(2):
        output += random.choice(numerics)

    for i in range(2):
        output += random.choice(symbols)

    for i in range(3):
        output += random.choice(all_chars)

    output_list = list(output)
    random.shuffle(output_list)
    output = ''.join(output_list)
    
    return output
