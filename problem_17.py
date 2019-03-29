onedigit = {
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}

twodigit = {
    '0': '',
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

tens = {
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
}

threedigit = 'hundred'
fourdigit = 'thousand'


allwords = ''
for number in range(1,1001):
    number = str(number)
    if len(number) == 1:
        allwords += onedigit[number]
    elif len(number) == 2:
        if number[0] == '1':
            allwords+= tens[number]
        else:
            allwords+= twodigit[number[0]]+onedigit[number[1]]
    elif len(number) == 3:
        allwords+=onedigit[number[0]]+threedigit
        if number[1] == '1':
            allwords+= 'and'+tens[number[1:3]]
        elif number[1] == '0' and number[2] == '0':
            pass
        else:
            allwords+= 'and'+twodigit[number[1]]+onedigit[number[2]]
    else:
        allwords += onedigit[number[0]]+fourdigit
    
print("Solution is: "+str(len(allwords)))