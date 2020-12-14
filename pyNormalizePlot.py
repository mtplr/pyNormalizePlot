#!/usr/bin/env python3

"""
pyNormalizePlot

Quick script to normalize data of one file ENDING with "IR.dat" in a folder.
It must have two x/y columns only.

Just launch it in the molecule folder (pyNormalizePlot.py)

Author: Matteo Paolieri, University of Cologne 2020

License: MIT
"""

import argparse


def main(inputf, outputf, reverse):

    # read it

    with open(inputf, 'r') as f:
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

    if reverse is True:
        for i in range(0, tot_numbers):
            intensity_list[i] = (intensity_list[i]-max_abs)/(min_abs-max_abs)
    else:
        for i in range(0, tot_numbers):
            intensity_list[i] = (intensity_list[i]-min_abs)/(max_abs-min_abs)

    # write a new file

    with open(outputf, 'w') as f:
        for i in range(0, tot_numbers):
            print(f'{wavenumber_list[i]} {intensity_list[i]}', file=f)
        

if __name__ == "__main__":
    # parser for shell
    parser = argparse.ArgumentParser(description='Normalize a plot.')
    parser.add_argument('--inputfile', type=str, default="IR.dat",
                        help="Input file, like a .dat, .txt ... With two columns: "
                             "Wavenumbers and Intensity. Default is 'IR.dat'")
    parser.add_argument('--outputfile', type=str, default="IR-norm.dat",
                        help="Output file, default is 'IR-norm.dat'")
    parser.add_argument('--reversey', type=bool, default=False,
                        help="Choose whether to reverse the y-axis or not. Default False.")

    args = parser.parse_args()
    main(args.inputfile, args.outputfile, args.reversey)
