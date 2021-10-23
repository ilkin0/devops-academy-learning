#!/bin/bash

echo "Please enter the numbers for multiplication: "

NUM1=$1
NUM2=$2
NUM3=$3

RESULT=$(expr "$NUM1" \* "$NUM2" \* "$NUM3")

echo Result is "${RESULT}"