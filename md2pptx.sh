#!/usr/bin/bash

sudo docker run -it --rm -v `pwd`:/workspace k1low/alpine-pandoc-ja pandoc $1 -f markdown -o $2