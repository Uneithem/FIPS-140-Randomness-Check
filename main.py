import random
 #Monobyte Testing compares frequencies of 0 and 1 to probability to meet them times amount of characters (in other word to predicted frequency in random distribution)
def MonobyteTest(s):
    s_block = []
#firstly we break string into blocks to make computations shorter
    for i in range(0, 20000, 2500):
        s_block.append(s[i:i + 2500])
    ones = 0
    zeros = 0
#count amount of zeros and ones in each sequence
    for i in range(0, len(s_block)):
        for j in range(0, len(s_block[i])):
            if s_block[i][j] == '0':
                zeros += 1
            elif s_block[i][j] == '1':
                ones += 1
#now let's compare them to the allowed range, we don't necessarily need to find if both of them fits into interval as if one does the other one does so automatically and if one doesn't other one also won't fit
    if 9654 <= zeros <= 10346:
        return True
    else:
        return False
#in this test we compare length of maximum same bit sequences to the allowed number of 36, if we find one bit for more than 36 times in a row, string is considered non-random
def MaxBitLen(s):
    s_ones = s.split('0')
    s_zeros = s.split('1')
    for i in range(len(s_ones)):
        if len(s_ones[i]) > 36:
            return False
    for i in range(len(s_zeros)):
        if len(s_zeros[i]) > 36:
            return False
    return True

#in Pokker test we firstly find how often each 4 digits block is found in sequence and then compare it to the allowed interval (see FIPS-140 Poker test for more info)
def PokkerTest(s):
    blocks = []
    for k in range(0, len(s), 4):
        blocks.append(s[k: k + 4])
    frequency = []
    for k in range(0, 16):
        summ = 0
        for j in range(0, len(blocks)):
            if blocks[j] == str(bin(k)[2:].zfill(4)):
                summ += 1
        frequency.append(summ)
    x3 = 0
    for k in range(0, 16):
        x3 += frequency[k]**2
    x3 = 2 ** 4 / len(blocks) * x3 - len(blocks)
    if 1.03 < x3 < 57.4:
        return True
    else:
        return False
#in series length test we calculate length of each same bit sequence and then compare it to the allowed interval
def SeriesLen(s):
    s_ones = s.split('0')
    s_zeros = s.split('1')
    ranges_1 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6+': 0
    }
    ranges_0 = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6+': 0
    }
    for k in range(len(s_ones)):
        if len(s_ones[k]) == 1:
            ranges_1['1'] += 1
        elif len(s_ones[k]) == 2:
            ranges_1['2'] += 1
        elif len(s_ones[k]) == 3:
            ranges_1['3'] += 1
        elif len(s_ones[k]) == 4:
            ranges_1['4'] += 1
        elif len(s_ones[k]) == 5:
            ranges_1['5'] += 1
        elif len(s_ones[k]) >= 6:
            ranges_1['6+'] += 1
    for k in range(len(s_zeros)):
        if len(s_zeros[k]) == 1:
            ranges_0['1'] += 1
        elif len(s_zeros[k]) == 2:
            ranges_0['2'] += 1
        elif len(s_zeros[k]) == 3:
            ranges_0['3'] += 1
        elif len(s_zeros[k]) == 4:
            ranges_0['4'] += 1
        elif len(s_zeros[k]) == 5:
            ranges_0['5'] += 1
        elif len(s_zeros[k]) >= 6:
            ranges_0['6+'] += 1
    if 2267 <= ranges_1['1'] <= 2733 and 1079 <= ranges_1['2'] <= 1421 and 503 <= ranges_1['3'] <= 748 and 402 >= \
            ranges_1['4'] >= 223 >= ranges_1['5'] >= 90 and 90 <= ranges_1['6+'] <= 223:
        k1 = True
    else:
        k1 = False
    if 2267 <= ranges_0['1'] <= 2733 and 1079 <= ranges_0['2'] <= 1421 and 503 <= ranges_0['3'] <= 748 and 402 >= \
            ranges_0['4'] >= 223 >= ranges_0['5'] >= 90 and 90 <= ranges_0['6+'] <= 223:
        k0 = True
    else:
        k0 = False
    return k0 and k1
