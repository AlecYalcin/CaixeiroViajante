if (!exists("ALGORITHM"))   ALGORITHM = "algorithm"
if (!exists("FILE"))        FILE = "dados.txt"
if (!exists("TYPE"))        TYPE = "distance"
if (!exists("TITLE"))       TITLE = "Gráfico Automático"
if (!exists("EXIT"))        EXIT = "saida.eps"
if (!exists("START"))       START = 0
if (!exists("END"))         END = 6

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

# Configurações
set terminal postscript eps enhanced color font 'Arial,14'
set output EXIT

set title TITLE
set xlabel "benchmark-n"
set ylabel Y_LABEL

# Plot
plot FILE using 1:Y_COL every ::START::END with linespoints title ALGORITHM