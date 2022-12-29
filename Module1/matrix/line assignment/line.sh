#!/bin/bash



cd  /home/imran/matrix/line
texfot pdflatex line.tex
python3 line.py
evince line.pdf


