
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

def shared_motif(dna_list):
    dna_sorted = sorted(dna_list, key=len)    #sorts strings of DNA in dna_list from shortest to longest
    short_dna = dna_sorted[0]        #takes the first string from the sorted dna list and defines it as short_dna
    rest_dna = dna_sorted[1:]        #rest of dna strings
    substring = ""
    for n in range(len(short_dna)):  # iterates one time for each letter in the shortest dna string
        for m in range(len(short_dna), len(substring) + n + 1, -1):  # iterates backwards from end of shortest string, getting longer with every inrease in n
            sub1 = short_dna[n:m]    # defines sub1 as the part of the shortest dna string from n to m
            
            check = True
            for sub2 in rest_dna:
                if sub1 not in sub2:  # This block of logic checks if sub1 is in the other dna strings
                    check = False
                    break             # if sub1 isn't in the rest of the strings, we break the for loop and it continues iterating
            if check:
                substring = sub1      # if sub1 is in the other strings we define substring as sub1 and we've found the shortest common substring
                
    return substring

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

def rev_palindrome(s):
    result = []
    length = len(s)                      #finds length of input which is a DNA string
    for i in range(length):              #iterares through length of DNA string
        for j in range(4, 13):           #goes through each letter 4 to 12 times for reverse palindromes of 4 to 12 letters
            if i + j > length:
                continue
            s1 = s[i:i+j]
            s2 = reverse_complement(s1)  #checks to see if reverse complement string is a reverse palindrome, using function defined above
            if s1 == s2:                 #if it is, add the position and length as a tuple to the output
                result.append((i, j))
    return result
