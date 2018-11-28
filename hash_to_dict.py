def convert_introns():
    #the GOAL of this is to put the hash table data into a dictionary,,,,i don't actually know if its working
    for name in range(len(segments)):
        data_wanted=intron_hash.get(name)
        #print(data_wanted)
        intron_dict={}
        #print("key? ",name)
        if data_wanted is not None:
            intron_dict[name]=data_wanted
            #print(intron_dict[name])


def convert_exons():
    for name in range(len(exon_hash)):
        data_wanted=exon_hash.get(name)
        exon_dict={}
        #dict_key = exon_hash.__getitem__(name)
        if data_wanted is not None:
            exon_dict[name]=data_wanted

    #for i in range(len(intron_hash)):
    #    print(intron_dict[i])
    #print(exon_dict)