#!/bin/sh

# check if sudo rights
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Uninstalling size_calculator..."
rm -rf /usr/local/bin/size_calculator
echo "Done!"