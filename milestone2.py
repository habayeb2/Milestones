
# milestone 2

import math

def find_splice(dna_motif, dna):
    index = 0
    indexarray = []
    for i in range(0, len(dna_motif)):          #iterates through once for each character in the DNA snippet
        index = dna.find(dna_motif[i], index)   #finds the location of each letter of DNA snippet
        indexarray.append(index)
        if (index == -1):
            return []
        index += 1                              # adds 1 to index after each iteration to test next letter
    return indexarray

def check_sub(short, whole):                 #FOR USE IN shared_motif(dna_list) DEFINED BELOW
    if len(whole) == 0 and len(short) == 0:  #makes sure substring has been specified by shared_motif function
        return False                         
    for n in range(len(whole)):              #iterates once for each string in dna_list, referred to as "whole" here
        if short not in whole[n]:            #if substring isn't in the string from dna_list, function refers false
            return False
    return True                              #If none of the other specifications failed, returns true, the substring is a common substring

def shared_motif(dna_list):
    sub = ""
    for n in range(len(dna_list[0])):                                     #iterates once for each character in the first string of dna_list
        for m in range(len(dna_list[0]) - n + 1):                         #nested loop: for each character in first string of dna_list, this loop iterates n less times, plus one due to exclusive nature of indexing
            if check_sub(dna_list[0][n:n+m], dna_list) and m > len(sub):  #uses check_sub function defined above to verify that string found is in other strings of dna_list
                sub = dna_list[0][n:n+m]                                  #defines sub as the longest common substring
    return sub

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
        perc = perc * ((1 - gc_content[i]) / 2) ** (dna.count("A")) #calculates the possibility of a dna sequence, dependent on the number of nucleotides, not the order in which they appear
        perc = perc * ((1 - gc_content[i]) / 2) ** (dna.count("T"))
        perc = perc * (gc_content[i] / 2) ** (dna.count("G"))
        perc = perc * (gc_content[i] / 2) ** (dna.count("C"))
        prob.append(math.log10(perc)) #adds the log base 10 of the chance to the list
    return prob

def reverse_complement(dna):
    dna = dna[::-1] #reverses the dna string
    fdna = ''
    for symbol in dna: #replaces the symbols
        if symbol == 'A':
            fdna = fdna + 'T'
        elif symbol == 'T':
            fdna = fdna + 'A'
        elif symbol == 'C':
            fdna = fdna + 'G'
        elif symbol == 'G':
            fdna = fdna + 'C'
    return fdna

def rev_palindrome(dna):
    result = []
    length = len(dna)                      #finds length of input which is a DNA string
    for i in range(length):              #iterares through length of DNA string
        for j in range(4, 13):           #goes through each letter 4 to 12 times for reverse palindromes of 4 to 12 letters
            if i + j > length:
                continue
            s1 = dna[i:i+j]
            s2 = reverse_complement(s1)  #checks to see if reverse complement string is a reverse palindrome, using function defined above
            if s1 == s2:                 #if it is, add the position and length as a tuple to the output
                result.append((i, j))
    return result

def assemble_genome(dna_list):
    base_dna = dna_list[0]
    i = 1
    while i < len(dna_list):
        nextstring = dna_list[i]
        for j in range(1, len(dna_list[i])):
            if base_dna[len(base_dna) - j: len(base_dna)] == nextstring[1: j+1]:
                deletetext = nextstring[0: j+1]
                next = nextstring.replace(deletetext, "")
                base_dna = base_dna + next
                break
        i = i + 1
    return base_dna
