#!/bin/bash

FILES="1000M[1-9]/R*"

for i in $FILES
do
    start=`date +%s%N`
    #python3 fasta2phylip.py $i/rose.aln.true.fasta $i/rose.aln.true.phylip
    #./FastTree -nt $i/rose.aln.true.fasta > $i/FastTree_GTR.et
    #./FastTree -nt -gtr $i/rose.aln.true.fasta > $i/FastTree_GTR.et
    rm $i/NJ_L.et
    ./fastme-2.1.5-linux64 -mN -dL -i $i/rose.aln.true.phylip -o $i/NJ_L.et
    end=`date +%s%N`
    python3 compare.py $i/rose.tt $i/NJ_L.et >> NJ_L.csv
    echo $(bc <<< "scale=2;($end - $start)/1000000000" ) >> NJ_L.csv
    echo "------------------------------------------------------------------------------------------------------"
done


#./FastTree -nt 1000M1/R0/rose.aln.true.fasta > testtree.txt