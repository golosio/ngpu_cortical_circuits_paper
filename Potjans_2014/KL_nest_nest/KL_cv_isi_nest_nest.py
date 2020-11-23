import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.stats import entropy

div_arr = []

y1mean = np.zeros((8, 300))
y2mean = np.zeros((8, 300))                 

for i_run in range(10):
    i1=i_run + 10
    div_row = []
    for i in range(8):
        fn1 = '../nest/Potjans_2014/data' + str(i_run) + '/cv_isi_' + str(i) \
              + '.dat'
        fn2 = '../nest/Potjans_2014/data' + str(i1) + '/cv_isi_' + str(i) \
              + '.dat'

        data1 = np.loadtxt(fn1)
        data2 = np.loadtxt(fn2)

        x1=[row[0] for row in data1]
        y1=[row[1] for row in data1]

        x2=[row[0] for row in data2]
        y2=[row[1] for row in data2]

        f1 = interpolate.interp1d(x1, y1,fill_value="extrapolate")
        f2 = interpolate.interp1d(x2, y2,fill_value="extrapolate")

        xnew = np.linspace(0, 1.5, 300)

        y1new = f1(xnew)
        y2new = f2(xnew)

        eps = 1.0e-3
        for j in range(len(y2new)):
            y2new[j] = max(y2new[j], eps)
            y1new[j] = max(y1new[j], eps)
            y1mean[i][j] = y1mean[i][j] + y1new[j]/10 
            y2mean[i][j] = y2mean[i][j] + y2new[j]/10

        div = entropy(y1new, y2new)
        div_row.append(div)

    div_arr.append(div_row)


    
div_arr = np.array(div_arr)
div_arr = div_arr.transpose()

for pop in div_arr:
    print(np.mean(pop), '+-',  np.std(pop))

for i in range(8):
    plt.figure(i+1)
    plt.plot(xnew, y1mean[i])
    plt.plot(xnew, y2mean[i])

plt.draw()
plt.pause(0.5)
input("Press Enter to continue...")
plt.close()


