def to_rna(dna_strand):
    if dna_strand == '':
        return ''
    dna_strandU = dna_strand.replace('A', 'U') 
    dna_strandUA = dna_strandU.replace('T','A')
    dna_strandUAL = dna_strandUA.replace('C', 'L')
    dna_strandUALG = dna_strandUAL.replace('G', 'C')
    rna = dna_strandUALG.replace('L', 'G')
    return rna
