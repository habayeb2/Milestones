
# milestone 2

import math

def find_splice(dna_motif, dna):
    index = 0
    indexarray = []
    for i in range(0, len(dna_motif)):
        index = dna.find(dna_motif[i], index)
        indexarray.append(index)
        if (index == -1):
            return []
        index += 1
    return indexarray

def perfect_match(rna):
    import math
    rna = rna.upper()
    matches = 0
    if rna.count("A") == rna.count("U") and rna.count("C") == rna.count("G"):
        matches = math.factorial(rna.count("A")) * math.factorial(rna.count("C"))
    else:
        matches = matches
    return matches

def random_genome(dna, gc_content):
    import math
    dna = dna.upper()
    prob = []
    for i in range(len(gc_content)):
        perc = 1
        perc = perc * ((1 - gc_content[i]) / 2) ** (dna.count("A"))
        perc = perc * ((1 - gc_content[i]) / 2) ** (dna.count("T"))
        perc = perc * (gc_content[i] / 2) ** (dna.count("G"))
        perc = perc * (gc_content[i] / 2) ** (dna.count("C"))
        prob.append(math.log10(perc))
    return prob

def reverse_complement(dna):
    dna = dna[::-1] #reverses the dna string
    fdna = ''
    for symbol in dna: #Replaces the symbols
        if symbol == 'A':
            fdna = fdna + 'T'
        elif symbol == 'T':
            fdna = fdna + 'A'
        elif symbol == 'C':
            fdna = fdna + 'G'
        elif symbol == 'G':
            fdna = fdna + 'C'
    return fdna

def rev_palindrome(s):
    result = []
    length = len(s)
    for i in range(length):
        for j in range(4, 9):
            if i + j > length:
                continue
            s1 = s[i:i+j]
            s2 = reverse_complement(s1)
            if s1 == s2:
                result.append((i, j))
    return result
