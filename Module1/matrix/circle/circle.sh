#!/bin/bash



cd  /sdcard/download/Circle
texfot pdflatex circle.tex
python3 gvv.py
termux-open circle.pdf



