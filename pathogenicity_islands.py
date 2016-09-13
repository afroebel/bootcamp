"""Locates areas of genome with """

#Part A: divides genomes into blocks and calculates GC content

def gc_blocks(seq, block_size):
    i = 0
    seq1 = seq[i:i + block_size]
    while len(seq1) == block_size:
        seq1 = seq[i:i + block_size]
        i += block_size
        if len(seq1) == block_size:
            print((seq1.count('G') + seq1.count('C')) / block_size)
        else:
            print('done')


#Part B: returns blocks and capitalizes only those above certain GC
#content threshold


def gc_map(seq, block_size, gc_thresh):
    i = 0
    seq1 = seq[i:i + block_size]
    mapped_seq = ''
    while len(seq1) == block_size:
        seq1 = seq[i:i + block_size]
        i += block_size
        if len(seq1) == block_size:
            if ((seq1.count('G') + seq1.count('C')) / block_size) < gc_thresh:
                mapped_seq += seq1.lower()
            else:
                mapped_seq += seq1
        else:
            print('done')
    print(mapped_seq)
    return mapped_seq
