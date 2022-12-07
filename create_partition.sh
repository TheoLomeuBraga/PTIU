#!/bin/bash

device="/dev/"$1
full_space_mb=$2
home_size_mb=$3
print $device

remaining_space_mb=$2-$3
echo $remaining_space_mb
if home_size_mb gt 0
then
echo "with home partition"
parted << EOF






EOF



else
echo "no home partition"
parted << EOF
select $device
using $device

mkpart 
primary 
fat32 
1 
500MB
Ignore

mkpart 
primary 
ext4 
500MB
${remaining_space_mb}MB
y
Ignore

print
EOF




fi
