#!/usr/bin/env python3

"""
pyNormalizePlot

Quick script to normalize data of one file ENDING with "IR.dat" in a folder.
It must have two x/y columns only.

Just launch it in the molecule folder (pyNormalizePlot.py)

Author: Matteo Paolieri, University of Cologne 2020

License: MIT
"""

import os

# get the only file ending with .dat

vs_files = [f for f in os.listdir('.') if f.endswith('IR.dat')]
if len(vs_files) != 1:
    raise ValueError('There should be only one file ending with IR.dat in the current directory!')

filename = vs_files[0]

# read it

with open(filename, 'r') as f:
    all_text = f.readlines()

wavenumber_list = []
intensity_list = []

# extract wavenumbers and intensities

for line in all_text:
    column = line.split()
    wavenumber = column[0]
    intensity = column[1]

    wavenumber_list.append(wavenumber)
    intensity_list.append(intensity)

tot_numbers = int(len(intensity_list))

# put everything in float

for i in range(0, tot_numbers):
    wavenumber_list[i] = float(wavenumber_list[i])
    intensity_list[i] = float(intensity_list[i])

# normalize all abs data: z_i = (x_i-min)/(max-min)

max_abs = max(intensity_list)
min_abs = min(intensity_list)

for i in range(0, tot_numbers):
    intensity_list[i] = (intensity_list[i]-min_abs)/(max_abs-min_abs)

# write a new file "IR-norm.dat"

with open('IR-norm.dat', 'w') as f:
    for i in range(0, tot_numbers):
        print(f'{wavenumber_list[i]} {intensity_list[i]}', file=f)
