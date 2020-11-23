# -*- coding: utf-8 -*-
#
# example.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""
Pynest microcircuit example
---------------------------

Example file to run the microcircuit.


This example uses the function ``GetNodes``, which is deprecated. A deprecation
warning is therefore issued. For details about deprecated functions, see
documentation.
"""

###############################################################################
# Import the necessary modules

import time
import numpy as np
import network
from network_params_norec import net_dict
from sim_params import sim_dict
from stimulus_params import stim_dict

###############################################################################
time_start = time.time()
# Initialize the network and pass parameters to it.
net = network.Network(sim_dict, net_dict, stim_dict)
time_network = time.time()

# Connect all nodes.
net.setup()
time_connect = time.time()

# Presimulate.
net.simulate(0.1)
time_presimulate = time.time()

# Simulate.
net.simulate(10000.0)
time_simulate = time.time()
#####################################################################
# Summarize time measurements. Rank 0 usually takes longest
# because of the data evaluation and print calls.
#######

print(
    '  Total time:          {:.3f} s\n'.format(
        time_simulate -
        time_start) +
    '  Time to initialize:  {:.3f} s\n'.format(
        time_network -
        time_start) +
    '  Time to connect:      {:.3f} s\n'.format(
        time_connect -
        time_network) +
    '  Time to calibrate: {:.3f} s\n'.format(
        time_presimulate -
        time_connect) +
    '  Time to simulate:    {:.3f} s\n'.format(
        time_simulate -
        time_presimulate))
