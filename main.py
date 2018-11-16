import numpy as np
from hash_table import HashTable

def generate_sequence():
    x = np.float16(np.random.randint(-100.00, 100.00, 200))
    index = (list(enumerate(x)))
    # print(x)
    return index

def generate_random_segment():
    '''
    Generates a random sequence of 10 values that can replace
    an unusable segment.

    '''
    x = np.float16(np.random.randint(-100.00, 100.00, 10))
    index = (list(enumerate(x)))
    # print(x)
    return index

seq = generate_sequence()

# split into segments of length 10
segments = [[seq[i + j] for j in range(10)] for i in range(0, len(seq), 10)]

def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            # since or data is stored in tuples, we compare
            # values at index 1 (which is the data)
            if y[0][1] > z[0][1]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


def extract_intron_exon(seg, ind_1, ind_2):
    exons = []
    # make sure that the one towards the end is popoed first
    # to ensure that the location of the second index valie does not change
    if ind_1 > ind_2:
        exons.append(seg.pop(ind_1))
        exons.append(seg.pop(ind_2))
    else:
        exons.append(seg.pop(ind_2))
        exons.append(seg.pop(ind_1))

    return seg, exons

def get_intron_exon(seg):
    sorted=msort(seg)
    negProd=sorted[0][1]*sorted[1][1]
    posProd=sorted[-1][1]*sorted[-2][1]

    if negProd>posProd:
        if sorted[0][1]==sorted[1][1]: #if the two smallest numbers are the same number
            return get_intron_exon(generate_random_segment())
        else:
            introns, exons = extract_intron_exon(seg, seg.index(sorted[0]), seg.index(sorted[1]))
            return introns, exons
    else:
        if sorted[-1][1]==sorted[-2][1]: #if the two largest numbers are the same numbers
            return get_intron_exon(generate_random_segment())
        else:
            introns, exons = extract_intron_exon(seg, seg.index(sorted[-2]), seg.index(sorted[-1]))
            return introns, exons


for sublist in segments:
    print('Sublist', '---',sublist)
    introns, exons = get_intron_exon(sublist)
    print('Introns', '---', introns)
    print('Exons', '---', exons)









# for r in range(len(segments)):
#     print('Segment', r + 1, ' --- ', segments[r])
#
# print(generate_random_segment(20))

H=HashTable()
for i in range(len(segments)):
    H.put(i, segments[i])


# print(H.slots)
# print(H.data)
