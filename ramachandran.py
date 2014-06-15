#!/usr/bin/python2

import json
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

#file format: phi/psi array

if (len(sys.argv) < 2):
  print("please pass a phi/psi file as commandline param")
else:
  angles = json.load(open(sys.argv[1]))

  fig, ax = plt.subplots()
  ax.plot([x[0] for x in angles],[x[1] for x in angles],'o')
  plt.title('Ramachandran plot of dihedral values in ' + sys.argv[1])
  plt.xlabel('phi')
  plt.ylabel('psi')
  plt.show()

