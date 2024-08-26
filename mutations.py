import random

Nucleotides = ['A', 'T', 'G', 'C']
example = 'ABCDEFGHIJK'

def randinsert(seq: str) -> str:
    """A random insertion mutation in the DNA sequence."""
    rand = random.randint(0, len(seq))
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand:]
    return new_seq

def randdel(seq: str) -> str:
    """A random deletion mutation in the DNA sequence."""
    rand = random.randint(0, len(seq))
    new_seq = seq[:rand] + seq[rand + 1:]
    return new_seq

def randsub(seq: str) -> str:
    """A random substitution mutation in the DNA sequence."""
    rand = random.randint(0, len(seq) - 1)
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand + 1:]
    return new_seq

def insertion(seq: str, pos: int, nuc: str) -> str:
    """A single insertion mutation of a specific nucleotide in the DNA 
    sequence before a specific position."""
    position = pos - 1
    new_seq = seq[:position] + nuc + seq[position:]
    return new_seq

def deletion(seq: str, pos: int) -> str:
    """A single deletion mutation in the DNA sequence at a specific position."""
    position = pos - 1
    new_seq = seq[:position] + seq[position + 1:]
    return new_seq

def substitution(seq: str, pos: int, nuc: str) -> str:
    """A single substitution mutation of a specific nucleotide in the DNA sequence
    before a specific position."""
    position = pos - 1
    new_seq = seq[:position] + nuc + seq[position + 1:]
    return new_seq

def seqtoinsert(seq1: str, seq2: str) -> bool:
    """Returns True if seq2 is an insertion mutation of seq1"""
    return len(seq2) == len(seq1) + 1

def seqtodel(seq1: str, seq2: str) -> bool:
    """Returns True if seq2 is an deletion mutation of seq1"""
    return len(seq2) == len(seq1) - 1

def seqtosub(seq1: str, seq2: str) -> bool:
    """Returns True if seq2 is an substitution mutation of seq1"""
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            return True
        else:
            return False

