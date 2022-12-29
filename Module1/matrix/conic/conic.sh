#!/bin/bash



cd  /sdcard/download/conic
texfot pdflatex conic.tex
python3 conic.py
termux-open conic.pdf



