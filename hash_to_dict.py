def convert(hash_table):
        dictionary = {hash_table.slots[x]:hash_table.data[x] for x in range(len(hash_table.slots)) if hash_table.slots[x] is not None}
        return dictionary