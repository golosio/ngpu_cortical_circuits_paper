for i in $(seq 0 19); do
    for j in $(seq 0 7); do
	echo 'sender time_ms' > data$i/spike_times_$j.dat
	for th in $(seq -w 0 15); do
	    tail -n +4 data$i/spike_detector-7717${j}-$th.gdf >> data$i/spike_times_$j.dat
	done
    done
done
