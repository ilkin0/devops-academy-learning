#!/bin/bash

echo "Enter th phrases for concatenation: "

PH1=$1
PH2=$2

concat_function() {
  echo "$PH1 $PH2"
}

concat_function
