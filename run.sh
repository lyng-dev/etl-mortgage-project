#!/bin/bash
for src in `ls src*`
do
    python3 main.py $src
done