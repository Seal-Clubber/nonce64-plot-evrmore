nonce.png: nonce.lst
	gnuplot -e " \
		set terminal png size 3840,2160 font 'VL P Gothic,18'; \
		set output '$@'; \
		set datafile separator ','; \
		set title 'Nonce Distribution Evrmore'; \
		set xlabel 'Block Height'; \
		set ylabel 'Nonce'; \
		set format x '%.0f'; \
		set format y '%.0f'; \
		set grid xtics ytics mxtics mytics; \
		set nokey; \
		plot '$<' using 1:2 with points pt 7 ps 0.1 lc rgb 'dark-red'; \
	"
