======================================================================
Material and data analysis for the paper
"Fast simulations of highly-connected spiking cortical models using GPUs"
======================================================================
Authors
--------
Bruno Golosio, Gianmarco Tiddia, Chiara De Luca, Elena Pastorelli, Francesco Simula, Pier Stanislao Paolucci
======================================================================

======================================================================
Potjan-Diesmann 2014 model
(folder Potjans_2014)
======================================================================
Comparison of Potjan-Diesmann 2014 model simulations based on NEST, GeNN and NeruronGPU
----------------------------------------------------------------------

The subfolders contain implementations of the Potjan-Diesmann 2014 model based on NEST 2.20, GeNN 3.2.0 and NeuronGPU 1.6.0, the spike times of all neurons from simulations of this model made using the three simulators, the scripts for evaluating statistical distributions and for evaluating the Kullback–Leibler divergence between distributions obtained with different implementations

----------------------------------------------------------------------
NEST (folder nest)
----------------------------------------------------------------------
Implementation of the Potjan-Diesmann 2014 model based on NEST 2.20.
----------------------------------------------------------------------
Running the script
$ source script.sh
launches 20 simulations with different seeds for random number generations, and
stores the results in the folders data0 - data19.
The script
$ source merge.sh
joins the files produced by different threads, putting them in appropriate format for the statistical analysis.
The script
$ source script_eval_time.sh
evaluates the building and simulation times on 20 simulations with different seeds for random number generations, and sends the output to the logfiles eval_time_log0.txt - eval_time_log19.txt
To evaluate the average and standard deviations of building and simulation times run the script
$ python meantimes.py

----------------------------------------------------------------------
GeNN (folder genn)
----------------------------------------------------------------------
Results of the simulation of the Potjan-Diesmann 2014 model, obtained using GeNN 3.2.0 by the first authors of GeNN and publicly available in
https://github.com/BrainsOnBoard/frontiers_genn_paper
in the folder scripts/potjans_spikes
In this case only the results from a single simulation are available

----------------------------------------------------------------------
NeuronGPU (folder ngpu)
----------------------------------------------------------------------
Implementations of the Potjan-Diesmann 2014 model based on NeuronGPU 1.6.0
----------------------------------------------------------------------
Running the script
$ source script.sh
launches 10 simulations with different seeds for random number generations, and
stores the results in the folders data0 - data9.
The script
$ source script_eval_time.sh
evaluates the building and simulation times on 10 simulations with different seeds for random number generations, and sends the output to the logfiles eval_time_log0.txt - eval_time_log19.txt
To evaluate the average and standard deviations of building and simulation times run the script
$ python meantimes.py

----------------------------------------------------------------------
Results of the simulations and statistical analysis
----------------------------------------------------------------------
The spike times of all neurons are stored in the files
data$i/spike_times_$j.dat
where i is the index of runs made using different seeds for random number generation and j is the index of the population.
The folder "distributions" contains the scripts that extract the distributions of firing rate, coefficient of variation of the interspike intervals, Pearson correlation of the spike trains produced by different neurons. In order to run those script it is necessary to install the "elephant" package:
https://elephant.readthedocs.io/en/latest/
It is recommended to create your conda environment (e.g., elephant):

$ conda create --name elephant python=3.7 numpy scipy tqdm

Activate your environment:

$ conda activate elephant

The scripts can be executed through the commands:
$ python firing_rate.py
$ python cv_isi.py
$ python correl.py
The distributions are stored in the files:
data$i/firing_rate_$j.dat
data$i/cv_isi_$j.dat
data$i/correl_$j.dat
where i is the index of the run and j is the index of the population-

----------------------------------------------------------------------
Comparison of the histograms with NEST and evaluation of the KL divergence
----------------------------------------------------------------------
The scripts KL_*_* plot a comparison of the histograms obtained using GeNN and NeuronGPU with NEST. nest_nest compare histograms obtained using nest with different seeds for random number generation. The scripts also display the mean value and the standard deviation of the  Kullback–Leibler divergence between the istograms.

======================================================================
Balanced networks of excitatory and inhibitory AdEx neurons
(folder balanced_network)
======================================================================
Comparison of balanced networks of excitatory and inhibitory AdEx neurons simulations based on NEST and NeruronGPU
----------------------------------------------------------------------

The subfolders contain Python scripts for balanced network simulations based on NEST 2.20 and NeuronGPU 1.6.0 and scripts for evaluating building time and simulation time at varying number of neurons and number of connections.

----------------------------------------------------------------------
NEST (folder nest)
----------------------------------------------------------------------
Running the script

$ source script.sh

launches all the simulations at varying number of neurons and number of connections and sends the output to the logfiles eval_time_log1.txt - eval_time_log10.txt and eval_time_conn_log1.txt - eval_time_conn_log5.txt 
To extract building and simulation times from the logfiles, run the script

$ python extract_time.py

the results will be written in the files
nest_build_time_conn.dat
nest_build_time.dat
nest_sim_time_conn.dat
nest_sim_time.dat

----------------------------------------------------------------------
NeuronGPU (folder ngpu)
----------------------------------------------------------------------
Running the script

$ source script.sh

launches all the simulations at varying number of neurons and number of connections and sends the output to the logfiles eval_time_log1.txt - eval_time_log10.txt and eval_time_conn_log1.txt - eval_time_conn_log5.txt 
To extract building and simulation times from the logfiles, run the script

$ python extract_time.py

the results will be written in the files
ngpu_build_time_conn.dat
ngpu_build_time.dat
ngpu_sim_time_conn.dat
ngpu_sim_time.dat

