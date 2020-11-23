import numpy as np
import matplotlib.pyplot as plt
building=[]
simulation=[]
n_neur=[]

for i in range(10):
    data=open('eval_time_log'+str(i+1)+'.txt', 'r')
    lineList = data.readlines()
    btstr=lineList[len(lineList)-2].split()
    ststr=lineList[len(lineList)-1].split()
    bt=btstr[len(btstr)-2]
    st=ststr[len(ststr)-2]
    btime=float(bt)
    stime=float(st)
    #print(btime, stime)
    building.append(btime)
    simulation.append(stime)
    n_neur.append((i+1)*100000)

np.savetxt('nest_build_time.dat',np.column_stack((n_neur, building)))
np.savetxt('nest_sim_time.dat',np.column_stack((n_neur, simulation)))

building=[]
simulation=[]
n_conn=[]

for i in range(5):
    data=open('eval_time_conn_log'+str(i+1)+'.txt', 'r')
    lineList = data.readlines()
    btstr=lineList[len(lineList)-2].split()
    ststr=lineList[len(lineList)-1].split()
    bt=btstr[len(btstr)-2]
    st=ststr[len(ststr)-2]
    btime=float(bt)
    stime=float(st)
    #print(btime, stime)
    building.append(btime)
    simulation.append(stime)
    n_conn.append(10000+i*5000)

np.savetxt('nest_build_time_conn.dat',np.column_stack((n_conn, building)))
np.savetxt('nest_sim_time_conn.dat',np.column_stack((n_conn, simulation)))

