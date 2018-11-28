from hash_table import HashTable
from sequence import generate_sequence
from extraction import get_intron_exon
import hash_to_dict

# generate a sequence of 200 elements
seq = generate_sequence()

# split into segments of length 10
segments = [[seq[i + j] for j in range(10)] for i in range(0, len(seq), 10)]

# initialize the empty hash tables that will
# hold the extracted introns and exons
intron_hash = HashTable()
exon_hash = HashTable()

print('\n The sublists that were extracted from the initial gene sequence \n')

i = 1
for sublist in segments:
    print('Sublist', i, '---',sublist)
    introns, exons = get_intron_exon(sublist)
    for index in range(len(introns)):
        intron_hash.put(introns[index][0],introns[index][1])
    exon_hash.put(exons[0][0],exons[0][1])
    exon_hash.put(exons[1][0],exons[1][1])
    i += 1

print('_' * 80)
print('\n NOTE: The sizes listed do not include slots or data values that are \'None\'')
print('\n', "INTRON HASH TABLE SLOTS", "( Size", len(intron_hash), ") --- ",intron_hash.slots)
print('\n', "INTRON HASH TABLE DATA", "( Size", len(intron_hash), ") --- ",intron_hash.data)
print('_' * 80)
print('\n', "EXON HASH TABLE SLOTS", "( Size", len(exon_hash), ") --- ",exon_hash.slots)
print('\n', "EXON HASH TABLE DATA", "( Size", len(exon_hash), ") --- ",exon_hash.data)
print('_' * 80)

intron_dictionary = hash_to_dict.convert(intron_hash)
exon_dictionary = hash_to_dict.convert(exon_hash)

print('\n', 'INTRON DICTIONARY', '( Size', len(intron_dictionary), ') ---', intron_dictionary)
print('\n', 'EXON DICTIONARY', '( Size', len(exon_dictionary), ') ---', exon_dictionary)
print('_' * 80)