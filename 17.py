words = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

megastring = ''

for i in range(1, 1001):
    if (i in words):
        megastring += words[i]
    else:
        if (len(str(i)) == 2):
            ministring = words[int(str(i)[0]) * 10] + words[int(str(i)[1])]
            megastring += ministring
        elif (len(str(i)) == 3):
            ministring = words[int(str(i)[0])] + 'hundredand'

            if ( 10 < (int(str(i)[1:3])) < 20 ):
                ministring += words[int(str(i)[1:3])]
            else:
                ministring += words[int(str(i)[1]) * 10] + words[int(str(i)[2])]

            if (i % 100 == 0):
                ministring = ministring.replace('and','')

            megastring += ministring
        elif (len(str(i)) == 4):
            megastring += 'onethousand'

print(len(megastring))