#!/usr/bin/python2.7

import numpy as np
from sconf import parser_init, parser, log_conf
import Gnuplot

__author__ = 'jm'

# Use this option to turn off fifo if you get warnings like:
# line 0: warning: Skipping unreadable file "/tmp/tmpakexra.gnuplot/fifo"
Gnuplot.GnuplotOpts.prefer_fifo_data = 0

# Global shortcuts
pi = np.pi
pi2 = np.pi * np.pi

# -- Simulation configuration I: parsing, debuging.
conf_file, debug, args1, hlp = parser_init()
if not hlp:
    logger = log_conf(debug)
else:
    logger = None
# -- Simulation configuration II: data entry (second parser).
description = 'Ring network of inhibitory and excitatory QIF neurons.'
opts, args = parser(conf_file, args1, description=description)  # opts is a dictionary, args is an object
# Parameters are now those introduced in the configuration file:
# >>> args.parameter1 + args.parameter2

# ############################################################
# 0) Prepare simulation environment
logger.debug('This is debug.')