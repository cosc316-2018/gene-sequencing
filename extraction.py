from sequence import generate_random_segment

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