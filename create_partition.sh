#!/bin/bash

device="/dev/"$1
home_size_mb=$2
swap_size_mb=$3+1

bios_size_mb=500

begin_bios_mb=1
end_bios_mb=$begin_bios_mb+$bios_size_mb+1

begin_swap_mb=$end_bios_mb
end_swap_mb=$begin_swap_mb+$swap_size_mb+1

begin_home_mb=$end_swap_mb+1
end_home_mb=$begin_home_mb+$home_size_mb+1

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

mklabel
gpt
y

mkpart
EFI 
fat32
${begin_bios_mb}MB
${end_bios_mb}MB
Ignore

mkpart 
swap
linux-swap
${begin_swap_mb}MB
${end_swap_mb}MB
y
Ignore

mkpart 
main
ext4
${end_swap_mb}MB
100%
y
Ignore


print
EOF

sudo mkfs.vfat -F 32 ${device}1

sudo mkswap ${device}2

fi
