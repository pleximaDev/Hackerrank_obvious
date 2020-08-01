#!/bin/bash
read N
a=0
for i in $(seq 1 $N);
    do
        read num
        a=$(( a+num ))
    done
out=$(( a/N ))
# echo "$out"
# echo "scale=2; $(( a/N ))" | bc
# bc -l <<< ''
printf "%.3f" $(echo "scale=10; $a/$N" | bc -l)
