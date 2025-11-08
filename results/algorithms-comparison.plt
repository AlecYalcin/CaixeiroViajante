
if (!exists("TYPE"))        TYPE = "distance"
if (!exists("START"))       START = 0
if (!exists("END"))         END = 6
if (!exists("INCLUDE_P"))   INCLUDE_P = 1 

PERMUTATION="permutation/permutation-benchmarks.txt"
HEURISTIC="heuristic/heuristic-benchmarks.txt"
HEURISTIC_N="heuristic_n/heuristic_n-benchmarks.txt"
MY_HEURISTIC="my_heuristic/my_heuristic-benchmarks.txt"
MY_HEURISTIC_N="my_heuristic_n/my_heuristic_n-benchmarks.txt"
TITLE = TYPE . " benchmarks comparison"

if (TYPE eq "distance") {
    Y_LABEL = "mean distance"
    Y_COL = 2
} else if (TYPE eq "time") {
    Y_LABEL = "avarage time"
    Y_COL = 3
} else {
    print "Tipo inválido! Coloque TYPE='distance' ou TYPE='time'"
    exit
}

set terminal postscript eps enhanced color font 'Arial,14'
set output TYPE . "-" . START . ":" . END . "-benchmarks-comparison.eps"

set title TITLE
set xlabel "benchmark-n"
set ylabel Y_LABEL

if (INCLUDE_P == 1) {
    plot \
        PERMUTATION     using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "Permutation", \
        HEURISTIC       using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "Heuristic", \
        HEURISTIC_N     using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "Heuristic N", \
        MY_HEURISTIC    using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "My Heuristic", \
        MY_HEURISTIC_N  using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "My Heuristic N"
} else {
    plot \
        HEURISTIC       using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "Heuristic", \
        HEURISTIC_N     using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "Heuristic N", \
        MY_HEURISTIC    using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "My Heuristic", \
        MY_HEURISTIC_N  using 1:Y_COL every ::START::END with linespoints lw 2 pt 7 title "My Heuristic N"
}