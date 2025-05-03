#!/bin/bash

echo "VISTA project commit log" > log.txt
git add log.txt
git commit -m "Initialize log file for commit tracking"

for i in {1..900}
do
  echo "Log entry $i at $(date)" >> log.txt
  git add log.txt
  git commit -m "Add log entry $i"
done
