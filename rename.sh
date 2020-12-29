#!/bin/bash

IFS='
'

i=0
DIR="/home/guilherme-resende/Desktop/show_chords/img"

ls ${DIR} | while read file
do
	mv ${DIR}/${file} ${DIR}/"chord_${i}.png"
	i=$((i + 1))
done
