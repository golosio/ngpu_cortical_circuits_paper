for i in $(seq 0 19); do
    cat sim_params.templ | sed "s/__seed__/1234$i/" > sim_params.py
    python  eval_microcircuit_time.py | tee eval_time_log$i.txt
done
