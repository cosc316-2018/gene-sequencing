import numpy as np
from hash_table import HashTable

def generate_sequence():
    x = np.float16(np.random.randint(-100.00, 100.00, 200))
    index = (list(enumerate(x)))
    # print(x)
    return index

def generate_random_segment(start_index):
    '''
    Generates a random sequence of 10 values that can replace
    an unusable segment.

        start_index: The index that the enumeration should start at.
            generate_random_segment(20) returns: [(20, 99.0), (21, 67.0),
                                    (22, -35.0), (23, -61.0), (24, 9.0),
                                    (25, -78.0), (26, -38.0), (27, -70.0),
                                    (28, -47.0), (29, 43.0)]
    '''
    x = np.float16(np.random.randint(-100.00, 100.00, 10))
    index = (list(enumerate(x, start=start_index)))
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


for sublist in segments:
    list_to_sort=sublist.copy()
    print(list_to_sort)
    sorted=msort(list_to_sort)
    print(sorted)
    negProd=sorted[0][1]*sorted[1][1]
    posProd=sorted[-1][1]*sorted[-2][1]
    if negProd>posProd:
        print(negProd, sorted[0][1], sorted[1][1])
    else:
        print(posProd, sorted[-1][1], sorted[-2][1])
    break






# for r in range(len(segments)):
#     print('Segment', r + 1, ' --- ', segments[r])
#
# print(generate_random_segment(20))

H=HashTable()
for i in range(len(segments)):
    H.put(i, segments[i])


# print(H.slots)
# print(H.data)
