from hash_table import HashTable as HT
from sequence import *
from extraction import get_intron_exon
from hash_to_dict import convert_introns, convert_exons

seq = generate_sequence()

# split into segments of length 10
segments = [[seq[i + j] for j in range(10)] for i in range(0, len(seq), 10)]

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


print('\n', "intron hash table --- ",intron_hash.data)
print('\n', "exon hash table slots --- ",exon_hash.slots)
print('\n', "exon hash table --- ",exon_hash.data)