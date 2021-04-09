
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

def get_edges(dna_dict):
    list1 = [] #empty list to store adjacency
    keylist = list(dna_dict.keys()) #Puts the keys of the dictionary into a list to help convert from value to key later
    valuelist = list(dna_dict.values()) #Puts the values of the dictionary into a list to help convert from value to key later
    for key in keylist: # Goes through every key in the dictionary
        for value in valuelist: # Goes through every value in the dictionary
            if value == dna_dict[key]: #If the value being tested is the one from the key being tested, go on and use the next value
                continue
            elif dna_dict[key][-3:] == value[:3]: #If the last 3 nucleotides of the key's value are the same as the first 3 of the value
                key2 = keylist[valuelist.index(value)] #turns the tested value back into its dictionary key.
                list1.append((key,key2)) #add both values as a match in the empty list
    return list1

def perfect_match(rna):
    import math
    rna = rna.upper()
    matches = 0 #start counter
    if rna.count("A") == rna.count("U") and rna.count("C") == rna.count("G"): #Makes sure every nucleotide has a pair so that matching is possible
        matches = math.factorial(rna.count("A")) * math.factorial(rna.count("C")) # calculates the total number of perfect matches using factorials
    else: #if there aren't enough of a certain nucleotide, there are 0 possible perfect matches
        matches = matches
    return matches

def random_genome(dna, gc_content):
    import math
    dna = dna.upper()
    prob = [] #creates an empty list of possibility
    for i in range(len(gc_content)): #for every value of the content list provided
        perc = 1
        perc = perc * ((1 - gc_content[i]) / 2) ** (dna.count("A")) #calculates the possibility of a dna sequence, which is dependent on the number of nucleotides and not the order they appear
        perc = perc * ((1 - gc_content[i]) / 2) ** (dna.count("T"))
        perc = perc * (gc_content[i] / 2) ** (dna.count("G"))
        perc = perc * (gc_content[i] / 2) ** (dna.count("C"))
        prob.append(math.log10(perc)) #adds the log base 10 of the chance to the list
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
        for j in range(4, 13):
            if i + j > length:
                continue
            s1 = s[i:i+j]
            s2 = reverse_complement(s1)
            if s1 == s2:
                result.append((i, j))
    return result
