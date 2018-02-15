import os
import sys
from Bio import SeqIO

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print '''

        Count nucleotidey

        Sarai Reyes

        usage:
	python percentage_identity_introgression.py --help
        python percentage_identity_introgression.py [Fasta_files]
        '''
	exit(0)


input_file = open(sys.argv[1], 'r')

all_count=[]
for cur_record in SeqIO.parse(input_file, "fasta") :
#count nucleotides in this record...
    gene_name = cur_record.name
    A_count = cur_record.seq.count('A')
    C_count = cur_record.seq.count('C')
    G_count = cur_record.seq.count('G')
    T_count = cur_record.seq.count('T')
    N_count = cur_record.seq.count('N')
    length = len(cur_record.seq)
    total=A_count+C_count+G_count+T_count+N_count
    print (gene_name,total)
    all_count.append (total)
#Min value = without Ns
print ("TOTAL",sum(all_count))
