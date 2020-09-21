#!/bin/bash

FILES="1000M[1-2]/R*"

for i in $FILES
do
    start=`date +%s%N`
    ./FastTree -nt $i/rose.aln.true.fasta > $i/FastTree_JC.et
    end=`date +%s%N`
    python3 compare.py $i/rose.tt $i/NJ_L.et >> FastTree_JC.csv
    echo $(bc <<< "scale=2;($end - $start)/1000000000" ) >> FastTree_JC.csv

    start=`date +%s%N`
    ./FastTree -nt -gtr $i/rose.aln.true.fasta > $i/FastTree_GTR.et
    end=`date +%s%N`
    python3 compare.py $i/rose.tt $i/NJ_L.et >> FastTree_GTR.csv
    echo $(bc <<< "scale=2;($end - $start)/1000000000" ) >> FastTree_GTR.csv

    python3 fasta2phylip.py $i/rose.aln.true.fasta $i/rose.aln.true.phylip
    start=`date +%s%N`
    ./fastme-2.1.5-linux64 -mN -dJ -i $i/rose.aln.true.phylip -o $i/NJ_JC.et
    end=`date +%s%N`
    python3 compare.py $i/rose.tt $i/NJ_L.et >> NJ_JC.csv
    echo $(bc <<< "scale=2;($end - $start)/1000000000" ) >> NJ_JC.csv

    start=`date +%s%N`
    ./fastme-2.1.5-linux64 -mN -dL -i $i/rose.aln.true.phylip -o $i/NJ_L.et
    end=`date +%s%N`
    python3 compare.py $i/rose.tt $i/NJ_L.et >> NJ_L.csv
    echo $(bc <<< "scale=2;($end - $start)/1000000000" ) >> NJ_L.csv

done

python3 final.py