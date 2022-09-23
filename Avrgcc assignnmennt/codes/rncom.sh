#!/bin/bash



cd  /sdcard/Download/avrgcc/codes
make
cd
#pio run -t nobuild -t upload
cd /sdcard/download/ideassignment
texfot pdflatex ideas.tex
termux-open ideas.pdf


