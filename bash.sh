#!/bin/bash

#command and variables
clear

line="............................."
echo "Starting at: $(date)"

echo "UPTIME";uptime;echo $line

echo "FREE";free;echo $line

echo "WHO";who;echo $line

echo "Finishing at: $(date)"


#if else fi
echo;echo;echo

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything OK"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi

#test command

if test -n "$PATH"; then echo "your path is not empty";fi

if [ -n "$PATH" ]; then echo "your path is not empty"; fi


# while loop
echo;echo

n=1

while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done

# for loop

for file in *.html; do
    name=$(basename "$file" .html)
    mv "$file" "$name.txt"
done