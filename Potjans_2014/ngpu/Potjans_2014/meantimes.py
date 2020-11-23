import numpy as np
import matplotlib.pyplot as plt
building=[]
simulation=[]

for i in range(10):
    data=open('eval_time_log'+str(i)+'.txt', 'r')
    lineList = data.readlines()
    ttstr=lineList[len(lineList)-7].split()
    ststr=lineList[len(lineList)-2].split()
    tt=ttstr[len(ttstr)-2]
    st=ststr[len(ststr)-2]
    ttime=float(tt)
    stime=float(st)
    btime=ttime-stime
    #print(ttime, btime, stime)
    building.append(btime)
    simulation.append(stime)

print 'Building time= ', np.mean(building), '+/-', np.std(building), 's'
print 'Simulation time= ', np.mean(simulation), '+/-', np.std(simulation), 's'
