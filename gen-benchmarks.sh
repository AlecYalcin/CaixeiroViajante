#!/bin/bash

help="SYNTAX:
 ./gen-benchmarks.sh <start-file> <end-file> <algorithm>
  <start-file> - start benchmark-n-<start-file> at core/maps
  <end-file> - end benchmark-n-<end-file> at core/maps
  <algorithm> - selected algorithm at algorithms/

 Example: 4 5 permutation"

if [ $# -eq 3 ]; then
    algorithm=$3

    result="results/$algorithm/$algorithm-benchmarks.txt"
    > $result
    for i in $(seq $1 $2); do
        file="core/maps/benchmark-n-$i.txt"
        if [ -f $file ]; then
            echo "Executando $algorithm no arquivo $file"
            echo -n "$i " >> "$result"
            python3 benchmarks.py "$algorithm" "$file" >> "$result"
        fi
    done

    echo "Execução finalizada!!!"
else
    echo "$help"
fi
