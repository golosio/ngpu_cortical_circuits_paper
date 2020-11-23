for i in $(seq 1 5); do
    fact=$(expr $i \* 5 + 5)
    python brunel_ngpu_conn.py $fact > eval_time_conn_log${i}.txt
done

for i in $(seq 1 10); do
    python brunel_ngpu.py ${i}00000 > eval_time_log${i}.txt
done
