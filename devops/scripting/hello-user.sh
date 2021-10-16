#!/bin/bash
echo Hello there. Please enter your name and birthday!

echo "Name: "
read -r Name

echo "Birthday: "
read -r Birth

CurrentYear=$(date +%Y)
Age=$(expr "$CurrentYear" - "$Birth")

echo Hello "${Name}", your age is "${Age}"
