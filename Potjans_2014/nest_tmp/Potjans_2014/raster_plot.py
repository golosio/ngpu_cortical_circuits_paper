###############################################################################
# Import the necessary modules and start the time measurements.

#from stimulus_params import stim_dict
#from network_params import net_dict
#from sim_params import sim_dict
#import network
#import nest
import numpy as np
import helpers

###############################################################################
# Plot a spike raster of the simulated neurons and a box plot of the firing
# rates for each population.
# For visual purposes only, spikes 100 ms before and 100 ms after the thalamic
# stimulus time are plotted here by default.
# The computation of spike rates discards the presimulation time to exclude
# initialization artifacts.

raster_plot_interval = np.array([2000.0,
                                 2200.0])
helpers.plot_raster(
    'data0/',
    'spike_detector',
    raster_plot_interval[0],
    raster_plot_interval[1],
    1.0)
