#!/bin/bash

# Gráficos de 4 a 9
benchmarks="permutation heuristic heuristic_n my_heuristic my_heuristic_n"
for valor in $benchmarks; do
    start=0
    end=6
    file="$valor/$valor-benchmarks.txt"
    for tipo in distance time; do
        target="$valor/$valor-$tipo-$start:$end.eps"
        gnuplot -e "ALGORITHM='$valor'; FILE='$file'; TYPE='$tipo'; TITLE='$tipo benchmarks for $valor$'; EXIT='$target'; START=$start; END=$end" algorithm-graph.plt
    done
done

# Gráficos de 10 a 70
benchmarks="heuristic heuristic_n my_heuristic my_heuristic_n"
for valor in $benchmarks; do
    start=6
    end=13
    file="$valor/$valor-benchmarks.txt"
    for tipo in distance time; do
        target="$valor/$valor-$tipo-$start:$end.eps"
        gnuplot -e "ALGORITHM='$valor'; FILE='$file'; TYPE='$tipo'; TITLE='$tipo benchmarks for $valor'; EXIT='$target'; START=$start; END=$end" algorithm-graph.plt
    done
done

for tipo in distance time; do 
    # Gráfico de comparação entre todos de 4 a 10
    gnuplot -e "TYPE='$tipo'; START=0; END=5" algorithms-comparison.plt
    # Gráfico de comparação entre todos de 10 a 70
    gnuplot -e "TYPE='$tipo'; START=6; END=13; INCLUDE_P=0" algorithms-comparison.plt
done

