from mutations import *

DNA = 'AACCGGTT'
Mutated_DNA = 'AACGGGTT'

start_text = """
[1] Add a single nucleotide mutation to a DNA sequence.
[2] Identify the single nucleotide mutation in 2 DNA sequences.
[3] Generate a random DNA sequence.
[4] Exit
"""

add_text = """
[1] Add random single nucleotide mutation.
[2] Add specific single nucleotide mutation.
[3] Back
"""

mutation_text = """
[1] Insertion Mutation
[2] Deletion Mutation
[3] Substitution Mutation
[4] Back
"""

start = input(start_text)

while start != '4':
    if start == '1':
        add = input(add_text)
    if start == '2':
        pass
    if start == '3':
        pass
    else:
        print('\nThat was not a valid choice! Please select again.')
        start = input(start_text)