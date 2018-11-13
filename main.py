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

# for r in range(len(segments)):
#     print('Segment', r + 1, ' --- ', segments[r])
#
# print(generate_random_segment(20))

H=HashTable()
for i in range(len(segments)):
    H.put(i, segments[i])


# H[54]="cat"
# H[26]="dog"
# H[93]="lion"
# H[17]="tiger"
# H[77]="bird"
# H[31]="cow"
# H[44]="goat"
# H[55]="pig"
# H[20]="chicken"

# print(H[20])
# print(H.slots)
# print(H.data)
# print(len(H))
# print(18 in H)
print(H.slots)
