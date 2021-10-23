#!/bin/bash

INPUT=$1

if [ -f "$INPUT" ]; then
  echo file is exist.
elif [ -d "$INPUT" ]; then
  echo directory is exist.
else
  echo Doesnt exist, nothing to show.
fi
