import pytest
import bioinfo_dicts as bd

def n_neg(seq):
    # Convert to uppercase
    seq = seq.upper()
    # Count E's and D's and return count
    return seq.count('D') + seq.count('E')

    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')
    for aa in seq:
        if aa not in bd.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')
