#!/usr/bin/bash

sudo docker run -it --rm -v `pwd`:/workspace k1low/alpine-pandoc-ja pandoc $1 -f docx -o $2 -V documentclass=ltjarticle -V classoption=a4j -V geometry:margin=1in --pdf-engine=lualatex