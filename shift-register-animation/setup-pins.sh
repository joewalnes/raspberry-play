#!/bin/bash

set -e

echo 17 > /sys/class/gpio/unexport 2> /dev/null || /bin/true
echo 17 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio17/direction

echo 21 > /sys/class/gpio/unexport 2> /dev/null || /bin/true
echo 21 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio21/direction

echo 22 > /sys/class/gpio/unexport 2> /dev/null || /bin/true
echo 22 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio21/direction

echo Done


