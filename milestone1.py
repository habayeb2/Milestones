# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:03:24 2021

@author: karee
"""
genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

def dna_count(dna):
    dna = dna.upper()
    dna_count ={}
    dna_count["A"] = dna.count('A')
    dna_count["C"] = dna.count('C')
    dna_count["G"] = dna.count('G')
    dna_count["T"] = dna.count('T')
    return dna_count

def dna2rna(dna):
    dna = dna.upper()
    rna = ''
    for symbol in dna:
        if symbol == 'A':
            rna = rna + 'A'
        elif symbol == 'T':
            rna = rna + 'U'
        elif symbol == 'C':
            rna = rna + 'C'
        elif symbol == 'G':
            rna = rna + 'G'
    return rna

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

#Test for reverse_complement
testDna = "AAAACCCGGT"
print(reverse_complement(testDna))

def mendels_law(hom, het, rec):
    dominant = 0
    n = (hom+het+rec)
    outcomes = 0
    while n != 0:
        outcomes += n - 1
        n += -1
    hom1 = hom
    while hom1 != 0:
        dominant += hom1 - 1
        hom1 += -1
    het1 = het
    while het1 != 0:
        dominant += .75*(het1 - 1)
        het1 += -1
    dominant += hom*het*1
    dominant += hom*rec*1
    dominant += het*rec*0.5
    prob = dominant/outcomes
    return prob

def fibonacci_rabbits(n,k):
    if n == 0 or n ==1:
        return n
    else:
        return fibonacci_rabbits(n-1, k) + k * fibonacci_rabbits(n-2, k)
 
        
def GC_content(dna_list):       #This function takes a list of DNA strands and counts the amount of guanine and cytosine in it
    highest_content = [0,0]         #baseline to add to as the max GC content measured gets higher
    for i in range(len(dna_list)):       # for the length of a dna string
       dna_list[i].upper()      #
       G_count = dna_list[i].count('G') #counts the amount of G in the DNA
       C_count = dna_list[i].count('C') #counts the amount of C in the string
       GC_count = G_count+C_count
       GC_content = GC_count/len(dna_list[i]) * 100      #gives the percent of the DNA made of guanine and cystosine
       if GC_content > highest_content[1]:      #if the new GC content is higher than the previously measured GC content, 
            highest_content[0] = i      # the index of the DNA sequence with the highest GC content
            highest_content[1] = GC_content      #The percent make-up of said DNA sequence
       else:
           continue
    return highest_content

def rna2codontri(triplet):
    genetic_code = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }
    allowed_codons = set('ACGU')
    if triplet in genetic_code:
        return genetic_code[triplet]
    else:
        return "Invalid"

def rna2codon(triplets):
    triplets1 = []
    amino = ''
    for i in range ( 0,int( len( triplets ) / 3 ) ):
        triplets1.append(triplets[ 3*i:3*i+3] )
    for triplet in triplets1:
        if rna2codontri(triplet) == '*':
            break
        amino = amino + rna2codontri(triplet)
    return amino


def locate_substring(dna_snippet, dna):
    def recurse(index_found, start): #finding and listing the index
        ind = dna.find(dna_snippet, start)
        if ind !=-1:
            return recurse(index_found + [ind], ind + 1 ) # Moves on to the next part of the dna string to search for the snippet
        else:
            return index_found
    return recurse([], 0)

def hamming_dist(dna1, dna2):
    count = 0
    for i in range(len(dna1)): 
        if (dna1[i] != dna2[i]): #For every index, check if values are equal.
            count += 1
    return count

def count_dom_phenotype(genotypes):
    offspring = 0
    n = 1
    for couples in genotypes:
        if n <= 3:
            offspring += couples*2
            n += 1
        elif n == 4:
            offspring += couples*1.5
            n += 1
        elif n == 5:
            offspring += couples*1
            n += 1
        elif n == 6:
            offspring += 0
    return offspring

def source_rna(protein):
    rna_combos = 3      #acts as a starting point for the math when finding combos
    rna_counter = []    #houses the number of occurences of each protein based on its key
    for n in range (0,len(protein)):        #for every individual protein in the string
        counter = 0     #the number of occurences of each protein in the dictionary
        for key in genetic_code:        #goes through every single triplet combination
            if genetic_code[key] != protein[n:n+1]:     #if the dictionary output isn't the protein we want, ignore it
                continue
            else:       #if it is, add one to the number of occurences
                counter += 1
        rna_counter.append(counter)     #adds the counted occurences to the list
    for x in rna_counter:       #takes all the stored number of occurences and multiplies them together
            rna_combos = rna_combos*x %1000000
    return rna_combos


def splice_rna(dna, intron_list):
    exons = dna
    rna = ''
    protein = ''
    for intron in intron_list: 
        exons = exons.replace(intron, "") #Removing introns from the string
    rna = dna2rna(exons)
    protein = rna2codon(rna) #converts the rna string into a protein string
    return protein
