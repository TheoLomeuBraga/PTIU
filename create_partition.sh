#!/bin/bash

device="/dev/"$1
home_size_gib=$2


if home_size_gib gt 0
then
echo "home"
parted << EOF
select $device
print

print



EOF
else
echo "nohome"
parted << EOF
select $device
print

print



EOF
fi
