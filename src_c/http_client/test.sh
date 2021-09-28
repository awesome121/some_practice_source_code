#!/bin/bash
count=0
file='small.txt'
while read p
do
    ((count++))
    echo $count
    ./test_download.sh $p 
done < $file

