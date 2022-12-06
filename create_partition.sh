#!/bin/bash

device="/dev/"$1



sudo parted << EOF
select 
$device

print
quit