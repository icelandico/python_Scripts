#!/bin/bash

count=50

for i in $(seq -w 1 $count)

do
    touch "Doc-"$RANDOM.txt
done