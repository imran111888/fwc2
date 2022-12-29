#!/bin/bash



cd  /sdcard/Download/opt
texfot pdflatex opt1.tex
python3 opt.py
termux-open opt1.pdf


