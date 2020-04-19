def timeConversion(s):
    pora = s[len(s)-2]
    twenty4 = 12
    dec = int(s[:len(s)-2].replace(':',  ''))/10000
    if pora == 'P':
        twenty4 += dec
        twenty4 *= 10000
        twenty4 = str(int(twenty4))

    else:
        twenty4 = list(str(int(dec * 10000)))
        print("twenty4", twenty4)
        if dec >= 12 and dec <= 12.9999:
            print("dec>: ", dec)
            dec -= 12
            print("dec: ", dec)
            twenty4 = str(int(dec * 10000))
            print("dec: ", twenty4)
            twenty4 = list(twenty4)
            twenty4.insert(0, '00')
            print('twenty4', twenty4, len(twenty4))
            if len(twenty4) == 4:
                twenty4.append('0')
        elif len(twenty4) == 5:
            print("twenty4 0", twenty4)
            twenty4.insert(0, '0')
        twenty4 = ''.join(twenty4)
    time24 = twenty4[:2] + ':' + twenty4[2:4] + ':' + twenty4[4:]
    print("time24", type(time24))
    return time24
        # AM 6AM => 06
        # AM 11 AM => 11
print(timeConversion('21:05:45AM'))
