# pyNormalizePlot

Quick script to normalize data of one plot in a folder. Initially created to normalize IR spectra from 0 to 1. 

The equation used to normalize each absorption point is: `normalized_abs_i = (old_abs_i-abs_min)/(abs_max-abs_min)`

```bash
usage: pyNormalizePlot.py [-h] [--inputfile INPUTFILE] [--outputfile OUTPUTFILE] [--reversey REVERSEY]

Normalize a plot.

optional arguments:
  -h, --help            show this help message and exit
  --inputfile INPUTFILE
                        Input file, like a .dat, .txt ... With two columns: Wavenumbers and Intensity. Default is 'IR.dat'
  --outputfile OUTPUTFILE
                        Output file, default is 'IR-norm.dat'
  --reversey REVERSEY   Choose whether reverse the y-axis or not. Default False.
  ```






