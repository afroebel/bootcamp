""" Convert DNA sequences to RNA """

def rna(seq):
    seq = seq.upper()
    return seq.replace('T','U')
