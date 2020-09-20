import sys
from skbio import TabularMSA, DNA
msa = TabularMSA.read(sys.argv[1], constructor=DNA)
msa.reassign_index(minter='id')
msa.write(sys.argv[2], format='phylip')