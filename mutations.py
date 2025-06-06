import random
from data import *

Nucleotides = ['A', 'T', 'G', 'C']

def randinsert(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide insertion mutation."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand:]
    return new_seq


def randdel(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide deletion mutation."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + seq[rand + 1:]
    return new_seq


def randsub(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide substitution mutation."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand + 1:]
    return new_seq


def insertion(seq: str, position: int, nucleotide: str) -> str:
    """Return the DNA seq with a single insertion mutation of a specific nucleotide
    at a specific position.
    """
    pos = position - 1
    new_seq = seq[:pos] + nucleotide + seq[pos:]
    return new_seq


def deletion(seq: str, position: int) -> str:
    """Return the DNA seq with a single deletion mutation at a specific position."""
    pos = position - 1
    new_seq = seq[:pos] + seq[pos + 1:]
    return new_seq


def substitution(seq: str, position: int, nucleotide: str) -> str:
    """Return the DNA seq with a single substitution mutation of a specific nucleotide 
    at a specific position.
    """
    pos = position - 1
    new_seq = seq[:pos] + nucleotide + seq[pos + 1:]
    return new_seq


def seqtoinsert(seq1: str, seq2: str) -> bool:
    """Return the position of seq2, where there is a insertion mutation of seq1.
    If there is no insertion mutation, return -1.
    
    >>> seqtoinsert('AATGC', 'AATGTC')
    True
    >>> seqtoinsert('AACC', 'AACCT')
    True
    """

    i = 0
    while i < len(seq1) and i < len(seq2) and seq1[i] == seq2[i]:
        i += 1

    # Check for any insertion that is in the MIDDLE of seq1.
    if i != len(seq1) and len(seq2) > len(seq1):
        result = 0
        for pos in range(i, len(seq1)):
            if seq1[pos] == seq2[pos + 1]:
                result += 1
        return result == len(seq2) - (i + 1) and len(seq2) == len(seq1) + 1
    
    # Check for insertion that is at the END of seq1.
    else:
        return len(seq2) == len(seq1) + 1 and i == len(seq1)


def seqtodel(seq1: str, seq2: str) -> bool:
    """Return True if seq2 has a single nucleotide deletion mutation of seq1.
    
    >>> seqtodel('ATTGC', 'ATTC')
    True
    >>> seqtodel('ATTGA', 'GTTC')
    False
    """

    return seqtoinsert(seq2, seq1)


def seqtosub(seq1: str, seq2: str) -> bool:
    """Return True if seq2 has a single nucleotide substitution mutation of seq1.
    
    >>> seqtosub('ATTGC', 'ATCGC')
    True
    >>> seqtosub('GCTCC', 'GCTCC')
    False
    """

    result = 0
    if len(seq1) == len(seq2):
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                result += 1
    return result == 1


def find_mutation_position(seq1: str, seq2: str) -> int:
    """Find the the position of seq2, where there is a mutation.
    
    >>> find_mutation_position('ATGC', 'AATGC')
    2
    >>> find_mutation_position('ATATAT', 'ATATT')
    5
    >>> find_mutation_position('ATGC', 'ATGG')
    4
    """

    i = 0
    while i < len(seq1) and i < len(seq2) and seq1[i] == seq2[i]:
        i += 1
    
    return i + 1


def translate(seq: str) -> bool:
    """Return the translated nucleotide sequence into amino acid.
    
    >>> translate("TTTCTT")
    'FL'
    >>> translate("TTTTCTTAGCAA")
    'FS'
    """
    result = ""
    seq = seq.replace("U", "T")

    n = 3
    seq = [seq[i:i+n] for i in range(0, len(seq), n)]

    for codon in seq:
        amino_acid = CODONS[codon]
        if amino_acid == "*":
            return result
        result += amino_acid

    return result


def is_synonymous(seq1: str, seq2: str) -> bool:
    """Return True if the mutation is synonymous.

    >>> is_synonymous("TTTCTT", "TTCCTC")
    True
    >>> is_synonymous("TTTCTT", "TTACTT")
    False
    """
    if seqtoinsert(seq1, seq1) > -1 or seqtodel(seq1, seq2) or seqtosub(seq1, seq2):
        seq1 = translate(seq1)
        seq2 = translate(seq2)

        return seq1 == seq2
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
