:>balanced_izh_psc_exp_2s_eval_time.dat
for p in 4 4.5 5 5.5 6; do
    # evaluate 10^p and round it to the nearest even number 
    n=$(echo "print(2*int(round(10**$p/2.0)))" | python3)
    echo "Number of neurons: $n"
    fn=balanced_izh_psc_exp_2s_eval_time_10e$p.log
    python3 balanced_izh_psc_exp_2s_eval_time.py $n > $fn        
    bt=$(cat $fn | tail -2 | head -1 | awk '{print $NF}')
    st=$(cat $fn | tail -1 | awk '{print $NF}')
    echo "$p $bt $st" >> balanced_izh_psc_exp_2s_eval_time.dat
done
