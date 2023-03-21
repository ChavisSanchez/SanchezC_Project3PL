#!/bin/sh

make clean

make main

echo "=====Compiling a1====="
./main a1.in
echo "=====Compiling a2====="
./main a2.in
echo "=====Compiling a3====="
./main a3.in
echo "=====Compiling a4====="
./main a4.in
echo "=====Compiling a5====="
./main a5.in
echo "=====Compiling a6====="
./main a6.in
echo "=====Compiling a7====="
./main a7.in
echo "=====Compiling a8====="
./main a8.in
