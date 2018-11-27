import numpy as np
from hash_table import HashTable as HT

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

#Mergesort found on stackoverflow
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

intron_hash = HT()
exon_hash = HT()

i = 1
for sublist in segments:
    print('Sublist', i, '---',sublist)
    introns, exons = get_intron_exon(sublist)
    for index in range(len(introns)):
        intron_hash.put(introns[index][0],introns[index][1])
    exon_hash.put(exons[0][0],exons[0][1])
    exon_hash.put(exons[1][0],exons[1][1])
    i += 1

print("")
print("intron hash table --- ",intron_hash.data)
#there are some None spots in there that should not be None ? they should be full of data
#instead they skip those data points
print("")
print("exon hash table slots --- ",exon_hash.slots)
print("exon hash table --- ",exon_hash.data)

#print("")

#the GOAL of this is to put the hash table data into a dictionary,,,,i don't actually know if its working
for name in range(len(segments)):
    data_wanted=intron_hash.get(name)
    #print(data_wanted)
    intron_dict={}
    #print("key? ",name)
    if data_wanted is not None:
        intron_dict[name]=data_wanted
        #print(intron_dict[name])

for name in range(len(exon_hash)):
    data_wanted=exon_hash.get(name)
    exon_dict={}
    #dict_key = exon_hash.__getitem__(name)
    if data_wanted is not None:
        exon_dict[name]=data_wanted

#for i in range(len(intron_hash)):
#    print(intron_dict[i])
#print(exon_dict)
