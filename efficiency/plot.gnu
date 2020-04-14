set term tikz standalone size 12,8 \
preamble '\usepackage{cmbright}\SetSymbolFont{largesymbols}{normal}{OMX}{iwona}{m}{n}'

set output "eff_geant.tex"

set style line 1 pt 11 lw 2 lc rgb "red"
set style line 2 pt 7 lw 2 lc rgb "#FFBB00"
set style line 3 pt 9 lw 2 lc rgb "#00BB00"
set style line 4 pt 5 lw 2 lc rgb "#0088FF"

set xrange [0:20]
set xlabel 'Energy threshold [MeVee]'

set yrange [0:100]
set ylabel 'Efficiency'
set ytics format '$%g\%%$' 0,20,100

set key top inside right reverse Left samplen 3

set grid lc rgb "black" dt 4 lw 1

plot\
	-1 w p ps 0 lc rgb "white" title '\textbf{Neutron mom.}',\
	"250MeV.txt" u 1:(100*$2) w lp ls 1 title '250 MeV$/c$',\
	"350MeV.txt" u 1:(100*$2) w lp ls 2 title '350 MeV$/c$',\
	"450MeV.txt" u 1:(100*$2) w lp ls 3 title '450 MeV$/c$',\
	"550MeV.txt" u 1:(100*$2) w lp ls 4 title '550 MeV$/c$

unset out
!pdflatex eff_geant