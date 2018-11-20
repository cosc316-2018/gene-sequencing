import numpy as np
import geneSequencing_hash

def generate_sequence():
    x = np.float16(np.random.randint(-100.00, 100.00, 200))
    index = (list(enumerate(x)))
    # print(x)
    return index

# def generate_random_segment():
#     '''
#     Generates a random sequence of 10 values that can replace
#     an unusable segment.
#
#         start_index: The index that the enumeration should start at.
#             generate_random_segment(20) returns: [(20, 99.0), (21, 67.0),
#                                     (22, -35.0), (23, -61.0), (24, 9.0),
#                                     (25, -78.0), (26, -38.0), (27, -70.0),
#                                     (28, -47.0), (29, 43.0)]
#     '''
#     x = np.float16(np.random.randint(-100.00, 100.00, 10))
#     index = (list(enumerate(x)))
#     # print(x)
#     return index

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

# def msort(x):
#     result = []
#     if len(x) < 2:
#         return x
#     mid = int(len(x)/2)
#     y = msort(x[:mid])
#     z = msort(x[mid:])
#     while (len(y) > 0) or (len(z) > 0):
#         if len(y) > 0 and len(z) > 0:
#             # since or data is stored in tuples, we compare
#             # values at index 1 (which is the data)
#             if y[0][1] > z[0][1]:
#                 result.append(z[0])
#                 z.pop(0)
#             else:
#                 result.append(y[0])
#                 y.pop(0)
#         elif len(z) > 0:
#             for i in z:
#                 result.append(i)
#                 z.pop(0)
#         else:
#             for i in y:
#                 result.append(i)
#                 y.pop(0)
#     return result

# This is written after refering the CLRS book and hints from the site http://en.literateprograms.org/Merge_sort_(Python)

#The merge method takes in the two subarrays and creates a output array
def merge(left, right):
    result = []
    i , j = 0 , 0
    while i < len (left) and j < len (right): # iterate through both arrays and arrange the elements in sorted order
        if left[i][1] <= right [j][1]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

#The loop may break before all elements are copied hence append the remaining elements
    result += left[i:]
    result += right[j:]
    return result

#The mergesort method to split the arrays into smaller subarrays
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)


# def get_intron_exon(seg):
#     sorted=mergesort(seg)
#     print(sorted)
#     negProd=sorted[0][1]*sorted[1][1]
#     posProd=sorted[-1][1]*sorted[-2][1]
#
#     if negProd>posProd:
#         if sorted[0][1]==sorted[1][1]: #if the two smallest numbers are the same number
#             return get_intron_exon(generate_random_segment(seg[0][0]))
#         else:
#             return seg, sorted
#     else:
#         if sorted[-1][1]==sorted[-2][1]: #if the two largest numbers are the same numbers
#             return get_intron_exon(generate_random_segment(seg[0][0]))
#         else:
#             return seg, sorted
def extract_intron_exon(seg, ind_1, ind_2):
    exons = []
    # make sure that the one towards the end is popped first
    # to ensure that the location of the second index value does not change
    if ind_1 > ind_2:
        exons.append(seg.pop(ind_1))
        exons.append(seg.pop(ind_2))
    else:
        exons.append(seg.pop(ind_2))
        exons.append(seg.pop(ind_1))
    return seg, exons

def get_intron_exon(seg):
    sorted=mergesort(seg)
    negProd=sorted[0][1]*sorted[1][1]
    posProd=sorted[-1][1]*sorted[-2][1]

    if negProd>posProd:#if two smallest numbers make the biggest product
        if sorted[0][1]==sorted[1][1]: #if the two smallest numbers are the same number
            return get_intron_exon(generate_random_segment(seg[0][0]))
        else:
            introns, exons = extract_intron_exon(seg, seg.index(sorted[0]), seg.index(sorted[1]))
            return introns, exons
    else: #if the two largest numbers make the biggest product
        if sorted[-1][1]==sorted[-2][1]: #if the two largest numbers are the same numbers
            return get_intron_exon(generate_random_segment(seg[0][0]))
        else:
            introns, exons = extract_intron_exon(seg, seg.index(sorted[-2]), seg.index(sorted[-1]))
            return introns, exons

# for sublist in segments:
#     print('Sublist', '---',sublist)
#     segment, sorted = get_intron_exon(sublist)
#     print('Segment Used', '---',segment)
#     print('Sorted', '---', sorted, '\n')


intron_hash = geneSequencing_hash.HashTable()
exon_hash = geneSequencing_hash.HashTable()


for sublist in segments:
    print('Sublist', '---',sublist)
    introns, exons = get_intron_exon(sublist)
    for index in range(len(introns)):
        intron_hash.put(introns[index][0],introns[index][1])
    exon_hash.put(exons[0][0],exons[0][1])
    exon_hash.put(exons[1][0],exons[1][1])

print("")
print("intron hash table --- ",intron_hash.data)
print("")
print("exon hash table --- ",exon_hash.data)




