import random

Nucleotides = ['A', 'T', 'G', 'C']

def randinsert(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide insertion mutation."""
    rand = random.randint(0, len(seq))
    new_seq = seq[:rand] + random.choice(Nucleotides) + seq[rand:]
    return new_seq

def randdel(seq: str) -> str:
    """Return the DNA seq with a random single nucleotide deletion mutation."""
    rand = random.randint(0, len(seq))
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
    in the DNA sequence before a specific position.
    """
    pos = position - 1
    new_seq = seq[:pos] + nucleotide + seq[pos + 1:]
    return new_seq

def seqtoinsert(seq1: str, seq2: str) -> bool:
    """Return True if seq2 is an insertion mutation of seq1."""
    return len(seq2) == len(seq1) + 1

def seqtodel(seq1: str, seq2: str) -> bool:
    """Return True if seq2 is a deletion mutation of seq1."""
    return len(seq2) == len(seq1) - 1

def seqtosub(seq1: str, seq2: str) -> bool:
    """Return True if seq2 is a substitution mutation of seq1."""
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            return True
    return False

