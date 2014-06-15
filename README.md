# Ramachandran Plot

simple script to draw a ramachandran plot.

## Prerequisites:

* Python 2.7.x
* matplotlib

## Usage:

    ~/git/ramachandran$ pdbTools_0.2.1/pdb_download.py 1axc
    ~/git/ramachandran$ pdbTools_0.2.1/pdb_torsion_json.py 1axc.pdb > 1axc.phipsi
    ~/git/ramachandran$ ./ramachandran.py 1axc.phipsi

## Copyright notice

This application uses a modified version of [pdbTools](https://code.google.com/p/pdb-tools/). The modified source code is distributed via this repository, compliant with GPLv3.
