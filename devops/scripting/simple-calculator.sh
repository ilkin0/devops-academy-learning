#!/bin/bash

echo Welcome to simple calulator. Please enter the numbers!

echo Enter first number:
read -r num1

echo Enter second number:
read -r num2

echo Please select expression to use
echo -e "Press 1 for + \nPress 2 for - \nPress 3 for * \nPress 4 for /"

read -r exp

if [ $exp == 1 ]; then
  RESULT=$(expr "$num1" + "$num2")
elif [ $exp == 2 ]; then
  RESULT=$(expr "$num1" - "$num2")
elif [ $exp == 3 ]; then
  RESULT=$(expr "$num1" \* "$num2")
elif [ $exp == 4 ]; then
  RESULT=$(expr "$num1" / "$num2")
fi

echo Result is "${RESULT}"
