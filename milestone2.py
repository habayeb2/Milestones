
# milestone 2

def find_motif(dna_motif, dna):
    index = 0 
    indexarray = [] 
    for i in range(0, len(dna_motif)):
        index = dna.find(dna_motif[i], index)
        indexarray.append(index) 
        index += 1 
    
    return indexarray
