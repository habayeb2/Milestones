# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 01:03:24 2021

@author: karee
"""

def dna_count(dna):
    dna = dna.upper()
    count_A = dna.count('A')
    count_C = dna.count('C')
    count_G = dna.count('G')
    count_T = dna.count('T')
    return count_A,count_C,count_G,count_T

def dna2rna(dna):
    dna = dna.upper()
    rna = ''
    for symbol in dna:
        if symbol == 'A':
            rna = rna + 'U'
        elif symbol == 'T':
            rna = rna + 'A'
        elif symbol == 'C':
            rna = rna + 'G'
        elif symbol == 'G':
            rna = rna + 'C'
    return rna

def locate_substring(dna_snippet, dna):
    def recurse(index_found, start):
        ind = dna.find(dna_snippet, start)
        if ind !=-1:
            return recurse(index_found + [ind], ind + 1 )
        else:
            return index_found
    return recurse([], 0)

#Test locate_substring
subdna = "ATAT"
dnalist = "GATATATGCATATACTT"
print(locate_substring(subdna, dnalist))

def hamming_dist(dna1, dna2):
    count = 0
    for i in range(len(dna1)):
        if (dna1[i] != dna2[i]):
            count += 1
    return count
#Test hamming_dist     
firstdna = "GAGCCTACTAACGGGAT"
seconddna = "CATCGTAATGACGGCCT"
print(hamming_dist(firstdna, seconddna))


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

def mendels_law(hom, het, rec):
    dominant = 0
    n = (hom+het+rec)
    outcomes = 0
    while n != 0:
        outcomes += n - 1
        n += -1
    homodom = hom
    while homodom != 0:
        dominant += homodom - 1
        homodom += -1
    hetero = het
    while hetero != 0:
        dominant += .75*(hetero - 1)
        hetero += -1
    dominant += hom*het*1
    dominant += hom*rec*1
    dominant += het*rec*0.5
    prob = dominant/outcomes
    return prob
